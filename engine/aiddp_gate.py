#!/usr/bin/env python3
"""
AI-DDP gate-enforcement engine.

Harness-neutral. Pure Python standard library, no dependencies. This is the
one piece of code shared by the Claude Code, Codex, and Kiro integrations in
harness/ -- each harness just wires its own hook config to call this same
script.

What it enforces
-----------------
Phase-level gating only (Screening -> Underwriting -> Thesis -> Monitoring).
It does NOT enforce the finer-grained within-phase stage dependencies
documented in stages/underwriting.md (e.g. that the `underwriting` stage
needs `financial-diligence` output) -- that level of enforcement isn't built
yet. What it DOES enforce, mechanically, not just by convention: an agent
cannot write a file into a later phase's output directory until the human has
explicitly approved every phase before it.

Convention
----------
Deal work is written under an engagement directory with one subfolder per
phase, e.g.:

    <engagement>/screening/...
    <engagement>/underwriting/...
    <engagement>/thesis/...
    <engagement>/monitoring/...

A write into `<engagement>/underwriting/...` is blocked unless the
`screening` gate has been approved. A write into `<engagement>/thesis/...` is
blocked unless both `screening` and `underwriting` are approved. And so on.

State
-----
Stored at `.aiddp/state.json` next to wherever `init` was run (typically the
engagement root, not the whole AI-DDP repo -- run `init` once per deal).

The approve command
--------------------
Deliberately refuses to run unless invoked from an interactive terminal
(stdin is a TTY) and the operator types the phase name back as confirmation.
This is the one real safeguard against an AI agent approving its own gate by
scripting a call to this file: an agent's tool calls are not interactive
terminal sessions, so `approve` fails closed for them by construction.

Exit codes (matter for the hook integrations)
----------------------------------------------
0 = allow / success
2 = block (Claude Code and Codex both treat exit code 2 as a hard PreToolUse
    block and surface stderr back to the model; Kiro blocks on ANY non-zero
    exit code, so 2 is safe there too)
1 = ordinary CLI usage error, not a gate decision
"""

import argparse
import json
import sys
import time
from pathlib import Path

PHASES = ["screening", "underwriting", "thesis", "monitoring"]
STATE_DIRNAME = ".aiddp"
STATE_FILENAME = "state.json"


def state_file(root: Path) -> Path:
    return root / STATE_DIRNAME / STATE_FILENAME


def default_state() -> dict:
    return {
        "current_phase": PHASES[0],
        "gates": {p: {"approved": False, "approved_at": None, "note": None} for p in PHASES},
        "log": [],
    }


def load_state(root: Path) -> dict:
    f = state_file(root)
    if not f.exists():
        raise SystemExit(
            f"No AI-DDP engagement state found at {f}. Run "
            f"`python engine/aiddp_gate.py init --root <engagement-dir>` first."
        )
    return json.loads(f.read_text(encoding="utf-8"))


def save_state(root: Path, state: dict) -> None:
    f = state_file(root)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(state, indent=2), encoding="utf-8")


def append_log(state: dict, event: str) -> None:
    state["log"].append({"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": event})


def cmd_init(args) -> int:
    root = Path(args.root).resolve()
    f = state_file(root)
    if f.exists() and not args.force:
        print(f"State already exists at {f} (use --force to reset).", file=sys.stderr)
        return 1
    state = default_state()
    append_log(state, f"Engagement initialized at {root}")
    save_state(root, state)
    print(f"Initialized AI-DDP engagement state at {f}")
    return 0


def cmd_status(args) -> int:
    root = Path(args.root).resolve()
    state = load_state(root)
    print(f"Engagement root: {root}")
    print(f"Current phase:   {state['current_phase']}")
    print("Gates:")
    for p in PHASES:
        g = state["gates"][p]
        mark = "APPROVED" if g["approved"] else "pending"
        detail = f" (at {g['approved_at']})" if g["approved"] else ""
        print(f"  {p:<14} {mark}{detail}")
    return 0


def cmd_approve(args) -> int:
    root = Path(args.root).resolve()
    state = load_state(root)
    phase = args.phase

    if phase not in PHASES:
        print(f"Unknown phase '{phase}'. Valid phases: {', '.join(PHASES)}", file=sys.stderr)
        return 1

    if not sys.stdin.isatty():
        print(
            "Refusing to approve a gate from a non-interactive context.\n"
            "`approve` must be run by a human at an actual terminal -- this is "
            "the mechanism that stops an agent from approving its own gate by "
            "scripting a call to this file.",
            file=sys.stderr,
        )
        return 1

    typed = input(
        f"Type the phase name exactly ('{phase}') to confirm human approval: "
    ).strip()
    if typed != phase:
        print("Confirmation did not match. Approval NOT recorded.", file=sys.stderr)
        return 1

    note = args.note or input("Optional note for the audit log (Enter to skip): ").strip() or None

    state["gates"][phase]["approved"] = True
    state["gates"][phase]["approved_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    state["gates"][phase]["note"] = note
    append_log(state, f"Gate '{phase}' approved by human. Note: {note}")

    idx = PHASES.index(phase)
    if idx + 1 < len(PHASES):
        state["current_phase"] = PHASES[idx + 1]
        append_log(state, f"Advanced current phase to '{state['current_phase']}'")

    save_state(root, state)
    print(f"Gate '{phase}' approved. Current phase is now '{state['current_phase']}'.")
    return 0


def cmd_log(args) -> int:
    root = Path(args.root).resolve()
    state = load_state(root)
    append_log(state, args.event)
    save_state(root, state)
    print("Logged.")
    return 0


def phase_for_path(path: str) -> str | None:
    """Return the phase name if `path` looks like it's under
    <engagement>/<phase>/..., else None."""
    parts = Path(path).parts
    for part in parts:
        if part.lower() in PHASES:
            return part.lower()
    return None


def check_write(root: Path, path: str) -> tuple[bool, str]:
    """Returns (allowed, message)."""
    phase = phase_for_path(path)
    if phase is None:
        # Not writing into a recognized phase directory -- not this engine's concern.
        return True, ""
    state = load_state(root)
    idx = PHASES.index(phase)
    for earlier in PHASES[:idx]:
        if not state["gates"][earlier]["approved"]:
            return False, (
                f"Blocked: writing into '{phase}/' requires the '{earlier}' gate "
                f"to be approved first. Run `python engine/aiddp_gate.py approve "
                f"{earlier}` from an interactive terminal to have a human sign off."
            )
    return True, ""


def cmd_check_write(args) -> int:
    root = Path(args.root).resolve()
    allowed, message = check_write(root, args.path)
    if allowed:
        return 0
    print(message, file=sys.stderr)
    return 2


def extract_candidate_path(event: dict) -> str | None:
    """Best-effort extraction of a file path from a PreToolUse-style event
    across Claude Code / Codex / Kiro payload shapes. Fails open (returns
    None) rather than raising if the shape doesn't match anything known --
    an unrecognized shape allows the action rather than crashing the hook."""
    tool_input = event.get("tool_input") or event.get("toolInput") or {}
    for key in ("file_path", "filePath", "path", "notebook_path"):
        if isinstance(tool_input, dict) and key in tool_input:
            return tool_input[key]
    # Bash-style commands aren't reliably parseable for a target path; skip.
    return None


def cmd_hook_sessionstart(args) -> int:
    """Entry point wired up by each harness's SessionStart hook. Prints the
    current phase/gate status so a new session picks up context automatically
    instead of requiring a human to re-explain where things left off, or the
    agent to remember to ask. Fails open (prints nothing, exits 0) if no
    engagement has been initialized at this root yet -- a missing engagement
    is not a hook error."""
    root = Path(args.root).resolve()
    f = state_file(root)
    if not f.exists():
        return 0
    state = json.loads(f.read_text(encoding="utf-8"))
    lines = [
        "AI-DDP engagement state (from .aiddp/state.json):",
        f"  Current phase: {state['current_phase']}",
    ]
    for p in PHASES:
        g = state["gates"][p]
        mark = "approved" if g["approved"] else "pending"
        lines.append(f"    {p}: {mark}" + (f" ({g['approved_at']})" if g["approved"] else ""))
    if state["log"]:
        lines.append(f"  Last log entry: {state['log'][-1]['event']} ({state['log'][-1]['ts']})")
    print("\n".join(lines))
    return 0


def cmd_hook_pretooluse(args) -> int:
    """Entry point wired up by each harness's PreToolUse hook config. Reads
    the event JSON on stdin, decides allow/block, exits 0 or 2 accordingly."""
    root = Path(args.root).resolve()
    try:
        raw = sys.stdin.read()
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        # Malformed input -- fail open rather than blocking on a parse error.
        return 0

    path = extract_candidate_path(event)
    if path is None:
        return 0

    allowed, message = check_write(root, path)
    if allowed:
        return 0
    print(message, file=sys.stderr)
    return 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="AI-DDP gate-enforcement engine")
    p.add_argument("--root", default=".", help="Engagement root directory (default: cwd)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("init", help="Initialize engagement state")
    sp.add_argument("--force", action="store_true", help="Reset existing state")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("status", help="Show current phase and gate status")
    sp.set_defaults(func=cmd_status)

    sp = sub.add_parser("approve", help="Approve a phase's gate (human-only, interactive)")
    sp.add_argument("phase", choices=PHASES)
    sp.add_argument("--note", default=None)
    sp.set_defaults(func=cmd_approve)

    sp = sub.add_parser("log", help="Append a freeform event to the audit log")
    sp.add_argument("event")
    sp.set_defaults(func=cmd_log)

    sp = sub.add_parser("check-write", help="Check whether a path may be written given current gate state")
    sp.add_argument("path")
    sp.set_defaults(func=cmd_check_write)

    sp = sub.add_parser("hook-pretooluse", help="Harness PreToolUse hook entrypoint (reads JSON on stdin)")
    sp.set_defaults(func=cmd_hook_pretooluse)

    sp = sub.add_parser("hook-sessionstart", help="Harness SessionStart hook entrypoint")
    sp.set_defaults(func=cmd_hook_sessionstart)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

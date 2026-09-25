#!/usr/bin/env python3
"""
One-command setup for a new AI-DDP engagement.

Collapses what used to be three manual Quick Start steps -- create the four
phase folders, run `aiddp_gate.py init`, and hand-wire a harness's hook
config with the right absolute path typed in by hand -- into one command.

What this does NOT do, on purpose:
  - Fill in the fund mandate. That's a human decision with real numbers in
    it; no script should guess a fund's equity check range.
  - Approve any gate. Gate approval is deliberately manual and interactive
    (see aiddp_gate.py's `approve` command) -- that's the actual mechanism
    that keeps an AI from approving its own work, and automating it away
    here would defeat the point of the whole framework.

Usage:
    python aiddp_new_deal.py <engagement-dir> [--harness claude-code|codex|none]

--harness defaults to "none" (just sets up folders and state; you wire the
hook yourself per harness/<name>/README.md). Kiro isn't offered here because
its exact hook-file schema isn't confirmed yet (see harness/kiro/README.md)
-- writing a guessed config would be worse than not writing one.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from aiddp_gate import PHASES, default_state, save_state, state_file  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
GATE_SCRIPT = (REPO_ROOT / "engine" / "aiddp_gate.py").as_posix()

CLAUDE_HOOKS = {
    "PreToolUse": [
        {
            "matcher": "Write|Edit|MultiEdit",
            "hooks": [
                {
                    "type": "command",
                    "command": f"python {GATE_SCRIPT} --root . hook-pretooluse",
                    "timeout": 10,
                }
            ],
        }
    ],
    "SessionStart": [
        {
            "hooks": [
                {
                    "type": "command",
                    "command": f"python {GATE_SCRIPT} --root . hook-sessionstart",
                    "timeout": 10,
                }
            ]
        }
    ],
}

CODEX_HOOKS = {
    "PreToolUse": [
        {
            "matcher": "",
            "hooks": [
                {
                    "type": "command",
                    "command": f"python {GATE_SCRIPT} --root . hook-pretooluse",
                    "timeout": 10,
                }
            ],
        }
    ],
    "SessionStart": [
        {
            "hooks": [
                {
                    "type": "command",
                    "command": f"python {GATE_SCRIPT} --root . hook-sessionstart",
                    "timeout": 10,
                }
            ]
        }
    ],
}


def create_phase_folders(root: Path) -> list[str]:
    created = []
    for phase in PHASES:
        d = root / phase
        if not d.exists():
            d.mkdir(parents=True)
            created.append(phase)
    return created


def init_state(root: Path) -> bool:
    """Returns True if state was created, False if it already existed."""
    f = state_file(root)
    if f.exists():
        return False
    save_state(root, default_state())
    return True


def merge_hooks_into(config_path: Path, new_hooks: dict) -> str:
    """Merges new_hooks into an existing hook-config JSON file's "hooks" key,
    appending to each event's list rather than overwriting, or creates the
    file if it doesn't exist. Returns a short description of what happened."""
    if config_path.exists():
        try:
            existing = json.loads(config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            backup = config_path.with_suffix(config_path.suffix + ".bak")
            config_path.rename(backup)
            print(f"  WARNING: {config_path} was not valid JSON. Backed up to {backup}.")
            existing = {}
        action = "merged into existing"
    else:
        existing = {}
        action = "created new"

    hooks = existing.setdefault("hooks", {})
    for event, entries in new_hooks.items():
        existing_entries = hooks.setdefault(event, [])
        # Avoid appending an identical entry twice on repeated runs.
        for entry in entries:
            if entry not in existing_entries:
                existing_entries.append(entry)

    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(existing, indent=2), encoding="utf-8")
    return action


def wire_harness(root: Path, harness: str) -> None:
    if harness == "claude-code":
        path = root / ".claude" / "settings.json"
        action = merge_hooks_into(path, CLAUDE_HOOKS)
        print(f"Claude Code hooks {action}: {path}")
    elif harness == "codex":
        path = root / ".codex" / "hooks.json"
        action = merge_hooks_into(path, CODEX_HOOKS)
        print(f"Codex hooks {action}: {path}")
        print("  Remember: Codex requires a one-time trust step -- run /hooks "
              "inside the Codex CLI session to approve this hook.")
    elif harness == "none":
        print("No harness wired. See harness/<name>/README.md to wire one "
              "manually when you're ready (Kiro's exact hook schema isn't "
              "confirmed yet, so it's not offered here -- see "
              "harness/kiro/README.md).")
    else:
        raise SystemExit(f"Unknown harness '{harness}'. Choose: claude-code, codex, none.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Set up a new AI-DDP engagement")
    parser.add_argument("engagement_dir", help="Path to the deal's working directory (created if missing)")
    parser.add_argument("--harness", default="none", choices=["claude-code", "codex", "none"],
                         help="Which AI tool's gate hook to wire up automatically (default: none)")
    args = parser.parse_args()

    root = Path(args.engagement_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)

    created = create_phase_folders(root)
    if created:
        print(f"Created phase folders: {', '.join(created)}")
    else:
        print("Phase folders already existed.")

    if init_state(root):
        print(f"Initialized engagement state at {state_file(root)}")
    else:
        print(f"Engagement state already existed at {state_file(root)} -- left as-is.")

    wire_harness(root, args.harness)

    print()
    print("Next steps:")
    print(f"  1. Fill in knowledge/_shared/fund-mandate.md with this deal's real numbers.")
    print(f"  2. Tell your AI assistant: \"Using the AI-DDP, act as the Screening Agent for this deal.\"")
    print(f"  3. When Screening is genuinely done, approve it yourself from a real terminal:")
    print(f"     python {GATE_SCRIPT} --root {root} approve screening")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

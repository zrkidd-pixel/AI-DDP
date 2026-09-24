# Kiro integration

Wires the same AI-DDP gate engine into Kiro's Agent Hooks system.

## Honesty check on this one, specifically

I confirmed the following about Kiro's hook system directly from
[Kiro's own documentation](https://kiro.dev/docs/hooks/) before writing
anything here:

- Hooks live as JSON files in `.kiro/hooks/`, one file can hold multiple hook
  definitions in a `hooks` array.
- `PreToolUse` is one of the trigger types that **can block** an action.
- A `command`-type action runs a shell command that receives session context
  on stdin.
- The block signal is confirmed precisely: **exit code 0 allows** (stdout is
  added to agent context); **any non-zero exit code blocks** and sends stderr
  to the agent. This matches `aiddp_gate.py`'s exit-2-on-block convention
  exactly, since 2 is non-zero.

What I could **not** confirm from the documentation available to me: the
exact field names for the hook definition itself (`trigger` vs. some other
key, `action` vs. some other key) — the JSON in `aiddp-gate-check.json` is my
best construction from the confirmed shape, not something I verified against
a working example. **Before relying on this, create a throwaway hook through
Kiro's own hook-creation UI first, inspect the JSON file it generates in
`.kiro/hooks/`, and adjust `aiddp-gate-check.json`'s field names to match if
they differ.** Don't assume this file is correct as-is the way you could for
the Claude Code and Codex versions, which I verified more precisely against
their published schemas.

## SessionStart: automatic status on resume

`aiddp-gate-check.json` also includes an `aiddp-session-status` hook on
`SessionStart` (confirmed as a valid Kiro trigger, "IDE only") that prints
current phase/gate status when a session begins — same caveat as above
applies to its exact field names.

## Install (once field names are confirmed)

1. Copy `aiddp-gate-check.json` into `.kiro/hooks/` in your engagement
   directory.
2. Replace `/absolute/path/to/AI-DDP/engine/aiddp_gate.py` with the actual
   absolute path.
3. From the engagement's root directory, run:
   ```
   python /absolute/path/to/AI-DDP/engine/aiddp_gate.py init
   ```

## Approving a gate

Same as the other two harnesses — from a real interactive terminal, never
through Kiro's agent:

```
python /absolute/path/to/AI-DDP/engine/aiddp_gate.py --root <engagement-dir> approve screening
```

## Known limitation

Same file-path-extraction limitation as the other two integrations — only
tool calls exposing a recognizable `file_path`/`path` field in their input
are intercepted; the script fails open (allows) for anything else rather
than guessing.

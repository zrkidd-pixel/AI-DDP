# Claude Code integration

Wires the AI-DDP gate engine (`engine/aiddp_gate.py`) into Claude Code's
native `PreToolUse` hook, confirmed against
[Claude Code's hooks reference](https://code.claude.com/docs/en/hooks).

## Install

1. Copy the contents of `settings.snippet.json` into your engagement's
   `.claude/settings.json` (project-level) — merge it into the `hooks` key if
   that file already has other hooks configured; don't just overwrite the
   file.
2. Replace `/absolute/path/to/AI-DDP/engine/aiddp_gate.py` with the actual
   absolute path to `engine/aiddp_gate.py` in this repo. Claude Code runs
   hook commands from the session's working directory, so a relative path is
   fragile — use an absolute one.
3. From your engagement's root directory (not the AI-DDP repo itself), run:
   ```
   python /absolute/path/to/AI-DDP/engine/aiddp_gate.py init
   ```
   This creates `.aiddp/state.json` for that specific deal.

## How it behaves

- The hook fires on every `Write`, `Edit`, and `MultiEdit` tool call.
- It reads the tool's target file path and checks it against
  `.aiddp/state.json`. If the path is under a phase subdirectory
  (`.../underwriting/...`, `.../thesis/...`, `.../monitoring/...`) and an
  earlier phase's gate hasn't been approved yet, **exit code 2 blocks the
  write** and Claude sees the reason in its own context (Claude Code feeds
  stderr from an exit-2 PreToolUse hook back to the model).
- Writes into `screening/` are never blocked (it's the first phase).
- Writes anywhere *outside* a recognized phase subdirectory are not this
  hook's concern and are always allowed — this only governs the four phase
  output directories, not arbitrary file writes in the working tree.

## Approving a gate

Run this yourself, from an actual terminal, not through Claude:

```
python /absolute/path/to/AI-DDP/engine/aiddp_gate.py --root <engagement-dir> approve screening
```

It will ask you to interactively type the phase name back as confirmation.
This is deliberate — it only succeeds from a real interactive terminal
session, which an agent's own tool calls are not, so Claude cannot approve
its own gate by scripting a call to this file.

## SessionStart: automatic status on resume

The snippet also wires a `SessionStart` hook that prints the current
phase/gate status at the start of every session. You (or Claude) shouldn't
have to remember to ask "what phase are we in" after closing and reopening a
session; it's surfaced automatically.

## Known limitation

This only intercepts `Write`/`Edit`/`MultiEdit`-style tool calls with a
`file_path` in their input. A `Bash` command that redirects output into a
phase directory (e.g. `python script.py > underwriting/output.md`) is not
currently intercepted — the hook fails open (allows) for tool-input shapes it
doesn't recognize rather than blocking blindly. Extending the matcher to also
cover `Bash` and parsing shell redirection targets would close this gap but
isn't built yet.

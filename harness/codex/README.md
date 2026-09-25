# Codex CLI integration

Wires the same AI-DDP gate engine into Codex's native hook system, confirmed
against [OpenAI's Codex hooks documentation](https://developers.openai.com/codex/hooks).
Codex's hook schema (matcher / hooks array / `type: "command"` / stdin JSON /
exit-code-2-blocks convention) is close enough to Claude Code's that this is
nearly the same file — the only real differences are file location and a
one-time trust step.

## Install

1. Copy `hooks.json` from this folder to either:
   - `<engagement-dir>/.codex/hooks.json` (project-level, recommended — scopes
     the hook to this specific deal), or
   - `~/.codex/hooks.json` (user-level, applies everywhere)
2. Replace `/absolute/path/to/AI-DDP/engine/aiddp_gate.py` with the actual
   absolute path on your machine.
3. **Trust step, unique to Codex:** Codex requires you to explicitly trust a
   hook definition before it will run. Run `/hooks` inside the Codex CLI
   session to review and approve this hook (or pass
   `--dangerously-bypass-hook-trust` if you're certain — not recommended for
   routine use).
4. From the engagement's root directory, run:
   ```
   python /absolute/path/to/AI-DDP/engine/aiddp_gate.py init
   ```

## How it behaves

The `matcher` is left empty (fires on every tool call) rather than naming
specific tool names, because Codex's file-editing tool isn't necessarily
named the same thing as Claude Code's (`Write`/`Edit`) — I did not verify the
exact canonical name Codex uses for its patch/write tool, and guessing wrong
would silently make the hook never fire. The gate-check script itself already
fails open safely when it can't find a recognizable file-path field in the
event, so firing on every tool call and letting the script filter is the
more robust choice here, at the cost of the hook running (cheaply) more
often than strictly necessary.

Same blocking behavior as Claude Code: exit code 2 from the script blocks the
tool call and Codex is told why via stderr; exit code 0 allows it.

## SessionStart: automatic status on resume

Also wires `SessionStart` to print current phase/gate status at the start of
every session, so a resumed session doesn't lose track of where the deal
stands.

## Approving a gate

Same as Claude Code — run `approve` yourself from a real interactive
terminal, never through Codex:

```
python /absolute/path/to/AI-DDP/engine/aiddp_gate.py --root <engagement-dir> approve screening
```

## Swarm dispatch for the Underwriting phase

`stages/underwriting-swarm.md` defines a real parallel-dispatch protocol for
the six Underwriting-phase diligence stages. `.codex/agents/` in this repo
has the six agents as TOML files, confirmed against Codex's actual custom-
agent schema (`name`, `description`, `developer_instructions` fields; Codex
exposes `spawn_agent`, `wait_agent`, `send_message`, `list_agents`,
`close_agent` as its orchestration primitives). To run the swarm, explicitly
ask Codex to spawn the five Wave 1 agents in parallel and wait for all of
them before proceeding -- Codex does not spawn subagents on its own
initiative, it's prompt-driven (e.g., "spawn financial-diligence-agent,
commercial-diligence-agent, management-assessment-agent, financing-
capstructure-agent, and market-intelligence-agent in parallel against this
finalist, wait for all five, then run the reconciliation step from
stages/underwriting-swarm.md"). `legal-structuring-agent` only joins as
Wave 2, once a finalist is being seriously pursued.

Each `.codex/agents/*.toml` file's `developer_instructions` is a pointer,
not a duplicate of the real rules -- it tells the subagent to go read
`agents/<name>.md` and its knowledge-base files as its actual instructions.

## Known limitation

Same as the Claude Code integration: only tool calls that expose a
`file_path`/`path`-style field in `tool_input` are intercepted reliably.
Verify against your actual Codex version which tool name is used for file
writes, and consider narrowing the `matcher` once you've confirmed it, both
for clarity and to reduce how often the hook fires.

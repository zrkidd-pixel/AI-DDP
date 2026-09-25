# Architecture and Design Notes

This is the companion document for anyone evaluating, extending, or just
curious about *how* AI-DDP actually works underneath — not needed to use it.
If you just want to run a deal through it, `README.md` is enough.

## What's mechanically enforced, and what isn't

**Enforced, mechanically:** the four phase gates. `engine/aiddp_gate.py`
tracks state per deal and physically blocks an AI assistant from writing
into a later phase's folder until a gate has actually been approved. It
still cannot approve its own gate — that requirement doesn't go away, it
just has two legitimate paths:

- A real interactive terminal — the AI physically cannot do this one, since
  it requires typing the phase name back, and an agent's own tool calls
  don't attach a real TTY to stdin.
- `approve --chat` — the AI runs this itself, but *only after* a human has
  typed an explicit approval in the conversation, never on its own
  inference. The command itself has no way to verify anything; it just
  records whatever quote it's given. The actual guarantee here lives
  entirely in instructions repeated at every entry point (`CLAUDE.md`,
  `AGENTS.md`, `.kiro/steering/ai-ddp.md`, `agents/composer.md`,
  `knowledge/composer/gate-state-protocol.md`) telling the AI never to call
  it without the human's literal words. This is a real tradeoff between
  convenience and independently-verifiable rigor, not a loophole nobody
  noticed — know which one you're relying on for a given deal.

**Not yet enforced, still just documented:** the finer *within-phase*
dependencies in `stages/underwriting.md` (for example, that Underwriting's
core LBO math needs Financial Diligence's and Financing's output first).
The engine enforces the four big phase boundaries; it doesn't yet parse and
check the full stage-level `produces`/`consumes` graph automatically. That's
the natural next extension, not something built into this version.

## Why the audit trail is a rendered file, not raw JSON

`.aiddp/state.json` is the actual source of truth, but nobody should have
to read JSON to know where a deal stands. `aiddp-state.md` is regenerated
from it on every single save — one choke point, so it can never drift —
and its "Stage Activity" section specifically surfaces the most recent
*substantive* log entry per phase, filtering past the engine's own
"Gate approved" bookkeeping messages. That mechanism only has content if
agents actually log real summaries instead of "done," which is why every
entry point explicitly requires it (see `CLAUDE.md` point 6).

## The parallel Underwriting swarm

Six of the Underwriting-phase stages have no dependency on each other and
can be dispatched concurrently rather than run one at a time. The full
protocol — scope (per-finalist, not per-candidate), the output contract
each stage must return, and how conflicting findings between two parallel
stages get reconciled (domain authority first, unresolved conflicts
escalate to the human) — lives in `stages/underwriting-swarm.md`, not
repeated here. Harness-specific dispatch mechanics (verified against each
tool's actual docs, not assumed uniform across all three) are in
`harness/*/README.md` and `.claude/agents/` / `.codex/agents/`.

## How extensions activate without cluttering every deal

`extensions/` holds opt-in rule packs for situational deal characteristics
(cross-border structuring, ESG mandates, distressed diligence) that don't
apply to every deal. Screening asks about the trigger conditions during the
mandate interview and records which apply in the deal's own
`fund-mandate.md`; downstream agents check that field and read the relevant
`.opt-in.md` file only when it's actually active. See `extensions/README.md`
for the mechanism and how to add a new one.

## Two distinct claim-quality disciplines

`knowledge/_shared/citation-standards.md` and `knowledge/_shared/
overconfidence-prevention.md` look similar but catch different failures.
Citation standards stop an *unsourced* claim from being stated as fact.
Overconfidence prevention stops a *sourced but genuinely uncertain*
judgment (management fit from two reference calls, a market-sizing
midpoint) from being stated with more confidence than the evidence actually
supports. A claim can pass one check and fail the other.

## A verification discipline this project holds itself to

Every claim in this repo about how a specific tool (Claude Code, Codex,
Kiro) actually behaves was checked against that tool's own published
documentation before being written down as fact — not assumed from a
plausible-sounding pattern. Where that verification wasn't possible (Kiro's
exact `.kiro/agents/`/hook field names), the repo says so explicitly rather
than guessing and hoping. This matters more than it might seem: a framework
about not trusting unsourced claims should not itself ship unsourced claims
about its own mechanics.

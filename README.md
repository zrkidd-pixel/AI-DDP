# AI-DDP: AI-Driven Deal Diligence Protocol

A structured way to do AI-assisted private equity deal work: four phases,
14 specialized agents, a domain knowledge base, and an enforcement engine
that stops work from moving forward without a human's sign-off.

The idea in one sentence: **the AI proposes, asks questions, and shows its
work — but a human has to explicitly approve before it moves to the next
phase, and every decision is saved so the work can be reviewed later.**

## Table of Contents

- [What using this actually feels like](#what-using-this-actually-feels-like)
- [Quick start](#quick-start)
- [The four phases](#the-four-phases)
- [The 14 agents](#the-14-agents)
- [Extensions: opt-in depth for situational deals](#extensions-opt-in-depth-for-situational-deals)
- [Tenets](#tenets)
- [Repository map](#repository-map)
- [Troubleshooting](#troubleshooting)
- [Version control for your deal folder](#version-control-for-your-deal-folder)
- [What this is not](#what-this-is-not)
- [Architecture and design notes](#architecture-and-design-notes)

---

## What using this actually feels like

1. You tell your AI assistant to start, naming AI-DDP and which phase you're
   in (or let it ask, if it's not obvious).
2. It reads the right rule file and gets to work — screening candidates,
   running the LBO math, drafting the thesis, or tracking a portfolio
   company, depending on the phase.
3. Along the way, it asks specific, narrowed questions instead of guessing —
   never more of them than it actually needs. When a data gap needs a
   licensed source rather than the open web, it names the specific
   source and report to pull (e.g., "an IBISWorld industry report for
   [NAICS code]"), not a generic "do you have more data?"
4. When something's uncertain, missing, or looks wrong in the data, it says
   so instead of quietly smoothing it over.
5. When a phase is genuinely done, you review what it produced and say
   "approved" — or you don't, if it isn't there yet.
6. The next phase only unlocks once you've actually said so. Nothing moves
   forward because the AI decided on its own that the work looked ready.
7. Everything gets written down — every decision, every approval, every gap
   — in a state file you can open and read at any point, not buried in a
   chat transcript.

---

## Quick start

1. **Set up the deal folder in one command:**
   ```
   python <path-to-AI-DDP>/engine/aiddp_new_deal.py <your-deal-folder> --harness claude-code
   ```
   (use `--harness codex` for Codex, or leave it off and wire Kiro manually
   per `harness/kiro/README.md` — its exact hook format isn't confirmed
   yet). This one command creates the four phase subfolders, sets up the
   engagement state, and wires the gate hook into your tool — merging
   safely into an existing `.claude/settings.json` or `.codex/hooks.json`
   if you already have one, never overwriting it.
2. **Fill in the fund mandate** — the setup command already copied a blank
   one to `<your-deal-folder>/fund-mandate.md`. You can fill it in yourself,
   or just skip straight to step 3: the Screening Agent checks it first and
   will ask you for whatever's still blank (equity check range, sector,
   geography, return targets), then write your answers into the file
   itself.
3. **Tell your AI assistant to start**: *"Using the AI-DDP, act as the
   Screening Agent for this deal."* If `CLAUDE.md`, `AGENTS.md`, or
   `.kiro/steering/ai-ddp.md` is loaded in your tool, it already knows what
   that means.
4. **When a phase is genuinely finished, approve it.** Two ways:
   - Just say so in the conversation — *"approved."* Your AI assistant runs
     `aiddp_gate.py approve <phase> --chat --quote "approved"` on your
     behalf and the next phase unlocks.
   - Or run it yourself, from a real terminal, if you want the stricter
     version where the AI can't be the one recording it:
     ```
     python <path-to-AI-DDP>/engine/aiddp_gate.py --root <your-deal-folder> approve screening
     ```
   Until one of these happens, the AI is physically blocked from writing
   into the next phase's folder.

That's the whole loop: work happens → you review it → you approve it → the
next phase unlocks. Repeat through Underwriting, Thesis, and Monitoring.

**To check where things stand, open `<your-deal-folder>/aiddp-state.md`** —
current phase, which gates are approved and how, and a running summary of
what actually got produced at each stage. It's regenerated automatically
every time anything changes, so it's always current; never hand-edit it.

---

## The four phases

| Phase | Answers | What happens |
|---|---|---|
| **Screening** | *Which target, against what criteria?* | Define the mandate and sector, filter candidates against it, flag any data-quality gaps before running numbers. |
| **Underwriting** | *Is the deal economically sound, and what are the risks?* | LBO math, comps, and every diligence workstream (financial, commercial, management, legal, financing) running against the finalists. |
| **Thesis** | *Should we do this, and why?* | Everything above gets synthesized into the actual investment memo and value-creation plan — written *last*, once you know what the numbers say, not in advance. |
| **Monitoring** | *Is reality tracking the plan?* | After close: track results against the plan, with defined triggers that send a deal back to Underwriting (or Screening) if something breaks. |

Six of the Underwriting stages (Financial Diligence, Commercial Diligence,
Management Assessment, Financing/Capital Structure, Market Intelligence,
and Legal & Structuring) can run **in parallel** rather than one at a time —
see `stages/underwriting-swarm.md` for how that works and how disagreements
between them get resolved. The full phase-to-phase map is in
`stages/_dependency-graph.md`.

---

## The 14 agents

| Phase | Agents |
|---|---|
| Screening | Screening Agent |
| Underwriting | Underwriting/LBO · Financial Diligence/QoE · Commercial Diligence · Management Assessment · Legal & Structuring · Financing/Capital Structure · Market & Sector Intelligence |
| Thesis | Value Creation/100-Day Planning · Thesis/IC Memo |
| Monitoring | Monitoring Agent |
| Always-on reviewers | Verification (double-checks the numbers independently) · Compliance/MNPI (clears any non-public data before it's used) |
| Orchestrator | Composer (tracks which gate is open, enforces approval, keeps the log) |

Every agent has its own rule file in `agents/` — what it needs, what it
produces, its specific rules, when it stops to ask a human, and what has to
be true before it hands off to the next agent. Two house-style rules apply
across all 14: `knowledge/_shared/question-format-guide.md` governs how any
agent phrases a question to a human, and `knowledge/_shared/overconfidence-
prevention.md` governs how a judgment call gets stated with confidence
proportional to its actual evidence (see `ARCHITECTURE.md` for how that
differs from citation-standards.md). A third,
`knowledge/_shared/data-source-directory.md`, maps specific data gaps to
specific licensed sources and reports (Capital IQ, SEC EDGAR, IBISWorld,
Factiva, LSEG Workspace, PitchBook, Preqin, Crunchbase) — so 11 of the 14
agents can suggest exactly what to pull, not just that more data would
help.

---

## Extensions: opt-in depth for situational deals

Not every deal needs cross-border tax structuring, ESG-mandate compliance,
or distressed-specific diligence — but some genuinely do, and baking all of
it into the core 14 agents permanently would clutter every plain-vanilla
deal in service of the uncommon one. `extensions/` holds opt-in rule packs
instead: Screening asks about the trigger conditions during the mandate
interview, records which apply in the deal's own `fund-mandate.md`, and the
relevant downstream agents pick up the extra depth automatically. See
`extensions/README.md` for the full list and how to add a new one.

---

## Tenets

Principles that shaped every design decision above, made explicit:

- **No duplication.** The source of truth lives in one place. When a rule
  applies to more than one agent, it goes in one shared knowledge file that
  every agent it applies to actually references — not restated with
  slightly different wording in each one.
- **Ask, and use context to sharpen the question — never to skip it.**
  Background a human offers narrows what gets asked; it never substitutes
  for an actual answer to it.
- **Sourced, or labeled as an assumption — never blended.** Every
  substantive claim carries a citation tag or an explicit assumption label.
  Nothing sits in between as an unmarked guess.
- **Confidence proportional to evidence, not to how confidently it's
  phrased.** A claim can be fully sourced and still overstated if the
  underlying evidence is thin — that's checked separately from citation
  coverage.
- **Human approval is mechanical, not just polite.** A gate doesn't open
  because the AI decided the human sounded satisfied. It opens because a
  human's own keystrokes or literal words were recorded, one of two
  independently real ways.
- **Verify before you claim it's real.** Nothing about how a specific tool
  behaves gets written down as fact until it's checked against that tool's
  own documentation. Where it couldn't be verified, that's stated
  explicitly, not guessed around.

---

## Repository map

```
AI-DDP/
  README.md                    <- this file
  ARCHITECTURE.md               <- how it works underneath, for anyone curious
  CLAUDE.md / AGENTS.md         <- entry points auto-loaded by Claude Code / Codex
  .kiro/steering/ai-ddp.md      <- entry point auto-loaded by Kiro
  agents/                       <- one rule file per agent (14 files)
  knowledge/                    <- the reference material each agent reads
  stages/                       <- the dependency graph, phase by phase
  engine/aiddp_gate.py          <- the gate-enforcement engine
  engine/aiddp_new_deal.py      <- one-command setup for a new deal
  harness/                      <- setup instructions per AI tool
  .claude/agents/  .codex/agents/  <- ready-to-use subagents for the Underwriting swarm
  extensions/                   <- opt-in rule packs for situational deal
                                    characteristics (cross-border, ESG,
                                    distressed) not baked into the core 14
```

---

## Troubleshooting

| Problem | Likely cause / fix |
|---|---|
| A write isn't being blocked when you expected it to be | The hook only reliably catches `Write`/`Edit`-style tool calls with a `file_path` field — a `Bash` command that redirects output into a phase folder isn't intercepted yet. See the "Known limitation" note in `harness/*/README.md`. |
| The AI seems to have approved its own gate | This should never happen. Open `aiddp-state.md`'s audit log and check the quoted words it recorded as your approval — if there's no real quote, or it doesn't match anything you said, that's a bug in the AI's behavior against its own instructions, not the engine's. |
| Hooks aren't firing at all in Kiro | Kiro's exact hook field names weren't confirmed when this was built. Scaffold a throwaway hook through Kiro's own UI first and compare its field names against `harness/kiro/README.md` before assuming the shipped config is correct. |
| `approve` keeps refusing even though you're at a real terminal | Some embedded/IDE terminals don't attach a real TTY to stdin even though they look interactive. Try a plain OS terminal window, or use `approve --chat` instead. |
| State doesn't seem to be updating | Check you're passing the same `--root <engagement-dir>` every time. State is per-directory — running from the wrong folder silently talks to (or creates) a different engagement. |
| `aiddp-state.md` looks wrong or stale | Never hand-edit it — it's regenerated from `.aiddp/state.json` on every save. If it looks wrong, the problem is in `state.json` or in what got logged, not in the rendering. |

---

## Version control for your deal folder

Commit, once real content exists:
- `fund-mandate.md` — the record of what was actually agreed for this deal
- `.aiddp/state.json` and `aiddp-state.md` — the state and its
  human-readable rendering; both, since the JSON is the actual source of
  truth and the markdown can't be reconstructed from nothing
- `.claude/settings.json` / `.codex/hooks.json` — so the hook wiring travels
  with the deal folder for anyone else who works on it
- `screening/`, `underwriting/`, `thesis/`, `monitoring/` — the actual work
  product

Think before committing, specifically because this is deal data, not code:
if any of the above contains material non-public information, follow your
firm's actual data-handling policy before pushing it anywhere shared —
`agents/compliance-mnpi-agent.md` exists precisely because "it's just a
local git repo" is not the same question as "is this cleared to leave the
room."

---

## What this is not

- **Not a fund's actual investment process.** It's a discipline for how
  AI-assisted deal work gets structured and reviewed.
- **Not legal or tax advice.** The Legal & Structuring Agent routes
  questions to counsel — it doesn't replace counsel.
- **Not a compliance program.** The Compliance/MNPI Agent points to a
  firm's real AI usage policy — it doesn't substitute for one.

The substance of any real recommendation still depends on real data, real
diligence, and real human judgment at every gate. This just makes sure that
judgment actually gets exercised, on the record, before work moves forward.

---

## Architecture and design notes

What's mechanically enforced versus just documented, why the audit trail is
a rendered file instead of raw JSON, how the parallel Underwriting swarm and
its conflict-reconciliation actually work, and the verification discipline
this repo holds itself to — see **[ARCHITECTURE.md](ARCHITECTURE.md)**.

# AI-DDP: AI-Driven Deal Diligence Protocol

A structured way to do AI-assisted private equity deal work: four phases,
14 specialized agents, a domain knowledge base, and an enforcement engine
that stops work from moving forward without a human's sign-off.

The idea in one sentence: **the AI proposes, asks questions, and shows its
work — but a human has to explicitly approve before it moves to the next
phase, and every decision is saved so the work can be reviewed later.**

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

| Phase | What happens |
|---|---|
| **Screening** | Define the mandate and sector, filter candidates against it, flag any data-quality gaps before running numbers. |
| **Underwriting** | LBO math, comps, and every diligence workstream (financial, commercial, management, legal, financing) running against the finalists. |
| **Thesis** | Everything above gets synthesized into the actual investment memo and value-creation plan — written *last*, once you know what the numbers say, not in advance. |
| **Monitoring** | After close: track results against the plan, with defined triggers that send a deal back to Underwriting (or Screening) if something breaks. |

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
prevention.md` governs how a judgment call (management fit, competitive
durability, market sizing) gets stated with confidence proportional to its
actual evidence — a different discipline than citation-standards.md, which
only stops *unsourced* claims, not *overstated but sourced* ones.

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

## Repository map

```
AI-DDP/
  README.md                    <- this file
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

## Design notes: what's actually enforced, and what isn't

**Enforced, mechanically:** the four phase gates. `engine/aiddp_gate.py`
tracks state per deal and physically blocks an AI assistant from writing
into a later phase's folder until a gate has actually been approved. It
still cannot approve its own gate — that requirement doesn't go away, it
just has two legitimate paths now: a real interactive terminal (the AI
physically can't do this one, since it requires typing the phase name
back), or `approve --chat`, which the AI runs *only after* you've typed an
explicit approval in the conversation, never on its own inference. The
`--chat` path is more convenient, but be clear-eyed about what it's
actually trading away: the command itself can't verify anything, so the
guarantee comes entirely from the AI waiting for your literal words rather
than deciding on its own that the work looks done — a real tradeoff, not a
loophole nobody noticed.

**Not yet enforced, still just documented:** the finer *within-phase*
dependencies in `stages/underwriting.md` (for example, that Underwriting's
core LBO math needs Financial Diligence's and Financing's output first).
The engine enforces the four big phase boundaries; it doesn't yet check
those smaller dependencies automatically. That's the natural next step, not
something built into this version — flagged here rather than left for
someone to discover the hard way.

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

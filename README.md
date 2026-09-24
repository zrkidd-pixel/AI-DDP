# AI-DDP: AI-Driven Deal Diligence Protocol

A private-equity adaptation of [AWS's AI-Driven Development Life Cycle
(AI-DLC)](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle) —
the same core idea (AI proposes, asks clarifying questions, and implements
only after human approval, with every decision persisted for traceability),
rebuilt around a PE deal's actual workflow instead of a software team's.

## Lineage, and one honest caveat

AI-DLC exists in two forms that matter differently here:

1. **The original blog post concept** — a simple, three-phase methodology
   (Inception → Construction → Operations) with human approval gates and
   persistent context. This is what AI-DDP is actually modeled on.
2. **The current [aidlc-workflows](https://github.com/awslabs/aidlc-workflows)
   GitHub repo** — has since grown into "AI-DLC Workflows 2.0": 5 phases, 33
   stages, 14 software-specific agents, and 85+ TypeScript files implementing
   a compiled orchestration engine with its own YAML schema. That engine is
   tightly coupled to software-development artifacts (code, architecture,
   deployments, git repos) and isn't something a non-engineering team should
   try to fork wholesale.

**AI-DDP borrows patterns from the 2.0 repo (stage dependencies, a
claim-sourcing discipline, adversarial vs. advisory reviewers, scoping rigor
to job size) but implements them as plain markdown files an AI assistant
reads directly each session, plus a small standalone enforcement engine
(`engine/`) instead of a compiled 85-file TypeScript system.**

**What is mechanically enforced, not just written down:** phase-level
gating. `engine/aiddp_gate.py` is a harness-neutral, dependency-free Python
script that maintains a state file per engagement and physically blocks an
AI assistant from writing into a later phase's output directory
(`underwriting/`, `thesis/`, `monitoring/`) until a human has explicitly
approved every phase before it — via a PreToolUse hook wired into Claude
Code, Codex, and Kiro (see `harness/`). The `approve` command only works from
a real interactive terminal and requires typing the phase name back, so an
agent cannot approve its own gate by scripting a call to it.

**What is still procedural, not mechanical:** the finer-grained *within-phase*
stage dependencies documented in `stages/underwriting.md` (e.g., that the
`underwriting` stage specifically needs `financial-diligence`'s and
`financing-capstructure`'s output before it can finalize). The engine
enforces the four big phase boundaries; it does not yet parse and enforce the
full stage-level `produces`/`consumes` graph. That would be the natural next
extension, not something built into this version.

**A correction worth stating plainly:** AI-DLC 2.0's `core/hooks/` directory
(session start/end, state-transition guarding, audit logging, workflow
resumption) is *not* software-specific the way its agents are — those are
generic AI-session-lifecycle mechanics, and AI-DDP's engine lifts two of them
directly: `hook-pretooluse` is the state-transition guard, and `state.json`'s
log array is the audit log. `hook-sessionstart` (added to all three harness
configs) lifts a third — surfacing current phase/gate status automatically
when a session resumes, so nobody has to remember to ask. The one hook
deliberately left out is a persistent status-line display (AI-DLC's
`aidlc-statusline.ts`) — genuinely Claude-Code-specific UI with no equivalent
concept in Codex or Kiro, and low value relative to the harness-specific
special-casing it would require.

## The four phases

Renamed from AI-DLC's software-lifecycle phases into PE's own deal-lifecycle
vocabulary — and reordered in one place, deliberately: Thesis comes *after*
Underwriting, not before, because a real investment thesis is a synthesis of
what the screen and the numbers actually showed, not a narrative written in
advance and backfilled with supporting figures.

| Phase | What happens |
|---|---|
| **Screening** | Define the mandate and sector, filter a candidate universe against it, surface data-taxonomy gaps before computing anything. |
| **Underwriting** | The LBO math, comps, and every diligence workstream (financial/QoE, commercial, management, legal/structuring, financing) running against the candidate set. |
| **Thesis** | Synthesize everything above into the actual investment narrative, value-creation plan, and IC memo — written last, not first. |
| **Monitoring** | Post-close: track actual results against the underwritten plan, with defined triggers that loop back into Underwriting (or Screening, if the sector thesis itself breaks) rather than running open-ended. |

See `stages/_dependency-graph.md` for the full pipeline diagram.

## The 14 agents

11 domain experts + 2 reviewers (adversarial / advisory) + 1 orchestrator —
mirroring AI-DLC's own 11+2+1 structure, but every one of AI-DLC's original
software roles (architect, developer, devsecops, pipeline-deploy, etc.) has
been replaced with a standard institutional PE function instead of relabeled:

- **Screening** — Screening Agent
- **Underwriting** — Underwriting/LBO Agent, Financial Diligence/QoE Agent,
  Commercial Diligence Agent, Management Assessment Agent, Legal &
  Structuring Agent, Financing/Capital Structure Agent, Market & Sector
  Intelligence Agent
- **Thesis** — Value Creation/100-Day Planning Agent, Thesis/IC Memo Agent
- **Monitoring** — Monitoring Agent
- **Reviewers** — Verification Agent (adversarial: re-derives outputs
  independently), Compliance/MNPI Agent (advisory but mandatory: gates any
  non-public information before it's used)
- **Orchestrator** — Composer (tracks gate state, enforces human approval,
  logs everything)

Full rule file for each agent — mission, what it consumes/produces, its
specific operating rules, when it escalates, and its gate criteria — is in
`agents/`.

## Repository structure

```
AI-DDP/
  README.md                    <- this file
  CLAUDE.md                    <- entry point auto-loaded by Claude Code
  AGENTS.md                    <- entry point auto-loaded by Codex
  .kiro/steering/ai-ddp.md     <- entry point auto-loaded by Kiro
  agents/                      <- one operating-rules file per agent (14 total)
  knowledge/                   <- domain reference content each agent reads
    _shared/                   <- fund mandate, citation standards, glossary,
                                   data-source crosswalk (read by everyone)
    screening/
    underwriting/
    financial-diligence/
    commercial-diligence/
    management-assessment/
    legal-structuring/
    financing-capstructure/
    market-intelligence/
    value-creation/
    thesis-icmemo/
    monitoring/
    verification/
    compliance-mnpi/
    composer/
  stages/                       <- the dependency graph: which stage requires,
                                    consumes, and produces what, per phase
  engine/
    aiddp_gate.py               <- harness-neutral gate-enforcement engine
                                    (stdlib Python, no dependencies)
  harness/                      <- thin, tool-specific wiring for the engine
    claude-code/                   (verified against Claude Code's own hooks docs)
    codex/                         (verified against OpenAI's Codex hooks docs)
    kiro/                          (partially verified -- see its README)
```

## How "using the AI-DDP..." actually works

Saying that phrase doesn't do anything on its own — it works because
`CLAUDE.md`, `AGENTS.md`, and `.kiro/steering/ai-ddp.md` are auto-loaded by
their respective tools at session start, and each one tells the model what
to do when it hears a trigger phrase like that: bootstrap by reading
`README.md`, check `.aiddp/state.json` for engagement state, ask which phase
if unclear, then load that phase's specific agent file and referenced
knowledge before doing any work. If you're using a tool other than Claude
Code, Codex, or Kiro, there's no auto-loaded entry point yet — paste one of
those three files' contents into your tool's own context manually, or just
tell the AI directly to read `README.md` first.

## How to actually use this

1. Fill in `knowledge/_shared/fund-mandate.md` for the specific fund/deal —
   nothing downstream should run against a placeholder mandate.
2. Set up a working directory for this specific engagement (not inside the
   AI-DDP repo itself) with one subfolder per phase:
   `screening/`, `underwriting/`, `thesis/`, `monitoring/`. Run
   `python <path-to-AI-DDP>/engine/aiddp_gate.py init` from that directory.
3. Wire up the PreToolUse hook for whichever AI tool you're using — see
   `harness/claude-code/README.md`, `harness/codex/README.md`, or
   `harness/kiro/README.md`. This is what makes the gates real rather than
   just documented.
4. Point your AI assistant at this repo and tell it which phase you're in
   (e.g., "act as the Screening Agent per `agents/screening-agent.md`").
   Have it read that agent's file and the knowledge files it references
   before starting, and write its output into that phase's subfolder.
5. Work through each phase's stages per `stages/<phase>.md` — parallel
   diligence workstreams can run together, but respect the `requires_stage`
   hard dependencies (Underwriting's core LBO math cannot finalize without
   Financial Diligence's adjusted EBITDA and Financing's sourced terms).
6. When a phase is genuinely done, approve it yourself, from a real
   terminal: `python <path-to-AI-DDP>/engine/aiddp_gate.py --root
   <engagement-dir> approve <phase>`. Until you do, the hook will physically
   block the AI assistant from writing into the next phase's folder — this
   is no longer just a rule the AI is trusting itself to follow.
7. When Monitoring's triggers fire post-close, loop back into Underwriting
   (or Screening, if the sector thesis itself has broken) rather than
   treating the pipeline as one-way — you'll need to re-approve the relevant
   gate again before work can proceed into it a second time.

## What this is not

Not a fund's actual investment process, not legal or tax advice (see
`agents/legal-structuring-agent.md` — it routes to counsel, it doesn't
replace counsel), and not a compliance program (`agents/compliance-mnpi-agent.md`
points to a firm's real AI usage policy; it doesn't substitute for one). This
is a discipline for how AI-assisted deal work gets structured and reviewed —
the substance of any real recommendation still depends on real data, real
diligence, and real human judgment at every gate.

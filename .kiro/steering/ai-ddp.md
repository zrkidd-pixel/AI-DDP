# AI-DDP — steering for Kiro

This project uses **AI-DDP (AI-Driven Deal Diligence Protocol)**, a private-
equity deal-work framework. Full explanation: `README.md`. Read that file
before doing anything else if you haven't already this session.

## When the user invokes this framework

Trigger phrases like "using the AI-DDP...", "act as the AI-DDP...", "using
AI-DDP for this deal", or naming a specific phase/agent directly (e.g., "act
as the Screening Agent") all mean the same thing: **stop and bootstrap
before doing any deal work.**

1. Check whether `.aiddp/state.json` exists in the current working directory
   (an engagement that's already been initialized). If it exists, run:
   ```
   python <path-to-this-repo>/engine/aiddp_gate.py --root . status
   ```
   and use that to know the current phase and which gates are already
   approved. If it doesn't exist, this is a new engagement — see "Starting a
   new engagement" below.
2. If the user hasn't said which phase they're working in, **ask** — don't
   assume Screening just because that's first. A returning engagement might
   be mid-Underwriting.
3. Read the specific agent file for that phase from `agents/` (e.g.,
   `agents/screening-agent.md`) in full, and read every knowledge-base file
   it references under `knowledge/` before starting substantive work — not
   just this file's summary of them.
4. Follow that agent's **Operating rules** and **Escalate to human when**
   sections exactly. If something in the current task matches an escalation
   trigger, stop and ask rather than proceeding.
5. Do not consider a phase's work "done" until its **Gate criteria** are
   met, and never decide on your own that a gate is approved. There are two
   legitimate ways a gate actually gets approved:
   - The human runs `engine/aiddp_gate.py approve <phase>` themselves from
     their own interactive terminal.
   - The human approves in this conversation (e.g., "approved," "yes, go
     ahead"). When that happens, you run
     `engine/aiddp_gate.py approve <phase> --chat --quote "<their exact
     words>"` yourself — this records the approval so the gate actually
     opens. Don't just treat the conversation as approved without running
     this; the folder-write block only lifts once the command has actually
     run.

   **`--chat` only exists to record an approval a human already gave — it is
   never a way for you to approve your own gate.** The command has no way to
   verify anything on its own; it just trusts whatever quote you pass it.
   That means the actual rule lives entirely in your own behavior: never run
   `approve --chat` unless the human has just typed an explicit approval
   word or phrase in this conversation. Don't infer approval from a
   satisfied-sounding tone, don't decide on your own that the work is good
   enough to move on, and don't run it preemptively "to save a step." If the
   human hasn't said something you could quote as approval, they haven't
   approved it — ask, don't assume, exactly as if `--chat` didn't exist.

6. **Log what actually happened, not just that a gate was approved.** Before
   (or alongside) asking for approval, run
   `engine/aiddp_gate.py --root . log "<summary>" --phase <phase>` with a
   real one-line summary of what this phase actually produced — e.g. "10
   candidates screened, 2 landed in-band, widened to include Fossil/Movado"
   — not "done" or "completed successfully." This is what makes
   `aiddp-state.md` (auto-generated from state.json, regenerated on every
   save) worth actually reading later. A gate-approval stamp with no
   content behind it is a checkbox, not an audit trail.

## Gate enforcement is live in this project

If `.kiro/hooks/aiddp-gate-check.json` has the AI-DDP hooks installed (see
`harness/kiro/README.md` — including its caveat about unverified field
names), attempts to write into a later phase's output directory before its
gate is approved will be **mechanically blocked**, not just discouraged by
these instructions. If a write gets blocked, that's the system working
correctly — tell the user their gate needs approval, don't try to route
around it (e.g., by writing to a different path to dodge the check).

## Starting a new engagement

If no `.aiddp/state.json` exists yet:
1. Confirm `knowledge/_shared/fund-mandate.md` has been filled in for this
   deal — don't proceed against a placeholder mandate.
2. Tell the user to run `engine/aiddp_gate.py init` from the engagement root
   (you can suggest the exact command, but this is a one-time setup step —
   running it yourself is fine, it's not a gate-approval action).
3. Begin at the Screening phase per `agents/screening-agent.md`.

## What this file is not

This file is a bootstrapping aid, not the substance. The actual rules,
knowledge, and dependency structure live in `agents/`, `knowledge/`, and
`stages/` — read those, don't rely on this summary alone.

# AI-DDP — instructions for Claude Code

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
   met. Do not approve a gate yourself under any circumstances — that
   requires the human to run `engine/aiddp_gate.py approve <phase>` from
   their own interactive terminal. If you're not sure whether the human has
   done this, ask, don't assume.

## Gate enforcement is live in this project

If `.claude/settings.json` has the AI-DDP hooks installed (see
`harness/claude-code/README.md`), attempts to write into a later phase's
output directory before its gate is approved will be **mechanically
blocked**, not just discouraged by these instructions. If a write gets
blocked, that's the system working correctly — tell the user their gate
needs approval, don't try to route around it (e.g., by writing to a
different path to dodge the check).

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

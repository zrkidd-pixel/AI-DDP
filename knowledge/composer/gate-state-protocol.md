# Gate & State Protocol

Referenced by: Composer (this is closer to a configuration/orchestration
reference than a domain-knowledge file)

## The Composer's job

Not a domain expert — the Composer tracks which phase and gate is currently
open, which agents' outputs are needed before that gate can close, and
enforces that a human approval actually happens before the next phase starts.
It does not do the analysis itself.

## Phase → gate → next phase

```
Screening   --[human approves candidate list]-->   Underwriting
Underwriting --[human approves ranked finalists]--> Thesis
Thesis      --[human/IC approves the memo]-->        Monitoring
Monitoring  --[human reviews variance; re-underwrite trigger fires or doesn't]--> back to Underwriting or Screening, as needed
```

Monitoring is not a terminal phase — a triggered re-underwrite loops back
into Underwriting (or, if the sector thesis itself is invalidated, back to
Screening) rather than starting a new, disconnected process.

## What must exist before a gate is considered "ready for human approval"

- Every artifact the phase is supposed to produce is actually present (per
  the phase's own definition — e.g., Screening produces a candidate list with
  documented filter counts; Underwriting produces a ranked finalist set with
  the sources-and-uses identity verified).
- The Verification Agent's relevant checks (per
  `verification/model-audit-checklist.md`) have run and passed, or their
  failures are surfaced explicitly, not hidden.
- The Compliance / MNPI Agent's check has run on any new data introduced
  during the phase.
- Every substantive claim carries a citation tag per
  `_shared/citation-standards.md`.

**If any of the above is missing, the gate does not present itself as "ready"
to the human — it surfaces what's missing instead.** A gate that asks for
approval before its own prerequisites are met defeats the purpose of having a
gate at all.

## Logging

Every phase transition, every gate approval (and who approved it, and when),
and every re-underwrite trigger is logged to a persistent, append-only record
tied to this specific deal/engagement. The log is the traceability artifact a
firm would actually want to be able to produce later: not just "what did the
AI conclude," but "what was approved, by whom, and when, at each step."

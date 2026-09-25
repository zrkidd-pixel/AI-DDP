# Underwriting Swarm Protocol

What actually happens when the six parallel Underwriting-phase stages run
concurrently instead of one at a time, including how conflicting findings
between them get resolved before Underwriting Agent finalizes anything.

## Scope: which candidates the swarm runs against

**The swarm does not run against the full Screening candidate list.** The
mechanical LBO math (Underwriting Agent's own equity-check calculation) does
— it's cheap and runs against every candidate that cleared Screening. The
six diligence/research stages below are expensive, investigative work; in
real practice nobody does full QoE, management reference checks, and legal
structuring review on ten candidates. The swarm activates **after** an
initial ranking narrows the field to a small number of finalists (typically
2-5, per the mandate's own finalist-count rule from `screening/fund-criteria-
checklist.md`) — one swarm wave per finalist under active consideration, not
one wave for the whole candidate list.

## Which stages swarm, and in what wave

**Wave 1 (always, per finalist):** Financial Diligence, Commercial
Diligence, Management Assessment, Financing/Capital Structure, Market &
Sector Intelligence — five independent stages with no `requires_stage`
dependency on each other (per `stages/underwriting.md`), dispatched
concurrently against the same finalist.

**Wave 2 (conditional, per finalist that survives Wave 1):** Legal &
Structuring joins once a finalist is seriously being pursued, not before —
its own execution rule already says this (`agents/legal-structuring-
agent.md`).

## Output contract every swarming stage must produce

A stage's output isn't done when it has an answer — it's done when the
output can be mechanically cross-checked against the other five stages'
outputs. Every stage returns:

1. **Findings**, each tagged per `_shared/citation-standards.md`
   (`[data]`/`[source]`/`[assumption]`/`[calc]`) — no untagged claims, same
   rule as everywhere else in this framework.
2. **Cross-domain facts referenced** — an explicit list of any specific
   number or claim the stage used that falls *outside* its own primary
   domain (e.g., if Financial Diligence's earnings-quality adjustment relies
   on a customer-concentration percentage, that percentage gets listed here,
   not just used silently). This is the field the reconciliation step below
   actually reads.
3. **Escalation triggers hit**, if any, per that stage's own `agents/*.md`
   file — reported here even though they'd also stop that stage's own work,
   so the reconciliation step has full visibility across all six stages at
   once rather than hearing about each escalation one at a time.

## Reconciliation: the step between the swarm finishing and Underwriting Agent starting

This does not happen automatically just because all six stages returned an
answer. Whoever dispatched the swarm (the primary session, or the Composer
if it's doing the dispatching) runs this explicitly once every stage in the
current wave has returned:

1. **Wait for the full wave**, not a partial set. If a stage is blocked
   (hit one of its own escalation triggers and can't produce a final
   output), that counts as the wave not being complete — don't reconcile
   around a gap and proceed as if it were finished.
2. **Collect every stage's "cross-domain facts referenced" list** and check
   for overlaps: did two stages reference the same underlying fact (same
   entity, same metric, same time period)?
3. **If two stages agree on an overlapping fact**, nothing to do — that's
   corroboration, worth noting in the handoff to Underwriting Agent as a
   point of confidence, not just silently dropped.
4. **If two stages disagree on an overlapping fact**, resolve by domain
   authority first: the stage whose primary knowledge base actually governs
   that fact type is authoritative for the *fact itself* (e.g., Commercial
   Diligence's customer-concentration percentage is authoritative over
   Financial Diligence's, since concentration is computed from
   `commercial-diligence/customer-concentration-frameworks.md`'s own
   methodology) — but the *other* stage's interpretation of that fact within
   its own domain still stands (Financial Diligence's earnings-quality
   judgment about what that concentration level implies for adjusted EBITDA
   is still Financial Diligence's call, even once the underlying number
   itself is corrected to match Commercial Diligence's).
5. **If domain authority doesn't cleanly resolve it** (the two stages are
   making genuinely competing claims about the same thing, not just one
   being more authoritative), **do not silently pick one** — this escalates
   to the human exactly like any other agent-level escalation trigger,
   surfaced explicitly as an unresolved cross-stage discrepancy, not folded
   into whichever stage's narrative reads more confidently.
6. **Only after reconciliation is complete** does the combined output get
   handed to Underwriting Agent as its `Financial Diligence` /
   `Commercial Diligence` / etc. inputs per its own Consumes list.

## Why this matters more than it might seem

Two parallel agents independently computing "the same" number and getting
different answers is a realistic, likely failure mode — not a hypothetical.
It already happened once in this framework's own development, in a
different context: pulling stock prices from a web search's AI-generated
summary versus a direct page fetch produced internally inconsistent figures
in the same answer (see `market-intelligence/source-credibility-
hierarchy.md`). Six agents working the same finalist concurrently, from
different data sources, are exactly as capable of quietly disagreeing with
each other as one agent was of disagreeing with itself.

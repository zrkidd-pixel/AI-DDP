# Distressed Diligence (opt-in)

Activates when: the target shows distress signals — going-concern language
in recent financials, a covenant breach, a forced corporate action (e.g.,
the reverse stock split flagged in `_shared/data-source-crosswalk.md`'s own
worked example), or leverage materially above sector norms. Read by
Financial Diligence, Legal & Structuring, and Verification in addition to
their normal rules.

## Why standard diligence isn't enough here

`financial-diligence/qoe-redflag-checklist.md` normalizes EBITDA assuming
the business is a going concern with a normal operating trajectory. A
distressed target's recent financials may reflect emergency cost-cutting,
deferred obligations, or one-time restructuring actions that make "normal
run-rate EBITDA" a much harder, more uncertain estimate than usual — treat
any adjusted figure here with the calibration discipline in
`_shared/overconfidence-prevention.md`, not the same confidence as a
healthy target's QoE.

## Additional financial diligence

- **Cash runway.** Compute how many months of operations the target can
  fund at current burn before needing new financing or breaching a
  covenant — this is often the single most decision-relevant number for a
  distressed target and isn't part of standard QoE.
- **Creditor status.** Is the target current on its existing debt, in
  active covenant negotiations, or already in default? This determines
  whether a transaction can even proceed without existing lender consent.
- **Deferred and off-balance-sheet obligations.** Distressed targets often
  defer payables, underfund pension obligations, or delay capex in ways
  that inflate near-term cash flow at the cost of liabilities a buyer would
  inherit — flag explicitly, don't let deferred obligations read as
  genuine cost discipline.

## Additional structuring considerations

- **Distressed-for-control or loan-to-own structures** may be more
  applicable than a standard buyout, depending on where the target sits in
  its capital structure and creditor negotiations — flag this as a
  structuring question for counsel, per
  `legal-structuring/deal-structure-decision-tree.md`, rather than
  defaulting to the standard asset/stock deal framework.
- **Existing lender consent and intercreditor dynamics** may be a
  precondition to closing, not just a diligence item — confirm this
  earlier than in a standard deal, since it can be the actual timeline
  driver.

## Additional verification checks

- Re-derive the target's actual covenant headroom (or lack of it) from raw
  financials independently, per `verification/model-audit-checklist.md` —
  a distressed target's own reporting has more incentive to understate
  distress than a healthy target's does.
- Confirm whether any forced corporate action (reverse split, asset sale,
  suspended dividend) has a publicly disclosed cause, and whether that
  cause is still active or has actually been resolved — don't assume a
  past-tense mention means the underlying issue is over.

## What this extension does not do

Does not make a going/no-go recommendation on a distressed target — it adds
the specific diligence depth a distressed situation requires so that
recommendation, whichever way it goes, is actually informed by the target's
real financial condition.

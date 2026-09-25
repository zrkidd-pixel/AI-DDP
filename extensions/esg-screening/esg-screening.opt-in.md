# ESG Screening (opt-in)

Activates when: the fund's LPs impose ESG mandates or exclusionary screens
beyond the standard sector exclusions already in `_shared/fund-mandate.md`.
Read by Screening, Thesis/IC Memo, and Monitoring in addition to their
normal rules.

## What this adds to Screening

Standard screening excludes sectors where EV/EBITDA isn't the core
valuation metric. ESG screening is a separate, additional filter layer —
run it after the standard criteria, not instead of them:

- **Exclusionary screens.** Check the fund's specific LP-imposed exclusions
  (recorded in `_shared/fund-mandate.md`'s "ESG / exclusionary screens"
  field) against each candidate — e.g., revenue thresholds from specific
  activities, involvement in specific practices. This is mechanical
  filtering, same discipline as any other screening criterion: report the
  count excluded and why.
- **Data availability is itself a diligence finding.** Smaller or
  founder-led targets often don't have ESG-specific disclosures at all.
  Absence of ESG data is not the same as a clean ESG profile — flag it as
  an open diligence item, not a pass.

## What this adds to Thesis / IC Memo

- **State the actual basis for any ESG characterization**, per
  `_shared/overconfidence-prevention.md` — "this company has strong labor
  practices" needs the same evidentiary discipline as any other qualitative
  claim. A lack of negative findings is not the same as verified positive
  practices.
- If the fund markets itself on ESG criteria to its own LPs, the memo's
  risk section should address reputational and LP-reporting risk if the
  target's ESG profile turns out weaker than initially assessed post-close.

## What this adds to Monitoring

- If the fund has LP-facing ESG reporting commitments, add the relevant
  metrics to `monitoring/kpi-dashboard-templates.md`'s tracked set for this
  deal specifically — don't let ESG commitments exist only in the original
  memo with no ongoing tracking mechanism.
- Material ESG-related incidents post-close (regulatory action, safety
  incidents, labor disputes) are a monitoring trigger in their own right,
  not just a KPI-dashboard line item — route per
  `monitoring/covenant-reporting-cadence.md`'s escalation logic.

## What this extension does not do

Does not define what counts as acceptable ESG performance — that's the
fund's own policy, recorded in `_shared/fund-mandate.md`. This extension
makes sure that policy actually gets applied consistently across Screening,
Thesis, and Monitoring instead of only being checked once, informally,
somewhere in the process.

# Returns & Sensitivity Conventions

Referenced by: Thesis / IC Memo Agent, Underwriting Agent

## Case construction

- **Base case:** the underwritten plan as documented in the 100-day plan and
  value-creation levers — not a rosy scenario, the actual expected-case
  numbers with their assumptions tagged and sourced.
- **Downside case:** what happens to returns if the primary risk factors
  identified in the risk section materialize — e.g., a key customer churns,
  a margin lever doesn't land, multiple compresses at exit. Build the
  downside from the *specific* risks already identified in the memo, not a
  generic "revenue is 10% lower" haircut with no connection to the actual
  risk narrative.
- **Upside case:** what happens if the value-creation plan outperforms or an
  additional lever (e.g., a bolt-on materializes sooner than planned)
  executes — equally specific, tied to a named lever.

## Reporting returns

Report both **IRR and MOIC** for every case — they capture different things
(MOIC is magnitude, IRR is magnitude *and* timing) and a deal can look very
different on one metric versus the other, especially if exit timing varies
across scenarios. State the assumed exit multiple and exit year explicitly for
every case; a returns table without stated exit assumptions is not
reproducible or checkable. State the assumed exit *route* too, per
`thesis-icmemo/exit-route-taxonomy.md` — a trade sale, IPO, and secondary
buyout carry different valuation dynamics and timing risk, not just
different multiples.

## Sensitivity analysis

At minimum, show sensitivity of IRR/MOIC to: (1) exit multiple, and (2) exit
timing/hold period — these are usually the two biggest swing factors and the
ones most subject to disagreement or uncertainty. Additional sensitivities
(leverage level, margin achievement) are useful but shouldn't substitute for
these two.

## The multiple-expansion assumption specifically

Don't assume exit-multiple expansion (or even flat multiples) as a default
base-case input without stating why. Bain & Company's analysis of buyout
value-creation drivers (2013-23 deal entries) found that the average deal
still derives 47% of its enterprise-value growth from multiple expansion
alone, with margin expansion contributing almost nothing (see
`value-creation/value-lever-taxonomy.md`) - meaning a base case built the
way the average historical deal was built is disproportionately exposed to
a factor the sponsor doesn't control `[source: Bain & Company, Global
Private Equity Report 2024]`. In a period where rising rates put sustained
downward pressure on multiples, a base case assuming flat-to-expanding
multiples needs an explicit justification for why this deal is different,
not an implicit carryover of historical averages. Cross-check the assumed
exit multiple's plausibility against `value-creation/value-lever-taxonomy.md`'s
empirical revenue/margin/multiple split - a plan with no stated
margin-expansion mechanism leaning entirely on multiple expansion resembles
an average deal, not the top-quartile profile the fund is presumably
underwriting to.

## Comparing to the fund's hurdle

Explicitly state whether the base, downside, and upside cases each clear the
target returns threshold in `_shared/fund-mandate.md` — don't leave the
reader to compare the numbers themselves. If the downside case fails to clear
the hurdle, say so plainly rather than only showing a base case that does.

# Fund Mandate Template

Referenced by: Screening Agent, Underwriting Agent, Financing / Capital
Structure Agent, and Thesis / IC Memo Agent — the fixed context each of them
checks before finalizing its own output, rather than re-deriving fund
parameters independently.

**This copy, at `knowledge/_shared/fund-mandate.md`, is a blank template —
never fill it in directly or edit it per deal.** `engine/aiddp_new_deal.py`
copies it into each engagement's root as `fund-mandate.md` when the deal is
set up; every agent reads and writes that deal-local copy, not this one.
Keeping this one blank is what stops two deals sharing an AI-DDP checkout
from overwriting each other's numbers.

**The deal-local copy must have real values before Screening finishes** —
but nobody has to hand-edit it first. If the Screening Agent finds a
placeholder value there, its own operating rules say to ask the human for
that specific field conversationally and write the answer into the file
itself, rather than blocking and telling the human to go edit it by hand.
Treating a placeholder as a blocking gap doesn't mean "stop and wait for a
file edit" — it means "stop and ask a question," the same as any other gap
in this framework.

## Fund parameters

- **Fund name / vintage:** *(fill in)*
- **Equity check range:** *(e.g., $X–$Y million per platform investment)*
- **Target hold period:** *(fill in)*
- **Target returns:** *(e.g., gross IRR / MOIC hurdle)*
- **Geography:** *(fill in — country/region restrictions)*
- **Sector inclusions/exclusions:** *(fill in — note any sector where EV/EBITDA
  is not the core valuation metric and is therefore excluded from screening,
  e.g. banks, insurers, REITs, upstream energy)*
- **Listing requirement:** *(e.g., must be actively listed on a specified
  exchange, or private-only, or either)*
- **Ownership requirement:** *(e.g., control/majority only, minority permitted)*
- **ESG / exclusionary screens, if any:** *(fill in)*
- **LP-imposed restrictions, if any:** *(fill in)*
- **Active extensions:** *(fill in — none, or a list from `extensions/README.md`'s
  table, e.g. "cross-border-structuring" if the target has meaningful
  non-US operations. Screening asks about the trigger conditions for each
  available extension during the mandate interview.)*

## Fund-level risk tolerance notes

- **Leverage tolerance:** *(any fund-level ceiling on pro forma leverage)*
- **Turnaround/distressed tolerance:** *(does the fund's mandate permit
  distressed or special-situations candidates, or clean, growing businesses
  only)*
- **Concentration limits:** *(any single-sector or single-geography exposure
  cap across the portfolio)*

## How this file is used

- **Screening Agent** filters candidates against equity check, geography,
  sector, and listing fields directly from this file.
- **Underwriting Agent** checks any proposed leverage against the fund-level
  leverage tolerance before finalizing a recommendation.
- **Financing / Capital Structure Agent** checks any proposed capital
  structure's leverage against the same fund-level tolerance.
- **Thesis / IC Memo Agent** cites this file's target-returns line when framing
  whether a candidate's projected IRR/MOIC clears the bar.
- Any agent that cannot find a value it needs here should surface that as a gap
  and ask, rather than assume a number from a prior deal or a training example.

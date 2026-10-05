# Fund Mandate — Dynacast engagement

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

Tags per `knowledge/_shared/citation-standards.md`. Nothing below came from a
fund document; everything is derived from the case, the model, or the user's
assignment brief, and anything not sourced is labeled `[assumption]`.

- **Fund name / vintage:** Partners Group (PG), private markets manager, ~$50B AUM, 800+ professionals, 18 offices; this is its first focused push into direct US PE `[data: case p.1]`. Fund vintage: not stated in the case `[GAP]`.
- **Equity check range:** not stated `[GAP]`. Reference points: case sources list $483M new sponsor + management rollover equity `[data: case p.2]`; the posted model gives a $576.6M sponsor check plus $30.7M mgmt rollover `[data: model D22, D21]`. Model is used as given. Screening treats the model's check as in-band because no band exists `[assumption]`.
- **Target hold period:** 5 years `[data: model D11]`.
- **Target returns:** no fund hurdle in the case `[GAP]`. Working hurdles from the assignment brief: Bull target ~25-30% IRR; minimum acceptable outcome ~12-15% IRR `[assumption: user assignment brief]`. The model's "Quick IRR" tab maps 2.0x/5yr to ~15% and 3.0x/5yr to ~25% `[data: model, Quick IRR tab]`.
- **Geography:** global; PG operates in 18 offices `[data: case p.1]`. Target operates 23 plants in 16 countries `[data: case p.2]`. No restriction stated `[assumption: none]`.
- **Sector inclusions/exclusions:** Industrials: precision metal components / die casting (confirmed by Claude's judgment per user instruction, not a fund list `[assumption]`). EV/EBITDA is the core valuation metric (comps are quoted on T12M EV/EBITDA `[data: case Ex.8]`), so no EV/EBITDA-excluded sector applies.
- **Listing requirement:** target is privately held (Kenner-led consortium owns it) but files a 10-K because of public notes `[data: case p.2, Ex.2]`. Private-company LBO, no listing needed.
- **Ownership requirement:** controlling stake, with Kenner & Co. and management rolling equity `[data: case p.2, Ex.1]`.
- **ESG / exclusionary screens, if any:** none stated `[GAP]`; recorded as "none known".
- **LP-imposed restrictions, if any:** none stated `[GAP]`.
- **Active extensions:** `cross-border-structuring` (23 plants / 16 countries; Asia Pacific + Europe = ~72% of 2013 sales `[calc: (236.0+184.3)/580]`). Distressed-diligence: not triggered (no going-concern language or covenant breach in the case). ESG: not triggered on current information. **Subject to change as new information arrives (user instruction).**

## Fund-level risk tolerance notes

- **Leverage tolerance:** no fund ceiling stated `[GAP]`. Model structure used as given: single Term Loan B at 4.25x PF LTM EBITDA of $123.5M `[data: model D12, D7]`. The model deliberately simplifies the case's first-lien/second-lien/rollover structure; per user instruction the model governs.
- **Turnaround/distressed tolerance:** not stated; target is a growing, profitable business so not tested.
- **Concentration limits:** not stated `[GAP]`.

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

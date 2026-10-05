# Screening output — Dynacast engagement

Basis: single named target supplied by the case. No universe sweep is possible or needed; Exhibit 8 trading comps are valuation references, not candidates.
Sector: Industrials — precision metal components / die casting `[assumption: Claude judgment, per user]`.

## Filter sequence (order per knowledge/screening/fund-criteria-checklist.md)

| # | Filter | Result | Count remaining |
|---|---|---|---|
| 0 | Starting pool | Dynacast International Inc. (1 entity) | 1 |
| 1 | Sector / subsector | Pass — die cast / MIM precision components; EV/EBITDA is core metric | 1 |
| 2 | Geography | Pass — no restriction stated; global target | 1 |
| 3 | Listing status | Pass — private equity, signed SPA 12/16/14, closing expected Feb 2015; not in bankruptcy `[data: case p.2]`. Dated as of case, not today | 1 |
| 4 | Complete data | Pass with gaps — EBITDA $123.5M, revenue $650M, debt $486M, NWC all in model `[data: model]`. No share price/share count (private; transaction EV $1.1B stands in). Cash is not broken out in the model (existing debt $486M used as given) | 1 (0 dropped) |
| 5 | Currency | Pass — USD reporting `[data: case Ex.3-6]` | 1 |
| 6 | Profitability | Pass — positive EBITDA ($123.5M PF LTM) | 1 |
| 7 | Equity-check band | **Not testable** — no band in mandate. Implied sponsor check $576.6M `[calc: model D22]`. Recorded, not filtered | 1 |
| 8 | Duplicates | None | 1 |

## Pass/fail against mandate rule
The mandate has no "N of M in-band" rule. Pass condition is therefore trivially met (1 of 1). Widen-search playbook not triggered.

## Data gaps and quirks (taxonomy-gaps)
1. No fund equity band, hurdle, vintage or leverage ceiling in case — `[GAP]`; working hurdles come from the user's brief.
2. Model uses PF LTM Sep-14 revenue $650M / EBITDA $123.5M; case Ex.3/6 show 9M-14 sales $465.5M and 2013 sales $580M. Taken as given per instruction; not adjusted.
3. Model uses one Term Loan B at 4.25x; the case has first lien $530M, second lien $170M, revolver and rollover. Model governs per instruction.
4. Model sponsor equity ($576.6M + $30.7M rollover) differs from the case's $483M; reflects the model's own S&U. Model governs.
5. Title cell reads "Summer 2025"; model dated 2014-15 data. Cosmetic.
6. Cached workbook values are stale because iterative calculation is off; must be on for any scenario output.

## Compliance / MNPI
Inputs are a published Columbia CaseWorks case (licensed for course use), 10-K excerpts, and a student model. No non-public deal data. No MNPI issue identified.

## Extensions recorded
cross-border-structuring: ACTIVE. distressed: no. esg: no. Revisit if new information appears.

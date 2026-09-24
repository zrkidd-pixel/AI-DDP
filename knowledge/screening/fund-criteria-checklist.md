# Fund Criteria Checklist

Referenced by: Screening Agent

The mechanical checklist applied to every candidate before it enters the comp
set. Pulls its parameters from `_shared/fund-mandate.md` — this file is the
*procedure*, that file is the *data*.

## Filter sequence (apply in order, report the count remaining at each step)

1. **Sector / subsector match** against the mandate's inclusion/exclusion list.
   Exclude specialized sectors where EV/EBITDA is not the core valuation metric
   (banks, insurers, REITs, upstream energy) even if they otherwise fit —
   check `_shared/fund-mandate.md` for the fund's specific exclusion list.
2. **Geography** match against the mandate's stated restriction.
3. **Listing status** — actively trading, not acquired, not in bankruptcy, not
   delisted. Verify this as of today, not as of the data source's snapshot
   date (see `_shared/data-source-crosswalk.md` on stale data).
4. **Complete-data filter** — required fields (price, shares outstanding, debt,
   cash, EBITDA, revenue) all present. Report the count before and after; do
   not silently drop rows without reporting how many were dropped and why.
5. **Currency consistency** — flag and separate non-functional-currency rows
   rather than converting them (see `_shared/data-source-crosswalk.md`).
6. **Profitability screen** — positive EBITDA, if the mandate requires it for a
   top choice (a mandate may still permit unprofitable names in the broader
   comp table for context, while requiring positive EBITDA for the actual
   recommendation — check which applies).
7. **Equity-check band** — compute the implied equity check (per
   `underwriting/lbo-mechanics.md`) using **current**, dated market data, and
   filter to the mandate's stated range.
8. **Duplicate check** — flag duplicate entities (e.g., same company appearing
   under multiple identifiers or share classes) rather than silently
   double-counting.

## What to report at the gate, regardless of outcome

- The count remaining after each filter step, not just the final number.
- Any candidates excluded for a close call (e.g., just outside the equity-check
  band) — these are useful context even when excluded.
- Whether the "at least N of M finalists in-band" rule (or whatever the
  mandate's specific pass condition is) is satisfied — and if not, trigger
  `screening/widen-search-playbook.md` rather than forcing a match.

## Anti-patterns

- Applying filters in a different order each time, making results
  non-reproducible.
- Silently excluding a candidate without recording why.
- Using a data source's default/stale price for the equity-check filter.

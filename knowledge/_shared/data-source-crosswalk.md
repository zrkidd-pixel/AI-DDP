# Data Source Crosswalk

Referenced by: Screening Agent, Underwriting Agent, Financial Diligence Agent, Verification Agent

Every financial data vendor encodes the same underlying facts differently. This file
exists because trusting a field name at face value is how screens quietly go wrong.
Add an entry here the first time any agent discovers a vendor quirk in the wild —
don't wait for a clean writeup; a one-line note beats a forgotten lesson.

## Identifier fields

- **Never assume a "clean" identifier column exists.** A Compustat-derived panel we
  used shipped `cik_x`, `cik_clean`, and `cik_y` — three different CIK columns, no
  column literally named `cik`. Always inspect the actual header before writing a
  join or filter; don't guess the column name from convention.
- **`gvkey` (Compustat) is the stable time-series identifier, not the ticker.**
  Tickers get reused across delisted and newly listed companies and change on
  corporate actions (mergers, spin-offs, rebrands). Match company-year panels on
  `gvkey`, not `tic`, whenever tracking one company across fiscal years.
- Import every identifier column (`gvkey`, `cik*`, `tic`) **as text**, never as a
  number. Leading zeros and non-numeric identifiers get silently corrupted by
  numeric parsing.

## Classification taxonomies don't agree with each other

A single vendor file can carry three independent classification schemes at once —
e.g., a proprietary `industry_category` field, `sic` (SIC code), and `naicsh`
(NAICS code) — and they will not map cleanly onto each other or onto how a human
would describe the sector.

- One real panel's `industry_category` had exactly eight buckets: Financial
  Services, Materials & Industrials, Energy, Information Technology, Business
  Services, Healthcare, Other, Consumer. **"Consumer" bundled retail and consumer
  goods into a single bucket with no way to separate them**; there was no
  standalone "Retail" or "Consumer Electronics" category at all.
- Genuinely consumer-facing hardware companies were found scattered across
  `industry_category` buckets that had nothing to do with "consumer": GoPro under
  "Materials & Industrials," Peloton under "Business Services." **If a screen
  relies solely on the vendor's own category label, it will silently miss real
  candidates.** Cross-check against SIC/NAICS codes (or another taxonomy) before
  concluding a category is exhaustive.
- When a screen needs a sector the vendor's own taxonomy doesn't cleanly support,
  do a systematic sweep by classification code across the *whole* dataset (all
  categories, not just the "obvious" one) rather than relying on brand
  recognition to assemble the candidate list. Brand recall missed real, relevant
  companies that a code-based sweep caught.

## Price, share count, and "current" vs. "as of" fields

- `prcc_f`-style fields are typically a **fiscal-year-end closing price**, not
  today's price. `csho`-style fields are typically **annual average or
  period-end common shares outstanding in millions** — not a fully diluted share
  count. Never combine a stale annual price/share field with a "current
  enterprise value" claim; if the assignment or mandate calls for a current EV,
  go get a current quote and current share count separately, and date both.
- **Corporate actions can silently invalidate a historical share count.** One
  company in a live screen executed a 1-for-50 reverse stock split between its
  last annual filing and "today" (forced by an exchange-listing deficiency
  notice). Using the old share count with the new price — or vice versa —
  overstates or understates market equity by the split ratio. When a current
  price and a historical share count disagree by an implausible multiple, check
  for a stock split or reclassification before assuming a data error.
- Always record the **as-of date** next to any price or share count, and keep
  "most recent complete fiscal year" (for income-statement/balance-sheet
  figures) explicitly separate from "current market data" (for price/EV). Don't
  let a downstream reader assume both came from the same moment in time.

## Currency and geography exceptions

- A "USA" filter on the `loc`/country field does not guarantee USD reporting.
  Some rows will carry a non-USD `curncd` (e.g., a Canadian or Chinese reporting
  currency) despite a USA location field. Flag and exclude these from
  dollar-denominated calculations rather than converting them — a currency
  conversion introduces an FX-rate assumption that wasn't asked for and usually
  isn't disclosed as such.
- Currency-invariant ratios (margins, ratios of same-currency line items) can
  still be computed for non-USD rows even when dollar-denominated figures
  (market cap, EV) are left missing. Don't drop a row entirely just because one
  derived column is undefined.

## Practical rule

Before running any calculation across a vendor file: read the actual header,
check for more than one identifier or classification column, spot-check whether
the price/share fields are "as of" a stale date, and confirm currency
consistency. None of this is optional diligence — it is the difference between a
screen that's right and one that's confidently wrong.

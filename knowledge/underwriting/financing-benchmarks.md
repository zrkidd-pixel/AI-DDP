# Financing Benchmarks

Referenced by: Underwriting Agent, Financing / Capital Structure Agent

**This file is a LIVE document, not a static reference.** Debt multiples, base
rates, and fee conventions move with credit markets. Any figure in this file
carries an as-of date and a source; an agent that finds this file stale (more
than ~1 quarter old, or predating a major rate move) should refresh it before
relying on it, not use it as-is.

**Last reviewed:** 2023-12-31 (US large-corp LBO market, per PitchBook|LCD
full-year 2023 data — see "Dated reference point" section below; this is a
historical snapshot, not current market, and must be refreshed before use on
a live deal per the staleness rule above)

## Why this file exists

A classroom or teaching exercise typically hands you a fixed formula (e.g., a
flat 25% premium, 50% debt funding, 2% financing fee, 1% transaction fee) as a
training-wheel simplification so the arithmetic is checkable. **Real
underwriting cannot use fixed assumptions like this** — actual leverage
availability, pricing, and fees are deal-specific and market-dependent, sourced
from actual lender conversations, term sheets, and current market data, not
assumed. The Underwriting Agent should treat any hardcoded percentage as a
placeholder to be replaced with a sourced, dated figure before a real
recommendation goes to IC — not as a formula to reuse across deals.

## What to source, and where, for a real deal

- **Acquisition premium.** Sourced from recent precedent transactions in the
  same or adjacent sector/size band (control premium paid over the
  unaffected share price), not assumed as a flat percentage. Precedent
  transaction premiums vary widely by deal competitiveness, strategic vs.
  sponsor buyer, and market conditions at signing.
- **Leverage (debt as % of transaction value, and debt/EBITDA multiple).**
  Sourced from: (a) actual indicative term sheets from prospective lenders for
  this specific deal, (b) syndicated leveraged loan market data for
  comparable size/sector/rating (e.g., published leveraged loan indices and
  private credit market surveys), and (c) the target's own current leverage
  and covenant headroom. Leverage availability compresses meaningfully in
  tighter credit markets and expands in looser ones — a multiple that was
  standard 18 months ago may not be available today.
- **Base rate.** Whatever floating reference rate the actual debt package will
  reference (e.g., the prevailing benchmark rate at signing), plus the
  negotiated spread — both need a specific, dated source, not an assumption
  carried over from a prior deal or a training example.
- **Financing fees and transaction fees.** Vary by deal size, deal complexity,
  and advisor/lender relationships — sourced from actual fee letters or
  recent comparable deals, not a flat percentage rule.
- **Debt product mix.** Whether the structure is a single unitranche facility,
  a senior/subordinated split, or includes a seller note or preferred piece
  changes the effective blended cost and covenant package materially — this is
  the Financing / Capital Structure Agent's specific output, not something the
  Underwriting Agent should assume on its own (see
  `financing-capstructure/debt-product-taxonomy.md`).

## Dated reference point: US large-corp LBO market, full-year 2023

The figures below are a real, sourced snapshot — useful to sanity-check a
fresh pull against, or to use directly **only if explicitly labeled as a
2023 year-end reference point**, never presented as current market data on a
live deal without re-verifying `[source: PitchBook|LCD, full-year 2023 US
LBO market data, as of Dec 31, 2023]`:

- **Average buyout leverage:** 4.8x total debt/EBITDA — a 13-year low, down
  from ~6x in 2022, vs. a 10-year average of 5.80x and a 2007 peak of 6.23x.
- **Average sponsor equity contribution:** 51.09% of transaction value — the
  first time on record this topped 50%, vs. a 10-year average of 43.50%.
- **Average TLB yield at issuance:** 10.91%; **average TLB spread:** 446 bps
  (vs. a 439 bps 10-year average).
- **Average interest coverage ratio:** 2.4x — a 16-year low, directly
  relevant to the covenant-headroom discussion in
  `financing-capstructure/covenant-conventions.md`: a market-wide low
  coverage ratio means less headroom is structurally available across deals
  closing in this kind of market, not just an individual credit's problem.
- **Average purchase price multiple:** 10.8x — matched the 10-year average
  exactly, notable because it moved independently of the leverage collapse
  (see the inverse-relationship note directly below).
- **Deal volume and size:** only 32 large-corp LBOs priced in 2023 vs. a
  110-deal 10-year average; average transaction size rose to $4.2B;
  take-private deals reached a record 37.5% share of 2023 buyout count.

### A second, independently-sourced 2023 data point — and why it doesn't match the first

Bain & Company's *Global Private Equity Report 2024* (data via LSEG LPC and
LCD, as of Dec 31, 2023) gives figures for the same year that are useful to
cross-check against the PitchBook|LCD figures above `[source: Bain &
Company, Global Private Equity Report 2024]`:

- **US large-corporate debt/EBITDA for LBO loans: 5.9x** (down 17% from
  2022, lowest since 2012) — this does **not** match the 4.8x "average
  buyout leverage" figure above from PitchBook|LCD for the same year.
  Neither figure is wrong; they come from different data cuts (deal-size
  threshold, which loans are included, and index-construction
  methodology all differ even when both sources ultimately draw on LCD
  data). **Treat this as the working example of why a leverage figure
  needs its exact source and methodology stated, not just "leverage was
  4.8x/5.9x in 2023"** — citing a number without which specific index
  or deal-size cut it came from is not a usable citation for underwriting.
- **Average purchase price multiple: 10.8x US / 10.1x Europe** — this
  closely corroborates the PitchBook figure above (10.8x), which is a
  useful cross-validation when two independent sources agree.
- **Interest coverage ratio: 2.4x** — matches the PitchBook figure above
  exactly, reinforcing confidence in that specific number.

### The leverage/equity relationship is inverse, and it matters for returns

When debt availability tightens (as in 2023), sponsors don't walk away from
deals at the same purchase multiples — they fill the gap with more equity.
The 2023 data shows this directly: leverage fell to a 13-year low while the
purchase price multiple held at the 10-year average, and the equity
contribution share hit a record high to bridge the difference. **A lower
leverage input isn't just a financing-side detail — it directly compresses
the equity-multiple amplification a sponsor gets on exit**, holding the exit
multiple and hold period constant, per
`thesis-icmemo/returns-sensitivity-conventions.md`. When sourcing a leverage
assumption for a live deal, treat the corresponding equity-check size as
part of the same sourced figure, not a residual plug — and flag to Thesis /
IC Memo that a lower-leverage environment changes the returns math even if
every operating assumption is unchanged.

## Sanity-check ranges (illustrative only — verify before use)

Do not treat any number below as current market data. It exists only to flag
when a sourced figure looks implausible and worth double-checking, not to be
cited in a memo:

- Total leverage on a middle-market sponsor-backed deal has historically run
  somewhere in the mid-single-digit multiple of EBITDA range, with wide
  variance by sector, size, and credit cycle — a figure far outside a
  single-digit multiple in either direction deserves a second look before
  being accepted.
- Combined financing + transaction fees on a mid-sized deal are typically a
  low-single-digit percentage of transaction value in total — a figure many
  multiples higher or lower than that is worth re-verifying against its source.

## Practical rule

If the Underwriting Agent is about to use a percentage in this file without a
source and an as-of date attached, that is the signal to stop and either (a)
find and cite a current source, or (b) explicitly label the figure as an
illustrative training assumption, not a market-sourced one — and say so in the
memo, not just in this file.

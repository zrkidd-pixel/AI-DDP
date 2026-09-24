# Financing Benchmarks

Referenced by: Underwriting Agent, Financing / Capital Structure Agent

**This file is a LIVE document, not a static reference.** Debt multiples, base
rates, and fee conventions move with credit markets. Any figure in this file
carries an as-of date and a source; an agent that finds this file stale (more
than ~1 quarter old, or predating a major rate move) should refresh it before
relying on it, not use it as-is.

**Last reviewed:** *(fill in — leave unset rather than guess a date)*

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

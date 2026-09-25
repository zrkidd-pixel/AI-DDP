# Covenant Conventions

Referenced by: Financing / Capital Structure Agent, Monitoring Agent

## Common covenant types

- **Leverage covenant (maximum):** total debt/EBITDA cannot exceed a specified
  ceiling, tested on a defined cadence (often quarterly). Breaching this is
  typically the most common trigger for lender intervention.
- **Interest coverage covenant (minimum):** EBITDA/interest expense must stay
  above a specified floor — measures ability to service debt from operating
  earnings.
- **Fixed charge coverage ratio:** broader than interest coverage; measures
  EBITDA (or a defined cash-flow proxy) against total fixed obligations
  (interest, mandatory debt amortization, sometimes capex and taxes).
- **Capex limits:** caps on annual capital expenditure, sometimes with a
  carry-forward provision for unused capacity.
- **Restricted payment covenants:** limits on dividends, distributions, or
  payments to equity holders while debt is outstanding.

## Maintenance covenants vs. incurrence covenants

- **Incurrence covenants** generally require that if an issuer takes an
  action (paying a dividend, making an acquisition, issuing more debt), it
  must still be in compliance after that action. A worked example: an
  issuer with an incurrence test limiting debt to 5x cash flow can only
  take on more debt if, pro forma, it stays within that constraint — doing
  so anyway is a breach and technical default. But if the issuer ends up
  above 5x simply because its earnings deteriorated, with no new debt
  incurred, that is **not** a breach `[source: S&P Syndicated Loan Primer,
  2006]`.
- **Maintenance covenants** are far more restrictive: the same 5x leverage
  test, if written as a maintenance covenant, must be passed every quarter
  whether or not the issuer takes any action — meaning the issuer breaches
  it if *either* earnings erode *or* debt increases. Lenders generally
  prefer maintenance covenants because they allow earlier intervention if
  an issuer is deteriorating; issuers prefer incurrence covenants for
  exactly the same reason, in reverse `[source: S&P Syndicated Loan Primer,
  2006]`.
- **Covenant-lite loans** are a specific, named structure: loans carrying
  bond-like incurrence covenants instead of the maintenance covenants
  typical of a standard loan agreement `[source: S&P Syndicated Loan
  Primer, 2006]`. Recognize this term specifically when a deal's proposed
  structure is described as "cov-lite" — it means incurrence-only, not a
  vague absence of covenants.
- Loosely, maintenance covenants are more common in broadly syndicated
  leveraged loans; looser, incurrence-only (including cov-lite) packages are
  more common in private credit / direct-lending structures — but this
  varies by market conditions and negotiating leverage, and should be
  confirmed per deal, not assumed.

## Covenant headroom — why Monitoring cares about this specifically

"Headroom" is the gap between the current covenant test level and the actual
covenant ceiling/floor — e.g., if the leverage covenant ceiling is 6.0x and
the company is running at 5.2x, headroom is 0.8x. **Shrinking headroom over
consecutive testing periods is an early-warning signal that deserves a
Monitoring Agent flag well before an actual breach occurs** — waiting until
the covenant is actually breached to react is waiting too long; the value of
tracking this is catching the trend early enough to act (renegotiate,
cure, or adjust the operating plan).

## Cure rights and lender relationship management

Many facilities include a cure right — allowing the sponsor to inject
additional equity to retroactively fix a covenant breach for testing
purposes, within limits (a cap on the number of cures over the facility's
life, or a maximum equity cure amount). Confirm what cure rights exist in the
actual credit agreement before assuming a breach is unrecoverable — but also
don't treat cure rights as a substitute for actually fixing the underlying
performance issue.

**A breach is also a negotiation, not just a mechanical trigger.** Lenders
asked for a waiver on a covenant violation may extract real concessions in
exchange — a fee, an incremental spread, or additional collateral
`[source: S&P Syndicated Loan Primer, 2006]`. When Monitoring flags a
covenant breach or imminent breach, the realistic range of outcomes isn't
just "cure it or default" — it includes a negotiated waiver at a real
economic cost, which should be factored into any re-underwrite rather than
treated as a side detail.

## Sources

- S&P, *A Syndicated Loan Primer*, by Steven Miller (2006).

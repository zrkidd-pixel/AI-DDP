# Debt Product Taxonomy

Referenced by: Financing / Capital Structure Agent, Underwriting Agent

## Seniority: the actual payment-priority waterfall

Seniority is where an instrument ranks in priority of payment — the
issuer pays the senior-most creditors first and the most junior
equityholders last. In a typical structure: senior secured and unsecured
creditors first (secured instruments typically move to the front of the
line specifically in bankruptcy), then subordinated bondholders, junior
bondholders, preferred shareholders, and common shareholders last.
Leveraged loans are typically senior secured instruments and rank highest
in the capital structure `[source: S&P, "A Syndicated Loan Primer" by
Steven Miller, 2006]`. Every tranche recommended below should be placed
explicitly on this waterfall, not just labeled "senior" or "junior" in the
abstract.

## Common structures, from senior to junior in the capital stack

- **First lien loan:** the most precise term for what's often called
  "senior secured" — its claim on collateral is senior in right of
  repayment to any other obligation of the borrower, secured by a pledge
  of specific collateral with a perfected interest, and typically the
  collateral or enterprise value securing the loan exceeds the outstanding
  loan balance `[source: S&P Syndicated Loan Primer, 2006]`. Often
  includes a revolver for working-capital needs alongside the term loan.
  Typically the lowest-cost debt in the structure, consistent with sitting
  first on the seniority waterfall above.
- **Second lien loan:** junior to a first lien loan's claim on the same
  collateral. Typically carries a less restrictive covenant package (wider
  maintenance-covenant levels than the first lien) — which is exactly why
  it's priced at a premium: historically, that premium has started around
  200 bps when collateral coverage extends well beyond both tranches'
  claims, rising to 1,000+ bps when collateral coverage is thinner
  `[source: S&P Syndicated Loan Primer, 2006 — treat as an illustrative
  historical reference point, not a current benchmark; source fresh
  pricing per `underwriting/financing-benchmarks.md` for any live deal]`.
- **Unitranche:** a single blended facility combining what would otherwise be
  separate senior and subordinated tranches into one loan with one lender (or
  a small club), at a blended rate between senior and subordinated pricing.
  Simplifies negotiation (one lender, one set of terms) at the cost of
  typically less flexible amendment/waiver dynamics than a syndicated
  structure.
- **Mezzanine debt:** deeply subordinated, often unsecured, frequently
  combines a cash interest component with a PIK (payment-in-kind, accruing
  rather than cash-paid) component and sometimes warrants or equity
  participation — highest cost of capital in the stack, used to bridge a gap
  between what senior/second-lien lenders will provide and total funding need.
- **Seller note:** debt issued by the buyer to the seller as part of the
  purchase price, deferring a portion of proceeds — effectively seller
  financing, often subordinated to third-party debt, and can help bridge a
  valuation gap between buyer and seller.
- **Preferred equity:** technically equity, not debt, but economically
  debt-like (fixed dividend/return expectation, liquidation preference ahead
  of common equity) — sits between debt and common equity in the capital
  stack and priority of claims.

## Collateral — what it actually is, and a real structural risk

Collateral usually includes all tangible and intangible assets of the
borrower and, sometimes, specific assets backing a particular loan.
Virtually all leveraged loans are backed by a pledge of collateral. One
common structure pledges the **capital stock of operating subsidiaries**
rather than the operating companies' own assets directly — the borrower's
assets sit at the operating-company level, unencumbered by liens, while
the holding company pledges the operating-company stock to lenders. This
effectively gives lenders control of the subsidiaries and their assets if
the company defaults `[source: S&P Syndicated Loan Primer, 2006]`.

**The real risk in this structure:** if a bankruptcy court collapses the
holding company into the operating companies (substantive consolidation),
the pledged stock can be rendered worthless, and loan holders are
demoted to unsecured creditors on the same level as other senior
unsecured claims. This actually happened to lenders of several retail
companies in the early 1990s `[source: S&P Syndicated Loan Primer,
2006]`. Flag a stock-pledge collateral structure explicitly when
recommending it — it is not economically equivalent to a direct pledge of
operating assets, despite often being described casually as such.

## Subsidiary guarantee

Not collateral in the strict sense, but most leveraged loans are backed by
subsidiary guarantees, so that if the issuer enters bankruptcy, all of its
units are on the hook to repay the loan — common for unsecured
investment-grade loans too `[source: S&P Syndicated Loan Primer, 2006]`.
Confirm which subsidiaries are actually guarantors (not every subsidiary
necessarily is) rather than assuming full-group coverage.

## Choosing a structure — the actual tradeoffs

- **Cost vs. flexibility:** unitranche is simpler but often less flexible on
  covenants/amendments than a syndicated senior/sub split with multiple
  lenders to negotiate with individually.
- **Speed and certainty of close:** fewer lenders generally means faster,
  more certain execution — relevant in a competitive process where speed
  matters.
- **Covenant package:** junior capital often comes with looser financial
  covenants than senior debt, but at meaningfully higher cost — the tradeoff
  is headroom vs. price.

## Handoff to Underwriting

This agent's output feeds the Underwriting Agent's `new_debt` figure — but as
a **blended structure with its own weighted-average cost and covenant
package**, not a single flat leverage percentage. Where the underwriting
mechanics reference file assumes a single "debt%" for simplicity, a real
capital structure recommendation should specify the actual tranche mix, each
tranche's pricing and terms, and the resulting blended cost — sourced per
`underwriting/financing-benchmarks.md`, not assumed.

## Sources

- S&P, *A Syndicated Loan Primer*, by Steven Miller (2006).

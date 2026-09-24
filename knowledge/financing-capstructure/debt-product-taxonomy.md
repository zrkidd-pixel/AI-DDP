# Debt Product Taxonomy

Referenced by: Financing / Capital Structure Agent, Underwriting Agent

## Common structures, from senior to junior in the capital stack

- **Senior secured / revolving credit facility:** first-priority claim on
  assets, typically the lowest-cost debt in the structure, often includes a
  revolver for working-capital needs alongside a term loan.
- **Unitranche:** a single blended facility combining what would otherwise be
  separate senior and subordinated tranches into one loan with one lender (or
  a small club), at a blended rate between senior and subordinated pricing.
  Simplifies negotiation (one lender, one set of terms) at the cost of
  typically less flexible amendment/waiver dynamics than a syndicated
  structure.
- **Second lien:** subordinated to senior secured debt in priority of claim
  and typically in payment, priced higher to compensate for the subordinated
  position.
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

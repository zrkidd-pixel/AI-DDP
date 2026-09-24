# LBO Mechanics Reference

Referenced by: Underwriting Agent, Verification Agent

The standard formula chain for computing an implied equity check and the
resulting leverage/return profile. Treat every percentage in the worked
example as illustrative unless sourced per
`underwriting/financing-benchmarks.md` — this file defines the *mechanics*,
not the assumptions.

## Core formula chain

```
market_equity      = share_price × shares_outstanding
net_debt            = total_debt − cash_and_equivalents
current_EV          = market_equity + net_debt
transaction_EV       = (1 + premium%) × market_equity + net_debt
new_debt             = debt% × transaction_EV
financing_fees       = financing_fee% × new_debt
transaction_fees     = transaction_fee% × transaction_EV
total_fees           = financing_fees + transaction_fees
equity_check         = transaction_EV + total_fees − new_debt
```

## Identity check (always verify this before trusting an output)

```
new_debt + equity_check  ==  transaction_EV + total_fees
```

This must hold exactly, by construction — new debt plus sponsor equity is what
funds the transaction plus fees. If it doesn't tie out to the cent (allowing
for rounding at display only, not in the underlying calculation), there is a
formula error upstream. This is the Verification Agent's first check on any
underwriting output.

## Multiples and leverage ratios

```
EV/EBITDA (current)      = current_EV / EBITDA
EV/EBITDA (transaction)  = transaction_EV / EBITDA   [rarely the ranking basis — see below]
EV/Revenue               = current_EV / revenue
pro_forma_leverage       = new_debt / EBITDA
current_net_leverage     = net_debt / EBITDA
```

**Ranking candidates for cheapness is normally done on *current* EV/EBITDA
(pre-premium), not transaction EV/EBITDA** — ranking on transaction EV/EBITDA
would just re-rank candidates by how large a premium was assumed, not by how
cheap they actually are today. State explicitly which basis is used.

## Precision and rounding

Carry full precision through every step of the calculation. Round only at the
final display layer, and round different figure types by their own convention
(e.g., dollar amounts to the nearest whole unit, multiples to one decimal,
percentages to one decimal) — never round an intermediate value and then
compute further off the rounded figure, which compounds error.

## Handling missing or invalid inputs

- If EBITDA is zero or negative, EV/EBITDA and leverage ratios are undefined —
  leave them missing, don't force a value (a negative multiple is
  mathematically computable but not economically meaningful).
- If a required input field is missing, exclude the row from calculations that
  need it rather than substituting a zero or an average.

## What this file does not cover

Actual leverage availability, pricing, and fee levels — those are sourced,
dated, deal-specific inputs from `underwriting/financing-benchmarks.md` and
the Financing / Capital Structure Agent, not assumptions this file provides.

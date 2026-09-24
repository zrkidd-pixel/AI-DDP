# Model Audit Checklist

Referenced by: Verification Agent

The Verification Agent's job is separation of duties: whoever built the
underwriting model should not be the only one checking it. This checklist is
run independently, ideally by re-deriving figures from raw inputs rather than
just re-reading the model's own formulas.

## Checks to run on every underwriting output

1. **Sources-and-uses identity.** `new_debt + equity_check == transaction_EV +
   total_fees`, exactly (to rounding at display only). If this doesn't tie
   out, there's a formula error — find it before trusting anything else in the
   output.
2. **Independent recomputation of at least one output.** Pick the top-ranked
   or highest-stakes candidate and recompute its full calculation chain
   directly from raw source fields, not by re-running the same script. If the
   independent recomputation and the pipeline's output disagree, that's a bug,
   not a rounding difference — investigate before proceeding.
3. **Precision and rounding order.** Confirm rounding was applied only at
   final display, not before filtering, ranking, or intermediate calculation
   (see `underwriting/lbo-mechanics.md`).
4. **Denominator validity.** Confirm ratios with zero or negative denominators
   (e.g., EV/EBITDA with negative EBITDA) were left missing, not computed into
   a misleading negative or nonsensical multiple.
5. **Currency consistency.** Confirm no dollar-denominated figure silently
   mixes currencies (see `_shared/data-source-crosswalk.md`).
6. **Ranking basis stated and correct.** Confirm candidates were ranked on the
   intended basis (typically current EV/EBITDA, not transaction EV/EBITDA —
   see `underwriting/lbo-mechanics.md`) and that the stated basis matches what
   was actually computed.
7. **As-of-date consistency.** Confirm market data (price, shares) and
   financial-statement data (revenue, EBITDA, balance sheet) are each dated,
   and that a stale price wasn't combined with fresh financials or vice versa.
8. **Screening rule compliance.** Re-check that every candidate in a final
   recommendation set actually satisfies every stated screening criterion
   (sector, geography, profitability, equity-check band) by re-deriving from
   raw fields — don't just trust that the screening step applied its own rules
   correctly.

## Adversarial posture

This agent's default stance is skeptical, not confirmatory — its job is to
find the reason the output is wrong, not to bless it. A verification pass
that finds nothing wrong on the first try should prompt a second look at
whether the checks were actually adversarial enough, not immediate sign-off.

## Output

A pass/fail per check above, with specifics on any failure (not just "looks
off") — vague verification findings are as useless as no verification at all.

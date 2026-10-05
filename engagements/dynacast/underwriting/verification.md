# Verification — Underwriting (independent re-derivation)

Method: a separate Python replica of the model (average-balance interest circularity solved to convergence), written before the workbook was built, versus the recalculated workbook (LibreOffice with iterative calc on).

| Case | Replica IRR / MOIC / 2019 TL | Workbook IRR / MOIC / 2019 TL | Match |
|---|---|---|---|
| Base | 20.57% / 2.548x / 180.58 | 20.57% / 2.548x / 180.58 | Yes |
| Bull | 28.92% / 3.561x / 120.79 | 28.92% / 3.561x / 120.79 | Yes |
| Bear | 12.14% / 1.773x / 241.79 | 12.14% / 1.773x / 241.79 | Yes |

Other checks: user's circularity benchmark (2015 growth 9%->5% moves 2019 term loan $181 -> $199) reproduced in the replica (180.58 -> 199.48). Sources = Uses on both scenario tabs (difference 0.0). No formula errors on any tab. Base tab formulas and inputs identical to the posted model (only float formatting on F50:I50, unused because capex references $E$50). Scenario tabs differ from base only in growth (E29:I29), margin (E31:I31), exit multiple (D67), title/banner text and the notes block at rows 99+.
Limit: recalculated in LibreOffice, not Excel itself; Excel recalcs on open with iteration flag set in the file.

Note: the first workbook build was slightly under-converged on the circular interest (Bull 2019 TL 120.85, Bear 241.72); the saved file was recalculated with tighter iteration (epsilon 1e-7) and now matches the replica to six digits. Headline IRR/MOIC unchanged at displayed precision.

## Returns Attribution tab checks
- Bridge 1 (total equity value: invested equity + EBITDA growth + multiple expansion + debt paydown - entry fees - exit fees) ties to model exit equity (D72) in all three cases, difference 0.0.
- Bridge 2 (sponsor share at 94.95% entry ownership of each driver, less dilution to the 90% exit ownership) ties to model sponsor proceeds less sponsor equity (D74 - D75), difference 0.0.
- MOIC turns (five drivers + 1.00x return of capital) sum to the model MOIC in all three cases.

## Sensitivity Analysis tab checks
- 270 grid cells (3 cases x [entry x exit and exit-year x exit] x [IRR and MOIC], 5x5 and 4x5) recomputed in a separate Python replica; max absolute difference 3e-11.
- Centre cell of each entry x exit grid and the 2019 row of each exit-year grid equal the case tab IRR (D78) and MOIC (D77); check rows read 0.0000.
- Grids are closed-form formulas, not Excel Data Tables (deviation from the reference tab's mechanism, explained on the tab): neither entry nor exit multiple changes the debt schedule in this model.

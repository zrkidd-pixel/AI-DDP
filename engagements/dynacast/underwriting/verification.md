# Verification — Underwriting (independent re-derivation)

Method: a separate Python replica of the model (average-balance interest circularity solved to convergence), written before the workbook was built, versus the recalculated workbook (LibreOffice with iterative calc on).

| Case | Replica IRR / MOIC / 2019 TL | Workbook IRR / MOIC / 2019 TL | Match |
|---|---|---|---|
| Base | 20.57% / 2.548x / 180.58 | 20.57% / 2.548x / 180.58 | Yes |
| Bull | 28.9% / 3.56x / 120.9 | 28.92% / 3.561x / 120.85 | Yes |
| Bear | 12.1% / 1.77x / 241.7 | 12.14% / 1.773x / 241.72 | Yes |

Other checks: user's circularity benchmark (2015 growth 9%->5% moves 2019 term loan $181 -> $199) reproduced in the replica (180.58 -> 199.48). Sources = Uses on both scenario tabs (difference 0.0). No formula errors on any tab. Base tab formulas and inputs identical to the posted model (only float formatting on F50:I50, unused because capex references $E$50). Scenario tabs differ from base only in growth (E29:I29), margin (E31:I31), exit multiple (D67), title/banner text and the notes block at rows 99+.
Limit: recalculated in LibreOffice, not Excel itself; Excel recalcs on open with iteration flag set in the file.

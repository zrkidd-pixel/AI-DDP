# Underwriting Wave 1 — Dynacast (case-information only)

Scope rule (user instruction): all facts come from the Columbia case (`inputs/case.txt`) and the posted model. No outside research. Third-party material cited is the third-party material *inside* the case: TechNavio, North American Die Casting Association (NADCA), and Partners Group's own football field / trading comps (Exhibits 7-8, "Source: Partners Group").
Base case is taken as given and is not adjusted. These findings only bound the Bull/Bear ranges.
Run inline by the primary session, not by sub-agents. Legal & Structuring deferred (conditional wave).

## Financial diligence (QoE view)
- Adj. EBITDA margin history: 2012 18.0%, 2013 18.0%, 9M-13 18.7%, 9M-14 19.4% `[calc: Ex.6 Adj. EBITDA / Ex.3 sales]`. Model: 19.0% PF LTM, 20.0% in 2015, 21.0% after `[data: model E31:I31]`. Base already assumes ~1.6 pts of margin expansion vs. 2013.
- Segment adj. EBITDA margins 9M-14: Europe 21.0%, Asia 21.6%, North America 21.8%, before corporate cost of $9.2M (~2.0% of sales) `[calc: Ex.6]`.
- Add-backs: management fees $1.9M (9M-14) / $2.5M (2013) and transaction/restructuring items are small; no large one-offs in the bridge `[data: Ex.6]`.
- Capex % of sales: 2012 4.2%, 2013 6.8%, 9M-14 4.9%, 2014 budget $29.2M (~5.0% of 2013 sales) `[calc: Ex.5, p.12]`. Model: 4.6% `[data: model E50]`. Ex-MIM expansion spend is stated as low-capital `[data: p.12]`.
- NWC (AR + inventory + prepaids - AP - accrued) as % of sales: 6.2% at Dec-13, 8.6% at Sep-14 on $650M PF LTM `[calc: Ex.4]`. Model: 7.7% `[data: model E52]`, inside the historical range.
- Tax: reported effective rates are distorted (2013: $14.6M on $15.8M pre-tax; 9M-14: $8.4M on $21.2M) `[data: Ex.3]`. Model 25% is retained; not used as a scenario lever because history can't bound it.
- Flag: 9M-14 D&A $29.4M and Ex.5 show D&A above capex historically; model sets D&A = capex `[data: Ex.5, model E51]`. Model governs; not changed.
Cross-domain facts used: customer concentration (Commercial), floating-rate exposure (Financing).
Escalations hit: none.

## Commercial diligence
- Top 10 customers 36.4% of 2013 sales; largest $46.4M / 8.0% `[data: p.12]`. Relationships >15 years for most of top 10; sole-source on many products `[data: p.7]`.
- No long-term contracts; POs only, JIT delivery `[data: p.14, Ex.10]`. Metal cost pass-through with a one-month lag `[data: Ex.10]`.
- End markets 2013: auto safety/electronics 38.2%, consumer electronics 20.6%, telecom 7.6%, healthcare 7.3%, hardware/computer/tooling 17.8% `[data: p.12]`.
- Growth by segment 2013: Asia +14.4%, North America +12.1%, Europe +8.0% `[calc: Ex.2 text, Ex.6]`. Total 2013 growth +11.7%; 9M-14 +8.6% `[calc: Ex.3]`.
- Growth levers named in the case: IBD global accounts (50+ MNC targets), Shanghai replication in China, MIM (new 2013), aluminum die casting `[data: p.9-12]`.
- Third-party: TechNavio forecasts global aluminum die casting CAGR 11.89% for 2012-16 `[source: TechNavio, as cited in case p.8]`. Aluminum is 19.8% of Dynacast revenue, so this supports upside only for part of the mix `[data: p.11]`.
- Downside risks: Europe recession and fixed-cost base, auto end-market exposure, customers can cancel or delay orders, customer insolvency `[data: Ex.10]`.
Cross-domain facts used: capex plans (Financial).
Escalations hit: none (largest customer 8.0%, below typical concentration trigger).

## Management assessment
- CEO Newman (with Dynacast since 1979, CEO since 2002), CFO Murphy (since 1990), EVP Asia Angell (since 1993), EVP Europe Ungerhofer (since 1989); GM average tenure ~15 years `[data: Ex.9, p.12]`. The case itself flags key-person dependency on these four `[data: Ex.10]`.
- Management is rolling equity (model: 5% of equity value) and the 10% sponsor dilution at exit is taken as modeled `[data: model D13, D73]`.
- Fit read: deep operating bench, supports execution of the Bull levers; key-person loss is a Bear-case risk but is not a scenario lever in the model.
Escalations hit: none.

## Financing / capital structure
- Case structure: $530M first lien TL (L+4.25%), $50M revolver (unfunded), $170M second lien (L+8.5%), $6M rollover debt at 2% `[data: p.2]`. Model simplifies to one $524.9M Term Loan B at 4.25x PF EBITDA, all-in 10.08% (SOFR 5.33% + 4.75%) `[data: model D12, K21, L21]`. Model governs per user.
- Interest is floating and unhedged; a leverage-ratio increase adds 25 bp `[data: Ex.10]`. Interest rate is a candidate Bear lever but is not used (the three Bear levers are operating/exit).
- Covenants: minimum interest coverage and maximum total leverage `[data: Ex.10]`. Model 2015 coverage: EBITDA $141.7M / interest $50.9M = 2.8x `[calc: model]`.
- `underwriting/financing-benchmarks.md` is dated (last reviewed 2023-12-31) and is not used here; no outside leverage data was pulled by instruction.
Escalations hit: none.

## Market intelligence (case-only)
- Market: small-component precision die casting; fragmented competition; barriers from multi-slide technology (introduced 1936, not sold externally since 1968) `[data: p.7, 10-11]`.
- Valuation context: Partners Group football field puts LBO-analysis EV at $942M-$1,128M (7.6x-9.1x on $123.5M) and trading comps at $1,142M-$1,489M (9.2x-12.1x) `[calc: Ex.7 / model D7]`. Entry here is 8.9x ($1,099M).
- Trading comps T12M EV/EBITDA: Metal & Die Casting median 10.1x (mean 11.3x), Specialty Manufacturing median 12.3x, all-comps median 11.1x `[data: Ex.8, source: Partners Group, 11/19/14]`.
Escalations hit: none.

## Reconciliation
Overlapping facts: concentration (Commercial only), capex (Financial and Commercial agree: 2014 budget $29.2M), floating-rate exposure (Financing and Market agree). No disagreements; no discrepancy to escalate.
Note: the case's $1.1B EV matches the model's $1,099M (8.9x), corroborating the entry assumption.

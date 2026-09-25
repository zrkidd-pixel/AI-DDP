# Data Source Directory

Referenced by: every agent that might hit a data gap only an external
paid/licensed source can fill. This file is what turns a generic "do you
have more data?" into a specific, actionable request — see
`_shared/question-format-guide.md`'s rule on stating why a question matters
and narrowing it to something concrete.

**This directory names sources and the kind of report to pull from each —
not a specific institution's access path.** Which gateway a given user
reaches these through (a school library, a firm subscription, a direct
account) varies and isn't this file's concern; if it matters for a specific
deal, that belongs in a note on the engagement, not baked in here.

## The rule

When an agent hits a gap that a licensed data source would resolve better
than open web search, it names the **specific source and the specific
report/screen/filter to pull** — not just "check a database somewhere."
Compare:
- Weak: "Do you have any industry data for this market?"
- Correct: "Can you pull an IBISWorld industry report for [NAICS code] — it
  would give us market size, 5-year growth, and industry structure with
  more rigor than the web-search range we have now."

## Source directory

### Capital IQ (Financials, screening, transactions)
**Best for:** company financials, comps, M&A/control transaction data,
company screening by sector/size/geography.
**Specific pulls to request:**
- A **Screener** export (Apps → Screener) for building or widening a
  candidate universe — see `screening/widen-search-playbook.md`.
- A **Transaction Screening** export for precedent M&A/control-transaction
  comps — feeds `underwriting/financing-benchmarks.md`'s premium sourcing.
- A company's **financials export** (multi-year history, segment detail)
  when the screening dataset's figures need verification or don't go back
  far enough for a 3-year CAGR.
**Primarily used by:** Screening, Underwriting, Financing/Capital Structure.

### SEC EDGAR (Primary filings)
**Best for:** 10-Ks, 10-Qs, S-1s, 8-Ks, merger agreement exhibits — for any
US-listed or -filing company, free and directly primary-source (Tier 1 per
`market-intelligence/source-credibility-hierarchy.md`).
**Specific pulls to request:**
- The target's **most recent 10-K/10-Q** when QoE adjustments need
  footnote-level detail the screening dataset doesn't carry.
- **8-K merger-agreement exhibits** from comparable recent transactions,
  for deal-structure precedent (indemnification caps, baskets, survival
  periods — see `legal-structuring/purchase-agreement-glossary.md`).
- An **S-1** if a target or comparable went public recently and needs
  founding/ownership history.
**Primarily used by:** Financial Diligence, Legal & Structuring,
Verification (as the preferred source to verify a figure against, being
Tier 1).

### IBISWorld (Industry reports)
**Best for:** market size, growth, structure/fragmentation, key success
factors, industry-specific regulatory environment — at the industry level,
not the company level.
**Specific pulls to request:**
- An **industry report for the specific NAICS/SIC code** in play, when web
  search only produces a wide, low-confidence market-size range (see
  `market-intelligence/market-sizing-methodology.md`'s point on preferring
  a rigorous source over an averaged range).
**Primarily used by:** Market & Sector Intelligence.

### Factiva (News and media)
**Best for:** news search across a huge range of publications — reputation
checks, litigation history, customer/competitor developments, management
background.
**Specific pulls to request:**
- A **news search on a specific executive's name** for management
  reference-check corroboration (`management-assessment/reference-check-
  framework.md`) — litigation, prior-company controversies, departures.
- A **news search on the target's largest customers or competitors** when
  `commercial-diligence/competitive-positioning-frameworks.md`'s
  competitive-landscape read needs more than what's publicly indexed.
**Primarily used by:** Management Assessment, Commercial Diligence.

### LSEG Workspace (Market/pricing data)
**Best for:** live and historical market pricing, credit spreads, rates —
deeper and more current than what a static financials panel provides.
**Specific pulls to request:**
- **Current credit spread / base rate data for the relevant sector and
  size band**, when `underwriting/financing-benchmarks.md` needs a sourced,
  dated figure rather than an illustrative one.
- **Current share price and trading data**, when a screening dataset's
  price field is stale (see `_shared/data-source-crosswalk.md`'s point on
  never combining a stale price with current financials).
**Primarily used by:** Financing/Capital Structure, Underwriting.

### PitchBook (Private markets)
**Best for:** private-company data, PE/VC deals, fund and investor
information — where Capital IQ's public-market strength doesn't reach.
**Specific pulls to request:**
- A **private-company screen** for potential bolt-on/roll-up targets in a
  fragmented subsector, feeding `value-creation/value-lever-taxonomy.md`'s
  multiple-arbitrage lever with a *named* candidate pipeline instead of an
  assumption that targets exist.
- A **PE/VC deal-comps export** for precedent private-market transaction
  terms, alongside or instead of Capital IQ's public-market transaction
  data.
**Primarily used by:** Value Creation, Underwriting.

### Preqin (Fund/LP data)
**Best for:** fund performance, fundraising, and manager benchmarking data
— fund-level context, not deal-level.
**Specific pulls to request:**
- **Benchmark return data for the fund's strategy and vintage**, when
  `thesis-icmemo/returns-sensitivity-conventions.md`'s base/upside/downside
  cases would benefit from a sourced comparison to how similar-strategy
  funds have actually performed.
**Primarily used by:** Thesis/IC Memo (lightly — this is fund-context, not
core to any single deal's diligence).

### Crunchbase (Startups/financings)
**Best for:** startup and growth-company financing history, investor
mapping — skews earlier-stage/venture than most buyout targets.
**Specific pulls to request:**
- A **financing-history search** when a bolt-on or platform candidate is
  young enough that Capital IQ/PitchBook coverage is thin.
**Primarily used by:** Value Creation, Screening (only for younger/growth
targets where this genuinely adds coverage Capital IQ/PitchBook don't).

## What this directory does not do

Does not tell an agent to pull data reflexively — per
`overconfidence-prevention.md` and the citation-standards discipline, an
agent should only suggest one of these when open-source research has
already hit a real, specific gap. Suggesting an IBISWorld pull for a market
that's already well-covered by two agreeing Tier 2 sources is asking for
data that wouldn't change the answer — don't.

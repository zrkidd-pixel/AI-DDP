# Source Credibility Hierarchy

Referenced by: Market & Sector Intelligence Agent, Thesis / IC Memo Agent,
Verification Agent

Every claim in a thesis or IC memo needs a source. Not every source is equally
trustworthy, and AI web search tools in particular can produce confident,
specific-sounding numbers that are simply wrong. This hierarchy governs what
counts as adequate sourcing and how to handle disagreement between sources.

## Tiers, most to least trustworthy

**Tier 1 — Primary regulatory, government, and exchange data.** SEC filings
(10-K, 10-Q, 8-K) and exhibits, direct exchange notices, statute or regulation
text, government statistical releases. Cite the specific filing/document, not a
summary of it.

**Tier 2 — Trade associations and industry bodies with disclosed methodology.**
Bodies that publish a stated survey or estimation methodology (e.g., an
industry association's annual market forecast). More reliable than a generic
research-firm estimate because the methodology is inspectable, but still an
estimate — attribute it as such.

**Tier 3 — Paid market-research firms.** Multiple firms will publish wildly
different total-market-size estimates for the same market, sometimes by a
factor of two or more, because they scope the category differently. **Never
cite a single research firm's market-size number as if it were settled fact.**
Cite a range across two or more firms and note that the spread reflects
differing category scope, not measurement error.

**Tier 4 — Company self-reported data.** Earnings releases, investor decks,
transcripts, and company websites. Authoritative for *that company's own*
disclosed figures (revenue, subscriber counts, disclosed segment splits) — not a
valid source for market-wide or competitor claims. A company's own investor
material can also be promotional; treat forward-looking statements and
management commentary as management's opinion, not fact.

**Tier 5 — News aggregators, blogs, and AI-generated search summaries.** Useful
for *finding* candidate sources and for directional / recent-news awareness.
**Never cite an aggregator or an AI search summary directly in a thesis or memo
claim.** Always trace the claim back to the Tier 1–4 source it's based on and
cite that instead.

## The AI-search-summary failure mode (seen firsthand, not hypothetical)

A web search tool's AI-generated summary reported a specific stock price for a
company that was internally inconsistent with its own market-cap and
shares-outstanding numbers in the same answer — the summary had blended
mismatched data points into one confident-sounding paragraph. A direct fetch of
the actual data page gave the correct, internally consistent figures.

**Rule: whenever an AI-generated search summary and a direct fetch of a primary
page disagree, trust the direct fetch, never the summary.** If a number looks
important (it will drive a calculation, not just color a sentence), verify it
against a second independent source before using it, especially for time-
sensitive data like stock prices, share counts, and recent corporate actions.

## Handling disagreement between sources

- If two Tier 1–2 sources disagree on a hard fact (e.g., two SEC filings imply
  different share counts at different dates), check the dates — the more recent
  one usually wins, but confirm there wasn't an intervening corporate action
  (see `_shared/data-source-crosswalk.md` on stock splits).
- If Tier 3 sources disagree on a market-size estimate, report the range, not
  an average — an average of two differently-scoped estimates is not a
  meaningful number.
- If a claim can't be traced above Tier 5, either find a better source or
  explicitly label it as an assumption, not a fact.

## Practical rule

A citation is not "a source was found for this." A citation is "this specific,
traceable, appropriately-tiered source supports this specific claim, and if it
disagrees with another source, that disagreement is disclosed rather than
hidden by picking whichever number is convenient."

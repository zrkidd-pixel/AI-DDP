# Exit Route Taxonomy

Referenced by: Thesis / IC Memo Agent, Monitoring Agent.

Complements `thesis-icmemo/returns-sensitivity-conventions.md`, which
governs the exit *multiple and timing* assumption in each return case. This
file covers the exit *mechanism* — how the position actually gets
realized, since different routes carry different valuation dynamics, market
dependencies, and timing risk that a multiple assumption alone doesn't
capture.

## Verification note

Every example below was checked before being written down, not assumed.
Where a primary source (press release, filing) could be directly fetched,
that's the citation. Where the primary source blocked automated access
(BusinessWire, Reuters, and Bloomberg all returned 403s to a direct fetch;
a PitchBook profile page required a login this framework doesn't have),
the fact was corroborated through independent secondary reporting instead
of used unverified — consistent with `_shared/citation-standards.md`'s
rule that an unverifiable claim doesn't ship as fact.

## The routes

### Trade sale (strategic sale)
Selling the portfolio company to an existing operating company — typically
a strategic buyer in the same or an adjacent industry seeking market share,
technology, or synergies. Often the highest-valuation route, since a
strategic buyer can justify paying for synergies a financial buyer can't.
**Example:** Court Square Capital Partners' sale of Advanced Diabetes
Supply Group to Cardinal Health for $1.1B, announced November 2024 — Court
Square had acquired the company in December 2020 `[source: Court Square
press release / Winston & Strawn deal summary, corroborated via
citybiz.co and Nasdaq press release syndication, Nov 2024]`.

### Initial public offering (IPO)
Listing shares on a public exchange. Complex, time-consuming, high
regulatory burden, and directly exposed to market volatility at the moment
of listing — the exit isn't complete at the IPO itself, since a sponsor
typically retains and sells down shares over time (lockups, secondary
offerings), so the realized return depends on execution well beyond
listing day. **Example:** SailPoint's February 2025 IPO under Thoma Bravo,
valued at $12.8B, raising $1.38B (upsized from an initial $1.05B target)
`[source: Reuters reporting, corroborated via Bloomberg Law and Yahoo
Finance syndication, Feb 2025]`. Worth noting for the taxonomy: SailPoint
had already IPO'd once in 2017, was taken private again by Thoma Bravo in
2022 for $6.9B, then IPO'd a second time — a real illustration that "exit"
and "permanent liquidity" aren't the same thing, and a sponsor can take
the same asset through more than one exit-route cycle.

### Secondary sale (secondary buyout)
Selling to another private equity firm or financial sponsor rather than a
strategic buyer or the public market. Often faster and less operationally
disruptive than an IPO or trade sale, since the buyer is a sophisticated
financial counterparty already familiar with sponsor-owned businesses.
**Example:** KKR's acquisition of Varsity Brands from Bain Capital and
Charlesbank Capital Partners, completed August 2024, funded through KKR's
North America Fund XIII; transaction terms not disclosed `[source: KKR
press release, media.kkr.com, Aug 2024 — directly verified]`.

### Management buyout (MBO)
The existing management team purchases the company from the sponsor,
usually with acquisition financing from banks or other lenders. Genuinely
rare — the table this file is built from calls it out as such — because it
requires a management team both willing and financially able to take on
the position, and the price is often below what a strategic or secondary
buyer would pay given the management team's limited capital. **Example:**
Votronic Elektronik-Systeme (a German electronic-components manufacturer):
VR Equitypartner, a mid-market financial investor, sold its stake to the
company's own long-tenured managing directors `[source: VR Equitypartner /
Real Deals reporting, corroborated via Cadenberg and Syntra deal
summaries]`. Worth noting: one source describes this specifically as a
"company-internal succession plan with the support of a financial
investor" — meaning this example also overlaps with the "transition in
ownership" deal archetype in `_shared/deal-archetypes.md`, illustrating
that an MBO is often the *exit-route expression* of a succession-driven
entry thesis, not an unrelated event.

### Recapitalization (partial exit / dividend recap)
Restructuring the capital structure — typically issuing new debt — to fund
a distribution back to the sponsor while retaining a significant equity
stake. Realizes part of the return without a full exit, keeping upside
exposure to future growth. **This is a leverage decision, not free money —
flag it as such.** **Example:** Clayton, Dubilier & Rice's dividend
recapitalization of Shearer's Foods, roughly seven months after acquiring
the company from Ontario Teachers' Pension Plan in February 2024. Fiesta
Purchaser Inc. priced a $450M bond at a 9.625% yield to fund the
distribution, pushing the company's leverage ratio from 5.8x to 7.0x
EBITDA; S&P Global Ratings assigned the debt a CCC+ rating `[source:
Bloomberg reporting, corroborated via BNN Bloomberg syndication, Sept
2024]`. **The specific risk pattern worth naming:** a recap executed very
soon after acquisition, at a meaningfully higher leverage multiple and a
speculative-grade (CCC+) rating, is exactly the kind of aggressive
re-leveraging that credit markets and, eventually, an IC reviewing a later
deal should scrutinize — cite this as a cautionary pattern, not just a
mechanism, when a thesis proposes an early recap.

### Liquidation
Selling the company's assets piecemeal to repay debt and distribute any
remaining proceeds — generally a last resort, typically resulting in lower
returns than any other route. Usually occurs when the company is
financially distressed or no buyer can be found through the other exit
routes. Connects directly to `extensions/distressed-diligence/` — if
liquidation is a realistic downside scenario for a deal, that extension
should already be active.

## How this connects to the returns section

`thesis-icmemo/returns-sensitivity-conventions.md` requires stating the
exit multiple and exit year for every case. This file adds the missing
piece: **state which exit route each case assumes**, since the route
itself affects both the multiple that's realistic (a trade sale can
support synergy-driven premiums an IPO or secondary sale can't) and the
execution risk (an IPO case is exposed to market-timing risk a secondary
sale isn't). A downside case that silently assumes the same exit route as
the base case, just at a lower multiple, is missing a real source of
downside risk — the route itself may need to change.

## How this connects to Monitoring

Over the hold period, exit readiness is itself something worth tracking —
strategic-buyer interest emerging, public-market conditions turning
favorable or unfavorable for the sector, a competitor's IPO or sale
setting a fresh comp. `monitoring/kpi-dashboard-templates.md` doesn't
currently have a dedicated exit-readiness section; when the underwritten
exit route or timing looks like it's changing, that's a variance worth
logging explicitly, not just implied by other KPI drift.

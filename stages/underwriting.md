# Stage Definitions — Underwriting Phase

Seven stages operate in this phase. Six are independent diligence/research
workstreams that can run in parallel against the same candidate list; the
seventh (`underwriting`) is the core LBO math and has hard dependencies on
two of the others.

## Diligence & research stages (parallel, independent)

| slug | agent | execution | requires_stage | produces | consumes |
|---|---|---|---|---|---|
| `financial-diligence` | `agents/financial-diligence-agent.md` | ALWAYS | `screening` | `adjusted-ebitda`, `redflags`, `working-capital-peg` | target financials |
| `commercial-diligence` | `agents/commercial-diligence-agent.md` | ALWAYS | `screening` | `concentration-metrics`, `competitive-positioning` | target customer/contract data |
| `management-assessment` | `agents/management-assessment-agent.md` | ALWAYS | `screening` | `fit-assessment`, `key-person-risk` | management materials, references |
| `financing-capstructure` | `agents/financing-capstructure-agent.md` | ALWAYS | `screening` | `capital-structure`, `blended-cost` | fund mandate, target debt profile |
| `market-intelligence` | `agents/market-intelligence-agent.md` | ALWAYS | `screening` | `market-overview` (consumed by Thesis, not by `underwriting` stage) | confirmed sector |
| `legal-structuring` | `agents/legal-structuring-agent.md` | CONDITIONAL — runs once a specific finalist is being pursued, not against the full candidate list | `screening` | `structuring-questions`, `tracked-terms` | entity/jurisdiction facts, draft agreement (once available) |

## Core stage (hard dependencies)

| slug | agent | execution | requires_stage | produces | consumes | reviewer |
|---|---|---|---|---|---|---|
| `underwriting` | `agents/underwriting-agent.md` | ALWAYS | `financial-diligence`, `financing-capstructure` (hard); `legal-structuring` output consumed if/when available | `ranked-finalist-set`, full calc detail, verified sources-and-uses identity | `candidate-list`, `adjusted-ebitda`, `capital-structure` | `verification-agent` |

**Note:** `underwriting` cannot produce a valid ranked output without
`financial-diligence`'s adjusted EBITDA and `financing-capstructure`'s sourced
leverage terms. `commercial-diligence` and `management-assessment` findings
feed the Thesis phase's risk section directly and are not hard blockers for
the equity-check math itself — but a material finding from either (e.g.,
severe customer concentration, single-person dependency) should still be
flagged back into `underwriting` if it would change the recommended ranking.

## Gate to Thesis

Does not open until:
1. `underwriting`'s sources-and-uses identity has been independently verified
   by `verification-agent`.
2. All ALWAYS-execution diligence stages have produced their outputs (
   `legal-structuring` only required if it actually ran for the finalist set).
3. A human has approved the ranked finalist set and ranking rationale.

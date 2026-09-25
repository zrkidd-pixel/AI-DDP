# Extensions

Opt-in rule packs for deal characteristics that show up sometimes, not
every time — situational depth that shouldn't be permanently baked into
the core 14 agents, but needs real coverage when it actually applies.

## Why these are separate from the core agents

The core agents (`agents/`) handle every deal, every time — sourcing,
underwriting, diligence, thesis, monitoring. Cross-border tax structuring,
ESG-mandate compliance, and distressed-specific diligence do not apply to
every deal. Baking all of it into the core agents permanently would mean
every deal's Legal & Structuring Agent, say, carries rules about tax
treaties and repatriation constraints that are irrelevant to a plain-vanilla
domestic buyout — clutter for the common case, in service of the uncommon
one.

## How activation works

During Screening, when the fund mandate is being filled in (per
`agents/screening-agent.md`'s operating rule 8), the agent also asks about
the trigger conditions below and records which extensions apply in the
deal's own `fund-mandate.md`, under a new **Active extensions** field.
Every downstream agent checks that field before finalizing its own output;
if an extension is listed, that agent reads the relevant `.opt-in.md`
file(s) and follows them *in addition to* its normal rules — not instead
of them.

## Available extensions

| Extension | Trigger condition | Primarily read by |
|---|---|---|
| `cross-border-structuring/` | Target has meaningful non-US revenue, operations, or ownership | Legal & Structuring, Financing/Capital Structure, Underwriting |
| `esg-screening/` | The fund's LPs impose ESG mandates or exclusionary screens beyond standard sector exclusions | Screening, Thesis/IC Memo, Monitoring |
| `distressed-diligence/` | The target shows distress signals (going-concern language, covenant breach, forced corporate action like a reverse split, leverage far above sector norms) | Financial Diligence, Legal & Structuring, Verification |

## Adding a new extension

An extension is a folder with a short trigger condition (add it to the
table above) and one or more `<name>.opt-in.md` files with the actual
rules — written the same way as any other knowledge file (a real,
applicable checklist, not a description of the topic). Name the file with
the `.opt-in.md` suffix so it's visually distinct from a baseline knowledge
file that every deal reads regardless.

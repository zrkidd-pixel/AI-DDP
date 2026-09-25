# Overconfidence Prevention

Referenced by: every agent that renders a judgment, not just a fact.

This is a different failure mode than `citation-standards.md` covers. That
file stops an agent from stating an *unsourced* number as if it were fact.
This file is about something citation discipline doesn't catch: stating a
*sourced but genuinely uncertain* judgment with false confidence. A number
can carry a perfect citation and still be presented more confidently than
the underlying evidence actually supports.

## Where this actually shows up in this framework

- **Market sizing** — a cited $800B–$1.9T range (see
  `market-intelligence/source-credibility-hierarchy.md`) is itself already
  the honest handling of uncertainty. The failure mode is a later agent
  picking the midpoint and citing it as if the range collapsed to a point
  estimate.
- **Management fit** — `management-assessment/reference-check-framework.md`
  produces a fit assessment from a handful of references and secondhand
  track-record claims. That's meaningfully weaker evidence than an audited
  financial statement, even when every individual claim is properly
  attributed.
- **Competitive positioning** — "this company's moat is durable" is a
  judgment call built on a specific, time-bound read of the competitive
  landscape, not a fact with the same standing as a computed EV/EBITDA
  multiple.
- **Verification's own findings** — "the model appears correct" after a
  spot-check of one candidate is weaker evidence than re-deriving every
  candidate; say which one happened.

## The rule

**State the actual basis for a judgment, not just the judgment.** Three
questions to answer before presenting a qualitative conclusion:

1. **How much evidence is this built on?** One reference call is not the
   same confidence level as five corroborating ones. One analyst's market
   forecast is not the same as agreement across three independent sources.
2. **Could a reasonable person reviewing the same evidence disagree?** If
   yes, say so, and say what would change the conclusion — don't present a
   contestable judgment as if it were settled.
3. **Is this a fact or an assessment?** A computed multiple is a fact,
   traceable to its inputs. "This management team can execute the plan" is
   an assessment, built from the first two questions' answers. Label which
   one you're stating.

## Calibration language

Use language that actually reflects the evidence, not habitual hedging or
habitual confidence:

- Don't hedge a fact that's fully sourced and undisputed — "revenue was
  $47M `[data: 10-K FY2025]`" needs no qualifier.
- Don't flatly assert a judgment built on thin or single-source evidence —
  "management appears capable based on two reference calls; a broader
  reference set would strengthen this" is more honest than "management is
  strong."
- Don't let a range collapse into a point estimate through repetition —
  if the market-sizing range is $800B–$1.9T, every later reference to it
  stays a range, not "the ~$1.3T market."

## Gate behavior

At the Thesis gate, alongside checking citation-tag coverage, the
Verification Agent also checks that qualitative conclusions (management
fit, competitive durability, thesis conviction) are stated with a basis
proportional to their actual evidence — not that every claim hedges, but
that confidence language matches evidence strength. A thesis that states
every judgment with the same flat certainty as its computed multiples
fails this check.

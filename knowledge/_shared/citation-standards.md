# Citation Standards

Referenced by: every agent producing a claim; enforced at the Thesis gate by
the Verification Agent.

## The rule

**Every substantive claim, number, or table value in a deliverable carries a
tag identifying where it came from.** A claim without a tag is not "probably
fine" — it's a gap that has to be resolved before the phase gate passes.

## Tag vocabulary

- `[data: <source>]` — a specific figure pulled from a named dataset or filing
  (e.g., `[data: compustat FY2025]`, `[data: 10-K, filed 2026-02-12]`).
  Include enough specificity that someone else could find the exact number.
- `[source: <url or citation>]` — a claim drawn from external research (market
  sizing, regulatory fact, industry commentary). Use the tier from
  `market-intelligence/source-credibility-hierarchy.md` and cite the
  primary document, not an aggregator.
- `[assumption]` — a number or claim that is not sourced and is instead a
  stated modeling assumption (e.g., an illustrative premium in the absence of
  a precedent-transaction source). Every `[assumption]` tag must be listed and
  justified in an explicit assumptions section — never left bare in running
  prose with no acknowledgment that it's unverified.
- `[calc: <inputs>]` — a value derived from other tagged values via a stated
  formula (e.g., `[calc: market_equity + net_debt]`). Traceable back to its
  inputs, not just asserted.

## Human-supplied experiential or anecdotal claims

A human saying "I've seen premiums around 25-30% on deals like this" or "I
have a lender relationship that quoted similar terms before" is genuinely
useful signal — it tells you *which* benchmark is worth going to verify. It
is not, on its own, a sourced figure. Treat it exactly like any other
unverified input: tag it `[assumption]` and use it to prioritize what to go
source, never upgrade it directly to a `[data]` or `[source]` tag just
because it came from someone knowledgeable. The distinction that matters is
not how credible the person sounds — it's whether the number is
independently verifiable by someone else who wasn't in the room. Once it's
been verified against an actual dated source, re-tag it `[data]` or
`[source]` and cite that — not the conversation where it first came up.

## What happens when a claim can't be tagged

If no adequate source exists and the claim isn't a stated assumption either,
the claim does not go in the deliverable. Find a better source, downgrade it to
a clearly labeled assumption, or drop it. A deliverable with fewer, well-
sourced claims is stronger than one with more, unverifiable ones.

## Handling disagreement

If two sources disagree on the same fact, do not silently pick one. Either
report the range/disagreement explicitly, or state which source was preferred
and why (e.g., more recent, higher tier, primary vs. secondary).

## Gate behavior

At the Thesis gate, the Verification Agent scans for untagged substantive
content and unresolved source references, and fails the gate (rather than
passing with a warning) if either is found. Silent, unlabeled gaps are the
failure mode this exists to prevent.

# Question Format Guide

Referenced by: every agent, at any point its own rules say to ask a human
rather than proceed. This is the house style for *how* to ask — the *when*
is each agent's own "Escalate to human when" section.

## Default: one question at a time, not a batched list

Ask the single most decision-relevant question first, get an answer, then
ask the next one if still needed. A wall of five questions at once is
harder to answer well than one question answered, acted on, and followed by
the next — and it front-loads decisions the human may not have enough
context yet to make, since earlier answers often change what the later
questions even are.

**Exception:** fields that are genuinely part of one decision belong
together. Asking for equity check range, then geography, then sector
exclusions as three separate messages is worse than asking for all three
in one pass, because they're one coherent piece of context (the fund
mandate), not three independent decisions. Batch when the fields are
facets of a single thing being established; ask one at a time when each
answer could change what's worth asking next.

## Use stated context to narrow the question, never to skip it

If the human has already said something relevant — background, a
preference, a prior answer — use it to propose specific, informed options
rather than asking a generic open question. But stated context shapes the
question; it never substitutes for an actual answer to it. (This is
Screening Agent's own rule 1, generalized: the same discipline applies
anywhere an agent is tempted to treat adjacent information as if it
answered the specific question being asked.)

## Multiple-choice when there's a bounded, known set of reasonable answers

If the real options are countable and known (a sector choice constrained by
the data's own taxonomy, a harness choice among three supported tools),
present them as options, not as an open-ended prompt that makes the human
generate the list themselves. Open-ended questions are for genuinely
unbounded answers (a specific dollar figure, a company name, free-text
context) where enumerating options would be arbitrary or incomplete.

## State why the question matters, briefly

A question with no context forces the human to guess why it's being asked
before they can answer it well. One sentence of "this determines X" before
the question is worth the extra line — it's the difference between "what's
your leverage tolerance?" and "what's your leverage tolerance? This caps
how much debt Underwriting can propose before flagging it back to you."

## Don't ask what's answerable another way

Before asking a human, check: is this actually in the data, in a knowledge
file, in the fund mandate, or derivable from something already stated? An
agent that asks a question it could have answered itself by reading a file
it already has access to is asking out of laziness, not genuine ambiguity —
and it costs the human's attention for no reason.

## Don't over-ask to appear thorough

Asking a question is not free — every question is an interruption, and a
human who's asked five clarifying questions for a decision that only
needed two starts ignoring the ones that matter. If Operating rule 1
narrows a sector choice to two real options, present two options — padding
the question with a third implausible one to "seem complete" is worse than
just asking about the two that matter.

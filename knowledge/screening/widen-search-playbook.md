# Widen-Search Playbook

Referenced by: Screening Agent, Composer

Used when an initial screen fails to produce enough qualifying candidates against
fund mandate criteria (e.g., too few land inside the target equity-check band).
The instinct to avoid is silently forcing a match — lowering the bar without
saying so, or picking whichever candidates are closest regardless of fit. This
playbook is the sequence to follow instead.

## Step 1 — Run the screen exactly as specified, first

Apply the fund's literal criteria (sector, geography, equity-check band,
profitability, listing status) before considering any adjustment. Report the
raw count that clears every filter, and the count at each filter stage — don't
report only the final number. If a filter removes most of the candidate pool,
that's information, not noise.

## Step 2 — Check the actual pass/fail rule before touching the sector definition

Most mandates have an explicit minimum (e.g., "at least two of three finalists
must fall inside the equity-check band"). Check that rule precisely. Do not
average, round favorably, or interpret "close enough" charitably — if the rule
requires two in-band and only one qualifies, that is a fail, not a near-pass.

## Step 3 — Sweep systematically before concluding the sector is too narrow

Before widening the sector definition, verify the initial candidate list wasn't
just too small because it relied on brand recognition. Run a systematic sweep by
classification code (SIC/NAICS/GICS or whatever taxonomy the data supports)
across *every* category in the dataset, not just the category that seems like
the obvious fit — real candidates get miscategorized (see
`_shared/data-source-crosswalk.md`). Only conclude the pool is genuinely thin
after a code-based sweep, not a name-recall pass.

## Step 4 — Refresh to current data before finalizing anything

A candidate that fit the mandate on stale (e.g., fiscal-year-end) pricing can
fail entirely on a current quote, and vice versa. **Always re-run the equity-check
math on current market data as the last step before presenting finalists** — a
screen built on stale prices can produce an entirely different qualifying set
than the same screen built on today's prices. This is not a hypothetical: a
finalist selected on a nine-month-old price no longer qualified once refreshed,
while a different company that looked too large on the old price turned out to
fit once its price had fallen.

## Step 5 — If still thin, widen deliberately and say so

If a systematic, current-data sweep still produces too few qualifying
candidates, widen the sector or subsector definition — and document exactly
what changed and why (e.g., "expanded from X to X+Y because fewer than two
candidates cleared the equity-check band in X alone"). Never expand silently.
If the underlying reason is that the sector's real-world size distribution is
bifurcated (e.g., clustered into mega-caps far above the mandate and micro-caps
far below it, with almost nothing in between), say that explicitly — it's a
genuine structural finding about the sector, and useful thesis material in its
own right, not a screening failure to hide.

## Step 6 — Disclose deviations in the finalist set, don't smooth them over

If the final three (or N) candidates include one that doesn't cleanly meet
every criterion — cheapest multiple but below the equity-check floor, or a
real red flag uncovered during research (e.g., a forced reverse stock split, a
going-concern note, a recent restatement) — include it only with the caveat
explicit and prominent, not folded into an otherwise-clean recommendation. A
deviation that's disclosed is a judgment call; a deviation that's hidden is a
mistake waiting to be found by someone else.

## Anti-patterns to avoid

- Rounding a below-band equity check up to "essentially in range."
- Treating a name-recall candidate list as exhaustive without a code-based sweep.
- Comparing candidates on prices from different dates without noting it.
- Widening the sector without recording what changed or why.
- Presenting a flagged, higher-risk candidate with the same confidence as a
  clean one.

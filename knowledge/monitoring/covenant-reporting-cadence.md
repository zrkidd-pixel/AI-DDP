# Covenant Reporting Cadence

Referenced by: Monitoring Agent

## Standard reporting obligations post-close

- **Compliance certificates:** most credit agreements require periodic
  (often quarterly) certification that financial covenants are satisfied,
  typically delivered alongside financial statements within a specified
  number of days after period-end. Track the actual deadline from the credit
  agreement — don't assume a generic 30/45/60-day convention applies without
  checking.
- **Board reporting:** typically monthly or quarterly, covering the KPI
  dashboard (`monitoring/kpi-dashboard-templates.md`), variance
  explanations, and 100-day-plan-and-beyond initiative status.
- **LP reporting (fund level, not portfolio-company level):** governed by the
  fund's own LP agreement and reporting calendar — distinct from
  company-level covenant/board reporting, but portfolio company KPIs
  typically roll up into it on a defined schedule.

## The refresh discipline

Every periodic refresh should be **dated and versioned against the prior
period, with an explicit diff** — what changed, not just the new numbers
restated fresh. A refresh that silently overwrites the prior period's record
destroys the ability to see the trend that matters most (deteriorating
headroom, accelerating variance).

## Defined re-underwrite triggers

Rather than leaving "when do we redo the model" as an ad hoc judgment call
each time, define triggers in advance: a covenant headroom compression below
a stated threshold, a KPI miss beyond the escalation threshold set in
`monitoring/kpi-dashboard-templates.md`, a material unplanned event (customer
loss, management departure, new competitive entrant), or simply a fixed
periodic re-underwrite cadence (e.g., annually) regardless of whether a
trigger has fired. Document which trigger fired when a re-underwrite is
initiated — "we decided to check" is not the same as "the headroom trigger
fired."

## Human review point

Variance reports and covenant status go to the human/board for review before
any action (waiver request, refinancing conversation, operational
intervention) is taken — this agent's job is to surface the variance clearly
and early, not to decide the response.

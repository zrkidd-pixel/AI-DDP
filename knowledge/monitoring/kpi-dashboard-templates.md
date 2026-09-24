# KPI Dashboard Templates

Referenced by: Monitoring Agent

## Core financial KPIs (track every reporting period, vs. plan and vs. prior period)

- Revenue, EBITDA, and EBITDA margin — vs. the 100-day plan / underwriting
  case, not just vs. prior period. A business can look fine on a
  period-over-period basis while falling steadily behind the plan it was
  underwritten on — track both.
- Net debt and leverage (net debt/EBITDA) — vs. the pro forma leverage assumed
  at close, and vs. covenant thresholds per
  `financing-capstructure/covenant-conventions.md`.
- Working capital / cash conversion — vs. the peg established during
  diligence.
- Capex — actual vs. plan, both in total and by category (maintenance vs.
  growth capex).

## Value-creation-lever-specific KPIs

Each lever in `value-creation/value-lever-taxonomy.md` and the 100-day plan
should have its own tracked metric, not just roll up into the total EBITDA
number — e.g., if a lever was "procurement consolidation targeting X%
savings," track actual procurement cost against that specific target, not
just overall margin. Losing lever-level visibility makes it impossible to
tell *which* part of the plan is or isn't working when the total number
misses.

## Commercial health KPIs (carried over from pre-close diligence)

- Customer concentration and net revenue retention — tracked on the same
  basis established in `commercial-diligence/customer-concentration-frameworks.md`,
  so pre- and post-close figures are comparable.
- Pipeline / bookings, if forward-looking revenue visibility was part of the
  original thesis.

## Presentation discipline

Every KPI dashboard entry shows: actual, plan/underwritten target, variance
(absolute and %), and a one-line explanation of the variance driver when it's
material — a dashboard of numbers with no variance explanation doesn't tell
the reader anything actionable. Version and date every dashboard; a
Monitoring update should always be diffable against the prior period, not just
a fresh snapshot.

## When a KPI trend should trigger action, not just reporting

Define, per KPI, what variance threshold or trend (e.g., two consecutive
periods missing plan by more than X%) should trigger an explicit escalation
or re-underwrite — rather than leaving "when do we act on this" as an
undefined judgment call made fresh every time.

# Stage Definitions — Monitoring Phase

| slug | agent | execution | requires_stage | produces | consumes |
|---|---|---|---|---|---|
| `monitoring` | `agents/monitoring-agent.md` | ALWAYS, recurring (per the cadence in `monitoring/covenant-reporting-cadence.md`) | `thesis-icmemo` (for the approved plan), `value-creation` (for the 100-day-plan baseline) | dated/versioned `kpi-dashboard`, `variance-report`, `trigger-status` | ongoing financials, covenant compliance certificates, prior-period dashboard |

## This phase does not terminate the pipeline

Unlike the other three phases, `monitoring` is recurring, not a one-time
gate-and-advance stage. Each period, it re-runs against the same baseline and
produces a new dated/versioned output. It only routes *out* of Monitoring
when a trigger fires:

- **Trigger fires, thesis still holds** (e.g., a covenant-headroom
  compression or a lever underperforming its plan): loop back into
  `underwriting` for a re-underwrite, carrying forward the current financial
  and capital-structure facts.
- **Trigger fires, sector thesis itself is invalidated** (e.g., a structural
  market shift that changes the original investment rationale, not just this
  company's execution): loop all the way back into `screening` — see
  `stages/_dependency-graph.md`.
- **No trigger fires:** the phase simply produces its dated dashboard and
  waits for the next reporting period, per
  `monitoring/covenant-reporting-cadence.md`.

## Human-facing inputs / outputs

- **Input needed each period:** actual financial results and covenant
  compliance data for that period.
- **Output the human reviews:** the dashboard, the variance-to-plan report,
  and an explicit trigger-fired/not-fired determination.

## Gate behavior

No action (waiver request, refinancing conversation, operational
intervention, or a loop-back re-underwrite) is taken until a human has
reviewed the variance and trigger status for that period. The Composer
records which trigger fired, when, and what loop-back (if any) resulted.

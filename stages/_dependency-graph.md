# AI-DDP Dependency Graph

The full pipeline, phase by phase. This file is the map; `screening.md`,
`underwriting.md`, `thesis.md`, and `monitoring.md` in this folder are the
detail for each phase's internal stages.

```
                    ┌───────────────┐
                    │   SCREENING   │  (screening-agent)
                    └───────┬───────┘
                            │ candidate-list  [human gate]
                            ▼
        ┌───────────────────────────────────────────┐
        │               UNDERWRITING                 │
        │                                             │
        │  financial-diligence ─┐                     │
        │  commercial-diligence─┤  (parallel,         │
        │  management-assessment┤   independent       │
        │  financing-capstructure  diligence           │
        │  market-intelligence ─┤   workstreams)       │
        │  legal-structuring ───┘                     │
        │            │            │                    │
        │            ▼            ▼                    │
        │      underwriting-agent (hard-requires        │
        │      financial-diligence + financing-        │
        │      capstructure output)                    │
        └───────────────────┬─────────────────────────┘
                            │ ranked-finalist-set  [Verification check]  [human gate]
                            ▼
        ┌───────────────────────────────────────────┐
        │                  THESIS                     │
        │                                             │
        │  value-creation-agent (100-day plan)         │
        │            │                                 │
        │            ▼                                 │
        │  thesis-icmemo-agent (consumes ALL upstream   │
        │  outputs: screening, underwriting, every      │
        │  diligence stream, market intelligence,       │
        │  value creation)                              │
        └───────────────────┬─────────────────────────┘
                            │ ic-memo  [Verification check]  [Compliance check]
                            │ [human/IC gate]
                            ▼
        ┌───────────────────────────────────────────┐
        │                MONITORING                   │
        │                                             │
        │  monitoring-agent (baseline = 100-day plan)  │
        │  → dated/versioned KPI dashboard             │
        │  → trigger fired? ──yes──┐                   │
        └───────────────────────────┼─────────────────┘
                                     │
                    ┌────────────────┴──────────────────┐
                    ▼                                    ▼
            loop back to UNDERWRITING          loop back to SCREENING
            (re-underwrite; thesis            (sector thesis itself
             still holds)                      is invalidated)
```

## Cross-cutting agents (run inside every phase, not sequential stages)

- **Compliance / MNPI Agent** — gates any new data source entering any phase,
  before that phase's other agents touch it.
- **Verification Agent** — gates the Underwriting and Thesis outputs
  specifically (see each phase file for exactly where).
- **Composer** — tracks state across all of the above; is the thing that
  actually knows whether a gate is "ready" per `composer/gate-state-protocol.md`.

## Reading this graph

`requires_stage` in each phase file means a **hard dependency** — the
downstream stage cannot produce a valid output without the upstream one.
Stages without a `requires_stage` relationship to each other within the same
phase can run in parallel (e.g., the diligence workstreams in Underwriting all
read the same candidate but don't depend on each other's output).

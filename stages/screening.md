# Stage Definitions — Screening Phase

| Field | Value |
|---|---|
| **slug** | `screening` |
| **agent** | `agents/screening-agent.md` |
| **execution** | ALWAYS |
| **requires_stage** | none — entry point of the pipeline |
| **consumes** | `_shared/fund-mandate.md`; the raw financial/screening dataset(s); human-confirmed sector/subsector |
| **produces** | `candidate-list` (with filter-stage counts); `taxonomy-gaps` (documented data quirks); `pass-fail-determination` (against the mandate's finalist-count rule) |
| **reviewer** | `compliance-mnpi-agent` (clears the dataset for use before filtering begins) |
| **review_artifact** | `taxonomy-gaps` — the reviewer confirms no undisclosed data-access issue exists before the candidate list is treated as final |

## Human-facing inputs / outputs

- **Input needed from the human before this stage can start:** the sector or
  subsector choice, and the fund mandate parameters (equity check band,
  geography, exclusions) filled in on `_shared/fund-mandate.md`.
- **Output the human reviews at the gate:** the candidate list, the filter
  counts at each stage, and whether the mandate's pass/fail rule was met
  cleanly or required a documented widen-search action.

## Gate to Underwriting

Does not open until:
1. The candidate list is produced with full filter-stage counts.
2. Any widen-search action is explicitly disclosed, not silent.
3. A human has approved the resulting candidate list.

If the gate fails (pass/fail rule not met and no widen-search action taken),
the stage does not advance — it loops back into
`screening/widen-search-playbook.md` within this same stage.

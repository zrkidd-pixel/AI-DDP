# Stage Definitions — Thesis Phase

| slug | agent | execution | requires_stage | produces | consumes | reviewer |
|---|---|---|---|---|---|---|
| `value-creation` | `agents/value-creation-agent.md` | ALWAYS | `financial-diligence`, `commercial-diligence`, `management-assessment`, `underwriting` | `value-creation-plan`, `100-day-plan` | diligence findings, finalist's financial/operating profile | — |
| `thesis-icmemo` | `agents/thesis-icmemo-agent.md` | ALWAYS | `underwriting`, `value-creation`, `market-intelligence`; consumes `legal-structuring` and `management-assessment` output if available | `ic-memo` (per `thesis-icmemo/ic-memo-template.md`), mandatory risk section, judgment-call list | every upstream phase's output | `verification-agent` (citation/risk-section check), `compliance-mnpi-agent` (non-public info clearance) |

## Why `thesis-icmemo` is last, not first

This is the one deliberate departure from a naive "write the thesis, then
prove it" ordering. `thesis-icmemo` requires *every* upstream stage's output
— it cannot start meaningfully before Underwriting and the diligence
workstreams are complete, because the narrative is a synthesis of what was
found, not a prediction of what would be found. An agent attempting to draft
`ic-memo` content before its `requires_stage` list is satisfied is operating
out of sequence.

## Human-facing inputs / outputs

- **Input needed from the human before `thesis-icmemo` can close its gate:**
  none beyond what upstream stages already produced — this stage synthesizes,
  it doesn't require new human input to function, though a human may add
  qualitative color (e.g., relationship or reputational context) that isn't
  derivable from the data.
- **Output the human/IC reviews at the gate:** the full memo, with its
  citation coverage and risk-section specificity already checked by
  `verification-agent`.

## Gate to Monitoring

Does not open until:
1. `verification-agent` has confirmed citation-tag coverage and risk-section
   specificity.
2. `compliance-mnpi-agent` has cleared any non-public information referenced
   in the memo.
3. A human (or the firm's actual IC process) has approved the memo — this is
   the highest-stakes gate in the pipeline and should not be treated as a
   formality.
4. `value-creation`'s 100-day plan is handed forward explicitly as the
   Monitoring phase's tracking baseline.

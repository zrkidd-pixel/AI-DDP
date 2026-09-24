# MNPI & AI Data-Handling Framework

Referenced by: Compliance / MNPI Agent (gate on every phase that touches
non-public information), all other agents as a precondition check

This workstream does not exist in a classroom screening exercise built on public
financial-statement data. It becomes necessary the moment real deal work
involves anything a firm received under an NDA, in a data room, or through a
banker's confidential process — which is most real deal work. Treat this as a
gate that runs *before* Screening, Underwriting, or Diligence touch any new
piece of information, not a step performed after the fact.

## What counts as MNPI (material non-public information)

Information is potentially MNPI if it is **both**: (1) not available to the
general public, and (2) the kind of information a reasonable investor would
consider important to a decision to buy, sell, or hold a security — including
private-company debt or equity, not only public stock. Common examples in a PE
context: an unannounced acquisition or sale process, unreleased financial
results, a management change, a pending financing, or a specific bid price
under consideration.

**Test to apply before treating anything as "just data": if this leaked, would
it be plausible for someone to trade or negotiate differently because of it?**
If yes, treat it as MNPI-sensitive until confirmed otherwise, not the reverse.

## Public vs. non-public: the boundary is not always obvious

- A company's own SEC filings, press releases, and earnings calls are public
  once released — but data pulled from a banker's teaser, a CIM
  (confidential information memorandum), or a data room is not, even if it
  describes a company whose *other* information is public.
  - If the target is a subsidiary or division of a public company, do not
    assume divisional detail is public just because the parent's consolidated
    filings are.
  - Draft, unfiled, or embargoed regulatory filings are not public until filed.
- A deal that is "known about" informally within an industry (rumored) is not
  the same as a deal that is publicly announced. Treat rumor-stage information
  about a specific process as sensitive.

## Information walls (wall-crossing) checklist

Before using any information in a new context, confirm:

- Is there another deal team at the firm pursuing the same target, a
  competing target, or a related financing where this information could create
  a conflict?
- Has this information source (banker, management team, data room) explicitly
  or implicitly restricted its use to a specific deal team or purpose?
- If the information needs to move across an existing wall (e.g., a generalist
  research finding is relevant to two live deal teams), has that crossing been
  explicitly approved through the firm's actual wall-crossing procedure — not
  assumed to be fine because the same underlying AI session or user has access
  to both?

**An AI tool with a shared memory or session does not respect information
walls on its own.** If a firm uses one AI environment across multiple deal
teams, wall-crossing has to be enforced procedurally (e.g., segregated
sessions/workspaces per deal, explicit access grants) — it will not happen
automatically just because the underlying technology could technically keep
things separate.

## What can and cannot go into an AI tool

This depends entirely on the specific firm's AI usage policy and the specific
tool's data-handling terms (e.g., whether inputs are used for model training,
where data is stored, retention period) — **this file cannot substitute for
that policy and should point to it, not replace it.** Absent a specific policy,
default to the more conservative reading:

- Public filings, published research, and information the firm has already
  cleared for external sharing: generally lower risk to process through an AI
  tool, subject to the tool's own data-handling terms.
- Data room documents, unfiled financials, management projections, or anything
  received under an NDA: **do not paste into a general-purpose or third-party AI
  tool without explicit confirmation that the tool and its data-handling terms
  have been approved for this use by the firm's compliance function.**
- Personally identifiable information about individuals (management team
  personal financial details, employee data uncovered in diligence): treat as
  sensitive regardless of the deal's confidentiality status; separate legal/
  privacy considerations apply.

## Gate behavior

This agent's job is to stop and ask, not to make the confidentiality
determination itself. When a new data source enters any phase, it should
surface: what is this information, where did it come from, is it public, and
if not, has the human confirmed it's cleared for this use and this tool. If any
answer is unclear, the gate does not pass silently — it blocks and asks.

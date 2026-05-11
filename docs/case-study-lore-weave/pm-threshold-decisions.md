# PM Threshold Decisions — LoreWeave Phase 0

> **Status:** Pending project-owner commitment (2026-05-11).
> **Spec:** Phase 0 §2 inputs; PM walk-through at [`pm-calibration-guide.md`](../pm-calibration-guide.md); calibration anchors at [`calibration-standards.md`](../calibration-standards.md).
> **Tier applied:** **Tier 1 — Startup / Lean** (no historical PPB, no formal velocity baseline).
>
> Phase 0 §2 mandates these five decisions in writing **before** Phase 0 begins. Without them, Phase 0 has no scope and either runs forever or stops arbitrarily.

---

## 1. Significance threshold

> *What enters the Past Decisions Catalog.*

**Decision:** _Pending._

**Tier 1 default heuristic (per PM Calibration Guide §1):** a past decision enters the catalog if **any one** is true:

- It changed the project's scope (features added, removed, or reframed).
- Its reversal would require > 5 person-days of rework. *(Framework-internal Tier 1 anchor; adjust if LoreWeave's pace is very different.)*
- It was discussed in writing (RFC, ADR, design doc, or commit message with rationale).
- It created or removed an external integration (third-party API, model provider, payment gateway).
- It changed team structure (roles added, reassigned, or removed) — N/A for solo project; can be reused as "new tool / service added to the developer's working set".
- It has been referenced in subsequent decisions.

**Project-owner specifics (to fill):**

- Adjustments to the default heuristic: _(e.g., "5 person-days → 1 day for solo pace")_
- Additional criteria specific to LoreWeave: _(e.g., "any change touching the canon-integrity invariant counts")_

---

## 2. Materiality threshold (Failure Inventory)

> *What counts as a "real" failure worth surfacing.*

**Decision:** _Pending._

**Tier 1 default heuristic (per PM Calibration Guide §2):** anything that caused:

- Production downtime > 30 minutes, OR
- A user-visible regression that required rollback or hotfix, OR
- An off-hours on-call alert, OR
- Any data loss, OR
- A security incident at any severity.

Substitute for pre-production projects: "lost > 1 day of team time".

**Project-owner specifics (to fill):**

- LoreWeave production status (deployed / pre-production / mixed): _(to fill)_
- Adjustment: e.g., "> ½ day of solo-developer time lost on a regression" if no production yet.
- Architect-rot specifically in scope of materiality? — *strong recommendation: yes,* given the framework's central premise.

---

## 3. Audit scope

> *Which services / repos / modules.*

**Decision:** _All 6 services + foundation/governance/planning docs, split into 2 passes (per case-study README)._

**Pass 1 — TBD which services first.** Selected during Reckoning Team kick-off based on:

- Recent activity (commits in last 3 months).
- Subjective "rot signal" — which services the project owner feels most uncertain about.
- Dependencies (audit dependencies before dependents when possible).

**Pass 2 — remaining services + cross-cutting concerns.**

**Project-owner specifics (to fill):**

- Confirmed Pass 1 services: _(to fill after first read of the repo)_
- Out-of-scope content: _(e.g., third-party vendored code, generated migrations, test fixtures)_

---

## 4. Time budget

> *How long Phase 0 has.*

**Decision:** _Pending._

**Tier 1 default — M&A IT due-diligence rule of thumb (per PM Calibration Guide §4 Tier 1):**

| Codebase quality | Rate |
|---|---|
| Well-organized monorepo with good docs | 1 person-week per 50 KLOC |
| Polyglot with mixed quality | 1 person-week per 20 KLOC |
| Legacy / poorly documented | 1 person-week per 10 KLOC |

Multiply by 1.5 if multiple ages of code coexist.

**Time-boxing semantics (per debate 003 Q3):** soft target with 80% / 100% structured escalation.

**Project-owner specifics (to fill):**

- LoreWeave KLOC estimate: _(to fill — will run `cloc` or `scc` as part of Pass 1)_
- Codebase quality bucket: _(to fill)_
- Initial budget: _(to fill after KLOC measurement)_

---

## 5. Re-reckoning cadence

> *How often the Reckoning Record is reviewed after Phase 1 sealing.*

**Decision:** _Pending._

**Tier 1 default (per PM Calibration Guide §5 Tier 1):** quarterly + triggered by any major scope change or architectural pivot.

The cadence is committed in writing inside the Reckoning Record itself (per [debate 002](../debates/002-retrofit-vs-greenfield.md) Q6).

**Project-owner specifics (to fill):**

- Cadence: _(default: quarterly; project owner may adjust)_
- Pivot triggers specific to LoreWeave: _(e.g., "any new service added to contracts/api/", "any change to the canon-integrity invariant")_

---

## Acceptance

PM Threshold Decisions are finalized when:

- [ ] Each of the five sections above has a concrete decision (not "pending").
- [ ] Tier 1 defaults are either adopted verbatim or explicit adjustments are recorded.
- [ ] Decisions are committed in writing **before** the Reckoning Team begins inventory work.

Once all five are committed, the Reckoning Team kick-off can occur.

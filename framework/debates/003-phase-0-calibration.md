# Debate 003 — Phase 0 Calibration Questions

> **Status:** decided.
> **Opened:** 2026-05-08
> **Decided:** 2026-05-08
> **Decided by:** project owner
> **Affects:** [phase-0-for-debate.md](../phases/phase-0-for-debate.md). Produces [calibration-standards.md](../calibration-standards.md) and [pm-calibration-guide.md](../pm-calibration-guide.md) as supporting artifacts.
> **Raised by:** project owner — close-out triage for Phase 0.

---

## Context

Phase 0 was authored with four open questions deferred to a focused close-out debate. They are **calibration questions**, not design questions: how should the PM's authority to size Phase 0 be anchored without prescribing it. This debate proposes answers for all four together so Phase 0 can be locked.

---

## Q1 — Significance threshold heuristic for Past Decisions Catalog

### The question
PM owns the threshold. Should the framework offer a default heuristic to anchor PM judgment, or leave it fully unguided?

### Real-world anchor
Audit standards (ISA, GAAP) define materiality with both quantitative and qualitative anchors; preparers tune to context. PMBOK / PRINCE2 (current PRINCE2 7th edition, 2023) provide categorical guidance on what counts as a tracked project change. Architecture review board practice typically uses **organization-defined** thresholds — common examples include "affects > 2 services" or "creates a cross-team contract" — but specific cut-offs vary by team and are not standardized across the industry. Postmortem severity tiers (S1/S2/S3 in Etsy / Google SRE) anchor judgment while leaving project-specific calibration to teams. The pattern across all four: **categorical anchor + numeric flexibility**.

### Proposed answer
Framework provides a **categorical heuristic; PM tunes numbers and may extend or override.** Non-binding default.

A past decision is "significant" — and therefore enters the Past Decisions Catalog — if at least one is true:

- It changed the project's scope (features added, removed, or reframed).
- Its reversal would require more than a PM-defined threshold of person-days of rework.
- It was treated as significant at the time — discussed in writing (RFC, ADR, design doc, meeting minutes).
- It created or removed an integration with an external system.
- It changed team structure (roles added, reassigned, removed).
- It has been referenced in subsequent decisions (downstream impact, regardless of original visibility).

PM may add criteria, set/raise/lower numbers, or replace the list entirely if the project's nature warrants it. The framework's role is to anchor thinking, not to prescribe the threshold.

---

## Q2 — Reckoning Team composition rule

### The question
Phase 0 specifies 2–5 people with seniority mix as a recommendation. Should the composition become a hard rule?

### Real-world anchor
Code review practice prescribes a reviewer mix (owner + outside senior). NTSB aviation incident investigations require multi-disciplinary investigators (engineering, ops, human factors). Medical morbidity-and-mortality (M&M) conferences prescribe attending + resident, sometimes external review. Software audit teams prescribe a mix of code knowledge and audit independence. Across all four, **uniform teams produce one-sided findings** — the same risk that motivated the Council minimum-diversity rule.

### Proposed answer
Promote composition from recommendation to **rule**:

- **2–5 people** (size already established).
- **≥ 1 IC who actively maintains code in scope** — mandatory. The bottom-up principle requires actual bottom-up presence, not its proxy.
- **≥ 1 person with tenure spanning the period being reckoned** when project age permits — institutional memory; surfaces "we used to do X" knowledge that fresh members cannot access.
- **≥ 1 person from outside the immediate scope being reckoned** when team size permits — fresh-eyes review; catches contradictions and blind spots that insiders rationalize.

The two "when … permits" softeners cover small / young projects where the rules cannot all be met. For mid-to-large teams, all three are required.

---

## Q3 — Time-boxing semantics

### The question
PM sets a time budget for Phase 0. Is it a soft target or hard stop? What happens if quality gates are not met within the budget?

### Real-world anchor
Agile timeboxing (the Iron Triangle pattern) uses hard time and treats scope as the variable. PRINCE2 stages use soft time with a formal extension process via the tolerance pattern. Toyota's kaizen events (typically 3–5 days; US convention 3–5) hard-time and adjust scope. PMBOK tracks variance and escalates when off-budget. The shared logic: **hard limits force pressure; structured escalation prevents corner-cutting**.

### Proposed answer
**Soft target with structured escalation** (rejects both pure hard-stop and pure unbounded).

- PM sets a target budget at Phase 0 input.
- **At 80% elapsed**: status check. Reckoning Team reports percentage complete by section to PM and Facilitator.
- **At 100% elapsed**, if quality gates are not met, the PM must commit to one of three actions in writing:
  1. **Extend** — set a new target with rationale.
  2. **Reduce scope** — raise the significance threshold; items dropped become "deferred to next reckoning" entries in the Reckoning Record.
  3. **Continue without quality gates met** — accept incomplete inventory; record specific gaps in the Reckoning Record itself; gaps become known risks carried into Phase 1.
- A single extension is allowed without notification. A second extension requires Council awareness (notification, not approval).

Hard stop is rejected because it tends to produce sanitized inventories under deadline pressure. Unbounded extension is rejected because it tends to dissolve the discipline that protects against documentation-theater drift.

---

## Q4 — Greenfield "lightweight" Phase 0

### The question
Greenfield projects are allowed to skip Phase 0 or run it lightweight. What does "lightweight" mean specifically? When is full skip permissible?

### Real-world anchor
PMBOK "tailoring" prescribes process scaling — full for complex projects, lighter for simple ones. Agile Inception Deck preserves the same 10 questions across project sizes but varies execution depth. Lean Startup keeps minimal upfront artifacts, expanding as the project grows. The principle: **even greenfield teams carry assumptions, external commitments, and prior-project biases worth surfacing**, even when no code yet exists to audit.

### Proposed answer
**Lightweight Phase 0 is the default for greenfield. Full skip is permitted only when the team is a single person, or two people who have worked together before on similar projects.**

Lightweight Phase 0 **keeps**:
- **Assumption Surface** (replaces Implicit Principles Surface) — each Council member independently writes: "What assumptions am I bringing to this project? What 'of course we'll' patterns am I applying without thinking? What habits am I importing from prior projects?"
- **External Commitment Audit** — what has been promised to whom, by when, that constrains the project before code begins.
- **Stakeholder and Integration Map** — who depends on the outcome; which external systems will be touched.
- **(Optional)** Failure Lessons from Analogous Projects — failures from similar past projects the team or organization has done. Not strict self-inventory; lessons-learned input.

Lightweight Phase 0 **omits**:
- Current State Audit — N/A.
- Past Decisions Catalog — N/A.
- Failure Inventory of the project's own past — N/A.

Typical time budget: 1–3 days, versus weeks for retrofit. PM still owns thresholds and cadence; for greenfield, the re-reckoning cadence question typically reframes as "when do we re-run Phase 0 as the project matures?" Reasonable default: at the first major scope or architecture change, plus a PM-defined fixed interval (e.g., quarterly).

---

## Recommendation TL;DR

| Q | Decision |
|---|---|
| Q1 — Significance heuristic | Provide categorical heuristic (6 bullets), PM tunes numbers / extends / overrides. |
| Q2 — Reckoning Team composition | Promote to rule: ≥1 active-IC (mandatory) + ≥1 tenure-spanning + ≥1 outside-scope (last two when team size / project age permits). |
| Q3 — Time-boxing | Soft target with 80% check-in and 100% structured choice (extend / reduce / accept-incomplete with recorded gaps). |
| Q4 — Greenfield lightweight | Lightweight default for greenfield (Assumption Surface + Commitment Audit + Stakeholder Map). Full skip only for solo / duo teams. |

If approved, Phase 0 is closed and ready for application against LoreWeave.

---

## Decision

All four proposed answers approved with the additional commitment to anchor them on industry standards rather than framework-invented numbers.

**Framework-wide policy adopted in this debate:** Dead Light Framework adopts industry-standard formulas — it does not invent them. Documented in [calibration-standards.md](../calibration-standards.md).

- **Q1:** Approved. Categorical heuristic (6 bullets) is the default; PM tunes numbers, extends, or overrides. Anchored on ITIL Change Management tiers, ISA 320 / GAAP / IFRS materiality, PMBOK EVM variance thresholds, CMMI Causal Analysis & Resolution. PMs without prior calibration experience walk through this in [pm-calibration-guide.md § 1](../pm-calibration-guide.md#1-significance-threshold).
- **Q2:** Approved. Reckoning Team composition rule: 2–5 people, ≥1 active-IC (mandatory), ≥1 tenure-spanning (when project age permits), ≥1 outside-scope (when team size permits). Anchored on Brooks's Law communication overhead, Two-pizza team, Dunbar's layered model, Team Topologies enabling-team pattern.
- **Q3:** Approved. Soft target with 80% / 100% structured escalation. PM derives initial budget per [pm-calibration-guide.md § 4](../pm-calibration-guide.md#4-time-budget-for-phase-0), anchored on COCOMO II, M&A IT due-diligence rule of thumb, IFPUG Function Points, Putnam SLIM, or DORA baselines depending on PM tier.
- **Q4:** Approved. Lightweight Phase 0 default for greenfield (Assumption Surface + External Commitment Audit + Stakeholder & Integration Map). Time anchor: 1–3 days, or 1–2% of projected effort via COCOMO II planning mode. Full skip permitted only for solo / duo teams that have worked together before.
- **Decided on:** 2026-05-08
- **Decided by:** project owner

### Follow-up actions

- [x] Create [calibration-standards.md](../calibration-standards.md) reference catalog of industry standards.
- [x] Create [pm-calibration-guide.md](../pm-calibration-guide.md) practical step-by-step guide at three rigor tiers.
- [x] Bake the four decisions into [phase-0-for-debate.md](../phases/phase-0-for-debate.md): Inputs, Quality Gates, Roles, Anti-patterns updated; "Note on Method" open questions resolved.
- [x] Update [debates/README.md](README.md) index to status `decided`.
- [x] Establish framework-wide policy: industry standards over framework-invented formulas. Apply forward.

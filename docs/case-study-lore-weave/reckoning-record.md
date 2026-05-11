# Reckoning Record (draft) — LoreWeave Phase 0

> **Status:** Skeleton (2026-05-11). Content fills in as Pass 1 and Pass 2 of the Current State Audit complete and project owner contributes Past Decisions, Failures, and Implicit Principles entries.
>
> **Spec:** Phase 0 §4 (output format — four sections of the Reckoning Record draft); Phase 1 §10 (Phase 1 adds a fifth section after Reckoning step).
>
> **Audit pass map:** Pass 1 = toolchain/foundation + 2 most-active services. Pass 2 = remaining 4 services + cross-cutting concerns. Both passes feed this single Reckoning Record before the Council review session.
>
> **Document state model:** This file is the **draft** Reckoning Record. It reaches v1.0 when Phase 1 seals the Astronomican. After Phase 1, it becomes a **living document** — Fix-by-date items are tracked here as they're resolved.

---

## Section 1 — Current State Audit

> *What is actually deployed, what is actually in `main`, what services exist with what contracts.* (Phase 0 §3.1)
>
> Documentation is **evidence, not truth** — discrepancies between docs and reality are explicitly recorded.

### 1.1 Repository topology

_(Pending — to be filled by AI-aide-1 from `cloc` / `scc` run + tree walk over `C:\Works\_Researchs\lore-weave`. Project owner verifies before any "deployed" claim becomes final.)_

| Service | Path | KLOC | Languages | Last commit (approx) | Deployment status |
|---|---|---|---|---|---|
| identity | `contracts/api/identity/` _(to verify)_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ |
| books | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ |
| catalog | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ |
| model-billing | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ |
| model-registry | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ |
| sharing | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ |

### 1.2 Cross-service contracts (API, schema)

_(Pending — relevant for the Sector Astronomican trigger evaluation in Section 1.5.)_

### 1.3 Documentation vs reality discrepancies

_(Pending. Any case where `docs/` claims something the code does not do, or vice versa, lands here.)_

### 1.4 External integrations and dependencies

_(Pending — third-party model providers, payment processors, identity providers, storage backends.)_

### 1.5 Sector Astronomican trigger evaluation

Per [debate 001](../debates/001-laws-count-and-multirepo-scaling.md), Sector split requires **all four** of the following to be true:

| Trigger condition | Status for LoreWeave |
|---|---|
| ≥ 2 repositories or services that deploy independently | _to evaluate_ |
| Each has a dedicated team or on-call rotation | _to evaluate_ (LoreWeave is solo; this condition is hard to meet) |
| Cross-team contracts (API, schema) exist and must be negotiated | _to evaluate_ |
| Genuinely local decisions exist that the Imperial Council should not be making | _to evaluate_ |

Verdict will be: Sector split warranted **only** if all four are true; otherwise single Imperial Astronomican.

---

## Section 2 — Past Decisions Catalog

> *Significant scope changes, architectural pivots, abandoned directions, technology choices.* (Phase 0 §3.2)
>
> Each entry: decision, date, named decision-maker(s), context that drove it, what changed as a result.
> **Attribution is required** per [debate 002](../debates/002-retrofit-vs-greenfield.md) Q3.

### 2.1 Format

| # | Date (approx) | Decision-maker(s) | Decision | Context that drove it | What changed | Source of record |
|---|---|---|---|---|---|---|
| D-001 | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _git / docs / chat / recollection_ |

### 2.2 Entries

_(Project-owner-driven section. AI-aide-1 surfaces git-log candidates and asks "is this significant?"; project owner accepts or rejects each into the catalog with named attribution.)_

### 2.3 Decisions deferred / abandoned

_(Decisions that were considered and rejected, or that were started and abandoned. Equally informative as decisions that were taken.)_

---

## Section 3 — Failure Inventory

> *Material failures with date, blast radius, named participants, and root cause where known.* (Phase 0 §3.3)
>
> **Attribution required, blame avoided.** Borrowed framing from blameless-postmortem culture: names are kept, blame is not assigned.

### 3.1 Format

| # | Date (approx) | Failure | Blast radius | Named participants | Root cause (if known) | Confidence |
|---|---|---|---|---|---|---|
| F-001 | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _to fill_ | _high / medium / low_ |

### 3.2 Architect-rot specifically

Per case-study focus area #2 (per `README.md`), this sub-section deliberately enumerates failures that match the **architect-rot pattern** the framework names: conflicting refactors, scope drift, accumulated context rot, scope changes that contradicted earlier decisions.

| # | Pattern | Specific instance in LoreWeave | Failure-inventory link |
|---|---|---|---|
| AR-001 | _Conflicting refactor_ | _to fill_ | _F-NNN_ |
| AR-002 | _Scope drift_ | _to fill_ | _F-NNN_ |
| AR-003 | _Context rot (AI agent re-invented decision)_ | _to fill_ | _F-NNN_ |

### 3.3 Entries

_(Project-owner-driven; AI-aide-1 surfaces git-revert and refactor-thrash candidates from git log.)_

---

## Section 4 — Implicit Principles Surface

> *Each Reckoning Team member writes, **independently and without coordination**, the principles they believe the team has been operating under.* (Phase 0 §3.4)
>
> **Aggregation comes after independent capture; contradictions across members are the most valuable output of this section.**

### 4.1 Independent contributions

**Project owner — independent contribution:**

_(To fill: the project owner writes here, before reading the AI-aide draft below, what they believe LoreWeave has been operating under. Examples of the format the framework expects:_
- _"We always preserve canonical narrative over speed of iteration."_
- _"Of course we'll preserve author intent across translations."_
- _"AI agents help, but the human-authored narrative is the ground truth.")_

**AI-aide-1 — independent contribution (outside-scope perspective):**

_(To fill: AI-aide-1 reads the LoreWeave codebase + docs and writes here, without seeing the project owner's draft, what principles APPEAR to be in operation based on code/doc evidence. This is what the project_owner-aide pair captures as "the outside view of espoused vs in-use values" — Schein / Argyris-Schön per Phase 0 §9.)_

### 4.2 Synthesis (after independent capture)

**Convergent principles** (project owner and AI-aide-1 agree):
- _to fill_

**Contradictions** (project owner and AI-aide-1 disagree):
- _to fill — these are the most valuable Phase 0 output_

**Principles surfaced only by one member:**
- Project owner only: _to fill_
- AI-aide-1 only: _to fill_

### 4.3 Note on single-human risk

Per `reckoning-team-record.md` § "Single-reviewer risk acknowledgment", this section is structurally at risk of single-viewpoint capture because the project owner is the sole human Reckoning Team member. The AI-aide-1 independent contribution is the only mechanism by which a second perspective enters. Future re-reckoning iterations should aim to add a second human reviewer.

---

## Section 5 — Classifications (added by Phase 1 Reckoning step)

> *Phase 0 produces sections 1–4 as input to Phase 1. Phase 1's Reckoning step (inserted between Boundaries and Stress Test per phase-1 §10.2) adds this fifth section.*
>
> **This section is empty until Phase 1 runs.**

Per [debate 002](../debates/002-retrofit-vs-greenfield.md) Sub-decision B (B3 hybrid), each significant past decision (from Section 2) is classified into one of four buckets:

| Decision | Classification | Owner (if Fix-now / Fix-by-date) | Sunset date | Reasoning |
|---|---|---|---|---|
| _D-NNN_ | _Keep / Fix-now / Fix-by-date / Reconsider Law_ | _to fill_ | _to fill_ | _to fill_ |

**Migration Plan** (extraction of Fix-now and Fix-by-date items as actionable backlog) will be a separate file `migration-plan.md` in this folder once Phase 1 runs.

---

## Acceptance criteria — Reckoning Record (draft)

Per Phase 0 §5 quality gates, this draft is **NOT done** until all of the following are true:

- [ ] Section 1 covers all services / components in scope (per `pm-threshold-decisions.md` §3 scope, split across Pass 1 + Pass 2).
- [ ] Section 1 explicitly records every discrepancy between documented and deployed reality (rather than papering over).
- [ ] Section 2 covers every decision the PM has flagged as significant per `pm-threshold-decisions.md` §1.
- [ ] Section 3 includes every material failure per `pm-threshold-decisions.md` §2. Items the team is unsure about are listed with confidence note rather than omitted.
- [ ] Section 4 contains independent contributions from every Reckoning Team member, captured before any group discussion.
- [ ] Section 4 names contradictions between members where they exist (a clean consensus-style synthesis is a failure, not a success).
- [ ] Every Ascension Council member has read this draft at least once before the Council review session.
- [ ] The Council review session has occurred and the Reckoning Team has either resolved Council questions or recorded them as "investigation pending" with rationale.

When all eight are checked, this draft is ready for the Phase 1 session.

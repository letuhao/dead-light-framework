---
title: "Reckoning Record Template"
status: fillable
version: not versioned
audience: both
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Fillable template — copy into your project; fill the four-section inventory in Phase 0; the fifth section is added during Phase 1's Reckoning step.
> **Audience:** Reckoning Team (Phase 0 producers); Ascension Council (Phase 1 reviewers).
> **Purpose:** The living Reckoning Record document that spans Phase 0 inventory + Phase 1 classification + post-sealing Fix-by-date tracking.
> **Read next if:** you're starting Phase 0 and need the canonical artifact format.

# Reckoning Record — <project name>

> **Phase 0 produced sections 1–4 (draft); Phase 1 adds section 5 (classifications + Migration Plan); after Phase 1 sealing this becomes a living document.**

---

## Section 1 — Current State Audit

> *What is actually deployed, what is actually in `main`, what services exist with what contracts.* (Phase 0 §3.1)
>
> Documentation is **evidence, not truth** — discrepancies between docs and reality are explicitly recorded.

### 1.1 Repository topology

| Service / module / area | Path | KLOC | Languages | Last commit (approx) | Deployment status |
|---|---|---|---|---|---|
| <name> | <path> | <KLOC> | <Python / TS / Go / …> | <YYYY-MM-DD> | <production / staging / dev / N/A> |

### 1.2 Cross-service contracts (API, schema)

<List inter-service contracts that constrain or couple components.>

### 1.3 Documentation vs reality discrepancies

<Any case where docs/ claims something the code does not do, or vice versa.>

### 1.4 External integrations and dependencies

<Third-party APIs, model providers, payment processors, identity providers, storage backends.>

### 1.5 Sector Astronomican trigger evaluation

Per debate 001, Sector split requires all four:

| Trigger condition | Status for this project |
|---|---|
| ≥ 2 repositories or services that deploy independently | <yes / no / partial — describe> |
| Each has a dedicated team or on-call rotation | <yes / no — describe> |
| Cross-team contracts (API, schema) exist and must be negotiated | <yes / no — describe> |
| Genuinely local decisions exist that the Imperial Council should not be making | <yes / no — describe> |

**Verdict:** Sector split <warranted / not warranted> — <one-line rationale>.

---

## Section 2 — Past Decisions Catalog (with attribution)

> *Significant scope changes, architectural pivots, abandoned directions, technology choices.* (Phase 0 §3.2)
>
> **Attribution required** per debate 002 Q3.

| # | Date (approx) | Decision-maker(s) | Decision | Context that drove it | What changed | Source of record |
|---|---|---|---|---|---|---|
| D-001 | <YYYY-MM-DD> | <named human(s)> | <one-line decision> | <one-paragraph context> | <what changed as a result> | <git / docs / chat / recollection> |

<Add rows as significant decisions are inventoried per pm-threshold-decisions §1 Significance threshold.>

---

## Section 3 — Failure Inventory (with attribution)

> *Material failures with date, blast radius, named participants, and root cause where known.* (Phase 0 §3.3)
>
> Attribution required; blame avoided. Borrowed framing from blameless-postmortem culture.

| # | Date (approx) | Failure | Blast radius | Named participants | Root cause (if known) | Confidence |
|---|---|---|---|---|---|---|
| F-001 | <YYYY-MM-DD> | <one-line failure description> | <user-facing / cross-service / single-module> | <named human(s)> | <one-paragraph root cause; or "unknown — investigation pending"> | <high / medium / low> |

<Add rows as material failures are inventoried per pm-threshold-decisions §2 Materiality threshold.>

---

## Section 4 — Implicit Principles Surface

> *Each Reckoning Team member writes, independently and without coordination, the principles they believe the team has been operating under.* (Phase 0 §3.4)
>
> **Aggregation comes after independent capture; contradictions across members are the most valuable output of this section.**

### 4.1 Independent contributions

**<Team member name> — independent contribution:**

- <"We always preserve X over Y.">
- <"Of course we'll <pattern>.">
- <"AI agents help, but <ground truth statement>.">

**<Team member name> — independent contribution:**

- <...>

<Add per-member sections. Each member writes independently before any aggregation.>

### 4.2 Synthesis (after independent capture)

**Convergent principles** (multiple members agree):
- <principle>

**Contradictions** (members disagree — these are the most valuable output):
- <principle pair X vs Y; which member held which>

**Principles surfaced only by one member:**
- <member name>: <principle>

---

## Section 5 — Classifications (added by Phase 1 Reckoning step)

> *Phase 1's Reckoning step (inserted between Boundaries and Stress Test per phase-1 §10.2) classifies each significant past decision into one of four buckets.*

Per debate 002 Sub-decision B (B3 hybrid):

| Decision (link to §2) | Classification | Owner (if Fix-now / Fix-by-date) | Sunset date | Reasoning |
|---|---|---|---|---|
| D-NNN | <Keep / Fix-now / Fix-by-date / Reconsider-Law> | <named human or N/A> | <YYYY-MM-DD or N/A> | <one-line reasoning> |

**Migration Plan** (extraction of Fix-now and Fix-by-date items as actionable backlog): see `migration-plan.md` separate document once Phase 1 completes.

---

## Re-reckoning cadence

Per the cadence committed in `pm-threshold-decisions.md` §5: **<cadence; e.g., quarterly + pivot triggers>**.

Past re-reckoning events:

| Date | Trigger | Outcome |
|---|---|---|
| <YYYY-MM-DD> | <quarterly / scope-pivot / new-service / …> | <one-line outcome> |

---

## Provenance

- Template version: distribution v0.6.0.
- Phase 0 spec: `distribution/framework/phases/phase-0.md` §4 Outputs.
- Phase 1 retrofit additions: phase-1 spec §10 (in framework upstream; pending full seal).

---
title: "PM Threshold Decisions Template"
status: fillable
version: not versioned
audience: human
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Fillable template — copy into your project; fill the five sections; sign off before Phase 0 begins.
> **Audience:** Project Manager / Product Owner; committed in writing before Phase 0 inventory work begins.
> **Purpose:** The five PM commitments per Phase 0 §2 inputs (Phase 0 cannot begin without these).
> **Read next if:** you are the PM for a project starting Phase 0.

# PM Threshold Decisions — <project name>

> **Phase 0 §2 mandates these five decisions in writing before Phase 0 begins.** Without them, Phase 0 has no scope and either runs forever or stops arbitrarily.
>
> **Tier applied:** <Tier 1 — Startup / Lean | Tier 2 — Mid-org | Tier 3 — CMMI L4+>
>
> See `framework/pm-calibration-guide.md` for step-by-step walkthrough at each tier.

---

## 1. Significance threshold

> *What enters the Past Decisions Catalog.*

**Decision:**

A past decision enters the catalog if any one is true (Tier 1 categorical bullets; per PM Calibration Guide §1):

- It changed the project's scope (features added, removed, or reframed).
- Its reversal would require more than <X person-days> of rework.  *(Tier 1 default = 5 person-days; adjust if your team's pace is very different.)*
- It was discussed in writing (RFC, ADR, design doc, formal meeting minutes, or commit message with explicit rationale).
- It created or removed an external integration (third-party API, model provider, etc.).
- It changed team structure (roles added, reassigned, or removed).
- It has been referenced in subsequent decisions.

**Project-specific additions:**

- <e.g., "any change touching the <project-specific invariant>">
- <e.g., "any architectural rewrite at <scale>">

---

## 2. Materiality threshold (Failure Inventory)

> *What counts as a "real" failure worth surfacing.*

**Decision:**

Any of the following is material (Tier 1 base; per PM Calibration Guide §2):

- Production downtime > 30 minutes
- A user-visible regression that required rollback or hotfix
- An off-hours on-call alert
- Any data loss
- A security incident at any severity

**For pre-production projects:** substitute "lost > 1 day of team time" (or your project's equivalent).

**Project-specific additions:**

- <e.g., "any decision reversed within 30 days — architect-rot signal">
- <e.g., "any case where an AI agent contradicted previous design in committed code">

---

## 3. Audit scope

> *Which services / repos / modules.*

**Decision:**

In scope:

- <service / repo / module 1>
- <service / repo / module 2>
- <...>

Out of scope (explicit, with reasons):

- <third-party vendored code>
- <generated migrations / test fixtures>
- <...>

**Pass strategy (if scope is large):**

- Pass 1: <highest-signal areas — recent activity, uncertain areas, dependencies-of-dependents>
- Pass 2: <remaining areas + cross-cutting concerns>

---

## 4. Time budget

> *How long Phase 0 has.*

**Decision:**

Initial target: **<N person-weeks>** across the Reckoning Team's calendar.

Derivation:

- Codebase size: <KLOC measured via cloc / scc>
- Codebase quality: <well-organized / polyglot mixed / legacy poorly-documented>
- Tier 1 rate (M&A IT due-diligence rule): <1 person-week per 10–50 KLOC depending on quality; multiplier 1.5× if multiple ages coexist>
- Raw estimate at M&A rate: <N person-weeks>
- After AI-aide leverage (if invoking Adeptus Administratum): <% reduction>
- Project-owner attention estimate: **<N person-weeks>** (this is the binding number)

**Escalation rule (per debate 003 Q3):**

- At 80% elapsed: status check; Reckoning Team reports % complete by section.
- At 100% elapsed: project owner commits to one of: (a) extend with new target + rationale; (b) reduce scope (raise significance threshold, defer items); (c) accept incomplete inventory with named gaps as known risks for Phase 1.

---

## 5. Re-reckoning cadence

> *How often the Reckoning Record is reviewed after Phase 1 sealing.*

**Decision:**

Base cadence: **<quarterly | semi-annually | release-aligned | SPC-driven>** (Tier 1 default = quarterly).

Pivot triggers (re-reckoning fires regardless of calendar):

- <e.g., "any change touching the project-specific invariant">
- <e.g., "any new service added">
- <e.g., "any architectural rewrite at <scale>">
- <e.g., "any license / package / core-infrastructure pivot">
- <e.g., "Sector Astronomican trigger conditions flip">

**This cadence is committed in writing inside the Reckoning Record itself** (per debate 002 Q6) so it cannot be silently forgotten.

---

## Sign-off

- [ ] All five sections above have a concrete decision (not "<pending>").
- [ ] Tier 1 / 2 / 3 defaults are either adopted verbatim or explicit adjustments are recorded.
- [ ] These five thresholds are committed as the binding inputs to Phase 0 before inventory work begins.

**Signed:** <project owner name or identifier> · **Date:** <YYYY-MM-DD> · **Commit hash:** <git hash>

---

## Provenance

- Template version: distribution v0.6.0.
- Source: `distribution/framework/phases/phase-0.md` §2 inputs; PM walk-through at `distribution/framework/pm-calibration-guide.md`; calibration anchors at `distribution/framework/calibration-standards.md`.
- See `distribution/examples/lore-weave-snapshot/pm-threshold-decisions.md` for a worked example.

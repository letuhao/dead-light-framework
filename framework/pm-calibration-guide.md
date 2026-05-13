---
title: "PM Calibration Guide"
status: sealed
version: not versioned
audience: human
type: reference
last_updated: 2026-05-11
supersedes: null
sealed_by: debate-003
---

# PM Calibration Guide

> **Audience:** Project Managers who own the Phase 0 threshold decisions but may not have prior experience with quantitative calibration. This guide walks through *how* to derive the numbers Phase 0 requires, step by step. Examples and rule-of-thumb formulas are given at three rigor tiers so PMs at any organization size can apply them.
>
> **For PMs already comfortable with COCOMO II, Function Points, CMMI PPB, or DORA metrics** — you may skip directly to the [Calibration Standards Reference Catalog](calibration-standards.md). This guide exists for everyone else.
>
> **Framework principle (recap):** Dead Light adopts industry-standard formulas — it does not invent them. Every recommendation here cites established practice; the citations live in the catalog.

---

## Three rigor tiers

I'd suggest picking the tier your organization can actually support with data and tooling. Under-shooting is fine; over-claiming tends to be harmful in my experience — it produces numbers that look authoritative but are not anchored in real history.

| Tier | Data available | Tooling | Best for |
|---|---|---|---|
| **Tier 1 — Startup / Lean** | Limited or no historical data; team intuition + basic git/repo metrics | None required beyond git + a code-metrics tool like `cloc` or `scc` | Solo founders, early teams, < 1 year of history |
| **Tier 2 — Mid-org** | Some historical data: prior project budgets, sprint velocity, postmortems, ticketing | SonarQube or equivalent; postmortem archive; ticketing data | Established teams, 1–5 years of history, no formal CMMI |
| **Tier 3 — CMMI L4+ / Quantitative** | Process Performance Baselines (PPB); statistical baselines per metric type; multi-project history | Full PPB toolchain, SPC charts, dedicated metrics team | Regulated industries, large enterprises, formal process maturity |

Tiers can be **mixed across decisions** — Tier 1 for time budget but Tier 2 for materiality is fine. The framework does not require a uniform tier.

---

## The five PM threshold decisions in Phase 0

The PM commits these in writing **before** Phase 0 begins. Without them, Phase 0 has no scope and either runs forever or stops arbitrarily.

1. [Significance threshold](#1-significance-threshold) — what enters the Past Decisions Catalog
2. [Materiality threshold](#2-materiality-threshold-for-failure-inventory) — what enters the Failure Inventory
3. [Audit scope](#3-audit-scope-which-services-repos-modules) — which services / repos / modules
4. [Time budget](#4-time-budget-for-phase-0) — how long Phase 0 has
5. [Re-reckoning cadence](#5-re-reckoning-cadence) — how often Reckoning Record is reviewed after Phase 1

---

## 1. Significance threshold

**What it is:** the bar that determines whether a past decision enters the Past Decisions Catalog. Too low → catalog is unmanageable. Too high → critical decisions are missed.

### Tier 1 — Startup / Lean

Use the framework's categorical heuristic verbatim. A past decision enters the catalog if **any one** is true:

- It changed the project's scope (features added, removed, or reframed).
- Its reversal would require > 5 person-days of rework.
- It was discussed in writing (RFC, ADR, design doc, formal meeting minutes).
- It created or removed an external integration.
- It changed team structure (roles added, reassigned, or removed).
- It has been referenced in subsequent decisions.

5 person-days is a framework-internal Tier 1 starting anchor for teams with no historical velocity data. Tier 2 replaces this with team-velocity-derived rework cost (≥ ½-sprint equivalent in story points — see § Tier 2 below). Adjust if your team's pace is very different.

### Tier 2 — Mid-org

Combine categorical heuristic with quantitative anchor:

- Use the categorical bullets above.
- **Plus:** anchor "rework cost" using your team's actual velocity. Example: if the team typically delivers 30 story points per sprint, "significant rework" = ≥ ½ sprint = 15 story points equivalent.
- **Plus:** cross-check against ITIL Change Management tiers (Standard / Normal / Emergency). Any decision your team would have classified as "Normal" or "Emergency" is significant by definition.

Reference: [Calibration Standards § A](calibration-standards.md#a-decision-significance-and-change-impact) — ITIL CM, ISA 320, PMBOK EVM.

### Tier 3 — CMMI L4+

Derive from Process Performance Baseline:

1. Look up historical decision-archive rate per KLOC (or per Function Point, or per project size) from your PPB.
2. Set threshold so the expected count of significant decisions for THIS project equals `rate × project_size`, within control limits.
3. This auto-calibrates to your org's actual decision-making pace.

Reference: CMMI Causal Analysis & Resolution (CAR) and Quantitative Project Management (QPM) practices.

### Sanity check (all tiers)

- Inventory has < 5 entries for a 6-month-old project: threshold is too high.
- Inventory has > 50 entries: either threshold is too low, **or** your team makes too many ad-hoc decisions — that itself is a finding worth surfacing in Phase 1.

---

## 2. Materiality threshold for Failure Inventory

**What it is:** the bar for what counts as a "real" failure worth surfacing. Below this, it's noise.

### Tier 1

Anything that caused:

- Production downtime > 30 minutes, **or**
- A user-visible regression that required rollback or hotfix, **or**
- An off-hours on-call alert, **or**
- Any data loss, **or**
- A security incident at any severity.

If your project has no production yet, substitute: "lost > 1 day of team time".

### Tier 2

Use ITIL Severity tiers adapted to your project:

| Tier | Definition | Include? |
|---|---|---|
| **Sev1** | Platform-wide outage, data loss, security breach | Always |
| **Sev2** | Single-service outage, customer-visible degradation > 1 hour | Always |
| **Sev3** | Repeated minor incidents (≥ 3 in 90 days) | If pattern |
| **Sev4** | Edge-case bugs, near-misses | If PM judges relevant |

Cross-check with DORA Change Failure Rate: any change that contributed to a production incident appears.

Reference: [Calibration Standards § E](calibration-standards.md#e-failure--incident-measurement) — ITIL severity, DORA, SRE postmortem severity.

### Tier 3

Use your DORA baseline and CMMI defect classification. Any incident exceeding ±2σ from PPB control limits is automatically material. Add discretionary inclusions per Sev3/Sev4 judgment.

### Sanity check

If no failures appear in the inventory, either the bar is too high or the team may be uncomfortable surfacing problems. The latter is itself a finding worth noting.

---

## 3. Audit scope (which services / repos / modules)

**What it is:** what the Reckoning Team will audit. Too wide → run out of time. Too narrow → miss problem areas.

### Tier 1

Include any service / repo that meets **any one**:

- Has an active production deploy.
- Has ≥ 5 commits per month for the last 3 months.
- Owns its own data store (database, schema).

Drop everything else with a one-line "not in scope, reason X" note.

### Tier 2

Use code metrics to **rank**, not just to filter:

1. Run `cloc` or `scc` → SLOC per service.
2. Run a complexity tool (`radon` for Python, `lizard` for many languages, SonarQube) → cyclomatic complexity per module.
3. Run `git log --pretty=format: --name-only --since=6.months.ago | sort | uniq -c | sort -rn` → recent code churn per file.
4. Rank by `SLOC × avg_complexity × churn`. Top of the list is highest priority.
5. Audit from the top until time budget is consumed. Items below the cut are recorded as "deferred to next reckoning".

Reference: [Calibration Standards § D](calibration-standards.md#d-code-based-metrics-audit-scope).

### Tier 3

Use SQALE technical debt index from SonarQube (or equivalent). Audit in order of debt-density (debt-minutes per SLOC). High debt-density modules are usually where past decisions have accumulated unaddressed.

### Sanity check

- Audit scope covers < 50% of production code: probably under-scoped (unless project is genuinely modular and only a subset is being reckoned).
- Audit scope covers > 90% of all code including legacy / vendored / generated: probably over-scoped.

---

## 4. Time budget for Phase 0

**What it is:** how long the Reckoning Team has to produce the inventory.

### Tier 1 — M&A IT due-diligence rule of thumb

The Big 4 audit firms use this rule for software acquisitions:

| Codebase quality | Effort rate |
|---|---|
| Well-organized monorepo with good docs | 1 person-week per **50 KLOC** |
| Polyglot with mixed quality | 1 person-week per **20 KLOC** |
| Legacy / poorly documented | 1 person-week per **10 KLOC** |

Multiply by 1.5 if multiple ages of code coexist (microservices added at different times — common pattern).

**Worked example:** 200 KLOC polyglot codebase with mixed docs.
- Estimate: 200 / 20 = 10 person-weeks.
- With 4 Reckoning Team members: 10 / 4 = 2.5 calendar weeks.
- Add 30% buffer: ~3.5 weeks calendar time.

### Tier 2 — Simplified COCOMO II

1. Estimate current project's total effort using COCOMO II (or use historical baseline if you have one).
2. Phase 0 audit budget = **5–15% of original project effort**, depending on rot severity:
   - Light rot: 5% (clean architecture, few scope changes).
   - Medium rot: 10% (some scope changes, accumulated debt).
   - Heavy rot: 15% (frequent scope changes, conflicting refactors, multiple architectural rewrites).

If your org has past Phase-0-like activities (architecture review, due diligence audit), use those as historical baseline directly.

Reference: [Calibration Standards § B](calibration-standards.md#b-time-and-effort-estimation) — COCOMO II.

### Tier 3 — CMMI PPB

Look up Phase 0 effort from PPB. Set the budget to `PPB_mean ± 1σ`. Apply Statistical Process Control during Phase 0 to detect out-of-control variance early.

### Time-boxing escalation

Regardless of tier, the framework's escalation rule applies:

- **At 80% elapsed:** status check. Reckoning Team reports % complete by section.
- **At 100% elapsed**, if quality gates not met, PM commits in writing to one of:
  1. **Extend** with new target + rationale.
  2. **Reduce scope** — raise significance threshold; dropped items become "deferred to next reckoning".
  3. **Continue without quality gates met** — accept incomplete inventory; record gaps in the Reckoning Record; gaps become known risks for Phase 1.
- A single extension is allowed without notification. A second extension requires Council awareness.

### Sanity check

- < 1 person-week total: too short — going through the motions.
- > 12 person-weeks total: too long — you've conflated Phase 0 with rebuilding the whole project. Cut scope.

---

## 5. Re-reckoning cadence

**What it is:** how often the Reckoning Record is reviewed after Phase 1 sealing, so it doesn't become a forgotten artifact.

### Tier 1

- **Default:** quarterly (every 3 months).
- **Plus:** triggered by any major scope change or architectural pivot.

### Tier 2

- Tie to your team's release cadence: re-reckon at every major release (e.g., after each `MX.Y → MX+1.0`).
- Plus pivot trigger.

### Tier 3

- SPC-driven: re-reckon when control charts show out-of-control points.
- Plus baseline cadence (semi-annually).

The cadence is **committed in writing inside the Reckoning Record itself** (per [debate 002](debates/002-retrofit-vs-greenfield.md), Q6). This is so it cannot be silently forgotten.

---

## Greenfield lightweight Phase 0

If the project is greenfield (no existing code, no accumulated decisions), Phase 0 is run **lightweight** — typically 1–3 days, or 1–2% of projected total effort (COCOMO II planning mode).

Lightweight Phase 0 keeps:

- **Assumption Surface** — each Council member independently writes: "What assumptions am I bringing? What 'of course we'll' patterns am I applying without thinking? What habits am I importing from prior projects?"
- **External Commitment Audit** — what has been promised to whom, by when, that constrains the project before code begins.
- **Stakeholder & Integration Map** — who depends on the outcome; which external systems will be touched.
- **(Optional) Failure Lessons from Analogous Projects** — failures from similar past projects the team or organization has done.

Lightweight Phase 0 omits:

- Current State Audit (N/A).
- Past Decisions Catalog (N/A).
- Failure Inventory of own past (N/A).

**Full skip is permitted only when** the team is a single person, or two people who have worked together before on similar projects.

---

## How to choose your tier

If unsure:

| Your situation | Recommended tier |
|---|---|
| < 5 people, < 1 year of history, no metrics tooling | Tier 1 |
| 5–50 people, 1–5 years of history, some metrics in place | Tier 2 |
| > 50 people, formal metrics program, or CMMI L4+ certified | Tier 3 |

Tiers can be mixed across the five decisions if data availability differs (e.g., Tier 2 for materiality because you have postmortem records, Tier 1 for time budget because you have no comparable past projects).

---

## Common pitfalls

- **Picking too high a tier for show.** In my experience, claiming Tier 3 without an actual PPB tends to produce fake-precise numbers. If you don't have the data, drop to the tier you can actually support.
- **Setting thresholds to match a desired outcome.** "We want the inventory to have N items, so let's set the threshold to filter to N." This inverts the framework's intent — within Dead Light we set thresholds first; item count is the dependent variable.
- **Setting time budget by ceremony, not by data.** "Two weeks sounds about right" without anchoring to KLOC or COCOMO tends to produce budgets that miss reality in projects I've seen.
- **Skipping the sanity checks.** They exist because each threshold has known failure modes — running through them takes about 10 minutes and tends to catch common calibration errors.
- **Calibrating in isolation.** Talk to a senior engineer or architect on the team before committing thresholds in writing. If the PM is Council member only, this is the Council; if Council has not yet been seated, find a domain expert.

---

## When to consult further

- For full citations and academic sources of every standard cited above, see [calibration-standards.md](calibration-standards.md).
- For the framework's principle that drives this document — "we adopt industry-standard formulas, we do not invent" — see the principle statement at the top of the catalog.
- For decisions about which standards have been formally anchored vs left to PM choice, see [debates/003-phase-0-calibration.md](debates/003-phase-0-calibration.md).

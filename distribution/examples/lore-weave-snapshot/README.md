---
audience: human
last_updated: 2026-05-13
sealed_by: null
snapshot_date: '2026-05-13'
snapshot_of: case-studies/lore-weave/ (upstream working copy)
status: working
supersedes: null
title: Case Study — LoreWeave
type: case-study
version: not versioned
---

# Case Study — LoreWeave

> **Status:** Phase 0 in flight (2026-05-11). First retrofit application of Dead Light Framework against a real codebase.
>
> **Source codebase:** `C:\Works\_Researchs\lore-weave` (alternate workstation: `D:\Works\source\lore-weave`).
> **Framework version applied:** Phase 0 spec at [`framework/phases/phase-0.md`](../../framework/phases/phase-0.md); calibration anchors at [`framework/calibration-standards.md`](../../framework/calibration-standards.md); PM walk-through at [`framework/pm-calibration-guide.md`](../../framework/pm-calibration-guide.md).
> **Tier:** **Tier 1 — Startup / Lean** (solo project, no formal PPB, no SonarQube baseline, no historical sprint velocity).

---

## Why this case study exists

LoreWeave is the project that motivated Dead Light Framework. It hit the failure modes the framework aims to mitigate — conflicting refactors, scope drift between human and AI contributors, accumulated context rot. Running the framework against this codebase is the framework's first empirical test.

Phase 0 (Reckoning) is the natural starting point because LoreWeave is a **retrofit case**: existing code, accumulated decisions, formed habits.

---

## Scope of audit

Per Phase 0 §2 input "Scope of audit (which services / repos / components)", the audit covers **all** of LoreWeave but is split into **two passes** to keep each pass tractable:

- **Pass 1** — toolchain / foundation docs + the two most-active services (TBD which two; selected during Reckoning Team kick-off).
- **Pass 2** — the remaining four services + cross-cutting concerns (auth, sharing, model layer).

Both passes feed the same Reckoning Record before the Council review session.

---

## Focus areas

Per Phase 0 §3 "investigative phase" and §4 outputs, the case study surfaces four convergent threads (all four selected by project owner):

1. **Past scope changes** — the trigger that motivated the framework. Each significant scope change is catalogued in the Past Decisions Catalog with attribution and date.
2. **Architect rot specifically** — conflicting refactors, scope drift, accumulated context rot. The empirical anchor for the framework's central premise (README:26 — Bommasani 2021 / Park 2023). Material entries feed the Failure Inventory.
3. **Sector Astronomican trigger evaluation** — LoreWeave currently has **seven contract directories** in `contracts/api/` (identity, books, catalog, **llm-gateway**, model-billing, model-registry, sharing — `llm-gateway` is new since the 2026-05-09 HANDOFF) **and fifteen service implementations** in `services/`. Does this configuration meet the four conjunctive trigger conditions for Sector split per [debate 001](../../framework/debates/001-laws-count-and-multirepo-scaling.md)? Carry-forward from debate 001's follow-up actions checklist.
4. **Implicit principles surface** — independent capture (per Phase 0 §3 step 4) of "of course we'll" patterns that have been assumed but not stated. The most valuable Phase 0 output, per spec.

---

## Folder layout

```
case-studies/lore-weave/
├── README.md                       ← this file (overview, status, scope, focus)
├── pm-threshold-decisions.md       ← five PM commitments per Phase 0 §2 inputs
├── reckoning-team-record.md        ← team composition; named AI-aide Chapters per §7 accommodation
├── reckoning-record.md             ← the four inventory sections; fifth (classifications) added by Phase 1
└── methodology-notes.md            ← single-reviewer caveats, AI-aide invocations, framework-versus-reality observations
```

---

## How to read this case study

1. Start with [`pm-threshold-decisions.md`](pm-threshold-decisions.md) — the five thresholds frame everything else.
2. [`reckoning-team-record.md`](reckoning-team-record.md) — see who produced what and which AI-aide perspectives were invoked.
3. [`reckoning-record.md`](reckoning-record.md) — the actual Phase 0 inventory output.
4. [`methodology-notes.md`](methodology-notes.md) — caveats, single-reviewer risks, and framework-versus-reality observations as they emerged.

---

## Status

| Section | Status | Date |
|---|---|---|
| Folder skeleton + scope | **Drafted** | 2026-05-11 |
| PM Threshold Decisions | Pending project-owner input | — |
| Reckoning Team Record | Pending project-owner input | — |
| Reckoning Record — Pass 1 | Not started | — |
| Reckoning Record — Pass 2 | Not started | — |
| Methodology notes | Accumulating | 2026-05-11 |
| Phase 1 application (Reckoning step → Astronomican v1.0) | Not started | — |

---

## Outputs expected at end of Phase 0

Per Phase 0 §4:

| Artifact | Lives at | Status |
|---|---|---|
| **Reckoning Record (draft)** — four sections, becomes input to Phase 1 | [`reckoning-record.md`](reckoning-record.md) | Pending |
| **Reckoning Team Record** — names + roles + areas owned | [`reckoning-team-record.md`](reckoning-team-record.md) | Pending |
| **PM Threshold Decisions** — five commitments | [`pm-threshold-decisions.md`](pm-threshold-decisions.md) | Pending |

Phase 1 will later add a fifth section to `reckoning-record.md` (classifications + Migration Plan) and produce the Astronomican v1.0 + Re-consecration Playbook + Stress Test Log as separate files in this folder.
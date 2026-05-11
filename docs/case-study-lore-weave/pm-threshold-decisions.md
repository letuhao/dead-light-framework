# PM Threshold Decisions — LoreWeave Phase 0

> **Status:** **Draft proposal** by AI-aide-1 based on LoreWeave quick-scan 2026-05-11 — pending project-owner review, adjustment, and sign-off.
> **Spec:** Phase 0 §2 inputs; PM walk-through at [`pm-calibration-guide.md`](../pm-calibration-guide.md); calibration anchors at [`calibration-standards.md`](../calibration-standards.md).
> **Tier applied:** **Tier 1 — Startup / Lean** (solo project, no historical PPB, no formal velocity baseline).
> **Spec departure D-3 (recorded in methodology-notes):** Phase 0 §2 says PM commits these in writing BEFORE Phase 0 begins. Here AI-aide-1 produces a *proposal* drawn from a preliminary scan, and the project owner signs off (or adjusts) afterward. This is a productivity adaptation for solo + AI-aide configuration; the binding semantics are preserved (project owner remains the committer).
>
> Per project owner's choice at kick-off: project owner reviews this draft, modifies sections as needed, then commits with a sign-off line at the bottom.

---

## LoreWeave scan summary (input to this proposal)

Date of scan: 2026-05-11. Run by AI-aide-1.

- **Total code base:** ~358 KLOC across 1717 files (cloc, excluding node_modules / .git / .pytest_cache / build artifacts).
- **Language mix:** Python 67K, TypeScript 60K, Go 33K, HTML 30K, JSON 24K, plus smaller buckets.
- **Activity:** 1314 commits in the last 6 months. High velocity.
- **Top change-frequency areas (last 6 months):** `frontend/src` (1739 file-touches), `docs/03_planning` (1439), `services/knowledge-service` (945), `docs/sessions` (581), then long tail across 14 other services.
- **Scope signals identified:** (a) frontend v1→v2 rewrite with rename complete (commit `bada6bbd` "chore: rename frontend-v2/ to frontend/ — migration complete"); (b) novel-workflow → MMO-RPG module layering in flight (current branch `mmo-rpg/design-resume`, recent commits on Player Onboarding / AI Tier / Time Dilation / Progression Foundation / Resource Foundation); (c) license pivot MIT → AGPL-3.0-or-later; (d) infra pivot Redis → Valkey; (e) seven contract directories in `contracts/api/` and fifteen service directories in `services/`.
- **Pass 1 size (per project-owner-confirmed selection):** ~241 KLOC across `docs/01_foundation` (0.7 KLOC), `docs/02_governance` (1.4 KLOC), `docs/03_planning` (120 KLOC markdown), `frontend` (70.5 KLOC, mostly TypeScript), `services/knowledge-service` (49 KLOC, mostly Python).
- **Note on `frontend-v2`:** the directory no longer exists; v2 was renamed to `frontend`. The two-frontend phenomenon now lives in git history, not in the current tree. The v1→v2 rewrite event becomes a Past Decisions Catalog entry, not a Current State Audit observation.

---

## 1. Significance threshold

> *What enters the Past Decisions Catalog.*

**Proposed:** Tier 1 categorical heuristic verbatim from PM Calibration Guide §1, **plus** four LoreWeave-specific criteria.

### Tier 1 categorical heuristic (adopted)

A past decision enters the catalog if **any one** is true:

1. It changed the project's scope (features added, removed, or reframed).
2. Its reversal would require **> 1 person-day of rework**. *(Tier 1 default is "5 person-days"; lowered to 1 person-day to match solo-developer iteration pace per PM Calibration Guide §1 hedge "Adjust if your team's pace is very different.")*
3. It was discussed in writing (RFC, ADR, design doc, formal meeting minutes, or commit message with explicit rationale).
4. It created or removed an external integration (third-party API, model provider, payment gateway, storage backend).
5. It changed team structure (roles added, reassigned, or removed). *Reframed for solo project as:* it added or removed a persistent tool or agent class to the development working set (e.g., new MCP server, new AI Chapter, new build pipeline).
6. It has been referenced in subsequent decisions (downstream impact, regardless of original visibility).

### LoreWeave-specific additions

7. **Any change touching the novel-workflow ↔ MMO-RPG layering boundary** — this is the most load-bearing architectural decision in flight and any drift here cascades through every dependent service.
8. **Any change to a frozen invariant** — e.g., canon integrity, author intent across translations, or any other "of course we'll" pattern surfaced in Section 4 of the Reckoning Record.
9. **Any architectural rewrite** at the scale of the v1→v2 frontend rebuild — full directory replacement or wholesale service rewrite.
10. **Any license, package management, or core infrastructure pivot** (e.g., MIT→AGPL, Redis→Valkey class of decision).

### What does NOT enter the catalog

- Routine refactors that don't change scope or contracts.
- Bug fixes that don't change behavior contracts.
- Documentation polish without semantic change.
- Test additions / coverage improvements.

---

## 2. Materiality threshold (Failure Inventory)

> *What counts as a "real" failure worth surfacing.*

**Proposed:** Tier 1 base adapted for pre-production / solo / AI-collaboration context.

### Base (adopted from PM Calibration Guide §2 Tier 1)

Anything that caused:

- Production downtime > 30 minutes, OR
- A user-visible regression that required rollback or hotfix, OR
- An off-hours on-call alert, OR
- Any data loss, OR
- A security incident at any severity.

### Pre-production / solo adaptation

LoreWeave is in a mixed production-status state (per [reckoning-record §1](reckoning-record.md) §1.1, to verify in Pass 1). The Tier 1 spec hedges "If your project has no production yet, substitute: 'lost > 1 day of team time'." Adapted for solo project:

- **Lost > ½ day of solo-developer time on a regression or undo** that should not have been necessary.

### LoreWeave-specific additions (architect-rot framing per focus area #2)

- **Any decision reversed within 30 days** of being committed — architect-rot signal: late-stage realization that the original decision was wrong.
- **Any case where an AI agent contradicted a previous design decision in committed code** — the framework's central premise (README:26) names this as the canonical AI-collaboration failure mode; LoreWeave is the empirical test of whether it occurs and how.
- **Any incident of "conflicting refactors"** — two refactors landing in incompatible directions, the README:20's named failure mode.
- **Any data-loss-equivalent event for canon integrity** — the framework's narrative-integrity invariant being violated (incorrect cross-reference, contradicted character fact, broken translation alignment) counts as data loss for LoreWeave's purpose.

### What does NOT enter the inventory

- Pure infrastructure flakes (CI, build server) with no downstream impact.
- Solo-developer learning iterations on greenfield features ("first attempt didn't work, second one did" — not a failure, just iteration).
- Routine bugs caught and fixed within the same session.

---

## 3. Audit scope

> *Which services / repos / modules.*

**Decision:** All in-scope, split into two passes per case-study `README.md`. Pass 1 confirmed by project owner.

### Pass 1 (confirmed)

| Area | Path | Size | Why in Pass 1 |
|---|---|---|---|
| Foundation docs | `docs/01_foundation/` | 0.7 KLOC (4 files) | Origin-of-project context; small and quick |
| Governance docs | `docs/02_governance/` | 1.4 KLOC (9 files) | Project-level decisions; small and quick |
| Planning docs | `docs/03_planning/` | 120 KLOC (407 files) | **Highest scope-change-evidence density**; will be skimmed for decision events, not read end-to-end |
| Current frontend | `frontend/` | 70.5 KLOC | Result of v1→v2 rewrite; current production target |
| Heaviest backend | `services/knowledge-service/` | 49 KLOC | 945 file-touches in 6 months — far the most active backend service |

**Pass 1 total: ~241 KLOC (of which 120 KLOC is markdown, audited by scan-for-decisions rather than line-by-line read).**

### Pass 2 (deferred to next session)

| Area | Path | Size estimate | Notes |
|---|---|---|---|
| Remaining 14 services | `services/` (excluding knowledge-service) | ~80 KLOC | api-gateway-bff, auth, book, catalog, chat, glossary, notification, provider-registry, sharing, statistics, translation, usage-billing, video-gen, worker-ai, worker-infra |
| 7 contract directories | `contracts/api/` | Small (contract definitions) | identity, books, catalog, llm-gateway, model-billing, model-registry, sharing |
| Cross-cutting infra | `infra/`, `sdks/`, `scripts/`, `agentic-workflow/` | ~10–20 KLOC | Build, CI, SDK code |
| Top-level files | `AGENT_PROTOCOL.md`, `CLAUDE.md`, `README.md`, `.mcp.json` | Small | Working-protocol context |

### Explicitly out of scope

- `node_modules/`, `.git/`, `.pytest_cache/` — tooling artifacts.
- `data/` — runtime data (out of scope per Phase 0 §3.1: "Documentation is evidence, not truth — discrepancies between docs and reality are explicitly recorded"; we audit code/docs, not data values).
- Generated migrations, test fixtures, lock files.
- `design-drafts/` — TBD whether in scope; project owner please confirm whether design drafts are committed decisions (in catalog) or exploration (out).
- `poc/` — TBD whether in scope; same question as design-drafts.

---

## 4. Time budget

> *How long Phase 0 has.*

**Proposed:** Derived from Tier 1 M&A IT due-diligence rule of thumb (PM Calibration Guide §4 Tier 1).

### Sizing

LoreWeave is **polyglot with mixed quality** per the v1→v2 rewrite + multi-language stack signal. Per Tier 1: **1 person-week per 20 KLOC**.

LoreWeave also has **multiple ages of code coexisting** (legacy frontend → rewrite v2; novel-workflow core → MMO-RPG module layering). Per Tier 1: **multiply by 1.5**.

### Pass 1 budget

| Component | KLOC | Multiplier | Person-weeks |
|---|---|---|---|
| `frontend/` (TS-heavy) | 70.5 | 1.5 × 1pw/20K | 5.3 |
| `services/knowledge-service/` (Python) | 49 | 1.5 × 1pw/20K | 3.7 |
| `docs/03_planning/` (skim-for-decisions, not line-by-line; markdown audits faster than code) | 120 markdown | scan-only at ~1pw/60K-markdown | 2.0 |
| Foundation + governance docs | 2.1 | 0.1 | 0.2 |
| **Pass 1 raw estimate** | | | **~11.2 person-weeks** at full M&A rate |

### Pass 1 budget after AI-aide leverage

AI-aide-1 substantially reduces the project-owner's load on Current State Audit (grep, KLOC, dependency analysis, decision-candidate extraction from git log). The framework does not have a documented multiplier for this — this is a Phase 0 spec gap that the case study will surface in `methodology-notes.md`. AI-aide-1's *initial* estimate, conservative:

- Reduce by ~50% for tasks the AI-aide can fully draft (Section 1 Current State Audit, Section 2 git-log decision candidate extraction).
- Reduce by ~25% for tasks the project owner must drive (Section 3 Failure Inventory attribution, Section 4 implicit-principles independent contribution).
- Net Pass 1 estimate after AI-aide: **~5–7 person-weeks of project-owner attention**, spread over multiple calendar sessions.

**This is a substantial commitment.** If the project owner's available time is much less, Pass 1 should be further scoped down — e.g., drop `frontend/` from Pass 1 (deferred to Pass 2 or beyond).

### Time-boxing escalation (per debate 003 Q3)

- **80% elapsed (Pass 1 budget):** status check; project owner reports % complete by Reckoning Record section.
- **100% elapsed:** project owner commits to one of three actions in writing in `methodology-notes.md`:
  1. Extend Pass 1 with new target + rationale.
  2. Raise the significance threshold and defer items to Pass 2 / next reckoning.
  3. Continue without quality gates met; gaps become known risks for Phase 1.

### Pass 2 budget

Out of scope for this proposal — will be re-sized after Pass 1 completes and the project owner has direct feedback on AI-aide leverage rate.

### Proposed initial Pass 1 commitment

**Initial Pass 1 target: ~6 person-weeks of project-owner attention, calendar-spread.**

Project owner: please adjust this number based on your real available time. Lower-bound commitment that still produces a meaningful Pass 1: ~3 person-weeks (which would require dropping at least one of `frontend/` / `knowledge-service/` from Pass 1).

---

## 5. Re-reckoning cadence

> *How often the Reckoning Record is reviewed after Phase 1 sealing.*

**Proposed:** Tier 1 default + LoreWeave-specific pivot triggers.

### Base (adopted from PM Calibration Guide §5 Tier 1)

- **Default cadence:** quarterly (every 3 months).

### LoreWeave-specific pivot triggers (re-reckoning fires regardless of calendar)

- Any change touching the novel-workflow ↔ MMO-RPG layering boundary (per §1 criterion #7 above).
- Any new service added to `services/` or any new contract added to `contracts/api/`.
- Any architectural rewrite at the v1→v2 frontend scale.
- Any license / package-management / core-infrastructure pivot.
- Any case where the Sector Astronomican trigger conditions ([debate 001](../debates/001-laws-count-and-multirepo-scaling.md)) flip — i.e., the project crosses or un-crosses the 4-conjunctive threshold for Sector split.

### Commitment site

Per [debate 002 Q6](../debates/002-retrofit-vs-greenfield.md): the cadence is committed in writing **inside the Reckoning Record itself**, not just here. Once Phase 1 seals, the Reckoning Record carries this cadence as part of its living-document property.

---

## Sign-off (pending)

The project owner signs below to commit these five thresholds as the working PM decisions for LoreWeave Phase 0. Adjustments before sign-off go in the Adjustments section.

### Adjustments by project owner

_(none yet — project owner edits this section if proposed values need to change before sign-off)_

### Sign-off line

- [ ] Project owner has reviewed all five sections.
- [ ] Adjustments (if any) are recorded above.
- [ ] These five thresholds are committed as the binding inputs to Phase 0 Pass 1.

**Signed:** _(date + project-owner identifier when committed)_

---

## Provenance

- LoreWeave scan: 2026-05-11 by AI-aide-1, results in `methodology-notes.md` §6 audit trail.
- Proposal drafted: 2026-05-11 by AI-aide-1, framework version Dead Light Framework `main` at commit `0450e47` ("log Phase 0 spec departures D-1 D-2 before LoreWeave scan begins").
- Framework spec applied: Phase 0 v0.3-era (post-IVP-Phase-5 remediation; see [HANDOFF.md](../../HANDOFF.md) for current state).

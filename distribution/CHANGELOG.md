---
title: Distribution Changelog
status: working
version: not versioned
audience: human
type: reference
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Living document; updated per release per debate 006 sub-decision C.
> **Audience:** Adopters tracking version-to-version changes.
> **Purpose:** Record what's in each distribution version per Keep-a-Changelog convention.
> **Read next if:** you need to know what changed since you last cloned.

# Changelog

All notable changes to this distribution will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).




## [0.8.0] — 2026-05-13

### Added

- **Debate 008 sealed** (Adeptus Administratum Deployment Protocol). 10 sub-decisions standardising HOW AI agents engage with the framework at runtime — parallel meta-standard to debate 006 (which standardised paperwork organisation).
- **`CLAUDE.md` at repo root** — formal Adeptus Administratum bootstrap for Claude Code (A-tier provider). Auto-loaded per Claude Code session.
- **`distribution/deployment-matrix.md`** — IDE / tooling integration tier mapping (A Claude Code + Anthropic Workbench; B Cursor + ChatGPT + Gemini; C local LLMs + agent frameworks) + 7-failure-mode catalogue (F-J1 through F-J7) + multi-project Codex overrides documentation.
- **`distribution/templates/aa-codex-overrides-example/`** — worked example for adopter-side Codex overrides (README + additional-operational-bounds + additional-hard-stops + notify-trigger-extensions). Imperial+Sector pattern applied at Codex level per debate 008 sub-decision H4.
- **`distribution/for-adopters.md` § Quickstart** — 5-step adopter flow (clone → pick tier → scaffold case study → fill PM thresholds → start first AA instance).
- **`distribution/for-ai-aides.md`** — updated to Codex v1.2; new "Deployment quickstart for adopters" + "Provider tier check" sections.

### Changed

- **Adeptus Administratum Codex v1.1 → v1.2** (implementation-amendment per [debate 008](framework/debates/008-adeptus-administratum-deployment-protocol.md), following the v1.0→v1.1 precedent for implementation amendments):
  - §1 Identity and scope: added `.aa-codex-overrides/` mechanism reference + Imperial+Sector pattern at Codex level + worked-example pointer.
  - §8 Re-priming step 1: added project-root bootstrap reference (`CLAUDE.md` / `.cursorrules` / system prompt) + adopter `.aa-codex-overrides/` reading.
  - §8 Re-priming step 3: added `distribution/for-ai-aides.md` and `distribution/deployment-matrix.md` as deployment-context artifacts.
  - §10 Provenance: v1.2 row added to Version history table.
  - No structural changes to Hard Stops, Notify Triggers, Authority bounds, or Output Contract.

### Notes

- **Framework now has 5 sealed-concern layers** per debate 008 §18: project governance (debates 001-004) / operational aide bounds (Codex via debate 005) / document architecture (debate 006) / tooling infrastructure (debate 007) / **deployment protocol** (debate 008). Each layer is "fractal" of the frozen-authority thesis.
- **Imperial+Sector pattern re-applies at Codex level** (sub-decision H4) — same design pattern from debate 001 keeps surfacing as the right answer at new layers. Strong signal the pattern is structural, not coincidence.
- **Adopter-readiness milestone:** debate 006 made the framework *distributable*; debate 007 made it *tool-supported*; debate 008 makes it *deployable*. Framework is now at "minimum viable for first adopter pilot" maturity.
- **Phase 2/3 tooling deferred:** `scripts/start_aa_session.py`, `scripts/validate_codex_overrides.py`, and `.claude/commands/aa-prime.md` deferred per debate 008 §14 implementation plan. Build on need.
- **Debate cadence observation:** debate 008 opened and sealed same-day (commit `cc3e193` → `b0cea07`). Framework accelerated through debates 005, 006, 007, 008 in 3 days because the analytical machinery + scaffolding scripts are now in place.

## [0.7.1] — 2026-05-13

### Added

- **Adeptus Administratum Codex v1.0 → v1.1** (implementation-amendment per [debate 007 §G](framework/debates/007-scripting-infrastructure.md)).
  - §4 Autonomy Threshold: read-only script invocation now explicitly allowed solo; write-script `--apply` invocation explicitly requires acknowledgment.
  - §8 Re-priming protocol step 5: explicit reference to `scripts/validate_frontmatter.py` + `scripts/check_links.py` for mechanised drift detection; script output maps to N-3/N-4 notifies.
  - §10 Provenance: new Version history table; new Amendment procedure precedent.
- **Codex Re-consecration procedure precedent established** in Codex §10 — resolves debate 005 §11 open question #3. Two amendment classes defined:
  - *Implementation amendments* (execute prior decided debate's design without new design questions) — apply directly via minor version bump; reference originating debate; no new debate required.
  - *Design amendments* (introduce new design questions / contradict prior analysis / change structural design) — full debate rigor; major version bump.
  - This v1.0 → v1.1 itself is the first implementation-amendment, demonstrating the precedent in practice.

### Changed

- Adeptus Administratum Codex effective immediately as v1.1 for all future re-priming. Existing instances completing tasks under v1.0 understanding are not retrospectively impacted; new instances re-prime against v1.1.

### Notes

- **Debate 008 NOT opened.** The strict reading of Codex §10 v1.0 said "amendments require a new debate" — but the v1.1 precedent reframes that rule: implementation amendments (where the design decision is already sealed in a prior debate) do not need a separate debate. Debate 007 §G was the substantive analysis; this Codex patch is the implementation. Re-debating would have been process-for-process.
- The risk mitigation for the new precedent: AI-aides that detect a misclassification of "design" vs "implementation" emit N-2 (policy 2 / framework-internal arithmetic) notify, blocking until project owner adjudicates. First-line discipline at the Chapter; final adjudication at the project owner.

## [0.7.0] — 2026-05-13

### Added

- **Debate 007 sealed** (Scripting Infrastructure) — authorises Python tooling under `scripts/` to handle mechanical repository operations. Library stack: `python-frontmatter` + `typer` + `markdown-it-py`. Dry-run-by-default + `--apply` pattern for writes; strict transactions; severity-graded findings per IVP rubric.
- **12 scripts implemented** across 3 tiers:
  - Tier 1 (validation + sync): `validate_frontmatter.py`, `check_links.py`, `sync_distribution.py`.
  - Tier 2 (atomic operations): `frontmatter_set.py`, `bump_version.py`, `snapshot_case_study.py`, `update_handoff_tree.py`.
  - Tier 3 (orchestration + scaffolding + audit): `release.py` (8-step pipeline), `new_debate.py`, `new_chapter_codex.py`, `new_case_study.py`, `ivp_phase5.py`.
- `distribution/` regenerated via `sync_distribution.py`: 19 sealed files synced; INDEX.md auto-regenerated; LoreWeave snapshot refreshed.
- LLM token-cost surfaced as a third framework-design axis (alongside human-time + correctness) per debate 007 §17 — manual mechanical operations replaced by single-script invocations (~99% token reduction).

### Changed

- `HANDOFF.md` document tree section now bracketed by `<!-- DOC-TREE-START -->` / `<!-- DOC-TREE-END -->` markers; regenerable via `python scripts/update_handoff_tree.py --apply`.
- All framework files carry 9-field YAML frontmatter (post-debate-006 backfill is now enforced by `validate_frontmatter.py`).
- `README.md` + `HANDOFF.md` at repo root now have frontmatter (caught and fixed during Tier 1 script testing).
- `sync_distribution.py` rename rule refined: `-for-debate` suffix dropped only when `status: sealed` (working-status files retain their suffix; e.g., IVP spec at `audit/independent-verification-pass-for-debate.md`).

### Notes

- **Adeptus Administratum Codex amendment deferred to debate 008.** Until v1.1 seals, AA instances may invoke scripts informally as project-owner-authorized task work; the Codex §8 step 5 re-priming protocol does not yet formally reference scripts.
- `ivp_phase5.py` regex patterns are intentionally permissive (false positives flagged for reviewer dismissal); a reviewer dismisses non-issues in seconds and gets cross-doc numeric-consistency surfacing free.
- Known limitations from v0.6.0 (phase-1 + glossary not yet sealed; some dangling cross-folder links if `distribution/` extracted to standalone repo) remain — `check_links.py` confirms these are unchanged in scope.
- End-to-end pipeline tested via `python scripts/release.py minor --apply` (this release); push remains MANUAL per Adeptus Administratum Codex §3 HS-5 + debate 007 §10.

## [0.6.0] — 2026-05-13

### Added

- Initial distribution release after sealing of debate 006 (documentation architecture).
- Phase 0 sealed specification.
- 6 decided debates (001–006).
- Adeptus Administratum Codex v1.0 (sealed via debate 005).
- Calibration Standards reference catalog.
- PM Calibration Guide (3-tier walkthrough at startup / mid-org / CMMI L4+).
- Templates: Astronomican, Reckoning Record, PM Threshold Decisions, Reckoning Team Record (fillable scaffolds).
- Example snapshot: LoreWeave case-study at debate-006-seal time.
- Role-based reading guides: for-pms, for-ics, for-ai-aides, for-adopters.

### Not yet included

- Phase 1 (still partial in upstream `framework/` working area; will be in v0.7.0 or v1.0.0).
- Phase 2/3/4 (not started).
- Additional Chapters beyond Adeptus Administratum (deferred to real-project trigger).

### Notes

- This is the **first outward-facing release** of Dead Light Framework. Per debate 006, the framework was inward-facing until this point.
- Cumulative IVP audit state at this release: Phases 1–5 complete; 38 findings remediated (F-01 through F-39, F-26 retracted via erratum); Phases 6–7 queued.

### Known limitations (v0.6.0)

- Some sealed files in `framework/debates/` reference `framework/phases/phase-1-for-debate.md` and `framework/audit/findings-*.md`. These artifacts live in the upstream `dead-light-framework` repo (siblings of `distribution/`) but are NOT included in this v0.6.0 distribution. While `distribution/` lives inside the upstream repo, the relative links resolve via `../phases/...` and `../audit/...`. **If you extract `distribution/` to a standalone repo, these links will be dangling.** A future release (likely when Phase 1 fully seals) will rewrite these as plain-text references or inline the necessary content, fully closing the separability constraint of debate 006.

[0.6.0]: ./VERSION

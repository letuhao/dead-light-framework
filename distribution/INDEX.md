---
title: Distribution Master Index
status: working
version: 0.6.0
audience: both
type: reference
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Master TOC of distribution v0.6.0.
> **Audience:** Both — human readers triaging the framework, AI re-priming instances.
> **Purpose:** Single-point lookup for every artifact in this distribution.
> **Read next if:** you have a question about WHERE something is.

# Distribution Index — v0.6.0

## Framework specification (`framework/`)

Sealed artifacts. Adopter modifies = adopter forks.

| Artifact | Path | Status | Audience |
|---|---|---|---|
| Phase 0 — The Reckoning | `framework/phases/phase-0.md` | sealed | both |
| Phase 1 — The Astronomican | _(partial; not in v0.6.0)_ | working | — |
| Debate 001 — Laws Count Cap and Multi-Repo Scaling | `framework/debates/001-laws-count-and-multirepo-scaling.md` | decided | both |
| Debate 002 — Retrofit vs Greenfield | `framework/debates/002-retrofit-vs-greenfield.md` | decided | both |
| Debate 003 — Phase 0 Calibration | `framework/debates/003-phase-0-calibration.md` | decided | both |
| Debate 004 — Cap Revision: Miller Citation Correction | `framework/debates/004-cap-revision-miller-correction.md` | decided | both |
| Debate 005 — First Chapter: PM/High Lord Aide | `framework/debates/005-first-chapter-pm-high-lord-aide.md` | decided | both |
| Debate 006 — Documentation Architecture and Distribution | `framework/debates/006-documentation-architecture-and-distribution.md` | decided | both |
| Adeptus Administratum Codex v1.0 | `framework/chapters/adeptus-administratum/codex.md` | sealed | both |
| Calibration Standards (reference catalog) | `framework/calibration-standards.md` | sealed | both |
| PM Calibration Guide (3-tier walkthrough) | `framework/pm-calibration-guide.md` | sealed | human |

## Templates (`templates/`)

Fillable scaffolds. Copy into your project; fill placeholders marked `<...>`.

| Template | Path | Fills |
|---|---|---|
| Astronomican | `templates/astronomican-template.md` | Phase 1 output — sealed Astronomican v1.0 |
| Reckoning Record | `templates/reckoning-record-template.md` | Phase 0 four-section inventory + Phase 1 fifth-section classifications |
| PM Threshold Decisions | `templates/pm-threshold-decisions-template.md` | Phase 0 §2 five PM commitments |
| Reckoning Team Record | `templates/reckoning-team-record-template.md` | Phase 0 team composition + AI-aide invocations |

## Examples (`examples/`)

Read-only reference snapshots.

| Example | Path | Captures |
|---|---|---|
| LoreWeave snapshot | `examples/lore-weave-snapshot/` | First retrofit application; case-study state at debate-006-seal time (2026-05-13) |

## Role-based reading guides

Pick the guide that matches your role:

| Guide | Path | For whom |
|---|---|---|
| For PMs | `for-pms.md` | Project Managers / Product Owners |
| For ICs | `for-ics.md` | Individual Contributors / engineers / maintainers |
| For AI aides | `for-ai-aides.md` | Adeptus Administratum instances (re-priming primer) |
| For adopters | `for-adopters.md` | Organizations adopting the framework into their methodology |

## Conventions

- Every file has YAML frontmatter + human summary block (per debate 006 sub-decision F).
- Internal links are relative paths.
- Section IDs are `#kebab-case-of-title` (deterministic for AI cite-by-anchor).
- Cross-link format: `[file:line-range](path#section-id)` when pointing at a specific section.
- Diagrams in Mermaid where non-trivial; ASCII for trivial; transcribe images.

Per debate 006 sub-decision J (dual-audience design rules).

## Upstream

- Repository: `dead-light-framework` (source-of-truth).
- This distribution is generated from `../framework/` per sub-decision H one-way sync.
- For full framework history including IVP audit trail and working drafts, see `../framework/` and `../case-studies/`.

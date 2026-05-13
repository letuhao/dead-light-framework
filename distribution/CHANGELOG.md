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


## [0.7.0] — 2026-05-13

### Added

- _(describe what's new in this release; replace this placeholder)_

### Changed

- _(describe what changed; remove section if not applicable)_

### Notes

- _(any additional context for adopters; remove if not applicable)_

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

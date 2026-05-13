---
title: Distribution README
status: working
version: 0.6.0
audience: human
type: readme
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Distribution skeleton (v0.6.0). Populated progressively across migration commits.
> **Audience:** Framework adopters cloning this folder into their project.
> **Purpose:** Explain how to use this template and where to find each piece.
> **Read next if:** you're new — start with [`INDEX.md`](INDEX.md) for the master TOC. You're a PM — read [`for-pms.md`](for-pms.md). You're an engineer — [`for-ics.md`](for-ics.md). You're configuring an AI aide — [`for-ai-aides.md`](for-ai-aides.md).

# Dead Light Framework — Distribution v0.6.0

This folder is the **sealed, fillable template** for adopters cloning Dead Light Framework into their projects. It contains:

- **`framework/`** — the framework's sealed specification (immutable; modifying = forking).
- **`templates/`** — fillable scaffolds to copy into your project (Astronomican, Reckoning Record, etc.).
- **`examples/`** — read-only reference snapshots (e.g., LoreWeave case study at debate-006-seal time).

## Using this template

Three folder rules:

1. **`framework/`** — the framework's sealed specification. If you modify these files, you are forking the framework and accept responsibility for maintaining your divergence. Reach back upstream via a PR if you think your change should be in the framework.
2. **`templates/`** — fillable scaffolds. Copy these into your project and fill the placeholder text marked with `<...>`.
3. **`examples/`** — read-only reference snapshots. Use as illustrative examples; do not include in your project.

**You own your customization.** The framework does not audit downstream forks (standard OSS fork-and-modify contract per debate 006 §11).

## What's in v0.6.0

Per `VERSION` and `CHANGELOG.md`:

- Phase 0 (sealed)
- Phase 1 (partial; not included in this release — still in `framework/` working area upstream)
- Debates 001–006 (all decided)
- Adeptus Administratum Codex v1.0 (sealed via debate 005)
- Calibration Standards reference catalog
- PM Calibration Guide (3-tier walkthrough)

v1.0.0 will be reserved for "all initial phases sealed" (Phase 1 fully sealed; Phase 2/3/4 framework-level work completed).

## Tooling recommendation (informational)

Per debate 006 §12 J.7: VS Code + Red Hat YAML extension + Markdown All in One + Mermaid Preview Support; GitHub web view minimum. Optional polished release path: MkDocs Material or Docusaurus from this folder's source.

## Upstream

Source repository: `dead-light-framework`. Working drafts live at `../framework/`; this distribution is the sealed snapshot. See upstream `HANDOFF.md` for current framework state.

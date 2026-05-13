---
title: Reading guide for framework adopters
status: working
version: 0.6.0
audience: human
type: readme
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Reading guide for organizations adopting Dead Light Framework into their methodology.
> **Audience:** Human — framework adopters / framework-owner-equivalent within an adopting organization.
> **Purpose:** Explain the adopter contract, the customization scope, and how to integrate the framework with your existing process.
> **Read next if:** you're evaluating Dead Light or onboarding it into your org.

# For framework adopters

## The contract

You clone `distribution/`. You modify within your project. You own your customization. **The framework does not audit you** (per debate 006 §11 — standard OSS fork-and-modify contract: Linux + distros, React + Meta non-control over adopters, arc42, ISO + certification-body separation, Cookiecutter, PostgreSQL contrib).

Three folder rules:

1. **`framework/`** — sealed framework specification. Modifying = forking. You own divergence maintenance. PR upstream if your change is general enough.
2. **`templates/`** — fillable scaffolds. Copy + fill = your project's working artifacts.
3. **`examples/`** — read-only references. Don't include in your project.

## Read these in order

1. **`README.md`** of the distribution — orientation.
2. **`framework/phases/phase-0.md`** — Phase 0 (Reckoning) for retrofit projects; lightweight for greenfield.
3. **`framework/debates/002-retrofit-vs-greenfield.md`** — context for the retrofit-vs-greenfield distinction.
4. **`framework/debates/005-first-chapter-pm-high-lord-aide.md`** — how the AI-aide accommodation works.
5. **`framework/debates/006-documentation-architecture-and-distribution.md`** — this distribution's own design (what you're reading right now is its output).
6. **`framework/chapters/adeptus-administratum/codex.md`** — the AI-aide Chapter Codex; instantiate locally if you want AI-aide support.

## Integration with your existing methodology

Dead Light **composes on top of** Scrum / Kanban / SAFe / RUP / your existing delivery rhythm (per `framework/phases/phase-1.md` §1 thesis). It does not replace them. The composition pattern:

- **Use your existing rhythm** for delivery (sprints, releases, retrospectives).
- **Use Dead Light** for governance: who decides what, why, and how the answer survives staff turnover + AI context loss.
- **Use Codex per Chapter** for AI aide bounds: when your team uses AI agents, the Codex defines explicit operational bounds.

## Versioning expectations

This distribution follows SemVer 2.0 (per debate 006 §5). Initial v0.6.0; v1.0.0 reserved for "all initial phases sealed." Track via `VERSION` + `CHANGELOG.md`.

## When to update from upstream

Pull updates when:

- A new phase seals upstream (e.g., Phase 1 fully sealed → new MINOR version).
- A new Codex / Chapter is added that your project would benefit from.
- A sealed-Law amendment via Re-consecration upstream (MAJOR version bump).
- An IVP CRITICAL/HIGH finding remediated upstream (changes a sealed artifact you depend on).

Skip updates when:

- You have diverged your `framework/` significantly — pulling upstream re-merges; treat as merge-from-upstream-fork.
- The upstream change doesn't affect your current Astronomican or Codex usage.

## Contributing back

If your customization has general value, open a PR upstream. The framework welcomes:

- New Chapters for additional aide patterns (e.g., a "Codex Reviewer Chapter" sibling to Adeptus Administratum).
- Calibration anchors from real organizational data.
- Case studies (your own retrofit application).
- IVP findings (if your independent audit surfaces evidence the framework's current state is wrong).

The framework does not require PRs back. Forking is welcome; contributing is appreciated.

## Example to learn from

`examples/lore-weave-snapshot/` — the framework's first retrofit application, captured at debate-006-seal time. It shows what spec departures look like (D-1 anonymized attribution; D-2 AI-aide-first capture order; D-3 AI-aide-drafts-PM-thresholds) and how the framework handled them. Real-world friction is recorded, not smoothed over.

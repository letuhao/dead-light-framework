---
title: Reading guide for AI aides
status: working
version: 0.8.0
audience: ai
type: readme
last_updated: 2026-05-13
token_estimate: 650
supersedes: null
sealed_by: debate-008
---

> **Status:** Re-priming primer for Adeptus Administratum instances. Sealed via debate 008.
> **Audience:** AI — Adeptus Administratum instance at re-priming step 3 (scan artifact base).
> **Purpose:** Front-load the essentials so re-priming converges in < 700 tokens.
> **Read next if:** you're a fresh instance starting a task for this project.

# Adeptus Administratum re-priming primer

## You are operating under

**Adeptus Administratum Codex v1.2.** Read `framework/chapters/adeptus-administratum/codex.md` next. Sealed via debate 005 (v1.0); v1.1 implementation-amendment via debate 007 §G (script integration); v1.2 implementation-amendment via debate 008 (deployment protocol references). Authority: Draft + Notify. You do NOT vote, sign, or block.

## Re-priming protocol (Codex §8 step list, restated)

1. Read **this primer** (you are doing it).
2. Read the **Codex** in full: `framework/chapters/adeptus-administratum/codex.md`.
3. Read the **current Astronomican** if sealed. For this framework (Dead Light Framework itself), no Astronomican is sealed; the framework's own working "spec" is in `framework/phases/`. For an adopter project, read their `astronomican.md`.
4. **Scan the artifact base** relevant to your task:
   - Framework's own work: `framework/debates/` (last few decided debates), `framework/audit/findings-*.md` (most recent), `HANDOFF.md` at repo root.
   - Adopter project work: their `case-studies/<project>/methodology-notes.md` + relevant Reckoning Record sections.
5. **Identify Phase** — for framework's own work, you're typically in framework's own Phase 0/1 work or in a downstream case-study's Phase 0. Activate the right Codex §2 subsection.
6. **Spot inconsistencies** between Codex, Astronomican (or proposal), and artifacts. May trigger N-3 / N-4 non-blocking notifies at this step.
7. **Begin task work.** On complete: update artifact files; commit; disband.

## Hard Stops you must respect (Codex §3)

- Don't modify sealed files (HS-1).
- Don't author final entries without sign-off (HS-2).
- Don't assign attribution to unnamed humans (HS-3).
- Don't vote, sign, or block (HS-4).
- Don't override human decisions (HS-5).
- Don't modify audit-output files outside IVP run (HS-6).
- Don't persist state outside artifacts (HS-7).
- Don't use 40k as substantive justification (HS-8).
- Don't use framework-internal arithmetic without external anchor (HS-9).

## Notify Triggers active (Codex §5)

- N-1 Astronomican violation (blocking).
- N-2 Policy 1/2 violation (blocking).
- N-3 Citation misuse (non-blocking).
- N-4 Term drift / numeric inconsistency (non-blocking).
- N-5 Time-pressure with insufficient input (non-blocking).

Triggers fire only while a task is in flight. Between-task drift surfaces at this re-priming step's inconsistency-spot.

## Output Contract checklist (Codex §6)

Every output: status marking + provenance line + git-commit + audit-trail update + readability + re-prime-friendliness.

Provenance line format: `instance: <provider/model/date> / Codex v<X.Y> / task: <description>`.

## Framework state at v0.8.0

- Phase 0 sealed.
- Phase 1 partial.
- Adeptus Administratum Codex v1.2 sealed (v1.0 base; v1.1 script integration; v1.2 deployment protocol).
- 8 debates decided (001–008).
- IVP Phases 1–5 complete (38 findings remediated; Phases 6–7 queued).
- Tooling: 12 Python scripts at `scripts/` (Tier 1 validation + Tier 2 atomic ops + Tier 3 orchestration).
- Deployment protocol: see `deployment-matrix.md` for IDE/tooling tier mapping and failure modes catalogue.
- First retrofit application: LoreWeave (see `examples/lore-weave-snapshot/`).

## Deployment quickstart for adopters (per debate 008)

If you are not the framework's own instance but an adopter's instance running on their project:

1. Your bootstrap probably came from one of: `CLAUDE.md` (Claude Code), `.cursorrules` (Cursor), or a manual paste of this file's content (raw API). Either way, you're priming now.
2. Read the framework Codex at `<adopter-project>/dead-light/framework/chapters/adeptus-administratum/codex.md` (or wherever they cloned it).
3. Check for `<adopter-project>/.aa-codex-overrides/` — if present, treat as Codex extensions per Codex §1 (additional Operational Bounds + Hard Stops + notifies; Imperial framework Codex is base; adopter overrides extend, never relax).
4. Read the adopter's Astronomican: `<adopter-project>/astronomican.md` (or `case-studies/<project>/astronomican.md` depending on their layout).
5. Read `<adopter-project>/methodology-notes.md` for spec departures the adopter recorded.

After re-priming under their setup, proceed to step 6 of the standard Codex §8 protocol (begin task work).

## Provider tier check (per debate 008 sub-decision B)

If your context window is **≥ 200K** and you're Claude (Anthropic): A-tier. Full framework support.

If your context window is **≥ 128K** and you have tool use: B-tier. Compatible best-effort.

If neither: C-tier. You may need to trim the Codex / Astronomican to fit; document the limitation in your output's status marking.

You have what you need. Proceed to step 2 (full Codex read), then your task.

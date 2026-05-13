---
audience: both
last_updated: '2026-05-13'
sealed_by: null
status: working
supersedes: null
title: Session Handoff
type: readme
version: not versioned
---

# Session Handoff — 2026-05-11 (end of Session 4)

> Snapshot of Dead Light Framework state at end of Session 4. Read this first to resume work without re-deriving context. Supersedes the 2026-05-10 handoff (end-of-Session-3).

---

## What this project is

**Dead Light Framework** — a software development governance methodology for human + AI agent collaboration. It composes on top of existing methodologies (Agile, Scrum, RUP, …) rather than replacing them. The distinctive idea: a frozen source of authority (the *Astronomican*) that no participant — human or agent — can rewrite at will.

Working tree (project-owner workstation): `C:\Works\_Researchs\dead-light-framework` (alternate workstation: `D:\Works\source\dead-light-framework`).
Reference / case-study codebase (not yet integrated): `C:\Works\_Researchs\lore-weave`.

---

## Status

| Artifact | Status |
|---|---|
| README — Manifesto + Map | Drafted; AI-collaboration literature anchors added in session 3 (F-28 remediation) |
| Glossary — for debate | Working draft (final assembled bottom-up later) |
| Phase 0 — The Reckoning | **Sealed** (all calibration questions resolved in debate 003) |
| Phase 1 — The Astronomican | Partial — debates 001 and 004 resolved; 6 known questions still open (see § Open questions) |
| Phase 2 — Codex per Chapter | **First Chapter (Adeptus Administratum) sealed via debate 005 on 2026-05-11; v1.1 amendment 2026-05-13** (script-invocation references per debate 007 §G; commit `8ebc4da`); **v1.2 amendment 2026-05-13** (deployment-protocol references per debate 008 — §1 override mechanism, §8 bootstrap + deployment-matrix references). Remaining Chapters pending real-project trigger. Codex amendment-procedure precedent established at §10 — implementation amendments don't require new debate; design amendments do. |
| Documentation architecture & distribution | **Sealed via debate 006 on 2026-05-13.** Migration executed across commits `1a857c2` (folder restructure) → `c4a574e` (frontmatter backfill, 25 files) → `9e9afb8` (distribution/ populated with sealed framework + 4 templates + lore-weave snapshot). Distribution v0.6.0 ready at `distribution/` (separable from repo; clone target for adopters). |
| Scripting infrastructure | **Sealed via debate 007 on 2026-05-13.** All 3 tiers implemented (12 scripts at `scripts/`). Tier 1 (validate_frontmatter, check_links, sync_distribution — commit `1246b25`). Tier 2 (frontmatter_set, bump_version, snapshot_case_study, update_handoff_tree — commit `34eec65`). Tier 3 (release.py 8-step orchestrator, new_debate, new_chapter_codex, new_case_study, ivp_phase5 — commit `60cd4fa`). End-to-end pipeline tested via `release.py minor --apply` (v0.6.0 → v0.7.0). Codex v1.1 via debate 007 §G; Codex v1.2 via debate 008. Python 3.10+ with `python-frontmatter` + `typer` + `markdown-it-py`. |
| Deployment protocol | **Sealed via debate 008 on 2026-05-13.** Standardises HOW AI agents engage with the framework at runtime — parallel meta-standard to debate 006 (which standardised paperwork). 10 sub-decisions covering bootstrap pattern (CLAUDE.md auto-loaded for Claude Code A-tier; `.cursorrules` for B-tier; system-prompt paste for raw API), provider tier model (A Claude Code / B GPT-4+/Gemini 2+/Cursor / C local LLMs), session protocol (hybrid full + lightweight re-priming), authorization mechanism (D4 inline ack + audit trail), instance identity recording (audit trail + commit trailer), inter-instance handoff (HANDOFF dual purpose), IDE/tooling matrix (in `distribution/deployment-matrix.md`), multi-project Codex overrides (`.aa-codex-overrides/` per Imperial+Sector pattern), adopter onboarding (5-step quickstart), failure modes catalogue (F-J1..F-J7). Phase 1 implementation: `CLAUDE.md` + `distribution/deployment-matrix.md` + `distribution/templates/aa-codex-overrides-example/` + Codex v1.2 patch. Phase 2/3 tooling scripts deferred. |
| Phase 3 — Heresy detection | Not started |
| Phase 4 — Re-consecration | Not started |
| LoreWeave case study application | **Not started — recommended next step** |
| IVP audit infrastructure | **Spec v0.3 + slash command + Phases 1, 2 (full coverage), 3, 4, 5 complete; all 38 findings (F-01–F-39, with F-26 retracted) remediated; Phases 6, 7 queued** |
| Framework-wide voice policy + cleanup pass | **Policy #3 sealed (commit `344bbb2`, session 4). Voice cleanup pass applied across README, phase-0/1 working drafts, calibration docs, glossary, case study files, debates 002/003/004/006, audit findings executive verdicts (commits `1d81e0d` → `68daccb`). Codex v1.0 skipped (sealed — voice cleanup deferred to future Codex Re-consecration debate).** |

---

## Framework-wide policies (never violate in future drafts)

1. **40k vocabulary is naming and shared metaphor only.** Justification, structural arguments, and assessments of effectiveness must rest on real-world organizational systems with observable track records (constitutional federalism, religious institutions, military doctrine, established corporate practice, open-source governance, established software methodologies, …). When the 40k name and the real-world precedent diverge in implication, the real-world precedent governs the design.

2. **Industry standards over framework-invented formulas.** Calibration questions (thresholds, time budgets, team sizes, audit scopes, failure measurement) anchor to documented external practice — COCOMO II, CMMI v3.0, ITIL 4 / 5, ISA 320, DORA, McCabe, Miller, Brooks, Dunbar, Cohen's κ, Bommasani et al. 2021 Foundation Models, etc. PM and Council retain authority to *select, calibrate, or override*, but the starting point is always documented external practice, never framework arithmetic. Operationalised by the IVP audit (see § IVP). **Argument-warrant tier-floor (added IVP v0.3):** load-bearing arguments — not just citations — must rest on external anchors.

3. **Practitioner voice, not authority pronouncement.** The framework author is a working developer with approximately ten years of cross-project experience, not an academic, industry methodologist, or recognised authority. All framework writing — outward-facing (README, blog posts) and internal (debates, phase drafts, Codices, case studies, IVP findings) — frames hypotheses as personal exploration; qualifies load-bearing claims with first-person or tentative language; refuses to position the framework as correcting or superior to established methodologies (e.g. "Agile assumptions break" → "Agile was not designed with agent participants in scope"); and presents external standards (CMMI, COCOMO, ITIL, Toyota, Bommasani, …) as anchors the framework defers to, not credentials the framework owns. Outward-facing pages carry an explicit "Who is writing this" framing near the top. Universal-sounding pronouncements are rewritten as framework-internal commitments. Operationalised by an author-voice pass to be added to IVP (likely Phase 5b in spec v0.4).

---

## Decisions locked (all sessions)

| Debate | Decision (one-line) |
|---|---|
| [001 — Laws Count Cap and Multi-Repo Scaling](framework/debates/001-laws-count-and-multirepo-scaling.md) | Hierarchical Imperial + Sector Astronomicans with inherit-and-add rule. Default = single Astronomican; split only when ≥ 2 repos + dedicated teams + cross-team contracts + genuinely local decisions are all true. **Anti-survivorship-bias selection-criteria note added in session 3 (F-30 remediation).** |
| [002 — Retrofit vs Greenfield](framework/debates/002-retrofit-vs-greenfield.md) | Introduce **Phase 0: Reckoning** as prerequisite to Phase 1 for retrofit (greenfield runs lightweight or skips). Reckoning-first effective-date model with classification: Keep / Fix-now / Fix-by-date / Reconsider-Law. **Mechanism-based warrant for retrofit precedents (TRC's "explicit past-violations machinery" is the durability anchor) added in session 3 (F-31 remediation).** |
| [003 — Phase 0 Calibration](framework/debates/003-phase-0-calibration.md) | Significance heuristic (6 categorical bullets), Reckoning Team composition rule (≥1 active-IC mandatory + ≥1 tenure-spanning + ≥1 outside-scope), soft time budget with 80%/100% escalation, lightweight greenfield Phase 0 (Assumption Surface + Commitment Audit + Stakeholder Map). |
| [004 — Cap Revision: Miller Citation Correction](framework/debates/004-cap-revision-miller-correction.md) | Cap on Immutable Laws and Guiding Principles raised from `≤ 5` to **5–9 with target ~7** (anchored on Miller 1956's actual 7 ± 2). Same caps apply to Imperial and Sector. Driven by IVP finding F-01 (Miller misquote). |
| [005 — First Chapter: PM / High Lord Aide](framework/debates/005-first-chapter-pm-high-lord-aide.md) | First concrete Chapter sealed: **Adeptus Administratum** ([Codex v1.0](framework/chapters/adeptus-administratum/codex.md)). Multi-role (PM + High Lord aide); Draft + Notify authority (5 trigger types); D4 lifecycle (task-scoped instance + persistent role + artifact continuity via 7-step re-priming protocol); E2 multiplicity (singleton per Astronomican; concurrent instances allowed). Driven by project-owner observation during LoreWeave case-study kick-off that PM threshold-setting on a 358-KLOC project is a bottleneck. |
| [006 — Documentation Architecture and Distribution Template](framework/debates/006-documentation-architecture-and-distribution.md) | Full doc architecture sealed. **A4 folder topology** (root `framework/` + `case-studies/` + `distribution/`); **SemVer** versioning (initial v0.6.0); **document-type-aware** organization (phase = arc42; debate = ADR-extended; codex = 10-section; audit = IVP-spec; case-study = Diátaxis how-to; reference = Diátaxis reference); **500-line hard cap + 300 soft + 100 per-section soft**; **YAML frontmatter (9 fields) + human summary block**; **role-based reading guides** (for-pms / for-ics / for-ai-aides / for-adopters); **strictly one-way framework/ → distribution/ sync** with no adopter audit (standard OSS fork-and-modify per Linux/React/arc42/ISO); **I0 — no customization protocol** (folder convention + status frontmatter classify implicitly); **dual-audience design rules** (7 rules incl. Mermaid diagram convention + tool stack recommendation). |
| [007 — Scripting Infrastructure](framework/debates/007-scripting-infrastructure.md) | Authorise Python tooling under `scripts/` to handle mechanical work. All 3 tiers implemented (12 scripts). Library stack: python-frontmatter + typer + markdown-it-py. Dry-run-by-default for writes; strict transactions. Adds **LLM token-cost** as third design axis (alongside human-time + correctness). ~99% reduction on mechanical work. |
| [008 — Adeptus Administratum Deployment Protocol](framework/debates/008-adeptus-administratum-deployment-protocol.md) | Standardises HOW AI agents engage with framework at runtime. 10 sub-decisions covering bootstrap (A5 provider-tiered with CLAUDE.md + .cursorrules + start_aa_session.py fallback), provider abstraction (B3 tiered Claude/GPT/Gemini/local), session protocol (C4 hybrid full + lightweight re-priming), authorization (D4 inline ack + audit trail), identity recording (E4 combined), handoff (F4 HANDOFF dual purpose), tooling matrix in distribution/deployment-matrix.md, **multi-project Codex overrides via .aa-codex-overrides/ — Imperial+Sector pattern re-applied at Codex level**, 5-step adopter quickstart, 7 failure-mode catalogue F-J1..F-J7. Codex v1.2 implementation-amendment applied same-day per v1.1 precedent. |
| Council composition multi-role | PM is a Council member. Council requires ≥ 3 distinct functional perspectives (minimum-diversity rule). Council size 3–7 (anchored on Dunbar / Brooks for group dynamics — *not* affected by debate 004's Miller-anchored cap revision). Small-team accommodation: AI-assistant Chapters as aides; first Chapter (Adeptus Administratum) sealed via debate 005. |
| Six embedded answers (debate 002) | No Phase 0 sealing; smaller Reckoning Team produces, Council reviews; full attribution; no fixed grandfather cap; no fixed sunset horizon; PM-defined re-reckoning cadence. |

---

## IVP — Independent Verification Pass

Audit workflow specified, executed once (rodage 2026-05-08), then run end-to-end across Phases 2 (extension), 3, and 4 in session 3 (2026-05-09 → 2026-05-10) with remediation between phases. **All 30 surfaced findings remediated (F-01–F-31; F-26 retracted via erratum after re-reading).** The framework now has a substantially complete external-reviewable evidentiary check through Phase 4.

- **Spec** (v0.3, 2026-05-09): [`framework/audit/independent-verification-pass-for-debate.md`](framework/audit/independent-verification-pass-for-debate.md). 7 phases; pre-registered rubric; industry-pragmatic source-tier hierarchy; argument-warrant tier-floor (new in v0.3); cluster-level Phase 4 option (new in v0.3); multi-phase-run pattern with audit-erratum convention (new in v0.3); changelog at § 11.
- **Slash command**: [`.claude/commands/ivp.md`](.claude/commands/ivp.md) — `/ivp [scope]` to re-run.
- **Inventory** (2026-05-08): [`framework/audit/inventory.md`](framework/audit/inventory.md) — 44 load-bearing claims, 76 distinct citations, 40 defined terms, 11 analogy invocations. *Note: inventory paraphrases capture Phase-1-state at audit time and may lag remediation; per IVP v0.3 § 5 Phase 3 pre-step, refresh against current source files before re-running Phase 3.*
- **Findings**:
  - [`findings-2026-05-08.md`](framework/audit/findings-2026-05-08.md) — Phase 2 rodage on 30 citations. 17 V / 11 P / 1 C; 3 HIGH (F-01–F-03) + 4 MEDIUM (F-04–F-07) + 6 LOW (F-08–F-13). All remediated.
  - [`findings-2026-05-09.md`](framework/audit/findings-2026-05-09.md) — Phase 2 extension over the queued 46. 33 V / 12 P / 1 C; 3 HIGH (F-18 Schein/Argyris, F-19 RUP/XP spike, F-20 Lean Startup scope-as-variable) + 2 MEDIUM (F-14, F-21) + 6 LOW (F-15–F-17, F-22–F-24). All remediated. **76/76 citations now have a Phase 2 verdict.**
  - [`findings-phase3-2026-05-09.md`](framework/audit/findings-phase3-2026-05-09.md) — Phase 3 Citation Appropriateness on 73 verified citations. 70 APPROPRIATE / 3 STRETCHED. 1 MEDIUM (F-25, reduced to LOW via erratum) + 2 LOW (F-26 retracted via erratum; F-27 Goodhart). All practically-effective findings remediated. **Headline:** policy-1 check on R-001 (40k metaphor) PASSES.
  - [`findings-phase4-2026-05-09.md`](framework/audit/findings-phase4-2026-05-09.md) — Phase 4 Argument Analysis on 41 LB claims (clustered into 7) + 4 debates. 35 SOUND / 4 WEAK-WARRANT / 0 FALLACIOUS / 2 UNFALSIFIABLE-but-conventional. 2 MEDIUM (F-28 central-premise WEAK-WARRANT, F-31 retrofit survivorship) + 2 LOW (F-29 stress-test threshold, F-30 multi-tier survivorship). All remediated.
  - [`findings-phase5-2026-05-11.md`](framework/audit/findings-phase5-2026-05-11.md) — Phase 5 Internal Consistency across 40 terms, 4 decided debates, ~20 numeric thresholds, both framework-wide policies, and README link integrity. 0 CRITICAL / 0 HIGH / 4 MEDIUM (F-32 phase-1:299 stale "5 Laws max", F-33 calibration-standards Brooks anchor, F-34 Dunbar layer-1 overshoot, F-35 phase-0:34 Time budget) + 4 LOW (F-36 phase-1:309 stale open question, F-37 HANDOFF Two-tier sharpness reflection, F-38 debate-001 metadata annotation, F-39 three small framework-internal heuristics). All 8 remediated. **Headlines:** policy-1 (40k naming-only) PASSES across all 11 inventoried analogies; README link integrity PASSES; design decisions of debates 001–004 reflected at all prescriptive sites — drift was concentrated in meta-commentary sections.
- **Phases 6, 7**: not yet executed. Phase 6 = External Benchmarking (places framework in adjacent literature on AI-agent governance, software governance, frozen-spec patterns). Phase 7 = Synthesis Report (integrates all per-phase findings files into a single artifact for outside reviewers).

---

## Document tree

> **Tree post-debate-006-migration (2026-05-13).** Restructured per debate 006 §3 sub-decision A4 (hybrid): root folders `framework/` + `case-studies/` + `distribution/`. Working drafts in `framework/`; outward-facing sealed snapshot in `distribution/`; project applications in `case-studies/`.

<!-- DOC-TREE-START -->
```
dead-light-framework/
├── .claude/
│   └── commands/
│       └── ivp.md
├── README.md
├── HANDOFF.md
├── LICENSE
├── blogs/
│   └── 01-the-emperor-is-dead-the-light-remains.md
├── case-studies/
│   └── lore-weave/
│       ├── README.md  [working]
│       ├── methodology-notes.md  [working]
│       ├── pm-threshold-decisions.md  [draft]
│       ├── reckoning-record.md  [working]
│       └── reckoning-team-record.md  [working]
├── distribution/
│   ├── examples/
│   │   └── lore-weave-snapshot/
│   │       ├── README.md  [working]
│   │       ├── methodology-notes.md  [working]
│   │       ├── pm-threshold-decisions.md  [draft]
│   │       ├── reckoning-record.md  [working]
│   │       └── reckoning-team-record.md  [working]
│   ├── framework/
│   │   ├── audit/
│   │   │   ├── findings-2026-05-08.md  [working]
│   │   │   ├── findings-2026-05-09.md  [working]
│   │   │   ├── findings-phase3-2026-05-09.md  [working]
│   │   │   ├── findings-phase4-2026-05-09.md  [working]
│   │   │   ├── findings-phase5-2026-05-11.md  [working]
│   │   │   ├── independent-verification-pass-for-debate.md  [working]
│   │   │   └── inventory.md  [working]
│   │   ├── chapters/
│   │   │   └── adeptus-administratum/
│   │   │       └── codex.md  [SEALED]
│   │   ├── debates/
│   │   │   ├── 001-laws-count-and-multirepo-scaling.md  [DECIDED]
│   │   │   ├── 002-retrofit-vs-greenfield.md  [DECIDED]
│   │   │   ├── 003-phase-0-calibration.md  [DECIDED]
│   │   │   ├── 004-cap-revision-miller-correction.md  [DECIDED]
│   │   │   ├── 005-first-chapter-pm-high-lord-aide.md  [DECIDED]
│   │   │   ├── 006-documentation-architecture-and-distribution.md  [DECIDED]
│   │   │   ├── 007-scripting-infrastructure.md  [DECIDED]
│   │   │   └── README.md  [working]
│   │   ├── phases/
│   │   │   └── phase-0.md  [SEALED]
│   │   ├── calibration-standards.md  [SEALED]
│   │   └── pm-calibration-guide.md  [SEALED]
│   ├── templates/
│   │   ├── astronomican-template.md  [fillable]
│   │   ├── pm-threshold-decisions-template.md  [fillable]
│   │   ├── reckoning-record-template.md  [fillable]
│   │   └── reckoning-team-record-template.md  [fillable]
│   ├── CHANGELOG.md  [working]
│   ├── INDEX.md  [working]
│   ├── README.md  [working]
│   ├── VERSION
│   ├── for-adopters.md  [working]
│   ├── for-ai-aides.md  [working]
│   ├── for-ics.md  [working]
│   └── for-pms.md  [working]
├── framework/
│   ├── audit/
│   │   ├── findings-2026-05-08.md  [working]
│   │   ├── findings-2026-05-09.md  [working]
│   │   ├── findings-phase3-2026-05-09.md  [working]
│   │   ├── findings-phase4-2026-05-09.md  [working]
│   │   ├── findings-phase5-2026-05-11.md  [working]
│   │   ├── independent-verification-pass-for-debate.md  [working]
│   │   └── inventory.md  [working]
│   ├── chapters/
│   │   └── adeptus-administratum/
│   │       └── codex.md  [SEALED]
│   ├── debates/
│   │   ├── 001-laws-count-and-multirepo-scaling.md  [DECIDED]
│   │   ├── 002-retrofit-vs-greenfield.md  [DECIDED]
│   │   ├── 003-phase-0-calibration.md  [DECIDED]
│   │   ├── 004-cap-revision-miller-correction.md  [DECIDED]
│   │   ├── 005-first-chapter-pm-high-lord-aide.md  [DECIDED]
│   │   ├── 006-documentation-architecture-and-distribution.md  [DECIDED]
│   │   ├── 007-scripting-infrastructure.md  [DECIDED]
│   │   └── README.md  [working]
│   ├── phases/
│   │   ├── phase-0-for-debate.md  [SEALED]
│   │   └── phase-1-for-debate.md  [partial]
│   ├── calibration-standards.md  [SEALED]
│   ├── glossary-for-debate.md  [working]
│   └── pm-calibration-guide.md  [SEALED]
└── scripts/
    ├── README.md  [working]
    ├── bump_version.py
    ├── check_links.py
    ├── frontmatter_set.py
    ├── ivp_phase5.py
    ├── new_case_study.py
    ├── new_chapter_codex.py
    ├── new_debate.py
    ├── release.py
    ├── requirements.txt
    ├── snapshot_case_study.py
    ├── sync_distribution.py
    ├── update_handoff_tree.py
    └── validate_frontmatter.py
```
<!-- DOC-TREE-END -->

> **Note (post-debate-007):** The tree block above is between `<!-- DOC-TREE-START -->` and `<!-- DOC-TREE-END -->` markers and can be regenerated by `python scripts/update_handoff_tree.py --apply`. Annotation comments (←) are stripped on regeneration; if you want them back, re-edit the tree manually after regeneration or extend the script's annotation feature.

---

## Open questions still on the table

### Phase 1 (from `phase-1-for-debate.md` Note on Method)

Severity HIGH:
- **Two-tier sharpness** — when is something an Immutable Law vs a Guiding Principle? Content question affecting every Astronomican.
- **Failure of sealing** — what happens when stress-test divergence > 20% on sealing day, or Council deadlocks? Without an exit ramp, real teams stall.

Severity MEDIUM:
- Council size lower bound — is 3 truly enough?
- Storage of seal mechanics — signed git tag vs multi-sig vs notarized hash.

Severity LOW:
- Pre-work questions — 5 sufficient or a 6th on agent boundaries?
- Session format — co-located vs distributed timezone.

(The cap-count question and the "First-time vs retrofit" question were both previously listed and have since been closed — the former by debate 004, the latter by debate 002 + phase-1 §10.)

### IVP methodology (carried open in spec v0.3 § 9)

- Should the IVP spec itself be subject to a "meta-IVP" pass periodically? *v0.3 status: spec now references multiple phase-specific findings files; meta-IVP is increasingly relevant.*
- For multi-reviewer runs, what inter-rater-reliability metric is reported (Cohen's κ on classification, agreement rate on verdicts)? *v0.3 status: F-29 remediation introduced Cohen's κ as anchor for the framework's stress-test threshold; using the same metric for IVP's own inter-rater reliability would be coherent.*
- Recursion-risk for governance-citing-governance — when Dead Light cites PRINCE2/ITIL/CMMI, does it inherit the cited framework's evidentiary issues? When and how flagged in Phase 6?
- Should Phase 4 fallacy checklist be expanded based on which fallacies actually surface in real runs? *v0.3 status: survivorship bias surfaced multiple times (F-30, F-31); already in v0.2 checklist; no expansion needed yet.*
- *(New v0.3)* Formal definition of "argument cluster" for Phase 4 cluster-level decomposition.
- *(New v0.3)* Should remediation commits include a `Findings-addressed:` trailer for traceability?

### Glossary

Final glossary deferred — to be assembled bottom-up as later phases force real definitions. The 25 candidates and 11 needs-debate items are catalogued in `framework/glossary-for-debate.md`.

---

## Recommended next step

**Sign off [`pm-threshold-decisions.md`](case-studies/lore-weave/pm-threshold-decisions.md), then run LoreWeave Phase 0 Pass 1.**

End-of-session-4 state: LoreWeave case study is scaffolded; PM Threshold Decisions are drafted (under Adeptus Administratum Codex §2.1) and pending project-owner sign-off. Pre-Pass-1 work has already produced a scan summary (~358 KLOC, 1314 commits in 6 months, MMO-RPG pivot on `mmo-rpg/design-resume` branch, frontend v1→v2 rename complete, license + infra pivots in last month).

The framework is now equipped with:
- IVP through Phase 5 — within-document evidentiary check substantially complete.
- Adeptus Administratum Codex v1.0 — first Chapter sealed, available for PM-aide and Council-aide invocations during Phase 0 and Phase 1.
- Three spec departures (D-1 anonymized attribution; D-2 AI-aide-first Implicit Principles; D-3 AI-aide-drafts-PM-thresholds) logged and re-evaluated as compliant with the sealed Codex.

How to resume:
1. Review [`case-studies/lore-weave/pm-threshold-decisions.md`](case-studies/lore-weave/pm-threshold-decisions.md). Three items flagged for owner attention: (a) §1 #2 "lowered 5 person-days → 1 day for solo pace"; (b) §3 "design-drafts/ and poc/ — committed decisions or exploration?"; (c) §4 "~6 person-week initial commitment" — confirm or scope down.
2. Add adjustments in the "Adjustments by project owner" section of `pm-threshold-decisions.md` if any.
3. Check three sign-off checkboxes at the bottom and sign.
4. Open a new chat session — a new Adeptus Administratum instance re-primes per Codex §8 protocol and begins **Pass 1 Current State Audit** of LoreWeave (`docs/01_foundation/` + `docs/02_governance/` + `docs/03_planning/` + `frontend/` + `services/knowledge-service/`).
5. The Pass 1 work fills [`reckoning-record.md`](case-studies/lore-weave/reckoning-record.md) sections 1, 2 (partial), 3 (partial) for the in-scope areas.

---

## Alternative next steps

If LoreWeave mapping is not the right next move:

- **IVP Phase 6 (External Benchmarking)** — places the framework in adjacent literature (AI-agent governance, software governance, frozen-spec patterns). Heaviest IVP phase; produces `audit/benchmark.md`.
- **IVP Phase 7 (Synthesis Report)** — integrates all per-phase findings files. Lightweight now that Phases 1–5 are done; one of the cleanest "wrap up the audit story" moves available.
- **Phase 1 Failure of sealing** — short close-out debate; ceremony exit-ramp question.
- **Phase 1 Two-tier sharpness** — deeper internal debate; Law vs Principle distinction.
- **Phase 2 draft (Codex per Chapter)** — start defining Codex spec, including AI-assistant aide Chapters referenced from Phase 0 / Phase 1 anti-patterns.

Recommended ordering if doing further audit work over LoreWeave: LoreWeave first (it informs Phase 6 benchmarking with real empirical data), then Phase 6 + 7. Phase 7 alone (without Phase 6) is also viable as a synthesis of the now-complete Phases 1–5.

---

## Conventions to preserve

- All documents in `framework/`, `case-studies/`, and `distribution/` use English; conversation language with the project owner is Vietnamese.
- Working drafts use the `*-for-debate.md` suffix; final docs drop the suffix.
- Specific arguments live in `framework/debates/NNN-topic.md` with status (open / recommended / decided / superseded).
- Each debate has a Decision section to be filled when the project owner decides — **never** pre-fill it.
- The README's "planned" links indicate forthcoming docs; they should not be made into broken-link claims.
- IVP separation-of-concerns: audit-output files (`framework/audit/`) and remediation edits go in *separate commits*; audit run never modifies framework documents in the same pass. **Per session-3 lesson:** for this small docs-only repo with single-owner review, keep the separation at the *commit* level — do **not** default to separate branches per audit/remediation per phase. The 2026-05-09 multi-phase run created 7 branches + 7 stacked PRs and the project owner explicitly called this "chaos". For future runs prefer one branch per IVP run with multiple commits, OR one branch per phase max — not separate branches for each audit-vs-remediation pair.
- IVP spec changes go *between runs*, never during a run; rubric tables are pre-registered per pass. (Note: v0.3 clarified this is "between runs", not "between phases of the same run".)

---

## How to resume

1. Read this file end-to-end.
2. Read `README.md` for the framework's elevator pitch (now includes AI-collab literature anchors).
3. Skim `framework/phases/phase-0-for-debate.md` and `framework/phases/phase-1-for-debate.md` — the two main artifacts.
4. Skim `framework/debates/README.md` for decision history (6 debates decided).
5. If touching evidentiary claims or calibration anchors: skim IVP spec v0.3 § 4 rubric, § 5 phase procedures (especially Phase 3 inventory-paraphrase pre-step and Phase 4 cluster option), and § 11 changelog before editing.
6. Confirm with project owner which path to take from "Recommended next step" or "Alternative next steps" before starting work.
7. **For PR strategy on multi-phase IVP runs:** do not propose 7 stacked PRs; propose either a single branch with multiple commits or at most one PR per phase. See "Conventions to preserve" above.

---

## Repo state at end of Session 4

- Branch: `main` (clean as of end of session 4; ahead of `origin/main` by 15 commits — not yet pushed pending project-owner authorization).
- Recent commits on `main` (top of log, end of session 4):
  ```
  (commit pending) HANDOFF refresh after debate 007 seal + Tier 1 scripts
  1246b25  seal debate 007 + implement Tier 1 scripts (validate / check_links / sync_distribution)
  39dd8f7  open debate 007 — Scripting Infrastructure (post-debate-006 automation)
  fc5ee16  Phase 3 — HANDOFF refresh + final sweep (debate 006 migration complete)
  9e9afb8  Phase 2 — populate distribution/ with framework + templates + lore-weave snapshot
  c4a574e  Phase 1b — YAML frontmatter backfill across framework/ + case-studies/
  1a857c2  Phase 1a — folder restructure + cross-reference updates per debate 006
  7f58439  seal debate 006 — Documentation Architecture and Distribution Template
  68daccb  apply practitioner voice to audit findings executive verdicts
  d18472d  apply practitioner voice to debates 002 / 003 / 004 / 006
  52702fe  apply practitioner voice to operational + case-study docs
  f60a606  apply practitioner voice to phase-0 and phase-1 working drafts
  1d81e0d  apply practitioner voice to README + add "Who is writing this" section
  344bbb2  add framework-wide policy #3 (practitioner voice, not authority pronouncement)
  5077769  open debate 006 — Documentation Architecture and Distribution Template
  e35dcb6  propagate Adeptus Administratum Codex seal across framework + case study
  78d4bb4  seal debate 005 + create Adeptus Administratum Codex v1.0
  f4c7ba5  consolidate HANDOFF for end of Session 3  ← end of session 3
  ```
- All 38 surfaced findings (F-01 through F-39, with F-26 retracted via erratum) are remediated.
- IVP infrastructure: Phases 1, 2 (full coverage of all 76 citations), 3, 4, 5 complete.
- Phase 2 (Codex per Chapter): first Chapter (Adeptus Administratum) sealed via debate 005 on 2026-05-11; Codex v1.0 at [`framework/chapters/adeptus-administratum/codex.md`](framework/chapters/adeptus-administratum/codex.md); additional Chapters deferred to real-project trigger.
- LoreWeave case study: Phase 0 scaffolding complete; pre-Pass-1 work (folder, PM threshold proposal, scan, spec departures D-1/D-2/D-3) committed; pending PM sign-off of [`pm-threshold-decisions.md`](case-studies/lore-weave/pm-threshold-decisions.md) before Pass 1 begins.
- IVP spec at v0.3. Phase 5b (author-voice pass) referenced in framework-wide policy #3 but not yet drafted into spec v0.4.
- IVP Phase 5 complete; Phases 6, 7 queued.
- **Session 4 work summary:** Framework-wide policy #3 (Practitioner voice) sealed and applied across 17 files (commits `344bbb2` → `68daccb`). Debate 006 opened (`5077769`), refined through decide-debate dialogue (sub-decision D Lifecycle revised from D3 → D4 task-scoped instance; sub-decision I revised from I4 markers → I0 no-protocol; sub-decision J extended with J.6 Mermaid + J.7 tool stack), then sealed (`7f58439`). Three-phase migration executed: Phase 1a folder restructure (`1a857c2` — docs/ → framework/, case-studies/ at root, distribution/ skeleton); Phase 1b YAML frontmatter backfill across 25 files (`c4a574e`); Phase 2 populate distribution/ with sealed framework copy + 4 fillable templates + lore-weave-snapshot (`9e9afb8`); Phase 3 HANDOFF refresh + final sweep (`fc5ee16`). Then debate 007 (Scripting Infrastructure) opened (`39dd8f7`) and sealed same-day (`1246b25`) with Tier 1 scripts implemented (validate_frontmatter / check_links / sync_distribution under `scripts/`). First blog post drafted earlier in session at `blogs/01-the-emperor-is-dead-the-light-remains.md`. **Layer count surfaced:** framework now has four sealed-concern layers (project governance / operational aide / document architecture / **tooling infrastructure**) — each fractal of frozen-authority thesis per debate 007 §17. **LLM token-cost** added as a third framework-design axis (alongside human-time + correctness).
- No external dependencies, no build, no tests — this is a documentation repository.
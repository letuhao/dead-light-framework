# Session Handoff — 2026-05-10 (end of Session 3)

> Snapshot of Dead Light Framework state at end of Session 3. Read this first to resume work without re-deriving context. Supersedes the 2026-05-09 handoff (end-of-Session-2).

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
| Phase 2 — Codex per Chapter | Not started |
| Phase 3 — Heresy detection | Not started |
| Phase 4 — Re-consecration | Not started |
| LoreWeave case study application | **Not started — recommended next step** |
| IVP audit infrastructure | **Spec v0.3 + slash command + Phases 1, 2 (full coverage), 3, 4, 5 complete; all 38 findings (F-01–F-39, with F-26 retracted) remediated; Phases 6, 7 queued** |

---

## Framework-wide policies (never violate in future drafts)

1. **40k vocabulary is naming and shared metaphor only.** Justification, structural arguments, and assessments of effectiveness must rest on real-world organizational systems with observable track records (constitutional federalism, religious institutions, military doctrine, established corporate practice, open-source governance, established software methodologies, …). When the 40k name and the real-world precedent diverge in implication, the real-world precedent governs the design.

2. **Industry standards over framework-invented formulas.** Calibration questions (thresholds, time budgets, team sizes, audit scopes, failure measurement) anchor to documented external practice — COCOMO II, CMMI v3.0, ITIL 4 / 5, ISA 320, DORA, McCabe, Miller, Brooks, Dunbar, Cohen's κ, Bommasani et al. 2021 Foundation Models, etc. PM and Council retain authority to *select, calibrate, or override*, but the starting point is always documented external practice, never framework arithmetic. Operationalised by the IVP audit (see § IVP). **Argument-warrant tier-floor (added IVP v0.3):** load-bearing arguments — not just citations — must rest on external anchors.

---

## Decisions locked (all sessions)

| Debate | Decision (one-line) |
|---|---|
| [001 — Laws Count Cap and Multi-Repo Scaling](docs/debates/001-laws-count-and-multirepo-scaling.md) | Hierarchical Imperial + Sector Astronomicans with inherit-and-add rule. Default = single Astronomican; split only when ≥ 2 repos + dedicated teams + cross-team contracts + genuinely local decisions are all true. **Anti-survivorship-bias selection-criteria note added in session 3 (F-30 remediation).** |
| [002 — Retrofit vs Greenfield](docs/debates/002-retrofit-vs-greenfield.md) | Introduce **Phase 0: Reckoning** as prerequisite to Phase 1 for retrofit (greenfield runs lightweight or skips). Reckoning-first effective-date model with classification: Keep / Fix-now / Fix-by-date / Reconsider-Law. **Mechanism-based warrant for retrofit precedents (TRC's "explicit past-violations machinery" is the durability anchor) added in session 3 (F-31 remediation).** |
| [003 — Phase 0 Calibration](docs/debates/003-phase-0-calibration.md) | Significance heuristic (6 categorical bullets), Reckoning Team composition rule (≥1 active-IC mandatory + ≥1 tenure-spanning + ≥1 outside-scope), soft time budget with 80%/100% escalation, lightweight greenfield Phase 0 (Assumption Surface + Commitment Audit + Stakeholder Map). |
| [004 — Cap Revision: Miller Citation Correction](docs/debates/004-cap-revision-miller-correction.md) | Cap on Immutable Laws and Guiding Principles raised from `≤ 5` to **5–9 with target ~7** (anchored on Miller 1956's actual 7 ± 2). Same caps apply to Imperial and Sector. Driven by IVP finding F-01 (Miller misquote). |
| Council composition multi-role | PM is a Council member. Council requires ≥ 3 distinct functional perspectives (minimum-diversity rule). Council size 3–7 (anchored on Dunbar / Brooks for group dynamics — *not* affected by debate 004's Miller-anchored cap revision). Small-team accommodation: AI-assistant Chapters as aides; Codex specifics deferred to Phase 2. |
| Six embedded answers (debate 002) | No Phase 0 sealing; smaller Reckoning Team produces, Council reviews; full attribution; no fixed grandfather cap; no fixed sunset horizon; PM-defined re-reckoning cadence. |

---

## IVP — Independent Verification Pass

Audit workflow specified, executed once (rodage 2026-05-08), then run end-to-end across Phases 2 (extension), 3, and 4 in session 3 (2026-05-09 → 2026-05-10) with remediation between phases. **All 30 surfaced findings remediated (F-01–F-31; F-26 retracted via erratum after re-reading).** The framework now has a substantially complete external-reviewable evidentiary check through Phase 4.

- **Spec** (v0.3, 2026-05-09): [`docs/audit/independent-verification-pass-for-debate.md`](docs/audit/independent-verification-pass-for-debate.md). 7 phases; pre-registered rubric; industry-pragmatic source-tier hierarchy; argument-warrant tier-floor (new in v0.3); cluster-level Phase 4 option (new in v0.3); multi-phase-run pattern with audit-erratum convention (new in v0.3); changelog at § 11.
- **Slash command**: [`.claude/commands/ivp.md`](.claude/commands/ivp.md) — `/ivp [scope]` to re-run.
- **Inventory** (2026-05-08): [`docs/audit/inventory.md`](docs/audit/inventory.md) — 44 load-bearing claims, 76 distinct citations, 40 defined terms, 11 analogy invocations. *Note: inventory paraphrases capture Phase-1-state at audit time and may lag remediation; per IVP v0.3 § 5 Phase 3 pre-step, refresh against current source files before re-running Phase 3.*
- **Findings**:
  - [`findings-2026-05-08.md`](docs/audit/findings-2026-05-08.md) — Phase 2 rodage on 30 citations. 17 V / 11 P / 1 C; 3 HIGH (F-01–F-03) + 4 MEDIUM (F-04–F-07) + 6 LOW (F-08–F-13). All remediated.
  - [`findings-2026-05-09.md`](docs/audit/findings-2026-05-09.md) — Phase 2 extension over the queued 46. 33 V / 12 P / 1 C; 3 HIGH (F-18 Schein/Argyris, F-19 RUP/XP spike, F-20 Lean Startup scope-as-variable) + 2 MEDIUM (F-14, F-21) + 6 LOW (F-15–F-17, F-22–F-24). All remediated. **76/76 citations now have a Phase 2 verdict.**
  - [`findings-phase3-2026-05-09.md`](docs/audit/findings-phase3-2026-05-09.md) — Phase 3 Citation Appropriateness on 73 verified citations. 70 APPROPRIATE / 3 STRETCHED. 1 MEDIUM (F-25, reduced to LOW via erratum) + 2 LOW (F-26 retracted via erratum; F-27 Goodhart). All practically-effective findings remediated. **Headline:** policy-1 check on R-001 (40k metaphor) PASSES.
  - [`findings-phase4-2026-05-09.md`](docs/audit/findings-phase4-2026-05-09.md) — Phase 4 Argument Analysis on 41 LB claims (clustered into 7) + 4 debates. 35 SOUND / 4 WEAK-WARRANT / 0 FALLACIOUS / 2 UNFALSIFIABLE-but-conventional. 2 MEDIUM (F-28 central-premise WEAK-WARRANT, F-31 retrofit survivorship) + 2 LOW (F-29 stress-test threshold, F-30 multi-tier survivorship). All remediated.
  - [`findings-phase5-2026-05-11.md`](docs/audit/findings-phase5-2026-05-11.md) — Phase 5 Internal Consistency across 40 terms, 4 decided debates, ~20 numeric thresholds, both framework-wide policies, and README link integrity. 0 CRITICAL / 0 HIGH / 4 MEDIUM (F-32 phase-1:299 stale "5 Laws max", F-33 calibration-standards Brooks anchor, F-34 Dunbar layer-1 overshoot, F-35 phase-0:34 Time budget) + 4 LOW (F-36 phase-1:309 stale open question, F-37 HANDOFF Two-tier sharpness reflection, F-38 debate-001 metadata annotation, F-39 three small framework-internal heuristics). All 8 remediated. **Headlines:** policy-1 (40k naming-only) PASSES across all 11 inventoried analogies; README link integrity PASSES; design decisions of debates 001–004 reflected at all prescriptive sites — drift was concentrated in meta-commentary sections.
- **Phases 6, 7**: not yet executed. Phase 6 = External Benchmarking (places framework in adjacent literature on AI-agent governance, software governance, frozen-spec patterns). Phase 7 = Synthesis Report (integrates all per-phase findings files into a single artifact for outside reviewers).

---

## Document tree

```
dead-light-framework/
├── .claude/
│   └── commands/
│       └── ivp.md                                         ← Slash command for IVP re-run
├── README.md                                              ← Manifesto + Map (front door); AI-collab anchors added F-28
├── HANDOFF.md                                             ← This file
├── LICENSE                                                ← MIT
├── chat.txt                                               ← Original chat history that motivated framework
└── docs/
    ├── glossary-for-debate.md                             ← Working glossary (final assembled bottom-up later)
    ├── phase-0-for-debate.md                              ← Phase 0: The Reckoning [SEALED]
    ├── phase-1-for-debate.md                              ← Phase 1: The Astronomican [partial]
    ├── calibration-standards.md                           ← Industry-standards reference catalog
    ├── pm-calibration-guide.md                            ← Practical PM step-by-step at 3 rigor tiers
    ├── audit/
    │   ├── independent-verification-pass-for-debate.md    ← IVP methodology spec (v0.3)
    │   ├── inventory.md                                   ← Phase 1 inventory output (2026-05-08; may lag remediation)
    │   ├── findings-2026-05-08.md                         ← Phase 2 rodage (F-01–F-13)
    │   ├── findings-2026-05-09.md                         ← Phase 2 extension (F-14–F-24)
    │   ├── findings-phase3-2026-05-09.md                  ← Phase 3 Citation Appropriateness (F-25–F-27 + erratum)
    │   ├── findings-phase4-2026-05-09.md                  ← Phase 4 Argument Analysis (F-28–F-31)
    │   └── findings-phase5-2026-05-11.md                  ← Phase 5 Internal Consistency (F-32–F-39)
    └── debates/
        ├── README.md                                      ← Debate index
        ├── 001-laws-count-and-multirepo-scaling.md        [decided]
        ├── 002-retrofit-vs-greenfield.md                  [decided]
        ├── 003-phase-0-calibration.md                     [decided]
        └── 004-cap-revision-miller-correction.md          [decided]
```

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

Final glossary deferred — to be assembled bottom-up as later phases force real definitions. The 25 candidates and 11 needs-debate items are catalogued in `docs/glossary-for-debate.md`.

---

## Recommended next step

**Map Phase 0 + Phase 1 against LoreWeave as a real test case.**

Why this is still the right next step at end of session 3:

- LoreWeave is the framework's primary case study and the reason the framework exists. Project owner has signaled multiple scope changes — textbook retrofit case.
- Phase 0 + Phase 1 are now defined in enough detail to execute against real data, **and** the IVP audit has substantially de-risked the evidentiary base (76/76 citations verified, 41 load-bearing arguments analyzed, 30 findings remediated).
- Running the framework on a real codebase will expose design weaknesses faster than further abstract debate or further audit phases.
- LoreWeave has 6 services in `contracts/api/` (identity, books, catalog, model-billing, model-registry, sharing) — also a candidate for the Sector Astronomican mechanism from debate 001.
- The IVP work in session 3 surfaced two specific items the LoreWeave application can test empirically: F-29's stress-test 20% threshold (now anchored on Cohen's κ but pending real calibration) and F-21's M&A KLOC heuristic (now downgraded to sanity-check, pending COCOMO-derived budgets in practice).

How to start:
1. Read `C:\Works\_Researchs\lore-weave\docs\01_foundation\01_PROJECT_OVERVIEW.md` (~390 lines).
2. Skim `docs/02_governance/` and `docs/03_planning/` to identify scope changes and decisions.
3. Run a Tier 1 (startup) Phase 0 against LoreWeave per `pm-calibration-guide.md`.
4. Document findings as `docs/case-study-lore-weave.md` (referenced from README as planned).

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

- All documents in `docs/` use English; conversation language with the project owner is Vietnamese.
- Working drafts use the `*-for-debate.md` suffix; final docs drop the suffix.
- Specific arguments live in `docs/debates/NNN-topic.md` with status (open / recommended / decided / superseded).
- Each debate has a Decision section to be filled when the project owner decides — **never** pre-fill it.
- The README's "planned" links indicate forthcoming docs; they should not be made into broken-link claims.
- IVP separation-of-concerns: audit-output files (`docs/audit/`) and remediation edits go in *separate commits*; audit run never modifies framework documents in the same pass. **Per session-3 lesson:** for this small docs-only repo with single-owner review, keep the separation at the *commit* level — do **not** default to separate branches per audit/remediation per phase. The 2026-05-09 multi-phase run created 7 branches + 7 stacked PRs and the project owner explicitly called this "chaos". For future runs prefer one branch per IVP run with multiple commits, OR one branch per phase max — not separate branches for each audit-vs-remediation pair.
- IVP spec changes go *between runs*, never during a run; rubric tables are pre-registered per pass. (Note: v0.3 clarified this is "between runs", not "between phases of the same run".)

---

## How to resume

1. Read this file end-to-end.
2. Read `README.md` for the framework's elevator pitch (now includes AI-collab literature anchors).
3. Skim `docs/phase-0-for-debate.md` and `docs/phase-1-for-debate.md` — the two main artifacts.
4. Skim `docs/debates/README.md` for decision history (4 debates decided).
5. If touching evidentiary claims or calibration anchors: skim IVP spec v0.3 § 4 rubric, § 5 phase procedures (especially Phase 3 inventory-paraphrase pre-step and Phase 4 cluster option), and § 11 changelog before editing.
6. Confirm with project owner which path to take from "Recommended next step" or "Alternative next steps" before starting work.
7. **For PR strategy on multi-phase IVP runs:** do not propose 7 stacked PRs; propose either a single branch with multiple commits or at most one PR per phase. See "Conventions to preserve" above.

---

## Repo state at end of Session 3

- Branch: `main` (clean). All session-3 work merged via 7 PRs (#2–#8), then merged-branch cleanup (local + remote).
- Recent commits on `main` (top of log):
  ```
  dcfb619  refine IVP spec to v0.3 from multi-phase 2026-05-09 run lessons
  9094c4c  remediate IVP Phase 4 findings F-28 through F-31
  b080629  IVP Phase 4 (Argument Analysis) on 41 load-bearing claims + 4 debates
  6fcbd00  remediate IVP Phase 3 findings F-25 (reduced) and F-27
  f73384b  audit erratum: reduce F-25 (MEDIUM->LOW) and retract F-26
  b125401  IVP Phase 3 (Citation Appropriateness) on 73 verified citations
  5ec327b  remediate IVP 2026-05-09 findings F-14 through F-24
  843fcba  IVP Phase 2 extension: verify the queued 46 citations
  6a34721  Merge pull request #1 from letuhao/claude/read-handoff-status-53xfC  ← end of session 2
  ```
- All 38 surfaced findings (F-01 through F-39, with F-26 retracted via erratum) are remediated.
- IVP infrastructure: Phases 1, 2 (full coverage of all 76 citations), 3, 4, 5 complete.
- IVP spec at v0.3.
- IVP Phase 5 complete; Phases 6, 7 queued.
- No external dependencies, no build, no tests — this is a documentation repository.

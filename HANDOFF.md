# Session Handoff — 2026-05-09 (end of Session 2)

> Snapshot of Dead Light Framework state at end of Session 2. Read this first to resume work without re-deriving context. Supersedes the 2026-05-08 handoff.

---

## What this project is

**Dead Light Framework** — a software development governance methodology for human + AI agent collaboration. It composes on top of existing methodologies (Agile, Scrum, RUP, …) rather than replacing them. The distinctive idea: a frozen source of authority (the *Astronomican*) that no participant — human or agent — can rewrite at will.

Working tree (project-owner workstation): `C:\Works\_Researchs\dead-light-framework`
Reference / case-study codebase (not yet integrated): `C:\Works\_Researchs\lore-weave`

---

## Status

| Artifact | Status |
|---|---|
| README — Manifesto + Map | Drafted |
| Glossary — for debate | Working draft (final assembled bottom-up later) |
| Phase 0 — The Reckoning | **Sealed** (all calibration questions resolved in debate 003) |
| Phase 1 — The Astronomican | Partial — debates 001 and 004 resolved; 6 known questions still open (see § Open questions) |
| Phase 2 — Codex per Chapter | Not started |
| Phase 3 — Heresy detection | Not started |
| Phase 4 — Re-consecration | Not started |
| LoreWeave case study application | **Not started — recommended next step** |
| IVP audit infrastructure | **Spec v0.2 + slash command + first rodage complete; all 13 findings remediated; 46 citations queued for full Phase 2** |

---

## Framework-wide policies (never violate in future drafts)

1. **40k vocabulary is naming and shared metaphor only.** Justification, structural arguments, and assessments of effectiveness must rest on real-world organizational systems with observable track records (constitutional federalism, religious institutions, military doctrine, established corporate practice, open-source governance, established software methodologies, …). When the 40k name and the real-world precedent diverge in implication, the real-world precedent governs the design.

2. **Industry standards over framework-invented formulas.** Calibration questions (thresholds, time budgets, team sizes, audit scopes, failure measurement) anchor to documented external practice — COCOMO II, CMMI v3.0, ITIL 4 / 5, ISA 320, DORA, McCabe, Miller, Brooks, Dunbar, etc. PM and Council retain authority to *select, calibrate, or override*, but the starting point is always documented external practice, never framework arithmetic. Operationalised by the IVP audit (see § IVP).

---

## Decisions locked (all sessions)

| Debate | Decision (one-line) |
|---|---|
| [001 — Laws Count Cap and Multi-Repo Scaling](docs/debates/001-laws-count-and-multirepo-scaling.md) | Hierarchical Imperial + Sector Astronomicans with inherit-and-add rule. Default = single Astronomican; split only when ≥ 2 repos + dedicated teams + cross-team contracts + genuinely local decisions are all true. |
| [002 — Retrofit vs Greenfield](docs/debates/002-retrofit-vs-greenfield.md) | Introduce **Phase 0: Reckoning** as prerequisite to Phase 1 for retrofit (greenfield runs lightweight or skips). Reckoning-first effective-date model with classification: Keep / Fix-now / Fix-by-date / Reconsider-Law. |
| [003 — Phase 0 Calibration](docs/debates/003-phase-0-calibration.md) | Significance heuristic (6 categorical bullets), Reckoning Team composition rule (≥1 active-IC mandatory + ≥1 tenure-spanning + ≥1 outside-scope), soft time budget with 80%/100% escalation, lightweight greenfield Phase 0 (Assumption Surface + Commitment Audit + Stakeholder Map). |
| [004 — Cap Revision: Miller Citation Correction](docs/debates/004-cap-revision-miller-correction.md) | Cap on Immutable Laws and Guiding Principles raised from `≤ 5` to **5–9 with target ~7** (anchored on Miller 1956's actual 7 ± 2). Same caps apply to Imperial and Sector. Driven by IVP finding F-01 (Miller misquote). |
| Council composition multi-role | PM is a Council member. Council requires ≥ 3 distinct functional perspectives (minimum-diversity rule). Council size 3–7 (anchored on Dunbar / Brooks for group dynamics — *not* affected by debate 004's Miller-anchored cap revision). Small-team accommodation: AI-assistant Chapters as aides; Codex specifics deferred to Phase 2. |
| Six embedded answers (debate 002) | No Phase 0 sealing; smaller Reckoning Team produces, Council reviews; full attribution; no fixed grandfather cap; no fixed sunset horizon; PM-defined re-reckoning cadence. |

---

## IVP — Independent Verification Pass

Audit workflow specified, executed once (rodage 2026-05-08), and refined to spec v0.2 (2026-05-09). All 13 findings from the rodage have been remediated. The framework now has an external-reviewable evidentiary check.

- **Spec** (v0.2): [`docs/audit/independent-verification-pass-for-debate.md`](docs/audit/independent-verification-pass-for-debate.md). 7 phases; pre-registered rubric; industry-pragmatic source-tier hierarchy; mandatory primary-source read + disconfirming search for load-bearing claims (added in v0.2 after rodage exposed coverage gaps); changelog at § 11.
- **Slash command**: [`.claude/commands/ivp.md`](.claude/commands/ivp.md) — `/ivp [scope]` to re-run.
- **Inventory**: [`docs/audit/inventory.md`](docs/audit/inventory.md) — 44 load-bearing claims, 76 distinct citations, 40 defined terms, 11 analogy invocations.
- **Findings**: [`docs/audit/findings-2026-05-08.md`](docs/audit/findings-2026-05-08.md) — 30 citations rigorously verified (17 VERIFIED, 11 PARTIAL, 1 CONTRADICTED); 3 HIGH (F-01–F-03) + 4 MEDIUM (F-04–F-07) + 6 LOW (F-08–F-13) findings, all remediated.
- **Coverage gap**: 46 of 76 citations not individually verified in the rodage. Queued for full Phase 2 in a future run.
- **Phases 3–7**: not yet executed.

---

## Document tree

```
dead-light-framework/
├── .claude/
│   └── commands/
│       └── ivp.md                                         ← Slash command for IVP re-run
├── README.md                                              ← Manifesto + Map (front door)
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
    │   ├── independent-verification-pass-for-debate.md    ← IVP methodology spec (v0.2)
    │   ├── inventory.md                                   ← Phase 1 inventory output
    │   └── findings-2026-05-08.md                         ← Phase 2 partial findings (rodage)
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
- **#2 Two-tier sharpness** — when is something an Immutable Law vs a Guiding Principle? Content question affecting every Astronomican.
- **#3 Failure of sealing** — what happens when stress-test divergence > 20% on sealing day, or Council deadlocks? Without an exit ramp, real teams stall.

Severity MEDIUM:
- Council size lower bound — is 3 truly enough?
- Storage of seal mechanics — signed git tag vs multi-sig vs notarized hash.

Severity LOW:
- Pre-work questions — 5 sufficient or a 6th on agent boundaries?
- Session format — co-located vs distributed timezone.

(The cap-count question, originally listed here, was closed by debate 004.)

### IVP methodology (carried open in spec v0.2 § 9)

- Should the IVP spec itself be subject to a "meta-IVP" pass periodically? (Today the spec excludes itself from scope to avoid self-reference; a separate reviewer would be the cleanest answer.)
- For multi-reviewer runs, what inter-rater-reliability metric is reported (Cohen's κ on classification, agreement rate on verdicts)?
- Recursion-risk for governance-citing-governance — when Dead Light cites PRINCE2/ITIL/CMMI, does it inherit the cited framework's evidentiary issues? When and how flagged in Phase 6?
- Should Phase 4 fallacy checklist be expanded based on which fallacies actually surface in real runs? (Add only after observed; do not pre-emptively bloat.)

### Glossary

Final glossary deferred — to be assembled bottom-up as later phases force real definitions. The 25 candidates and 11 needs-debate items are catalogued in `docs/glossary-for-debate.md`.

---

## Recommended next step

**Map Phase 0 + Phase 1 against LoreWeave as a real test case.**

Why this is the right next step:
- LoreWeave is the framework's primary case study and the reason the framework exists. Project owner has signaled multiple scope changes — textbook retrofit case.
- Phase 0 + Phase 1 are now defined in enough detail to execute against real data.
- Running the framework on a real codebase will expose design weaknesses faster than further abstract debate.
- LoreWeave has 6 services in `contracts/api/` (identity, books, catalog, model-billing, model-registry, sharing) — also a candidate for the Sector Astronomican mechanism from debate 001.

How to start:
1. Read `C:\Works\_Researchs\lore-weave\docs\01_foundation\01_PROJECT_OVERVIEW.md` (~390 lines).
2. Skim `docs/02_governance/` and `docs/03_planning/` to identify scope changes and decisions.
3. Run a Tier 1 (startup) Phase 0 against LoreWeave per `pm-calibration-guide.md`.
4. Document findings as `docs/case-study-lore-weave.md` (referenced from README as planned).

---

## Alternative next steps

If LoreWeave mapping is not the right next move:

- **Phase 1 #3 (failure of sealing)** — short close-out debate; ceremony exit-ramp question.
- **Phase 1 #2 (two-tier sharpness)** — deeper internal debate; Law vs Principle distinction.
- **Phase 2 draft (Codex per Chapter)** — start defining Codex spec, including AI-assistant aide Chapters referenced from Phase 0 / Phase 1 anti-patterns.
- **IVP full Phase 2** — verify the 46 queued citations rigorously under v0.2 mandatory rules; re-run may surface new findings.
- **IVP Phase 3+** — Citation Appropriateness on the verified subset (likely catches stretched analogies like Goodhart's-Law-applied-to-recall), then Phases 4–7.

Recommended ordering if doing Phase work over LoreWeave: #3 (short) → #2 (deeper) → Phase 2 draft. Or just LoreWeave first.

---

## Conventions to preserve

- All documents in `docs/` use English; conversation language with the project owner is Vietnamese.
- Working drafts use the `*-for-debate.md` suffix; final docs drop the suffix.
- Specific arguments live in `docs/debates/NNN-topic.md` with status (open / recommended / decided / superseded).
- Each debate has a Decision section to be filled when the project owner decides — **never** pre-fill it.
- The README's "planned" links indicate forthcoming docs; they should not be made into broken-link claims.
- IVP separation-of-concerns: audit-output files (`docs/audit/`) and remediation edits go in *separate commits*; audit run never modifies framework documents in the same pass.
- IVP spec changes go *between passes*, never during a run; rubric tables are pre-registered per pass.

---

## How to resume

1. Read this file end-to-end.
2. Read `README.md` for the framework's elevator pitch.
3. Skim `docs/phase-0-for-debate.md` and `docs/phase-1-for-debate.md` — the two main artifacts.
4. Skim `docs/debates/README.md` for decision history (4 debates decided).
5. If touching evidentiary claims or calibration anchors: skim IVP spec v0.2 § 4 rubric and § 5 phase procedures before editing.
6. Confirm with project owner which path to take from "Recommended next step" or "Alternative next steps" before starting work.

---

## Repo state at end of Session 2

- Branch: `claude/read-handoff-status-53xfC` (per system instruction; not yet merged to `main`).
- All work pushed to `origin`. Five commits on this branch beyond the initial handoff:
  1. Add IVP spec + slash command (v0.1).
  2. IVP rodage Phases 1–2: inventory + 30-citation verification.
  3. Remediate IVP HIGH findings F-01 (Miller), F-02 (CMMI v3.0), F-03 (ISA 320).
  4. Remediate IVP MEDIUM and LOW findings F-04 through F-13.
  5. Refine IVP spec to v0.2 from rodage learnings.
- All 13 findings from the IVP 2026-05-08 rodage are remediated.
- 46 citations from Phase 1 inventory remain unverified — queued for full Phase 2.
- IVP Phases 3–7 not yet executed.
- No external dependencies, no build, no tests — this is a documentation repository.

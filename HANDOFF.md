# Session Handoff — 2026-05-08

> Snapshot of Dead Light Framework state at end of session. Read this first to resume work without re-deriving context.

---

## What this project is

**Dead Light Framework** — a software development governance methodology focused on human + AI agent collaboration. It composes on top of existing methodologies (Agile, Scrum, RUP, …) rather than replacing them. The distinctive idea: a frozen source of authority (the *Astronomican*) that no participant — human or agent — can rewrite at will.

Working tree: `C:\Works\_Researchs\dead-light-framework`
Reference / case-study codebase (not yet integrated): `C:\Works\_Researchs\lore-weave`

---

## Status: Phase 0 sealed; Phase 1 partially complete

| Artifact | Status |
|---|---|
| README — Manifesto + Map | Drafted |
| Glossary — for debate | Working draft (final glossary deferred — bottom-up from phases) |
| Phase 0 — The Reckoning | **Sealed** (all calibration questions resolved) |
| Phase 1 — The Astronomican | Partial — 3 of 7 known open questions resolved |
| Phase 2 — Codex per Chapter | Not started |
| Phase 3 — Heresy detection | Not started |
| Phase 4 — Re-consecration | Not started |
| LoreWeave case study application | **Not started — recommended next step** |

---

## Framework-wide policies established (apply to all future work)

These two policies were decided during the session and govern all subsequent framework authoring. **Do not violate them in future drafts.**

1. **40k vocabulary is naming and shared metaphor only.** Justification, structural arguments, and assessments of effectiveness must rest on real-world organizational systems with observable track records (constitutional federalism, religious institutions, military doctrine, established corporate practice, open-source governance, established software methodologies, …). When the 40k name and the real-world precedent diverge in implication, the real-world precedent governs the design.

2. **Industry standards over framework-invented formulas.** Calibration questions (thresholds, time budgets, team sizes, audit scopes, failure measurement) anchor to documented external practice — COCOMO II, CMMI PPB, ITIL, ISA 320, DORA, McCabe, etc. PM and Council retain authority to *select, calibrate, or override*, but the starting point is always documented external practice, never framework arithmetic.

---

## Decisions locked this session

| Debate | Decision |
|---|---|
| [001 — Laws Count Cap and Multi-Repo Scaling](docs/debates/001-laws-count-and-multirepo-scaling.md) | Adopt hierarchical Imperial + Sector Astronomicans with the inherit-and-add rule. Default = single Astronomican; split only when ≥ 2 repos, dedicated teams, cross-team contracts, and genuinely local decisions all exist. |
| [002 — Retrofit vs Greenfield](docs/debates/002-retrofit-vs-greenfield.md) | Introduce **Phase 0: Reckoning** as a prerequisite to Phase 1 for retrofit projects (greenfield runs lightweight or skips). Reckoning-first effective-date model with classification: Keep / Fix-now / Fix-by-date / Reconsider-Law. |
| [003 — Phase 0 Calibration](docs/debates/003-phase-0-calibration.md) | Significance heuristic (6 categorical bullets), Reckoning Team composition rule (≥1 active-IC mandatory, ≥1 tenure-spanning, ≥1 outside-scope), soft time budget with 80% / 100% escalation, lightweight greenfield Phase 0 (Assumption Surface + Commitment Audit + Stakeholder Map). |
| Six embedded answers from debate 002 | No Phase 0 sealing; smaller Reckoning Team produces; full attribution; no fixed grandfather cap; no fixed sunset horizon; PM-defined re-reckoning cadence. |
| Council composition multi-role | PM is a Council member. Council requires ≥ 3 distinct functional perspectives (minimum-diversity rule). Small-team accommodation: AI-assistant Chapters as aides (defer Codex specifics to Phase 2). |

---

## Document tree

```
dead-light-framework/
├── README.md                          ← Manifesto + Map (front door)
├── HANDOFF.md                         ← This file
├── LICENSE                            ← MIT
├── chat.txt                           ← Original chat history that motivated framework
└── docs/
    ├── glossary-for-debate.md         ← Working glossary (final assembled bottom-up later)
    ├── phase-0-for-debate.md          ← Phase 0: The Reckoning [SEALED]
    ├── phase-1-for-debate.md          ← Phase 1: The Astronomican [partial]
    ├── calibration-standards.md       ← Industry-standards reference catalog
    ├── pm-calibration-guide.md        ← Practical PM step-by-step at 3 rigor tiers
    └── debates/
        ├── README.md                  ← Debate index
        ├── 001-laws-count-and-multirepo-scaling.md   [decided]
        ├── 002-retrofit-vs-greenfield.md             [decided]
        └── 003-phase-0-calibration.md                [decided]
```

---

## Open questions still on the table

### Phase 1 — known open questions (from `phase-1-for-debate.md` Note on Method)

Severity HIGH:
- **#2 Two-tier sharpness** — when is something an Immutable Law vs a Guiding Principle? Content question affecting every Astronomican.
- **#3 Failure of sealing** — what happens when stress-test divergence > 20% on sealing day, or Council deadlocks? Without an exit ramp, real teams stall.

Severity MEDIUM:
- Council size lower bound — is 3 truly enough?
- Storage of seal mechanics — signed git tag vs multi-sig vs notarized hash.

Severity LOW:
- Pre-work questions — 5 sufficient or a 6th on agent boundaries?
- Session format — co-located vs distributed timezone.

### Glossary

Final glossary deferred — to be assembled bottom-up as later phases force real definitions. The 25 candidates and 11 needs-debate items are catalogued in `glossary-for-debate.md`.

---

## Recommended next step

**Map Phase 0 + Phase 1 against LoreWeave as a real test case.**

Why this is the right next step:
- LoreWeave is the framework's primary case study and the reason the framework exists. The user has signaled multiple scope changes occurred, making it the textbook retrofit case.
- Phase 0 + Phase 1 are now defined in enough detail to execute against real data.
- Running the framework on a real codebase will expose design weaknesses faster than further abstract debate.
- LoreWeave has 6 services in `contracts/api/` (identity, books, catalog, model-billing, model-registry, sharing) — also a candidate for the Sector Astronomican mechanism from debate 001.

How to start:
1. Read `C:\Works\_Researchs\lore-weave\docs\01_foundation\01_PROJECT_OVERVIEW.md` (already read once in this session — ~390 lines).
2. Skim `docs/02_governance/` and `docs/03_planning/` to identify scope changes and decisions.
3. Run a Tier 1 (startup) Phase 0 against LoreWeave per `pm-calibration-guide.md`.
4. Document findings as `docs/case-study-lore-weave.md` (referenced from README as planned).

---

## Alternative next steps

If LoreWeave mapping is not the right next move:

- **Phase 1 #2 (two-tier sharpness)** — close the Law vs Principle distinction. Internal design question, doesn't need case-study data.
- **Phase 1 #3 (failure of sealing)** — close the ceremony exit-ramp question. Short debate.
- **Phase 2 draft (Codex per Chapter)** — start defining Codex spec, including the AI-assistant aide Chapters referenced from Phase 0 / Phase 1 anti-patterns.

Recommended ordering if doing Phase work over LoreWeave: #3 (short close-out) → #2 (deeper) → Phase 2 draft. Or just LoreWeave first.

---

## Conventions to preserve

- All documents in `docs/` use English (audience is the framework, which is intended for sharing).
- Conversation language with the project owner is Vietnamese.
- Working drafts use the `*-for-debate.md` suffix; final docs drop the suffix.
- Specific arguments live in `docs/debates/NNN-topic.md` with status (open / recommended / decided / superseded).
- Each debate has a Decision section to be filled when the project owner decides — **never** pre-fill it.
- The README's "planned" links indicate forthcoming docs; they should not be made into broken-link claims.

---

## How to resume

1. Read this file end-to-end.
2. Read `README.md` for the framework's elevator pitch.
3. Skim `docs/phase-0-for-debate.md` and `docs/phase-1-for-debate.md` — these are the two main artifacts.
4. Skim `docs/debates/README.md` to see decision history.
5. Confirm with the project owner which path to take from "Recommended next step" or "Alternative next steps" before starting work.

---

## Repo state at handoff

- Branch: `main`
- Uncommitted changes: present (HANDOFF.md is new; many doc additions / edits in this session were not committed). Check `git status` to confirm.
- No external dependencies, no build, no tests — this is a documentation repository.

---

## Post-handoff updates — 2026-05-09 (Session 2)

### IVP audit infrastructure added

A formal audit workflow was specified and a rodage pass was executed against the framework.

- **`docs/audit/independent-verification-pass-for-debate.md`** — full IVP methodology spec: 7 phases (inventory → citation verification → citation appropriateness → argument analysis → internal consistency → external benchmarking → synthesis), pre-registered rubric, industry-pragmatic source tier hierarchy, anti-bias guardrails (symmetric search, mandatory audit trail, falsifiability test, separation of audit-from-authoring).
- **`.claude/commands/ivp.md`** — slash command `/ivp [scope]` to re-run IVP from the spec.
- **`docs/audit/inventory.md`** — Phase 1 output: 44 load-bearing claims, 76 distinct citations, 40 defined terms, 11 analogy invocations.
- **`docs/audit/findings-2026-05-08.md`** — Phase 2 partial output: 30 citations rigorously verified (17 VERIFIED, 11 PARTIAL, 1 CONTRADICTED, 0 UNVERIFIABLE); 3 HIGH, 4 MEDIUM, 6 LOW findings; 46 citations queued for full pass.

### HIGH findings remediated (this session)

| Finding | Action | Reflected in |
|---|---|---|
| F-01 — Miller's number cited as ~5±2; actual is 7±2 (CONTRADICTED) | Citation corrected; cap revised from `≤ 5` to `5–9 target ~7` (within Miller's range). | [debate 004](docs/debates/004-cap-revision-miller-correction.md); [debate 001](docs/debates/001-laws-count-and-multirepo-scaling.md) Miller line + Sector code block + Methodological note 2; [phase-1](docs/phase-1-for-debate.md) §3 Activities + §6 Failure Modes + §9 Sector |
| F-02 — CMMI v2.0 (2018) cited but v3.0 (2023) is current; v2.x retired June 2024 | Citations updated to CMMI Institute (ISACA) *CMMI Development V3.0* (2023). High-maturity practice areas (CAR, PPB, QPM) confirmed to persist in v3.0; capability levels 4 and 5 eliminated, high-maturity practices applied across CL 1–3. | [calibration-standards.md](docs/calibration-standards.md) §A row, §F rows, References list |
| F-03 — ISA 320 "5–10% of revenue/assets/expenses" misattributed | Re-framed as practitioner heuristic (per ISA 320.A8 examples + CEAOB / firm methodology surveys). ISA 320 itself prescribes professional judgement, not fixed percentages. | [calibration-standards.md](docs/calibration-standards.md) §A row |

MEDIUM and LOW findings (F-04 through F-13) are recorded in the findings file but **not** remediated this session — deferred until full IVP Phase 2 (which still has 46 citations queued for verification) is complete.

### Decisions locked since handoff

| Debate | Decision |
|---|---|
| [004 — Cap Revision: Miller Citation Correction](docs/debates/004-cap-revision-miller-correction.md) | Adopt 5–9 range with target ~7 (anchored on Miller 1956's actual 7 ± 2 working-memory range). Hard cap 9, soft target ~7, informal floor 5 (below permitted with Council review). Same caps apply to Imperial and Sector Astronomicans. Council size (3–7) and Reckoning Team size (2–5) are *not* affected — they anchor on Dunbar / Brooks for group dynamics, not Miller for item recall. |

### Document tree (added since handoff)

```
dead-light-framework/
├── .claude/
│   └── commands/
│       └── ivp.md                                                ← Slash command for IVP re-run
└── docs/
    ├── audit/
    │   ├── independent-verification-pass-for-debate.md           ← IVP methodology spec
    │   ├── inventory.md                                          ← Phase 1 inventory (added 2026-05-08)
    │   └── findings-2026-05-08.md                                ← Phase 2 partial findings
    └── debates/
        └── 004-cap-revision-miller-correction.md                 ← New decided debate
```

### Open questions in IVP methodology (to resolve before next pass)

Recorded in the spec § 9 and validated by the rodage:

- Symmetric (confirming + disconfirming) search should be **mandatory** for load-bearing claims, not "where applicable" — the rodage held this loosely.
- Source-tier ambiguity for AXELOS-style commercial-publisher quasi-standards (T1 vs T2) — needs clarification.
- Citation deduplication — same source cited in multiple files; spec should formalize "verify entity once; record locations."
- "Load-bearing" classification is itself a judgement; second-pass independent classification would help.

### MEDIUM and LOW findings remediated (same session, separate commit)

| Finding | Action | Reflected in |
|---|---|---|
| F-04 — PMBOK SPI/CPI 0.9/1.1 attributed too tightly to PMBOK | Re-framed as practitioner convention with PMBOK defining the indices, not the trigger values. Common bands documented (yellow 0.8–0.9 / 1.1–1.2; red <0.8 / >1.2). | [calibration-standards.md](docs/calibration-standards.md) §A row |
| F-05 — Sev1–Sev4 misattributed to ITIL (it is SRE vernacular) | Row re-titled "Incident severity tiers (Sev1–Sev4)" and re-attributed to industry SRE / incident-management practice (Etsy, Google SRE, Atlassian). Note added that ITIL 4 itself uses Priority via Impact × Urgency. | [calibration-standards.md](docs/calibration-standards.md) §A row |
| F-06 — Spolsky "correlate strongly" overclaims a statistical relationship | Re-phrased as anecdotal argument from the Netscape 4 → 6 case (per *"Things You Should Never Do, Part I"*, 2000), with explicit acknowledgement that this is anecdote, not statistics. | [debates/002](docs/debates/002-retrofit-vs-greenfield.md) "Refactoring discipline" row |
| F-07 — AWS LP "criticized inside Amazon" qualifier unsupported | Reworded to "widely critiqued — by external commentary and inside-Amazon-adjacent practitioners". Note that no public Amazon document formally acknowledges the critique. | [debates/001](docs/debates/001-laws-count-and-multirepo-scaling.md) Option A bullet |
| F-08 — Six Sigma originator attribution to Mikel Harry alone | Updated to "Bill Smith and Mikel Harry, Motorola" (Smith introduced Six Sigma in 1986; Harry developed MAIC and the 1.5σ shift). | [calibration-standards.md](docs/calibration-standards.md) §E row |
| F-09 — IEEE 1633-2016 cited as canonical source for MTBF/MTTR | Source column re-framed: MTBF/MTTR are general reliability-engineering metrics; IEEE 1633-2016 is software-reliability practice that operates on them, not their canonical originator. | [calibration-standards.md](docs/calibration-standards.md) §E row |
| F-10 — Two-pizza team year "~2002" | Updated to "late 1990s (Amazon management offsite); often cited around 2002 because that is when adjacent ideas were popularized." | [calibration-standards.md](docs/calibration-standards.md) §C row |
| F-11 — Maintainability Index <65 threshold without scale | Distinguished original Coleman et al. unnormalized formula (range 0–171; <65 hard-to-maintain, <85 moderate) from Visual Studio normalized 0–100 (0–9 difficult, 10–19 moderate, 20–100 highly maintainable). Reader must state which scale before quoting a threshold. Citation upgraded to include Oman & Hagemeister (1992) ICSM origin alongside Coleman et al. (1994) refinement. | [calibration-standards.md](docs/calibration-standards.md) §D row |
| F-12 — Catholic Church 1.3B membership figure | Updated to ~1.4B (1.422B at end of 2024 per *Annuario Pontificio* 2026). Doctrinal-coherence claim qualified to acknowledge the Great Schism (1054) and Reformation (1517); Roman Catholic legal-doctrinal continuity itself remains uninterrupted. | [debates/001](docs/debates/001-laws-count-and-multirepo-scaling.md) Catholic row |
| F-13 — ITIL 4 (2019) edition currency note | Source column adds: ITIL 5 Foundation launched February 2026; ITIL 4 modules sunset 31 December 2027. Both editions are valid for the calibration purpose. | [calibration-standards.md](docs/calibration-standards.md) §A row + References list |

### Repo state at end of Session 2

- Branch: `claude/read-handoff-status-53xfC` (per system instruction; not yet merged to `main`).
- All changes committed; pushed to `origin`. Three commits on this branch beyond the initial handoff: (1) IVP spec + slash command, (2) IVP rodage (inventory + Phase 2 partial findings), (3) HIGH remediation (F-01, F-02, F-03), (4) MEDIUM/LOW remediation (F-04 through F-13).
- F-01 through F-13 — all 13 findings from the rodage report — remediated.
- 46 citations from Phase 1 inventory remain unverified — queued for a full Phase 2 in a future IVP run.
- IVP Phases 3–7 (citation appropriateness, argument analysis, internal consistency, external benchmarking, synthesis) — not yet executed.
- IVP spec § 9 open methodology issues — open; to revisit before next IVP cycle.

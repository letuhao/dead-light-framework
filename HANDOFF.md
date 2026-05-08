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

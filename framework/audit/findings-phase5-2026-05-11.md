# IVP Findings — Phase 5 (Internal Consistency) — 2026-05-11

> **Status:** Phase 5 only. This run executes **Phase 5 (Internal Consistency — term drift, decision-to-doc reflection, quantitative consistency, policy compliance, README link integrity)** against the post-Session-3 framework text. Phases 6–7 remain queued.
>
> **Auditor:** Claude Code (Opus 4.7), single pass.
> **Mode:** Industry-pragmatic (per IVP spec v0.3 § 1).
> **Branch:** none — per Session-3 lesson (HANDOFF § Conventions), this small docs-only repo runs Phase 5 directly on `main` with separation enforced at the *commit* level (audit-output commit precedes remediation commit; remediation is a follow-up after project-owner review).
> **Inputs:** All `docs/**/*.md` (excluding `framework/audit/*` per IVP § Scope — audit-output files are themselves audit history, not framework artifacts), plus `README.md` and `HANDOFF.md`. Cross-reference: 4 decided debates in `framework/debates/`, 40 defined terms + 76 citations from [`inventory.md`](inventory.md) as a pointer-list.
> **Spec applied:** [`independent-verification-pass-for-debate.md`](independent-verification-pass-for-debate.md) v0.3 § 5 Phase 5 procedure + § 4.1 severity rubric.
> **Rubric integrity:** Pre-registered v0.3 § 4.1 severity scale used unmodified.
> **Methodological note from IVP v0.3 § 5 Phase 3 pre-step applied:** Phase 5 evaluates against **current source files**, treating `inventory.md` as a pointer-list only. Inventory paraphrases that lag remediation are noted separately (§ 8) but not counted as findings against the framework.

---

## 1. Executive verdict

Phase 5 checks the framework's internal consistency across five axes. Within the axes Phase 5 checks, the framework is **substantially consistent** after three sessions of remediation; no CRITICAL or HIGH findings surfaced. Eight findings are surfaced across the four MEDIUM/LOW remediation classes — all are localized text edits, none threatens a sealed decision or framework structure.

**Headline result:** the design-level decisions from debates 001–004 are correctly reflected in the phase docs **at the prescriptive level** (caps, ranges, composition rules, classifications). The drift is concentrated in **meta-commentary sections** (phase-1 § Note on Method, phase-0 § 2 Inputs, calibration-standards § C) where late-session remediation didn't propagate into prose that paraphrased the older numbers. HANDOFF.md's "open questions" list also drifted from phase-1's actual open-questions list.

**Eight new findings:**
- **F-32 (MEDIUM)** — `phase-1-for-debate.md:299` Note on Method still reads "5 Laws max", contradicting debate 004's cap of 9 (target ~7) applied at §3, §6, §9.
- **F-33 (MEDIUM)** — `calibration-standards.md:76` "Justifies cap of 5–7 for Reckoning Team and Council" contradicts spec (Reckoning Team 2–5; Council 3–7).
- **F-34 (MEDIUM)** — `calibration-standards.md:78` "Reckoning Team and Council both sit at layer 1 (≤5)" — Council 3–7 exceeds Dunbar layer 1; anchor claim is over-strong.
- **F-35 (MEDIUM)** — `phase-0-for-debate.md:34` "Time budget — soft or hard horizon" contradicts phase-0:211 (Open questions resolved: "Soft target with 80% / 100% structured escalation") per debate 003 Q3.
- **F-36 (LOW)** — `phase-1-for-debate.md:309` still lists "First-time vs retrofit" as an outstanding open question; debate 002 effectively answered this by introducing Phase 0 + retrofit additions in §10.
- **F-37 (LOW)** — `HANDOFF.md:108` lists "#2 Two-tier sharpness" as a phase-1 open question claimed to be "from phase-1-for-debate.md Note on Method"; this question is not present in phase-1's actual open-questions list (§303–310).
- **F-38 (LOW)** — `framework/debates/001-laws-count-and-multirepo-scaling.md:7` metadata "Affects: …'≤ 5 Immutable Laws' and '≤ 5 Guiding Principles' caps." is retrospective; debate 004 raised the cap to 9. A "subsequently revised by debate 004" annotation would prevent reader confusion.
- **F-39 (LOW)** — Three framework-internal heuristics in quality gates lack explicit external anchors (phase-1:75 "at least three explicit items in Boundaries"; phase-1:76 "≥ 5 scenarios" stress-test minimum; pm-calibration-guide:46 "> 5 person-days of rework"). All three are bounded minima or explicitly hedged starting anchors; under a strict v0.3 § 4.1 argument-warrant tier-floor reading they could be argued MEDIUM, but the hedging is faithfully recorded in the framework text.

All eight are remediation candidates of the same low-cost "edit a sentence or add an annotation" class. None changes the framework's structural design or a sealed decision.

**Combined cross-phase totals (Phases 2 + 3 + 4 + 5):**
- Phase 2: 76 citations have verdicts (50 V + 24 P + 2 C → both C remediated).
- Phase 3: 73 citations carried (70 APPROPRIATE + 3 STRETCHED, 1 retracted in erratum).
- Phase 4: 41 LB claims + 4 debates (35 SOUND + 4 WEAK-WARRANT + 2 UNFALSIFIABLE-conventional + 0 FALLACIOUS).
- Phase 5: 40 defined terms × cross-file consistency + 4 decided debates × reflection + ~20 numeric thresholds × cross-doc consistency + 2 framework-wide policies × every justification + README link integrity.
- **Total findings across phases (cumulative): 39 (0 CRITICAL · 6 HIGH · 12 MEDIUM · 20 LOW · 1 retracted via erratum = 38 of practical effect, of which 30 are remediated and 8 are new in Phase 5).**

---

## 2. Aggregate stats

| Category | Count |
|---|---|
| Defined terms evaluated for drift | 40 (T-001 to T-040) |
| Multi-file terms with cross-file drift | 1 (T-036 Time budget — F-35) |
| Decided debates checked for reflection | 4 (001–004) |
| Decisions with partial-reflection gaps | 1 (debate 004 — phase-1:299 stale; F-32) |
| Numeric thresholds cross-checked | ~20 (Laws/Principles cap, Council size, Reckoning Team size, divergence threshold, audit budgets, M&A KLOC, COCOMO constants, McCabe thresholds, Brooks formula, etc.) |
| Numeric inconsistencies surfaced | 3 (F-32, F-33, F-34) |
| Justification segments checked against policy 1 (40k naming) | All 11 inventoried analogies + README/glossary/phase docs |
| Policy 1 violations | 0 — policy-1 PASSES (confirms Phase 3 result on R-001) |
| Justification segments checked against policy 2 (industry standards) | Every quantitative claim + every quality gate |
| Policy 2 edge cases (LOW) | 3 small heuristics in F-39 |
| README link integrity issues | 0 — all 4 "planned" links properly tagged; LICENSE / debate / audit links resolve |
| Findings — severity CRITICAL | 0 |
| Findings — severity HIGH | 0 |
| Findings — severity MEDIUM | 4 (F-32, F-33, F-34, F-35) |
| Findings — severity LOW | 4 (F-36, F-37, F-38, F-39) |

---

## 3. Sub-check 1 — Term drift across defined terms

**Procedure.** For each defined term T-001 through T-040 from inventory § C, located every non-defining occurrence via Grep, read the surrounding context in current source files, and compared the in-context use against the definition. Single-file terms (no cross-file occurrence) are no-ops by construction. Cross-file term-uses are listed below with verdicts.

**Result.** 40 terms checked. 39 consistent across all occurrences. **1 term drifts** (T-036 Time budget).

### Detailed pass

| Term | Locations checked | Verdict |
|---|---|---|
| T-001 Astronomican | README:56, glossary:33, phase-1 throughout, debate 001 throughout | **Consistent.** All occurrences refer to the sealed document of Purpose / Immutable Laws / Guiding Principles / Boundaries. |
| T-002 Immutable Law | glossary:34, phase-1:43, 88, 218 | **Consistent.** Top-tier hard commitment; consistent across glossary and phase-1. |
| T-003 Guiding Principle | glossary:35, phase-1:44, 220 | **Consistent.** Interpretable second tier; consistent. |
| T-004 The Purpose | glossary:36, phase-1:42, 72, 87 | **Consistent.** One-sentence north star; consistent. |
| T-005 The Boundaries | glossary:37, phase-1:45, 60, 93 | **Consistent.** "What the project is NOT" definition stable across both files. |
| T-006 The Ascension Council | README:57, glossary:43, phase-1:18, 111–148, phase-0:144–146 | **Consistent-with-scope-expansion.** Definition stable as "one-time meeting that seals the Astronomican before kickoff and disbands after sealing." Phase-0:146 notes the Council is *assembled* before Phase 0 begins (earlier than Phase 1) in retrofit — which is consistent with "before kickoff" since Phase 0 is itself before kickoff. No drift, just retrofit-specific assembly timing. |
| T-007 The Sealing | glossary:44, phase-1:47 | **Consistent.** Glossary flags it as "needs-debate (possibly redundant with Ascension Council)"; phase-1 uses it as the ceremony's terminal event. Consistent. |
| T-008 Re-consecration | README:73 (planned link), glossary:45, phase-1:60, 179 | **Consistent.** "Process to amend a sealed Astronomican" across all locations. |
| T-009 High Lord | README:58, glossary:51, phase-1:145 | **Consistent.** "Interpretation authority over the Astronomican" in all three. |
| T-010 Planetary Governor | README:59, glossary:52, phase-1:147 | **Consistent.** "Human leading a module, applies Astronomican locally." |
| T-011 Inquisitor | glossary:53 | Single-file (glossary only) — no drift possible. |
| T-012 Chapter | README:60, glossary:59, phase-0:138, phase-1:107, 132 | **Consistent.** "A class/type of agent governed by its own Codex" — including the phase-0/phase-1 use of "AI-assistant Chapters as aides" which is a *role* Chapters can serve, not a redefinition. |
| T-013 Codex | README:60, glossary:60, phase-0:138, phase-1 throughout | **Consistent.** "Document defining a Chapter's bounds, hard stops, autonomy threshold, output contract." |
| T-014 Operational Bounds | glossary:61 | Single-file — no drift. |
| T-015 Hard Stop | glossary:62 | Single-file — no drift. |
| T-016 Autonomy Threshold | glossary:63 | Single-file — no drift. |
| T-017 Tithe | glossary:64 | Single-file (glossary only, flagged "needs-debate" for 40k flavor) — no drift. |
| T-018 Battle Brother | glossary:65 | Single-file — no drift. |
| T-019 The Chaos | README:61, glossary:71 | **Consistent.** Umbrella term for failure modes; consistent. |
| T-020 Heresy | README:73, glossary:72, phase-1:71 (Heresy detection) | **Consistent.** "Specific deviation from the Astronomican" used identically. |
| T-021 Corruption | glossary:73 | Single-file (flagged needs-debate) — no drift. |
| T-022 Schism | glossary:74 | Single-file (flagged needs-debate) — no drift. |
| T-023 Heresy Detection | README:73, glossary:80, phase-1:71 | **Consistent.** Sensors/processes flagging drift; consistent in all three. |
| T-024 Astropathic Signal | glossary:81 | Single-file (flagged needs-debate) — no drift. |
| T-025 Astronomican Reading | glossary:82 | Single-file (flagged needs-debate) — no drift. |
| T-026 Reckoning Team | phase-0:23–27, throughout phase-0, phase-1:211 | **Consistent.** "2–5 people meeting composition rule" with three sub-rules across all locations. |
| T-027 Reckoning Record | phase-0:78–96, phase-1:202, 228, 256 | **Consistent.** Four-section draft in phase-0 + fifth section added by phase-1 Reckoning step; living document. Phase-1 wording matches. |
| T-028 Imperial Astronomican | phase-1:167, debate 001:78 | **Consistent.** Same structure; binds every Sector; sealed first. |
| T-029 Sector Astronomican | phase-1:174–180, debate 001:84–92 | **Consistent.** Inherits all Imperial Laws; can only tighten, not relax. Same caps (≤ 9 local, target ~7) in both. |
| T-030 Reckoning step | phase-1:215, debate 002:71 | **Consistent.** Inserted between Boundaries and Stress Test; classifies past decisions. |
| T-031 Migration Plan | phase-1:229, debate 002:81 | **Consistent.** Extraction of Fix-now and Fix-by-date items as actionable backlog with named owners and explicit dates. |
| T-032 Keep / Fix-now / Fix-by-date / Reconsider-Law | phase-1:218–221, debate 002:73–75 | **Consistent.** Four classification buckets defined identically. |
| T-033 Aide (AI-assistant Chapter as aide) | phase-0:138, phase-1:107, 132 | **Consistent.** All three locations say aides surface analysis / stress-test / arguments; do not vote; do not sign. Note: stylistic variation ("AI-assistant Chapters" hyphenated in phase-0:138 vs "AI assistants — invoked as specific Chapters" descriptive in phase-1:107/132). Not a substantive drift; flagged only for stylistic hygiene below. |
| T-034 Significance threshold | phase-0:31, pm-calibration-guide:38, debate 003 Q1 | **Consistent.** "Threshold for entry into Past Decisions Catalog" across all three; categorical heuristic 6 bullets in pm-guide §1 matches debate 003 resolution. |
| T-035 Materiality threshold | phase-0:32, pm-calibration-guide:84, debate 003 | **Consistent.** "Threshold for entry into Failure Inventory" across all three. |
| T-036 Time budget (Phase 0) | phase-0:34, pm-calibration-guide:160, debate 003 Q3, phase-0:211 (Open questions resolved) | **DRIFTS.** phase-0:34 still says "soft or hard horizon for Phase 0 completion"; phase-0:211 and debate 003 Q3 say "Soft target with 80% / 100% structured escalation" (rejecting both pure hard-stop and pure unbounded). Internal contradiction within phase-0. → **Finding F-35 (MEDIUM)**. |
| T-037 Re-reckoning cadence | phase-0:156, pm-calibration-guide:215, debate 002 Q6 | **Consistent.** "PM-defined cadence, committed in writing inside the Reckoning Record itself." |
| T-038 Reckoning Team composition rule | phase-0:23–27, debate 003 Q2 | **Consistent.** 2–5 people, ≥1 active-IC mandatory, ≥1 tenure-spanning when permits, ≥1 outside-scope when permits. |
| T-039 Stress Test Log | phase-1:64 | Single-file — no drift. |
| T-040 Codex Slot Placeholders | phase-1:65 | Single-file — no drift. |

**Hygiene note (not a finding):** T-033 has a stylistic split between "AI-assistant Chapters" (phase-0:138, hyphenated noun phrase) and "AI assistants — invoked as specific Chapters with explicit Codex" (phase-1:107, 132 — descriptive). Substantively identical; future drafts might consolidate phrasing for readability.

---

## 4. Sub-check 2 — Decision-to-doc reflection

**Procedure.** For each `decided` debate (001–004), the full Decision section was read; each decision element was then traced into the relevant phase doc(s) to confirm the element is reflected at the prescriptive level. Missing reflections are surfaced as findings. HANDOFF.md was also checked as a session-state document claiming to reflect phase-1's open questions verbatim.

**Result.** 4/4 debates checked. 3/4 fully reflected; 1/4 (debate 004) has one stale paraphrase. HANDOFF.md drifts from phase-1's actual open-questions list.

### Debate 001 — Hierarchical Imperial + Sector

**Decision (HANDOFF §44):** Hierarchical Imperial + Sector Astronomicans with inherit-and-add rule. Default = single Astronomican; split only when 4 trigger conditions are all true.

| Decision element | Reflected in | Verdict |
|---|---|---|
| Two-tier Imperial + Sector structure | phase-1 §9 (Scaling) — Imperial + Sector subsections | **Reflected** |
| Sectors inherit and add — never relax | phase-1:175 "Inherits all Imperial Laws — they cannot be relaxed, only tightened" | **Reflected** |
| Default single Astronomican; 4 trigger conditions to split | phase-1:158–164 — 4 conditions listed verbatim | **Reflected** |
| Imperial Phase 1 before any Sector Phase 1 | phase-1:183 "Imperial Phase 1 must complete before any Sector Phase 1 begins" | **Reflected** |
| Anti-survivorship-bias selection-criteria note (F-30 remediation) | debate 001:75 — paragraph added | **Reflected** |

**Debate 001: Fully reflected.**

### Debate 002 — Retrofit vs Greenfield (Phase 0 introduction)

**Decision (HANDOFF §45):** Introduce Phase 0: Reckoning as prerequisite to Phase 1 for retrofit; greenfield runs lightweight or skips. Reckoning-first effective-date model with Keep/Fix-now/Fix-by-date/Reconsider-Law classification.

| Decision element | Reflected in | Verdict |
|---|---|---|
| Phase 0 as prerequisite for retrofit | phase-0 entire file; phase-1 §10.1 | **Reflected** |
| Phase 0 lightweight / skip for greenfield | phase-0 § "Open questions — resolved" Q4; pm-calibration-guide § Greenfield lightweight Phase 0 | **Reflected** |
| Reckoning step (Keep / Fix-now / Fix-by-date / Reconsider-Law) | phase-1 §10.2; debate 002 Decision section | **Reflected** |
| Six embedded answers (no Phase 0 sealing; smaller Reckoning Team produces, Council reviews; full attribution; no fixed cap; no fixed sunset; PM-defined cadence) | phase-0 § "Note on Method" + § 7 + § 8; phase-1 §10.7 | **Reflected** |
| Mechanism-based warrant for retrofit precedents (TRC's "explicit past-violations machinery" — F-31 remediation) | debate 002:49; phase-1:293 | **Reflected** |

**Debate 002: Fully reflected.**

### Debate 003 — Phase 0 Calibration

**Decision (HANDOFF §46):** Significance heuristic (6 categorical bullets); Reckoning Team composition rule; soft time budget with 80%/100% escalation; lightweight greenfield Phase 0.

| Decision element | Reflected in | Verdict |
|---|---|---|
| Q1 Significance heuristic (6 categorical bullets) | phase-0 § "Open questions — resolved"; pm-calibration-guide § 1 Tier 1 | **Reflected** |
| Q2 Reckoning Team composition rule | phase-0:23–27; phase-0 § "Open questions — resolved" | **Reflected** |
| Q3 Soft target with 80%/100% escalation | phase-0 § "Open questions — resolved" Q3 (line 211); pm-calibration-guide § 4 Time-boxing escalation | **Partially reflected.** phase-0:34 (Inputs/Prerequisites) still says "Time budget — soft or hard horizon"; the resolution baked in at phase-0:211 is "Soft target with 80%/100% structured escalation". phase-0:34 should be updated. → **F-35 (MEDIUM)**. |
| Q4 Lightweight greenfield Phase 0 (Assumption Surface + Commitment Audit + Stakeholder Map) | pm-calibration-guide § Greenfield lightweight Phase 0; phase-0 § "Open questions — resolved" Q4 | **Reflected** |
| Framework-wide policy: industry standards over framework-invented formulas | calibration-standards.md § Principle; phase-0:30 reference; pm-calibration-guide intro | **Reflected** |

**Debate 003: Reflected except for the time-budget-input-section staleness already captured under F-35.**

### Debate 004 — Cap Revision: Miller Citation Correction

**Decision:** Hard cap 9; soft target ~7; below 5 permitted with review. Citation now reads Miller 7±2. Same caps apply to Guiding Principles.

| Decision element | Reflected in | Verdict |
|---|---|---|
| phase-1 §3 cap — "Maximum 9 Immutable Laws (target ~7)" | phase-1:43 | **Reflected** |
| phase-1 §3 cap for Principles — same | phase-1:44 | **Reflected** |
| phase-1 §6 failure mode "More than 9 Laws or 9 Principles" | phase-1:90 | **Reflected** |
| phase-1 §9 Sector cap "Adds up to 9 local Laws and 9 local Principles (target ~7)" | phase-1:176 | **Reflected** |
| debate 001 §32 — "Miller's working-memory range, ~7 ± 2" | debate 001:32 | **Reflected** |
| debate 001 Sector code block — "≤ 9 Imperial Laws (target ~7)" | debate 001:81–89 | **Reflected** |
| phase-1 § Note on Method specificity claim — "5 Laws max" | phase-1:299 | **STALE.** This Note-on-Method sentence enumerates the framework's specific commitments and still says "5 Laws max, 7 Council members max, 20% divergence threshold, 1–2 day session". The "5 Laws max" is now wrong — should be "9 Laws max (target ~7)". Late-session remediation didn't propagate into this paraphrasing sentence. → **F-32 (MEDIUM)**. |

**Debate 004: Reflected at all prescriptive sites; stale paraphrase in phase-1 § Note on Method only.**

### Open questions reflection — phase-1 Note on Method vs HANDOFF

**Procedure.** HANDOFF.md § "Open questions still on the table" claims to enumerate phase-1's open questions "from `phase-1-for-debate.md` Note on Method". Compared HANDOFF list against phase-1:303–310.

| HANDOFF item | Found in phase-1:303–310? | Verdict |
|---|---|---|
| #2 Two-tier sharpness (Law vs Principle distinction) | **Not present** | HANDOFF lists this as a HIGH-severity open question claimed to come from phase-1 Note on Method, but phase-1's actual outstanding-open-questions list (§303–310) does not contain it. → **F-37 (LOW)**. |
| #3 Failure of sealing | phase-1:310 | Present in both. ✓ |
| Council size lower bound | phase-1:305 | Present in both. ✓ |
| Storage of seal | phase-1:308 | Present in both. ✓ |
| Pre-work questions (5 vs 6th) | phase-1:306 | Present in both. ✓ |
| Session format | phase-1:307 | Present in both. ✓ |
| (Not in HANDOFF) First-time vs retrofit | phase-1:309 | phase-1 still lists this as an open question, but debate 002 effectively answered it by introducing Phase 0 + retrofit additions in phase-1 §10. Stale. → **F-36 (LOW)**. |
| (Not in HANDOFF) Cap-count question | Removed | HANDOFF explicitly notes "the cap-count question, originally listed here, was closed by debate 004." ✓ |

### Debate 001 metadata line

**Procedure.** Read all four debate front-matter blocks for stale references to the older "≤ 5" cap value.

| Location | Wording | Verdict |
|---|---|---|
| debate 001:7 "Affects: phase-1, specifically the '≤ 5 Immutable Laws' and '≤ 5 Guiding Principles' caps." | Retrospectively accurate (this was debate 001's scope when written) but the cap has since been raised to 9 via debate 004 | LOW hygiene. A "subsequently revised by debate 004" annotation would prevent reader confusion. → **F-38 (LOW)**. |

---

## 5. Sub-check 3 — Quantitative consistency

**Procedure.** Every numeric threshold (sizes, percentages, durations, ranges) was located via Grep across all in-scope docs and cross-checked. Where two or more docs state a value for the same defined quantity, agreement is required. Where docs differ, the prescriptive spec (phase-0 / phase-1) is treated as authoritative; calibration-standards.md is treated as reference; HANDOFF as session-state.

**Result.** ~20 thresholds checked. 17 fully consistent. 3 inconsistencies surfaced.

### Threshold pass

| # | Threshold | Locations & values | Verdict |
|---|---|---|---|
| 1 | Cap on Immutable Laws / Guiding Principles | phase-1:43 (Hard cap 9; target ~7); phase-1:44 (same for Principles); phase-1:90 (more than 9 = failure mode); phase-1:176 (Sector: ≤ 9 local, target ~7); debate 001:81–89 (Sector code block ≤ 9, target ~7); debate 004 throughout; phase-1:299 (**still says "5 Laws max"** — stale) | **DRIFTS** at phase-1:299. → **F-32 (MEDIUM)**. |
| 2 | Council size | phase-1:20 (3–7); phase-1:128 (3–7); phase-1:105 (>7 fails Dunbar threshold); debate 004:54 (3–7); HANDOFF §48 (3–7); calibration-standards.md:76 ("cap of 5–7" — drifts); calibration-standards.md:78 ("layer 1 ≤5" — drifts) | **DRIFTS** in calibration-standards twice. → **F-33** (line 76) **and F-34** (line 78), both MEDIUM. |
| 3 | Reckoning Team size | phase-0:23 (2–5); phase-1:211 (2–5); debate 003:53 (2–5); debate 004:55 (2–5); calibration-standards.md:76 ("cap of 5–7" — drifts) | **DRIFTS** in calibration-standards. Covered under F-33. |
| 4 | Stress-test divergence threshold | phase-1:76 (< 20% with Cohen κ anchor); phase-1:92 (> 20% fail mode); debate 004:125 (stays < 20%); phase-1:299 (20% in paraphrase) | **Consistent at 20%.** ✓ |
| 5 | Stress-test scenario count minimum | phase-1:46 (5–10); phase-1:76 (≥ 5) | Consistent within phase-1. The "5" itself is unanchored to industry; companion to anchored 20% threshold — see F-39 (LOW). |
| 6 | Phase 0 retrofit audit budget | calibration-standards.md:42 (5–15% of original COCOMO-derived effort); pm-calibration-guide:183 (5–15% based on rot severity); debate 003 Q3 (anchored on COCOMO II) | **Consistent.** ✓ |
| 7 | Phase 0 greenfield lightweight budget | calibration-standards.md:42 (1–2% of projected effort); pm-calibration-guide:239 (1–2% via COCOMO II planning mode); phase-0:212 (Tier 2 simplified COCOMO II); debate 003:133 (1–3 days or 1–2%) | **Consistent.** ✓ |
| 8 | M&A IT due-diligence rule | calibration-standards.md:59 (1 person-week per 10–50 KLOC); pm-calibration-guide:167 (tiered table: 50 / 20 / 10 KLOC per person-week) | **Consistent.** ✓ |
| 9 | 80%/100% timeboxing escalation | debate 003 Q3 (80% check / 100% structured choice); pm-calibration-guide § 4 Time-boxing escalation; phase-0:211 (Open questions resolved) | **Consistent.** ✓ |
| 10 | "More than 9 Laws or 9 Principles" as failure mode | phase-1:90 | Consistent with cap. ✓ |
| 11 | AWS Leadership Principles count | debate 001:36 (16, originally 14 + 2 added 2021); debate 004:57 (16 as outer bound) | **Consistent.** ✓ |
| 12 | Catholic Church membership | debate 001:69 (1.422 billion at end of 2024, citing *Annuario Pontificio* 2026) | Single current authoritative source. Inventory R-007 says "~1.3 billion" — paraphrase staleness, not a framework drift; see § 8 note. ✓ |
| 13 | Brooks's communication channels | calibration-standards.md:76 (N=5 → 10 channels; N=7 → 21 channels); formula N(N−1)/2 verified | **Consistent.** ✓ |
| 14 | COCOMO II constants | calibration-standards.md:38–41 (A ≈ 2.94; B ≈ 0.91; E in 1.05–1.20) | Single source; no drift. ✓ |
| 15 | McCabe Cyclomatic Complexity thresholds | calibration-standards.md:90 (<10 simple; 10–20 moderate; >20 complex; >50 untestable) | Single source. ✓ |
| 16 | Maintainability Index threshold | calibration-standards.md:92 (now clarified: <65 hard-to-maintain on original Coleman 0–171 scale; Visual Studio 0–100 normalized has 0–9 difficult, 10–19 moderate, 20–100 highly maintainable) | Properly hedged with both scales. ✓ |
| 17 | Six Sigma DPMO | calibration-standards.md:109 (3.4 DPMO) | Single source. ✓ |
| 18 | Phase 0 internal timing | phase-0:44 (Reckoning Team kick-off half-day); phase-0:60 (Aggregation 1–2 days); phase-0:66 (Council review half-day to one day) | **Consistent.** ✓ |
| 19 | Phase 1 session length | phase-1:39 (1–2 days intensive); phase-1:299 (1–2 day session in paraphrase) | **Consistent.** ✓ |
| 20 | Council minimum-diversity rule | phase-1:126 (at least three distinct functional perspectives); debate 003 anchor on uniform-team risk | **Consistent.** ✓ |

### Quantitative inconsistency details

#### F-32 — phase-1:299 stale "5 Laws max"

- **Where:** `framework/phases/phase-1-for-debate.md:299` ("This draft is intentionally specific — it commits to numbers (**5 Laws max**, 7 Council members max, 20% divergence threshold, 1–2 day session)…").
- **Why this drifts:** debate 004 raised the cap to 9 (target ~7) and applied consequential edits at phase-1 §3, §6, §9. The Note-on-Method sentence at line 299 paraphrases the framework's specific commitments and was missed during the debate-004 propagation.
- **Severity:** **MEDIUM.** Per IVP § 4.1 rubric: "terminology drift between drafts" is MEDIUM; this is also a cross-doc inconsistency since debate 004 explicitly enumerates the consequential edits and this paraphrase is not in that list.
- **Recommended remediation:** edit phase-1:299 from "5 Laws max" → "9 Laws max (target ~7)".

#### F-33 — calibration-standards.md:76 "cap of 5–7 for Reckoning Team and Council"

- **Where:** `framework/calibration-standards.md:76` ("Brooks's Law… At N=5: 10 channels. At N=7: 21 channels. **Justifies cap of 5–7 for Reckoning Team and Council.**").
- **Why this drifts:** the framework's authoritative sizes per phase-0:23 and phase-1:128 (re-confirmed by debate 004:54–55) are **Reckoning Team 2–5** and **Council 3–7**. The "5–7 for both" claim is wrong on both: too high for Reckoning Team (which goes down to 2), too narrow for Council (which goes down to 3).
- **Severity:** **MEDIUM.** Cross-doc numeric inconsistency on a sealed range used for governance composition rules.
- **Recommended remediation:** rephrase to something like: "Justifies the framework's small-group sizes — Reckoning Team 2–5 and Council 3–7 — by bounding communication overhead: at N=7 (Council upper bound) channels reach 21, and beyond that the Dunbar layer-1 / Brooks regime no longer holds."

#### F-34 — calibration-standards.md:78 "layer 1 (≤5)" applied to Council

- **Where:** `framework/calibration-standards.md:78` ("Dunbar's number — layered model. 5 / 15 / 50 / 150 / 500 / 1500 cognitive layers. **Reckoning Team and Council both sit at layer 1 (≤5)** for tight decision groups.").
- **Why this drifts:** Council is 3–7, partially exceeding Dunbar layer 1 (≤5). debate 004:54 carefully hedges this — "Council size 3–7 (anchored on Brooks 1975 communication channels + Dunbar layer 1 (≤ 5 intimate))" — i.e., layer 1 is *one* anchor among two, not a strict cap. The calibration-standards.md wording overclaims: it asserts Council "sits at" layer 1, which is false for the upper half of 3–7.
- **Severity:** **MEDIUM.** Two consequences: (a) the anchor is partially mis-applied (Dunbar layer 1 supports 2–5, not 6–7); (b) the wording implies stronger external support than the source actually provides for the upper half of Council size — a policy-2 hedge that's already correct in debate 004 needs to propagate to calibration-standards.
- **Recommended remediation:** rephrase to match debate 004:54's hedge — "Reckoning Team (2–5) sits squarely at Dunbar layer 1; Council (3–7) extends slightly beyond layer 1 into the lower edge of layer 2, accommodating the functional-diversity rule. Brooks's N(N−1)/2 explains why the framework does not push Council size into layer-2 territory."

---

## 6. Sub-check 4 — Policy compliance

**Procedure.** Every justification segment (footnotes, "Why this works" sections, debate rationales, "anchored on…" attributions, calibration-standards anchor columns) was re-checked against the two framework-wide policies stated at HANDOFF §32:

- **Policy 1.** 40k vocabulary is naming and shared metaphor only; justification must rest on real-world precedent.
- **Policy 2.** Industry standards over framework-invented formulas (extended in IVP v0.3 § 4.1 to argument-warrants: load-bearing argument resting solely on framework-internal reasoning is at minimum MEDIUM).

### Policy 1 — 40k naming-only

| Inventoried analogy | Location | Verdict |
|---|---|---|
| A-001 epigraph "Emperor is dead. Light remains." | README:3 | Naming / flavor (epigraph). PASS. |
| A-002 Astronomican = "beacon that still shines after its god-emperor has all but died" | README:36 | **Explicitly framed** as "we use the metaphor because it names something real — *authority detached from any living agent*." Naming, not justification. PASS. |
| A-003 Astronomican / Council / High Lords / Governors / Chapters / Codex / Chaos | README:56–61 | Naming. PASS. |
| A-004 Acknowledgment to Games Workshop | README:91 | Disclaimer. PASS. |
| A-005 Tithe | glossary:64 | Needs-debate flag; only in glossary; no use as justification. PASS. |
| A-006 Battle Brother | glossary:65 | Same. PASS. |
| A-007 Astropathic Signal | glossary:81 | Same. PASS. |
| A-008 Imperial / Sector Astronomican | phase-1:167–179 | Naming. **debate 001 § Methodological Note explicitly removed prior 40k justification** for this concept. PASS. |
| A-009 Methodological note (40k justification removal) | debate 001:191–198 | Self-correcting anti-policy-1 safeguard. PASS. |
| A-010 AI-assistant Chapters with Codex as aides | phase-0:138 | Naming. PASS. |
| A-011 Heresy / Inquisitor / Schism / Corruption in glossary | multiple | Naming-only with needs-debate flags. PASS. |

**Policy 1: PASSES.** Confirms Phase 3 result on R-001. The framework's self-correcting pattern (debate 001 Methodological Note + debate 004 Methodological Note 2 establishing "citations are checked; framework's text yields when sources contradict") is structurally protective.

### Policy 2 — Industry standards over framework-invented formulas

All quantitative claims and quality gates were checked. The vast majority anchor explicitly to industry standards (calibration-standards.md is the catalog; every Phase 0 calibration question is anchored). Three edge cases surfaced where small framework-internal heuristics lack explicit external anchors:

#### F-39 — Three small framework-internal heuristics in quality gates

- **(a) phase-1:75** "Boundaries contains at least three explicit items (guards against vagueness)" — the "three" is a framework-invented minimum count with no industry anchor. Reasoning ("guards against vagueness") is plausible but unanchored.
- **(b) phase-1:76** "Stress test covers ≥ 5 scenarios; divergence rate between Council members < 20%" — the 20% is now anchored on Cohen κ + Krippendorff α (post-F-29 remediation). The "≥ 5 scenarios" minimum count itself is unanchored.
- **(c) pm-calibration-guide.md:46** "Its reversal would require > 5 person-days of rework" — Tier 1 (startup) categorical heuristic; **explicitly hedged at line 52** as "5 person-days is a starting anchor, not a law. Adjust if your team's pace is very different."

**Severity assessment.** Under a strict reading of IVP v0.3 § 4.1 argument-warrant tier-floor ("load-bearing argument resting solely on framework-internal reasoning is at minimum MEDIUM"), these could escalate. The IVP rule's intent is to prevent *primary load-bearing arguments* from being unanchored. These three are:

- (a) and (b): bounded *minima* attached to quality-gate counts, not primary load-bearing claims (the load-bearing structure is the "stress-test divergence < 20%" anchored on Cohen κ — the "5 scenarios" is the count threshold above which divergence is meaningfully measurable).
- (c): explicitly hedged in-text as "starting anchor, not a law" for Tier 1 mode where no historical data exists.

Treating these as **LOW** is consistent with v0.3 spec intent because the *hedging* faithfully records the framework-internal status. A stricter pass could argue MEDIUM for (a) and (b). Recommended remediation:

- (a) Either anchor "≥ 3 explicit items" to an industry source on requirements-bounding (Karl Wiegers / Volere / IEEE 830 patterns) or change wording to "boundaries include enough explicit items to cover the project's known scope vectors; if the list is below 3, Council should test whether vagueness has been silently accepted." This moves the framework from a count-based heuristic to a process-based check.
- (b) Either anchor the scenario-count minimum to test-design literature (Myers, Beizer, ISTQB) or rephrase as "scenarios cover the project's known failure modes and at least one scenario per Immutable Law; the count is dependent variable."
- (c) Already faithfully hedged. Optional improvement: replace "5 person-days" with "team-velocity-derived ½-sprint equivalent" so the anchor is the team's own historical velocity (an industry standard at organizational scope) rather than a framework number. Tier 2 / Tier 3 already use velocity / PPB respectively.

---

## 7. Sub-check 5 — README link integrity

**Procedure.** All markdown links in README.md were extracted via Grep; "(planned)" links were checked to ensure they do not assert content existence; non-planned links were checked to confirm the target file exists on disk.

| Link target | Tagged "(planned)"? | Target exists? | Verdict |
|---|---|---|---|
| `LICENSE` | No | **Yes** (root of repo) | ✓ |
| `docs/glossary.md` | **Yes** (line 65) | No (working draft is `framework/glossary-for-debate.md`) | ✓ |
| `docs/protocol/` | **Yes** (line 78) | No | ✓ |
| `docs/case-study-lore-weave.md` | **Yes** (line 86) | No | ✓ |
| README Astronomican Protocol table phases 2/3/4 | **Yes** (line 74–76 "*(planned)*") | N/A | ✓ |
| External arXiv link 2108.07258 (Bommasani et al. 2021) | No, but external | (Not verified by Phase 5 — out of scope per § 5) | ✓ |

**README link integrity: PASSES.** All "planned" links are properly tagged; all asserted-to-exist links resolve.

### Bonus check — cross-doc internal links

Spot-checked internal markdown links in phase docs and debates for stale targets:

| Sample link | From | To | Resolves? |
|---|---|---|---|
| `debates/002-retrofit-vs-greenfield.md` | phase-0:7 | framework/debates/002-…md | ✓ |
| `debates/003-phase-0-calibration.md` | phase-0:205 | framework/debates/003-…md | ✓ |
| `debates/004-cap-revision-miller-correction.md` | phase-1:43 | framework/debates/004-…md | ✓ |
| `[phase-1-for-debate.md section 8]` | phase-0:30 | phase-1 §8 (Roles in Phase 1) | ✓ (section exists at line 111) |
| `calibration-standards.md#a-decision-significance-and-change-impact` | pm-calibration-guide:62 | calibration-standards § A | ✓ |
| `phase-1-for-debate.md§3` (cap revision target) | debate 004:110 | phase-1 §3 Activities | ✓ |
| `audit/findings-2026-05-08.md` | debate 004:8 | audit/findings-2026-05-08.md | ✓ |

No broken internal links surfaced in the sample.

---

## 8. Inventory paraphrase staleness (informational; not findings)

Per IVP v0.3 § 5 Phase 3 pre-step, `inventory.md` paraphrases capture Phase-1-state at audit time (2026-05-08) and are expected to lag remediation. Phase 5 treats the inventory as a pointer-list only. The following staleness was observed but is **not** counted as findings against the framework:

| Inventory location | Stale paraphrase | Current source value | Note |
|---|---|---|---|
| inventory.md:20 (C-006) | "Maximum five Immutable Laws and five Guiding Principles." | phase-1:43–44 — "Hard cap 9; target ~7" | Pre-debate-004 paraphrase. |
| inventory.md:21 (C-007) | "the '≤ 5' cap is grounded in cognitive load (Miller's working-memory range, ~5 ± 2)." | debate 001:32 — "Miller's working-memory range, ~7 ± 2" | Pre-debate-004 and pre-F-01-remediation paraphrase. |
| inventory.md:81 (R-014) | "Miller's working-memory range, ~5 ± 2" | debate 001:32 — "~7 ± 2" | Same. |
| inventory.md:74 (R-007) | "~1.3 billion members" (Catholic Church) | debate 001:69 — "1.422 billion at end of 2024 per Annuario Pontificio 2026" | Pre-F-30-precedent-update. |

These are expected per the spec; the recommended treatment is either to refresh the inventory before re-running Phases 2/3 or to read source files directly (v0.3 § 5 Phase 3 procedure step 2). Phase 5 used the latter.

---

## 9. Findings

### MEDIUM findings (4)

| ID | Title | Sub-checks |
|---|---|---|
| F-32 | phase-1:299 Note-on-Method paraphrase still says "5 Laws max" | 2 + 3 |
| F-33 | calibration-standards.md:76 "cap of 5–7 for Reckoning Team and Council" contradicts spec | 3 |
| F-34 | calibration-standards.md:78 "Council sits at layer 1 (≤5)" overshoots Dunbar layer 1 for upper half of 3–7 | 3 |
| F-35 | phase-0:34 "Time budget — soft or hard horizon" contradicts phase-0:211 (debate 003 Q3 resolution: soft target with escalation) | 1 + 2 |

### LOW findings (4)

| ID | Title | Sub-checks |
|---|---|---|
| F-36 | phase-1:309 still lists "First-time vs retrofit" as open question; debate 002 answered it | 2 |
| F-37 | HANDOFF.md:108 lists "Two-tier sharpness" as a phase-1 Note-on-Method question; not present in phase-1:303–310 | 2 |
| F-38 | debate-001:7 metadata "Affects: '≤ 5' caps" lacks "subsequently revised by debate 004" annotation | 2 |
| F-39 | Three small framework-internal heuristics in quality gates lack explicit external anchors (phase-1:75; phase-1:76 "≥ 5 scenarios"; pm-calibration:46 "> 5 person-days") | 4 |

### CRITICAL / HIGH findings (0)

None surfaced.

### Severity reasoning

All four MEDIUM findings are localized prose edits where late-session remediation didn't propagate into a paraphrasing sentence or a reference catalog. They do not touch a sealed decision's prescriptive site, so the framework's *binding* is unaffected; they affect *readability and external-reviewer confidence* — a reader spotting a "5 Laws max" sentence next to a "9 Laws max" §3 would justifiably wonder which is current.

The four LOW findings are hygiene-class: stale open-questions list, retrospective metadata, and small heuristics that could either be anchored externally or rephrased to make their hedging explicit.

---

## 10. Limitations of this audit (Phase 5 specific)

- **Single reviewer.** Same as prior IVP phases. The same Phase-5 reviewer also wrote inventory.md in Phase 1 (2026-05-08); the term-drift classifications are correlated with prior classifications. Recorded in § 7 IVP spec § Limitations.
- **Inventory used as pointer-list only.** Per v0.3 § 5 Phase 3 pre-step procedure (b). The inventory was not refreshed before this run; staleness is recorded in § 8 of this file but not counted as findings.
- **README "planned" external link not verified.** The arXiv:2108.07258 link (Bommasani et al. 2021) was not fetched in this phase — Phase 5 scope is internal consistency, not external citation verification (that was Phase 2's job). The link is structurally sound; its content was verified in Phase 4 F-28 remediation.
- **Cross-references checked by sample, not exhaustively.** Six internal cross-doc markdown links were spot-checked (§7 Bonus check). The dataset has dozens of such links; the sample was selected to cover each phase doc once. No exhaustive walk was performed.
- **Audit files excluded from scope.** `framework/audit/*` files are themselves audit history (per IVP § Scope) and were not audited for internal consistency in this phase. Their content was *referenced* (HANDOFF status table) but not subject to term-drift / quantitative-consistency checks.
- **Out-of-scope reflection.** HANDOFF.md is in scope (per IVP § Scope) and the F-37 finding records one HANDOFF / phase-1 drift. A more exhaustive HANDOFF reflection would compare every HANDOFF claim against every source it summarizes; this run captured only the open-questions discrepancy because it was the most direct claim of verbatim reflection.

---

## 11. Audit trail

### Read actions

- `c:\Works\_Researchs\dead-light-framework\HANDOFF.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\README.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\glossary-for-debate.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\phase-0-for-debate.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\phase-1-for-debate.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\calibration-standards.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\pm-calibration-guide.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\debates\README.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\debates\001-laws-count-and-multirepo-scaling.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\debates\002-retrofit-vs-greenfield.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\debates\003-phase-0-calibration.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\debates\004-cap-revision-miller-correction.md` — full (2026-05-11)
- `c:\Works\_Researchs\dead-light-framework\docs\audit\inventory.md` — full (2026-05-11, as pointer-list)
- `c:\Works\_Researchs\dead-light-framework\docs\audit\independent-verification-pass-for-debate.md` — full (2026-05-11, methodology reference)

### Grep queries

- `5 ± 2|5±2|≤ 5 Law|≤ 5 Principle|≤5 Law|≤5 Principle|5 Laws max|5 Principles max|maximum five` — surfaces stale Miller/cap references (F-32 confirmed)
- `Council size|Council 3-7|Council 5-7|3–7|5–7|Reckoning Team|2–5` — Council/Reckoning Team size cross-doc check (F-33, F-34 confirmed)
- `Two-tier sharpness|First-time vs retrofit` — open-question reflection check (F-36, F-37 confirmed)
- `soft or hard|Time budget|time budget|time-budget` — time-budget wording check (F-35 confirmed)
- `5 person-days|five person-days|three explicit items|≥ 5 scenarios|at least three|at least five` — policy-2 small-heuristic check (F-39 confirmed)
- `≤ ?5 |maximum 5|≤ ?7 |cap of 5|cap of 7` — residual ≤ 5 wording check (F-38 metadata-line confirmed)
- `\(planned\)` — README planned-link tagging check (PASS)
- `debates/00[5-9]|phase-2|phase-3|phase-4-for-debate` — forward-reference broken-link check (no matches; clean)
- `Phase 2 \(Codex per Chapter\)|Phase 3|Phase 4` — forward-reference framing check (correctly tagged as planned/future)
- `\]\(([^)]+\.md)` — markdown link extraction (sample cross-references confirmed)

### Bash actions

- `ls -la docs/ framework/audit/ framework/debates/` — file-existence check for cross-references (all files referenced from HANDOFF and README resolve except the README "planned" links, which are correctly tagged)
- `ls README.md HANDOFF.md LICENSE chat.txt` — root-level file existence check (all present)

### IVP methodology references applied

- v0.3 § 4.1 severity rubric (CRITICAL / HIGH / MEDIUM / LOW + cross-cutting rules including argument-warrant tier-floor)
- v0.3 § 5 Phase 5 procedure (term drift / decision-to-doc reflection / quantitative consistency / policy compliance / README link integrity)
- v0.3 § 5 Phase 3 pre-step (refresh inventory paraphrases or treat as pointer-list); the latter was applied here.

---

## 12. Recommended remediation summary (for project owner)

All eight findings are remediation candidates. Suggested order of fix:

1. **F-32** — single-sentence edit in phase-1:299 (highest-visibility drift; readers comparing § 3 cap vs § Note on Method see direct contradiction).
2. **F-33 + F-34** — two-line edits in calibration-standards.md to align with phase-1 spec (Council 3–7, Reckoning Team 2–5) and to import debate 004:54's hedge for the Council–vs–Dunbar-layer-1 relationship.
3. **F-35** — single-line edit in phase-0:34 to reflect debate 003 Q3 resolution.
4. **F-36** — remove or rephrase phase-1:309 stale open question.
5. **F-37** — either add "Two-tier sharpness" to phase-1's open-questions list or remove from HANDOFF (project-owner call on whether the question is actually still open).
6. **F-38** — add a "subsequently revised by debate 004" annotation to debate-001:7 metadata line.
7. **F-39** — either anchor the three small heuristics externally or rephrase to surface their framework-internal status.

All eight fixes together are well under 30 lines of edit total. None requires re-opening a sealed decision.

---

*End of Phase 5 findings. Phases 6 (External Benchmarking) and 7 (Synthesis Report) remain queued.*

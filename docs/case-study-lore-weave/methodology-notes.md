# Methodology Notes — LoreWeave Case Study

> **Status:** Accumulating during Phase 0 (2026-05-11 onward).
> **Purpose:** Record how the framework was applied to LoreWeave in practice, what diverged from spec, what was lossy, what was novel. Feeds the framework's next refinement cycle.
>
> This file is the equivalent of an IVP "Limitations of this audit" section but for the framework's own application against a real codebase — the gap between spec and execution.

---

## 1. Reviewer profile

- **Single human reviewer** (project owner) acts simultaneously as Reckoning Team member, PM, and Council. The framework's "Single-person reckoning" anti-pattern (Phase 0 §6) is **structurally** in play; mitigations are documented in [`reckoning-team-record.md`](reckoning-team-record.md) § "Single-reviewer risk acknowledgment".
- **AI-aide-1** (Claude Code Opus 4.7) serves as the outside-scope perspective per Phase 0 §7 accommodation, under the interim Codex captured in `reckoning-team-record.md`. Phase 2 of Dead Light Framework (Codex per Chapter) is not yet defined; this interim Codex will be superseded when Phase 2 lands.

---

## 2. Departures from Phase 0 spec (recorded as we hit them)

### D-1 — Attribution anonymized to "project owner" throughout

**Spec text** ([debate 002](../debates/002-retrofit-vs-greenfield.md) Q3 + Phase 0 §3.2-3.3): "Full attribution. History is a valuable lesson, the team must accept it to move forward, and git commits already record names."

**Departure.** Project owner chose to keep attribution anonymized as **"project owner"** throughout this case-study artifact rather than naming individuals. Git commits remain unchanged (the original attribution is preserved in version control); the *case-study document* anonymizes.

**Risk recorded.** The framework's "names are kept, blame is not assigned" reasoning is partially defeated: future readers of the case study cannot independently triangulate decisions to commit authorship without going to git. The framework's social-structure-visibility argument (debate 002 Q3 — "hiding actors hides the social structure that produced the outcomes") is also partially defeated.

**Mitigation.** Where the project owner is the sole decision-maker (solo project), there is only one social structure to surface. The anonymization is effectively a publication-style choice, not a hiding of structure. If LoreWeave grows beyond solo, this departure should be re-evaluated.

**Reversibility.** This is a publication-style choice; reversing it later is a find-and-replace.

### D-3 — AI-aide drafts PM Threshold Decisions for project-owner review

**Spec text** (Phase 0 §2 inputs): "PM (Project Manager / Owner) decisions committed in writing **before** Phase 0 begins."

**Departure.** AI-aide-1 produced the [`pm-threshold-decisions.md`](pm-threshold-decisions.md) draft proposal from a preliminary LoreWeave scan; project owner then reviews, adjusts, and signs off. The spec's "before Phase 0 begins" sequencing is preserved (sign-off precedes inventory work), but the *authoring* is delegated to the AI-aide.

**Risk recorded.** PM-ownership of thresholds is partially diluted by AI-authored defaults — the project owner may accept proposed numbers without internalizing the trade-offs.

**Mitigation.** (a) The proposal is explicitly marked "draft proposal pending project-owner review, adjustment, and sign-off." (b) An "Adjustments by project owner" section invites changes before sign-off. (c) The proposal includes provenance (scan data, scan date, AI-aide identifier) so the project owner can audit the reasoning. (d) The sign-off line is explicit and binding.

**Why this departure was chosen.** Project owner's rationale: solo + AI-aide configuration benefits from an AI-drafted starting point so the project owner can react to concrete numbers rather than start from blank. The framework anticipates this kind of accommodation in its small-team accommodation language ("AI assistants may serve as aides to absent perspectives").

**Reversibility.** Reversible. If project owner is uncomfortable with this departure, they can rewrite `pm-threshold-decisions.md` from scratch; the AI-drafted version remains in git history as one input among others.

### D-2 — Implicit Principles capture order reversed (AI-aide first, project owner second)

**Spec text** (Phase 0 §3.4): "each Reckoning Team member writes, **independently and without coordination**, the principles they believe the team has been operating under. Aggregation comes after independent capture; contradictions across members are *the most valuable output of this section*."

**Departure.** Project owner chose to have **AI-aide-1 draft from evidence FIRST**, then write their independent contribution SECOND. The spec's "independently and without coordination" requirement is partially compromised because the AI-aide draft is technically available to the project owner before they write.

**Risk recorded.** The most valuable Phase 0 output — contradictions between members — is at risk of contamination. The project owner may unconsciously align with or against the AI-aide draft they've read.

**Mitigation.** The project owner commits to **writing their contribution BEFORE reading the AI-aide draft** when they reach Section 4 (enforced by self-discipline; the spec departure is that the AI-aide draft exists earlier in the workflow, not that the project owner reads it first). The project owner's contribution should be written in a session where the AI-aide draft is collapsed / hidden in the editor.

**Why this departure was chosen.** Project owner's rationale: for a solo + AI-aide configuration, having the AI-aide surface candidates first ensures no obvious "of course we'll" pattern is missed when the project owner writes their independent draft. The framework's strict "independently" rule presumes multiple humans with diverse viewpoints; with a single human, there is little to gain from strict independence and more to gain from comprehensive surfacing.

**Reversibility.** Difficult once the project owner has read the AI-aide draft. The departure is logged so future re-reckoning iterations (per `pm-threshold-decisions.md` §5 cadence) can either re-validate or course-correct.

---

### 2.X Operational departures (cosmetic; no spec violation)

### 2.1 Reckoning Team kick-off as a half-day session vs asynchronous

Phase 0 §3 specifies a half-day Reckoning Team kick-off followed by parallel time-budgeted inventory work. For a solo project with one human + one AI-aide, this collapses to:

- **Kick-off** = a single chat session where project owner commits PM Threshold Decisions and confirms Pass 1 service selection.
- **Inventory work** = a sequence of read-only AI-aide investigations + project-owner-driven contributions over multiple chat sessions.

Severity of departure: **expected**, given solo + AI-aide structure. No spec violation; the spec already accommodates "team size permits" softeners.

### 2.2 Aggregation and cross-review

Phase 0 §3 specifies "Reckoning Team cross-reviews each other's areas." With one human + one AI-aide, cross-review means project owner reviews AI-aide drafts; the reverse (AI-aide reviewing project-owner-only sections) is also performed but **with no voting authority** per the interim Codex.

### 2.3 Council review session

Phase 0 §3 specifies the full Ascension Council reads the draft Reckoning Record before the review session and the Reckoning Team presents the four sections. For a solo project, "Council reads then questions Reckoning Team" collapses to a single chat session where the project owner reads the AI-aide-produced and project-owner-produced drafts side-by-side. The session ends when the project owner feels they have enough context to walk into Phase 1.

---

## 3. Observations on framework-versus-reality

_(Accumulates as Phase 0 runs.)_

### 3.1 What worked well in spec

_(To fill.)_

### 3.2 What was awkward or under-specified

_(To fill.)_

### 3.3 What was novel / unexpected

_(To fill. Especially any case where the framework's anti-patterns or failure-mode language proved sharper than expected at catching real LoreWeave issues.)_

### 3.4 What the framework missed

_(To fill. Real LoreWeave issues that don't fit any Phase 0 section cleanly.)_

---

## 4. Carry-forward to framework refinement

Items here become candidates for the next debate cycle on Phase 0 / Phase 1.

| # | Observation | Recommended next-cycle action | Priority |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | _to fill_ |

---

## 5. Carry-forward to LoreWeave's Phase 1

Items the Phase 0 audit surfaced that should be flagged when LoreWeave runs Phase 1. The Reckoning step (phase-1 §10.2) will pick these up.

| # | Item | Recommended Phase 1 disposition (Keep / Fix-now / Fix-by-date / Reconsider-Law) | Reasoning |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | _to fill_ |

---

## 5.X Retroactive review — pre-seal work vs sealed Codex

**Trigger:** [Adeptus Administratum Codex v1.0](../chapters/adeptus-administratum/codex.md) sealed via [debate 005](../debates/005-first-chapter-pm-high-lord-aide.md) on 2026-05-11. Per debate 005's follow-up actions, the work done under the interim Codex (before the seal) is retroactively reviewed for compliance.

### Scope of retroactive review

Work performed under the interim Codex (2026-05-11 — same day as debate 005 seal, but in commits preceding the seal):

| Commit | Work product | Reviewed against |
|---|---|---|
| `324b9f6` | Case-study folder scaffold (README, pm-threshold-decisions skeleton, reckoning-team-record, reckoning-record skeleton, methodology-notes skeleton) | Codex §2.1 Operational Bounds; §6 Output Contract; §7 Authority bounds |
| `0450e47` | Logged departures D-1 (anonymized attribution) and D-2 (AI-aide-first Implicit Principles) | Codex §3 Hard Stops; §5 Notify Triggers |
| `9c04342` | LoreWeave scan (cloc + git-log + change-frequency map); PM Threshold Decisions proposal draft; departure D-3 logged | Codex §2.1; §3; §5; §6 |

### Compliance check

**§2.1 (Operational Bounds for Phase 0 tasks).** All pre-seal work falls within §2.1 permissions: drafting PM Threshold Decisions, running cloc / git-log queries, asking clarifying questions, drafting case-study scaffolding. **Compliant.**

**§3 (Hard Stops).** No pre-seal work violated any HS-1 through HS-9. Specifically:
- HS-1 (sealed Astronomican modification): no LoreWeave Astronomican exists yet — no violation possible.
- HS-2 (final entries without sign-off): all entries marked as draft / pending project-owner review.
- HS-3 (unconfirmed attribution): D-1 explicitly chose anonymized attribution — no unconfirmed naming occurred.
- HS-4 (vote/seal/sign): no voting, sealing, or signing actions performed.
- HS-5 (override of human decisions): no overrides; clarifying questions used instead.
- HS-6 (audit-output file modification outside IVP run): no `docs/audit/*` files were modified in pre-seal case-study work.
- HS-7 (state persistence outside artifacts): all load-bearing observations were committed to artifact files.
- HS-8 (40k as substantive justification): no 40k justification used; metaphor used only as naming per policy 1.
- HS-9 (framework-internal arithmetic without anchor): PM Threshold Decisions proposal anchored on M&A IT due-diligence rule of thumb (Tier 1 industry-pragmatic), COCOMO II hedge for time-budget, ITIL / DORA for materiality, debate 003 Q3 for time-boxing escalation. **Note for review:** the "lowered 5 person-days → 1 day for solo pace" adjustment in §1 #2 of pm-threshold-decisions.md is a project-specific tuning of an already-hedged Tier 1 anchor. The hedge is explicit ("Tier 1 default is '5 person-days'; lowered to 1 person-day to match solo-developer iteration pace per PM Calibration Guide §1 hedge 'Adjust if your team's pace is very different.'"). Compliant; would not trigger HS-9 under the sealed Codex.

**§5 (Notify Triggers).** Under the interim Codex (Draft only), no notify infrastructure existed. Under the sealed Codex (Draft + Notify), I retroactively scan the pre-seal work for events that *would have* triggered notifies:
- **N-1 (Astronomican violation):** N/A — no Astronomican sealed yet.
- **N-2 (policy violation):** none surfaced.
- **N-3 (citation misuse):** none surfaced. All citations were framework-internal references (debates, phase docs).
- **N-4 (term drift):** **one event** that would have triggered an N-4. During the LoreWeave scan (commit `9c04342`), AI-aide-1 observed that the framework's HANDOFF.md described LoreWeave as "6 services in contracts/api/" but the current repo has 7 (llm-gateway is new). Under the sealed Codex, this would have emitted an N-4 non-blocking notify. **Status:** the observation was surfaced to the project owner in the scan report text and recorded in `README.md` and `pm-threshold-decisions.md` — i.e., the *substance* of the notify was delivered, but it was not formatted as a Codex §5 N-4 notify entry. Retroactively recorded here as N-4-equivalent.
- **N-5 (time-pressure):** none surfaced.

**§6 (Output Contract).** Compliance check item by item:
- **Status marking:** the pm-threshold-decisions.md draft is explicitly marked "Draft proposal by AI-aide-1 ... pending project-owner review, adjustment, and sign-off." Compliant.
- **Provenance line:** debate 005 §10 mentioned the instance identifier (Claude Code Opus 4.7), and `methodology-notes.md` § 1 reviewer profile names it. Pre-seal artifacts could be more explicit about provenance per the sealed Codex's stricter requirement; this is a **minor gap** that we close going forward (every new instance task adds the provenance line per §6 item 2).
- **Git commit:** all pre-seal outputs were git-committed. Compliant.
- **Audit-trail update:** `methodology-notes.md` audit trail was updated per task. Compliant.
- **Readability:** pre-seal outputs are readable without session context. Compliant.
- **Re-prime-friendliness:** the scaffold structure (case-study README + per-section files with clear headers) supports re-prime. Compliant.

**§7 (Authority bounds).** Pre-seal work respected all four authority bounds: no voting, no signing, no blocking, no unilateral ownership. Compliant.

### Departures D-1, D-2, D-3 — re-evaluation under sealed Codex

| Departure | Sealed Codex stance | Verdict |
|---|---|---|
| D-1 (anonymized attribution to "project owner") | Codex §6 mandates *instance* provenance but does not mandate human-decision-maker naming format. D-1 is a PM-level publication choice, not a Codex-level governance choice. | **Stands.** Spec departure from Phase 0 §3.2-3.3 / debate 002 Q3 unchanged. |
| D-2 (AI-aide-first Implicit Principles capture) | Codex §2.1 permits aide to "Draft an AI-aide independent contribution for the Implicit Principles Surface, respecting the project-owner's chosen capture order." D-2 is the project-owner's chosen capture order. | **Stands.** Spec departure from Phase 0 §3.4 unchanged. |
| D-3 (AI-aide drafts PM Threshold Decisions for owner review) | Codex §2.1 explicitly permits "Draft PM Threshold Decisions for project-owner review." D-3 is the operational pattern the Codex was designed to support. | **Stands.** Spec departure from Phase 0 §2 is now the formally-permitted Codex behavior; the departure note is preserved as historical record but the *practice* is no longer a departure under sealed governance. |

### Recommended adjustments going forward

1. **Provenance line per Codex §6 item 2.** Every Adeptus Administratum instance output from 2026-05-11 onward includes an explicit provenance line. Backfill is not required for pre-seal artifacts (they were produced under the interim Codex).
2. **N-4 formatting.** When AI-aide-1 surfaces term-drift or numeric inconsistency (like the HANDOFF "6 → 7 services" case during the LoreWeave scan), format it as a Codex §5 N-4 non-blocking notify in the audit trail going forward.
3. **Pass 1 will be the first work product produced fully under the sealed Codex.** All §5 trigger types are now active; §6 Output Contract is fully enforced; §8 re-priming protocol runs at every new task instance.

### Single backfill (administrative)

The N-4-equivalent observation from the LoreWeave scan is **backfill-recorded** in the audit trail:

> **N-4 (backfill, retroactive 2026-05-11):** HANDOFF.md describes LoreWeave as having "6 services in contracts/api/" (per `HANDOFF.md` line 27 phrasing); current LoreWeave state has 7 (llm-gateway new since 2026-05-09). Term drift between framework's HANDOFF claim and LoreWeave reality. Recorded in `pm-threshold-decisions.md` § Scan summary and in `reckoning-record.md` §1.1 placeholder. Resolution: HANDOFF refresh expected as part of LoreWeave Pass 1 Current State Audit completion. Non-blocking; no acknowledgment required from project owner inline.

---

## 6. Audit trail for the case study itself

Every read of LoreWeave source, every grep, every git query, every command issued by AI-aide-1 is logged here for reproducibility. This is the case study's own audit trail (distinct from the Reckoning Record's evidence).

_(Accumulates as Pass 1 and Pass 2 run.)_

| Date | Action | Source / target | Output (link or summary) |
|---|---|---|---|
| 2026-05-11 | Created case-study folder skeleton | `docs/case-study-lore-weave/` | commit `324b9f6` |
| 2026-05-11 | Logged departures D-1 (anonymized attribution) and D-2 (AI-aide-first Implicit Principles) | `methodology-notes.md` §2; `reckoning-team-record.md`; `reckoning-record.md` §4 | commit `0450e47` |
| 2026-05-11 | `ls C:\Works\_Researchs\lore-weave` top-level walk | LoreWeave repo | 15 services + 7 contracts/api + 2 doc trees (foundation/governance/planning) + frontend + agentic-workflow + design-drafts + poc + tests + infra + sdks + scripts |
| 2026-05-11 | `git log` on LoreWeave: branches, recent commits, change-frequency last 6mo | LoreWeave git | 1314 commits in 6mo; current branch `mmo-rpg/design-resume`; top dirs by change frequency = frontend/src 1739, docs/03_planning 1439, services/knowledge-service 945 |
| 2026-05-11 | `cloc` full repo (exclude node_modules/git/cache/build) | LoreWeave | ~358 KLOC total: Python 67K, TypeScript 60K, Go 33K, HTML 30K, JSON 24K, plus smaller buckets |
| 2026-05-11 | `cloc` per Pass 1 candidate | LoreWeave | docs/01_foundation 0.7 KLOC; docs/02_governance 1.4 KLOC; docs/03_planning 120 KLOC; frontend 70.5 KLOC; services/knowledge-service 49 KLOC. frontend-v2 not present (v2 renamed to frontend per commit `bada6bbd`). |
| 2026-05-11 | Drafted PM Threshold Decisions proposal | `pm-threshold-decisions.md` | pending project-owner review/sign-off; departure D-3 recorded |
| 2026-05-11 | Opened debate 005 (First Chapter: PM/High Lord Aide) following project-owner observation that PM threshold-setting is a bottleneck on a 358-KLOC project | `docs/debates/005-first-chapter-pm-high-lord-aide.md` | commit `b0b952f` |
| 2026-05-11 | Revised debate 005 §6 Lifecycle (D3 → D4 task-scoped instance + persistent role + artifact continuity) per project-owner observation | `docs/debates/005-...` | commit `89039d1` |
| 2026-05-11 | Sealed debate 005; created Adeptus Administratum Codex v1.0 at `docs/chapters/adeptus-administratum/codex.md` | debate 005 + Codex | commit `78d4bb4` |
| 2026-05-11 | Propagated sealed-Codex references: phase-0 §7, phase-1 §8.1 + §4 + §7, case-study/reckoning-team-record (interim Codex superseded), this file (Retroactive review §5.X) | framework + case-study files | commit pending |
| 2026-05-11 | **N-4 backfill (retroactive):** HANDOFF describes LoreWeave as "6 services in contracts/api/"; current state has 7 (llm-gateway new). Term drift recorded; resolution deferred to Pass 1 Current State Audit completion | HANDOFF.md ↔ LoreWeave repo | this commit |

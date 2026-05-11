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

# Reckoning Team Record — LoreWeave Phase 0

> **Status:** Pending project-owner confirmation (2026-05-11).
> **Spec:** Phase 0 §2 (Reckoning Team composition rule) + §7 (anti-patterns, AI-aide accommodation) + §8.2 (producer roles).
>
> Phase 0 §2 mandates **2–5 people** with three composition sub-rules: ≥1 active-IC who maintains code in scope (mandatory); ≥1 person with tenure spanning the period being reckoned (when project age permits); ≥1 person from outside the immediate scope (when team size permits). Where literal humans cannot fill all three, AI-assistant Chapters with explicit Codex serve as **aides** to the absent perspectives.

---

## Team configuration

LoreWeave is a **solo human project**. The single human (project owner) carries the active-IC, tenure-spanning, and Council roles simultaneously. The outside-scope perspective is provided by an AI-assistant Chapter per the Phase 0 §7 accommodation.

| Member | Role | Areas owned | Producer or Council? |
|---|---|---|---|
| **project owner** (anonymized identity throughout this case study — see methodology-notes § Departure D-1) | Active-IC (mandatory); tenure-spanning; PM; Council member | All services in scope; foundation/governance/planning docs | Both Reckoning Team **and** Ascension Council |
| **AI-aide-1 (Claude Code Opus 4.7)** | Outside-scope aide; **does not vote, does not own areas, does not author final entries unilaterally** | Cross-cutting review of Reckoning Team's drafts; surface contradictions; rote-mechanical Current State Audit (`cloc`/grep across services) | Producer-aide only |

**Why this passes Phase 0 §2 composition rule:**

- ≥1 active-IC — project owner. ✓
- ≥1 tenure-spanning — project owner (sole tenured contributor). ✓ (the "when project age permits" softener; for solo project the same human fills it).
- ≥1 outside-scope — AI-aide-1 per §7 accommodation. ✓ (the "when team size permits" softener; for solo project the AI fills it as a Chapter-with-Codex aide).

**Why this respects voting authority:** voting authority is exclusively the project owner's (per phase-1 §8.1 small-team accommodation: "humans alone hold binding authority"). AI-aide-1 surfaces analysis, raises contradictions, provides outside-eyes review; it does not vote at Council, does not sign the seal, does not own final inventory entries.

---

## AI-aide Codex (interim)

Phase 2 of Dead Light Framework (Codex per Chapter) is not yet defined. The AI-aide invocation here uses an **interim Codex** captured below to keep the accommodation faithful to spec until Phase 2 lands.

### AI-aide-1 — interim Codex for LoreWeave Phase 0

**Operational Bounds.** The aide may:

- Read any file in the LoreWeave repo at `C:\Works\_Researchs\lore-weave`.
- Run read-only commands (`git log`, `cloc`, `scc`, grep) and report results.
- Draft inventory sections in the Reckoning Record for project-owner review.
- Raise contradictions, missing entries, or suspect attributions in drafts the project owner produces.

**Hard Stops.** The aide must NOT:

- Modify any file in `C:\Works\_Researchs\lore-weave`.
- Author a final inventory entry without project-owner sign-off.
- Assign attribution to a human decision-maker the project owner has not named.
- Vote, seal, or sign any artifact.
- Convert a draft entry to "final" without explicit project-owner acknowledgment.

**Autonomy Threshold.** The aide may act solo when the action is **read-only and reversible** (search, read, summarize, draft). For anything that creates or modifies a framework artifact, the aide drafts and waits for project-owner review.

**Output Contract.** Every aide output names what it is:

- "Draft inventory entry" → goes to project owner for verification, attribution check, and acceptance.
- "Read-only analysis" → audit trail; informs project owner's decisions.
- "Question for project owner" → blocks until answered.

This interim Codex is **superseded automatically** when Phase 2 (Codex per Chapter) is defined and a formal Codex for outside-scope aides is published.

---

## Areas owned (Pass 1 / Pass 2 assignment — to fill)

Filled during Reckoning Team kick-off after the project owner confirms Pass 1 service selection.

| Service / area | Owner | Reviewer | Pass |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | 1 |
| _to fill_ | _to fill_ | _to fill_ | 1 |
| _to fill_ | _to fill_ | _to fill_ | 2 |
| _to fill_ | _to fill_ | _to fill_ | 2 |
| _to fill_ | _to fill_ | _to fill_ | 2 |
| _to fill_ | _to fill_ | _to fill_ | 2 |
| Foundation docs (`docs/01_foundation/`) | Project owner | AI-aide-1 | 1 |
| Governance docs (`docs/02_governance/`) | Project owner | AI-aide-1 | 1 |
| Planning docs (`docs/03_planning/`) | Project owner | AI-aide-1 | 1 |

---

## Single-reviewer risk acknowledgment

Per IVP v0.3 § 7 limitations and Phase 0 §6 failure mode "Single-person reckoning. One author, one viewpoint, one bias", this case study **carries known single-reviewer bias** because the project owner fills active-IC + tenure-spanning + Council roles simultaneously. Mitigations:

1. AI-aide-1 explicitly carries the outside-scope perspective and is empowered to challenge project-owner assertions.
2. The Implicit Principles Surface step (Phase 0 §3 step 4) is **structurally** at risk of single-viewpoint capture because there is only one viewpoint to capture. Recorded as a Phase 0 limitation in `methodology-notes.md`.
3. Future re-reckoning iterations (per the cadence committed in `pm-threshold-decisions.md` §5) should aim to bring in a second human reviewer if LoreWeave's contributor count grows.

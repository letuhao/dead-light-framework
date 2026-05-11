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

## AI-aide Codex (sealed via debate 005)

**Status update — 2026-05-11:** the interim Codex previously captured in this section has been **superseded** by the sealed [Adeptus Administratum Codex v1.0](../chapters/adeptus-administratum/codex.md). Project owner approved all six sub-decisions of [debate 005](../debates/005-first-chapter-pm-high-lord-aide.md) on 2026-05-11; the sealed Codex now governs all AI-aide invocations for the LoreWeave case study (and any future Dead Light Framework project).

### Active Codex for this case study

| Property | Value |
|---|---|
| Chapter | **Adeptus Administratum** |
| Codex | [`docs/chapters/adeptus-administratum/codex.md`](../chapters/adeptus-administratum/codex.md) v1.0 |
| Sealed via | [debate 005](../debates/005-first-chapter-pm-high-lord-aide.md) |
| Sealed on | 2026-05-11 |
| Multiplicity | Singleton role at Imperial level (LoreWeave currently sits below Sector trigger threshold per [reckoning-record.md §1.5](reckoning-record.md) — pending Pass 1 evaluation). |
| Instance lifecycle | Task-scoped per Codex §8 (D4). Each chat session / task = new instance; instance disbands on output commit + audit-trail update. |
| Instance identity for case study | Anonymous-by-default, recorded per instantiation in [methodology-notes.md §6 audit trail](methodology-notes.md). The first instance was Claude Code Opus 4.7, invoked 2026-05-11 for the LoreWeave Phase 0 kick-off task. |

### Notes specific to LoreWeave's invocation of the Codex

- **Phase activation:** during Pass 1 and Pass 2 work, the active subsection of Codex §2 Operational Bounds is **§2.1 (Phase 0 / Reckoning) tasks**.
- **Outside-scope perspective fulfillment:** the Adeptus Administratum instance for LoreWeave fulfills the "≥ 1 outside-scope perspective" requirement of Phase 0 §2 composition rule (per the small-team accommodation in Phase 0 §7, now updated to reference the sealed Codex).
- **Departures D-1, D-2, D-3 — relationship to sealed Codex:**
  - D-1 (anonymized attribution) — *not* contradicted by the Codex; the Codex's Output Contract §6 mandates provenance for the *instance*, not for human decision-makers. D-1 stands as a PM-level choice.
  - D-2 (AI-aide-first Implicit Principles) — *not* contradicted by the Codex; this is an ordering choice for a specific Phase 0 step, not a Codex-level governance choice. D-2 stands.
  - D-3 (AI-aide drafts PM Threshold Decisions for project-owner review) — *not* contradicted; the Codex's §2.1 explicitly permits "Draft PM Threshold Decisions for project-owner review." D-3 is the operational pattern the Codex is designed to support. D-3 stands.
- **Retroactive review of pre-seal work:** the work done under the interim Codex (Pass 0: scaffold, scan, PM Threshold Decisions proposal, departure logging) has been retroactively reviewed for compliance with the sealed Codex. Findings in [methodology-notes.md § Retroactive review](methodology-notes.md).

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

---
title: "Reckoning Team Record Template"
status: fillable
version: not versioned
audience: human
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Fillable template — copy into your project; name your Reckoning Team members before Phase 0 begins.
> **Audience:** Project owner + Reckoning Team members.
> **Purpose:** Document Phase 0's composition rule satisfaction + AI-aide invocations.
> **Read next if:** you've signed off PM Threshold Decisions and are assembling the Reckoning Team.

# Reckoning Team Record — <project name>

> Phase 0 §2 composition rule: **2–5 people**, with three sub-rules:
> - ≥ 1 active-IC who maintains code in scope (mandatory).
> - ≥ 1 person with tenure spanning the period being reckoned (when project age permits).
> - ≥ 1 person from outside the immediate scope being reckoned (when team size permits).
>
> Where literal humans cannot fill all three, AI-assistant Chapters with explicit Codex serve as aides per Phase 0 §7 accommodation. The first sealed Chapter is **Adeptus Administratum** (Codex at `framework/chapters/adeptus-administratum/codex.md`).

---

## Team composition

| Member | Role | Areas owned | Producer or Council? |
|---|---|---|---|
| <named human 1> | <Active-IC / Tenure-spanning / Outside-scope / PM / multiple> | <area or "all in scope"> | <Reckoning Team / Ascension Council / both> |
| <named human 2> | <...> | <...> | <...> |
| <named human N> | <...> | <...> | <...> |
| **AI-aide-N (<provider/model>)** | Outside-scope aide per Phase 0 §7 accommodation; **does not vote, does not own areas, does not author final entries unilaterally** | Cross-cutting review; rote-mechanical Current State Audit | Producer-aide only |

## Composition rule check

- ≥ 1 active-IC: <yes — name(s)>
- ≥ 1 tenure-spanning: <yes — name; or "project too young, softener applied">
- ≥ 1 outside-scope: <yes — name(s); or "AI-aide-N filling per §7 accommodation">

## AI-aide invocations (if any)

If invoking Adeptus Administratum or any other Chapter as an aide:

| Aide identifier | Chapter Codex | Phase coverage active | Provenance line for outputs |
|---|---|---|---|
| <provider/model/instance-name> | Adeptus Administratum Codex v1.0 | Phase 0 §2.1 | `instance: <provider/model/date> / Codex v1.0 / task: <description>` |

**Authority bounds reminder:** voting authority is exclusively the project owner's / Council's (per phase-1 §8.1 + Adeptus Administratum Codex §7). AI-aides surface, draft, and notify — they do not vote, sign, block, or override.

---

## Areas owned (assigned during Reckoning Team kick-off)

| Area | Owner | Reviewer | Pass (if multi-pass) |
|---|---|---|---|
| <area> | <named human> | <named human or AI-aide> | <Pass 1 / Pass 2> |

---

## Spec departures (if any)

If your project intentionally departs from Phase 0 spec, record each here with rationale.

| Departure ID | Spec section | Departure | Rationale | Risk recorded | Mitigation | Reversibility |
|---|---|---|---|---|---|---|
| D-N | <Phase 0 §X> | <what you're doing differently> | <why> | <what could go wrong> | <how you're mitigating> | <reversible / not> |

See `examples/lore-weave-snapshot/methodology-notes.md` § 2 for worked examples (D-1 anonymized attribution; D-2 AI-aide-first Implicit Principles; D-3 AI-aide drafts PM Threshold Decisions).

---

## Provenance

- Template version: distribution v0.6.0.
- Source: `distribution/framework/phases/phase-0.md` §2 + §7 + §8.2.
- AI-aide framework: `distribution/framework/chapters/adeptus-administratum/codex.md`.
- Worked example: `distribution/examples/lore-weave-snapshot/reckoning-team-record.md`.

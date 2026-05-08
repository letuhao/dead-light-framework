# Phase 0 — The Reckoning (For Debate)

> **Status:** Draft, not final. To be refined through debate against the LoreWeave case study before any element is canonized.
>
> **Purpose:** Define the prep-phase that precedes Phase 1 for retrofit projects — surveying the past so that the Ascension Council can walk into Phase 1 with a shared, evidence-based view of reality rather than a memory of how things were supposed to be.
>
> **Scope:** Phase 0 is **mandatory for retrofit** projects (existing code, accumulated decisions, formed habits) and is either **skipped or run in lightweight form for greenfield** projects. The decision to introduce Phase 0 was made in [debate 002](debates/002-retrofit-vs-greenfield.md).

---

## 1. Goal (one sentence)

Phase 0 is complete when a Reckoning Record draft exists that surfaces the project's actual past — current state, decisions with attribution, failures with attribution, and implicit operating principles — at sufficient depth for the Ascension Council to confront reality during Phase 1 rather than aspire past it.

---

## 2. Inputs / Prerequisites

Before convening the Reckoning Team:

- **Project mandate** — same artifact that feeds Phase 1.
- **Read access** to the codebase, deployment configurations, design docs, ticket/issue history, and any prior postmortems or retrospectives.
- **Designated Reckoning Team** — 2–5 people meeting the composition rule:
  - ≥ 1 active-IC who maintains code in scope (mandatory).
  - ≥ 1 person with tenure spanning the period being reckoned (when project age permits).
  - ≥ 1 person from outside the immediate scope being reckoned (when team size permits).
  - Where literal humans cannot fill all three, AI-assistant Chapters may serve as aides per the anti-pattern note in section 7.
- **Facilitator** — runs the process; has no vote and no inventory authority.
- **Scribe** — drafts the document; can be the same person who scribes Phase 1.
- **PM (Project Manager / Owner) decisions** committed in writing before Phase 0 begins. The PM is a member of the Ascension Council (see [phase-1-for-debate.md section 8](phase-1-for-debate.md) for full Council composition); these are the role-specific responsibilities the PM additionally owns during Phase 0. PMs without prior calibration experience should walk through [pm-calibration-guide.md](pm-calibration-guide.md) — it provides step-by-step recipes at three rigor tiers (startup / mid-org / CMMI L4+). Underlying industry standards are catalogued in [calibration-standards.md](calibration-standards.md). The framework adopts industry-standard formulas; it does not invent them.
  - **Significance threshold** for inclusion in the Past Decisions Catalog — what counts as "significant enough" to record.
  - **Materiality threshold** for the Failure Inventory — what counts as a "real" failure worth surfacing.
  - **Scope of audit** — which services, repos, components are in scope.
  - **Time budget** — soft or hard horizon for Phase 0 completion.

The PM commitments matter because the framework deliberately leaves Phase 0 sizing to project-specific judgment (per the answers to open questions in [debate 002](debates/002-retrofit-vs-greenfield.md)). Without these decisions in writing, Phase 0 drifts.

---

## 3. Activities (sequence)

Phase 0 is an **investigative phase**, not a ceremonial one. There is no sealing event. The output flows directly into Phase 1.

### Reckoning Team kick-off (half-day)

- Read the Project mandate together.
- Review the PM's significance, materiality, and scope decisions.
- Assign areas to team members based on expertise (each member owns at least one area; areas may be services, modules, or cross-cutting concerns).
- Set internal milestones aligned to the PM's time budget.

### Inventory work (parallel, time-budgeted)

Conducted concurrently across team members:

1. **Current State Audit** — what is actually deployed, what is actually in `main`, what services exist with what contracts. Documentation is *evidence*, not *truth* — discrepancies between docs and reality are explicitly recorded.
2. **Past Decisions Catalog** — significant scope changes, architectural pivots, abandoned directions, technology choices. Each entry includes: decision, date, named decision-maker(s), context that drove it, what changed as a result. Attribution is required (per [debate 002](debates/002-retrofit-vs-greenfield.md), Q3) — the record names actors and separates personal accountability from systemic learning.
3. **Failure Inventory** — material failures with date, blast radius, named participants, and root cause where known. Attribution required, blame avoided. Borrowed framing from blameless-postmortem culture: names are kept, blame is not assigned.
4. **Implicit Principles Surface** — each Reckoning Team member writes, **independently and without coordination**, the principles they believe the team has been operating under. Aggregation comes after independent capture; contradictions across members are *the most valuable output of this section*.

### Aggregation and cross-review (1–2 days)

- Scribe assembles independent inputs into a single draft Reckoning Record.
- Reckoning Team cross-reviews each other's areas to catch gaps and contradictions.
- Open questions and unresolved investigations are explicitly marked rather than smoothed over.

### Council review session (half-day to one day)

- Full Ascension Council reads the draft Reckoning Record before the session.
- Reckoning Team presents the four sections in order; Council asks questions.
- **No approval vote occurs.** The Council does not seal Phase 0. The session ends when Council members feel they have enough context to walk into Phase 1.
- Items the Council requests further investigation on are noted; Reckoning Team either resolves them before Phase 1 or marks them as "investigation pending" with rationale.

The Council review session deliberately has no decision authority. This is consistent with the bottom-up nature of Phase 0 — the Reckoning Team produces, the Council consumes; Council is not the producer of inventory.

---

## 4. Outputs / Artifacts

| Artifact | Format | Status after Phase 0 |
|---|---|---|
| **Reckoning Record (draft)** | Markdown document with four sections | Input to Phase 1; not sealed |
| **Reckoning Team Record** | Names + roles + areas owned | Append-only |
| **PM Threshold Decisions** | Significance, materiality, scope, time-budget definitions | Stable for the duration of Phase 0; revisited in Phase 1 if Reckoning step exposes problems |

The Reckoning Record draft has four sections:

1. Current State Audit
2. Past Decisions Catalog (with attribution)
3. Failure Inventory (with attribution)
4. Implicit Principles Surface (per-member contributions plus synthesis)

Phase 1's Reckoning step adds a fifth section to this same document:

5. Classifications (Keep / Fix-now / Fix-by-date / Reconsider-Law) plus the Migration Plan.

The Reckoning Record reaches v1.0 at the moment Phase 1 seals the Astronomican. After that point, it is a **living document** — Fix-by-date items are tracked here as they're resolved.

---

## 5. Quality Gates — when is Phase 0 actually done?

Phase 0 is NOT done until all of the following are true:

- [ ] **Audit covers all services / components in scope** as defined by the PM. Discrepancies between documented and deployed reality are explicitly recorded, not papered over.
- [ ] **Past Decisions Catalog covers every decision** the PM has flagged as significant, plus any others surfaced during the work that meet the significance threshold.
- [ ] **Failure Inventory includes every material failure** known to the Reckoning Team. Items the team is unsure about are listed with a confidence note rather than omitted.
- [ ] **Implicit Principles Surface contains independent contributions** from every Reckoning Team member, captured before any group discussion of the synthesis.
- [ ] **Synthesis of implicit principles names contradictions** between members where they exist. A clean, consensus-style synthesis is a failure, not a success.
- [ ] **Every Council member has read the draft** at least once before the review session.
- [ ] **The Council review session has occurred** and the Reckoning Team has either resolved Council questions or recorded them as "investigation pending" with rationale.

---

## 6. Failure Modes — signals Phase 0 has gone off-track

| Signal | Diagnosis |
|---|---|
| Reckoning Team is composed entirely of senior decision-makers | Loses the perspective of those who maintain the code daily; the bottom-up signal is lost. Add ICs who actually run the systems. |
| Audit is documentation-driven only | Documentation lies. Force one person to verify against deployed reality (logs, configs, running processes). |
| Past Decisions Catalog reads as a success story | Sanitization. The catalog must include decisions that were made under pressure, decisions that were later reversed, and decisions whose rationale has been forgotten. |
| Failure Inventory lists symptoms, not root causes | Surface investigation. Either deepen each failure with a "what did we miss?" pass, or mark the entry "root cause unknown" honestly. |
| Implicit Principles Surface converges suspiciously cleanly | Members coordinated before independent capture. Reset and have each member write privately again. |
| Reckoning Team finishes early and reports "everything looks fine" | Either the project is genuinely small (verify against PM's scope), or the team is rationalizing past decisions as "necessary at the time" without examining alternatives that were available. |
| Council reaches the review session with major surprises | The Reckoning Team did not socialize the work in progress; surface contentious findings to Council before the formal session. |

---

## 7. Anti-patterns — what NOT to do

- **Skip Phase 0 for retrofit.** "We know our project, we don't need an inventory" is the precise reason retrofit Phase 1 fails — the team's confident memory and the actual state diverge.
- **Single-person reckoning.** One author, one viewpoint, one bias. The framework requires plural perspectives in the Reckoning Team for a reason.
- **Council members do reckoning work themselves.** Defeats the bottom-up signal. Council reviews; Reckoning Team produces.
- **Anonymize attribution.** Decided against in [debate 002](debates/002-retrofit-vs-greenfield.md). Names are required because (a) git already has them, (b) institutional learning requires knowing context, (c) hiding actors hides the social structure that produced the outcomes.
- **Treat Phase 0 as documentation theater.** Producing a polished document that no one reads or argues with. The output of Phase 0 is supposed to provoke debate in Phase 1, not pre-empt it.
- **Use Phase 0 to settle scores.** Attribution preserves names; blame is not the framework's tool. Facilitator stops this on contact.
- **Smooth over contradictions in implicit principles.** The contradictions are the data. A unified synthesis with no friction is fabricated.
- **Skip the PM threshold decisions.** Without them, Phase 0 has no scope and runs forever or stops arbitrarily.
- **Use small team size as an excuse to skip Phase 0 or violate the Reckoning Team composition rule.** Where literal humans cannot fill all three required roles (active-IC, tenure-spanning, outside-scope), AI assistants — invoked as specific Chapters with explicit Codex — can serve as **aides** to the absent perspectives. Aides surface analysis, raise contradictions, and provide outside-eyes review; they do not own areas, do not author final inventory entries unilaterally, and do not vote in any sense. Their use is **named in the Reckoning Team Record** (which Chapter and Codex stood in for which absent perspective). The specific Chapters and their Codexes are deferred to **Phase 2 (Codex per Chapter)** — the framework's planned next phase — and are not yet defined here. This accommodation is on-thesis with Dead Light Framework: humans + agents collaborate; humans alone hold authority.

---

## 8. Roles in Phase 0

### 8.1 The Council (multi-role, assembled before Phase 0)

The Ascension Council is assembled before Phase 0 begins, because Phase 0 already requires PM threshold decisions (and the PM is a Council member). The Council is multi-role; its full composition rules and minimum-diversity requirement are defined in [phase-1-for-debate.md section 8](phase-1-for-debate.md). Phase 0 specifically depends on the **PM** role being present on the Council to commit thresholds in writing before inventory work starts.

**Council during Phase 0** — Council members **read** the Reckoning Record draft and question the Reckoning Team during the review session. They do not approve, do not seal, do not vote — Phase 0 has no governance act. The Council's role here is to absorb context that they will need in Phase 1.

**PM-specific Phase 0 responsibilities** — as a Council member, the PM additionally:

- Defines the significance threshold (what enters the Past Decisions Catalog).
- Defines the materiality threshold (what enters the Failure Inventory).
- Defines the scope of audit (which services / components / repos).
- Defines the time budget for Phase 0.
- Defines the re-reckoning cadence (committed in writing inside the Reckoning Record itself, so it cannot be silently forgotten).

These commitments are made **before** Phase 0 begins. Without them, Phase 0 has no scope and either runs forever or stops arbitrarily.

### 8.2 Phase 0 producer roles (overlap with Council allowed)

| Role | Phase 0 responsibility | Continues into Phase 1? |
|---|---|---|
| **Reckoning Team member** | Owns one or more areas; produces inventory content for that area. Overlap with Council membership is allowed and is often natural for senior ICs. | May or may not be on Council |
| **Facilitator** | Runs the process; manages the Council review session | May continue as Phase 1 facilitator |
| **Scribe** | Drafts the Reckoning Record document | Typically continues as Phase 1 scribe |

> **Critical detail:** the Reckoning Team is **not** the Council acting in producer mode. The Reckoning Team can include Council members, and senior ICs who happen to also sit on the Council are natural fits — but the *team that does the inventory work* and the *body that reviews and later seals* are distinct in role, even when membership overlaps. This separation defends the bottom-up signal: inventory comes from people close to the code, governance comes from the multi-role Council. Conflating them — for example, having the full Council attempt to do the inventory itself — defeats the purpose, since the Council does not have bandwidth to review massive existing codebases ([debate 002](debates/002-retrofit-vs-greenfield.md), Q2).

---

## 9. What is borrowed vs novel

| Component | Source |
|---|---|
| Current state audit + decision archaeology | Borrowed from M&A due diligence practice; software archaeology (Diomidis Spinellis); *Working Effectively with Legacy Code* (Michael Feathers) |
| Failure inventory with full attribution but blameless framing | Borrowed from blameless postmortem culture (John Allspaw, "Blameless PostMortems and a Just Culture", 2012); long-established practice in aviation safety (NTSB) and clinical medicine (root-cause analysis) |
| Implicit principles surface — independent capture before synthesis | Borrowed from organizational ethnography (Edgar Schein, *Organizational Culture and Leadership* — espoused vs in-use values); Delphi method for forecast aggregation |
| Bottom-up Reckoning Team (not Council) producing the inventory | Borrowed from open-source maintainer-driven processes (Linux subsystem maintainers, Apache committers); RUP's "spike" pattern for investigation work |
| PM-defined thresholds for significance, materiality, scope, cadence | Borrowed from PMBOK / PRINCE2 project sizing patterns; Lean Startup's "scope is the variable" principle |
| No sealing ceremony for Phase 0 | Borrowed from the engineering review pattern in IETF and W3C — investigation outputs feed governance bodies but are not themselves governance acts |
| **Phase 0 → Phase 1 hand-off without approval gate** | **Novel** — most prep phases require formal approval; here the Council is a reader, not a gate |
| **Implicit principles independent capture as a *required* step in retrofit governance** | **Novel** — surfaced as a methodology pattern but not previously codified at the governance level |
| **Single living Reckoning Record spanning Phase 0 and Phase 1** | **Novel** — combines pre-decision investigation with post-decision migration tracking in one document |

---

## Note on Method

This Phase 0 specification was authored after the project owner answered the six open questions carried forward from [debate 002](debates/002-retrofit-vs-greenfield.md). Their answers are baked into the design above:

| Question | Decision |
|---|---|
| Q1 — Phase 0 sealing? | No sealing. Output is input to Phase 1's session. The full Reckoning Record cannot exist until Phase 1 has produced the proposed Astronomican to classify against. |
| Q2 — Reckoning quorum? | Smaller Reckoning Team produces; Council reviews. Bottom-up because the Council cannot review a large existing codebase by itself. |
| Q3 — Past-blame protection? | Full attribution. History is a valuable lesson, the team must accept it to move forward, and git commits already record names. |
| Q4 — Cap on grandfather count? | No fixed cap. PM decides per project scale and complexity. |
| Q5 — Sunset horizon? | No fixed horizon. PM decides per item and project. |
| Q6 — Re-reckoning cadence? | PM-defined cadence, committed in writing inside the Reckoning Record itself, so it cannot be silently forgotten. |

Q4–Q6 live operationally inside Phase 1's Reckoning step (where classifications are made) and the Reckoning Record's living section, but the *policy* that the PM owns these decisions is established in Phase 0 inputs.

### Open questions — resolved

The four Phase 0 calibration questions were closed in [debate 003](debates/003-phase-0-calibration.md):

| Question | Resolution |
|---|---|
| Significance threshold heuristic | Categorical heuristic (6 bullets) is the default; PM tunes / extends / overrides. Anchored on ITIL CM, ISA 320 / GAAP / IFRS materiality, PMBOK EVM variance, CMMI CAR. PM walk-through in [pm-calibration-guide.md § 1](pm-calibration-guide.md#1-significance-threshold). |
| Reckoning Team composition rule | Promoted to rule: 2–5 people, ≥ 1 active-IC mandatory, ≥ 1 tenure-spanning when project age permits, ≥ 1 outside-scope when team size permits. Anchored on Brooks's Law, Two-pizza, Dunbar layered, Team Topologies. |
| Time-boxing semantics | Soft target with 80% / 100% structured escalation. Initial budget derived per PM tier — Tier 1 uses M&A IT due-diligence rule; Tier 2 uses simplified COCOMO II; Tier 3 uses CMMI PPB. |
| Greenfield "lightweight" Phase 0 | Default for greenfield projects: Assumption Surface + External Commitment Audit + Stakeholder & Integration Map. Time anchor: 1–3 days, or 1–2% of projected effort via COCOMO II planning mode. Full skip permitted only for solo / duo teams that have worked together before. |

**Framework-wide policy adopted alongside this resolution:** Dead Light Framework adopts industry-standard formulas; it does not invent new ones. Reference catalog: [calibration-standards.md](calibration-standards.md). Practical PM walk-through: [pm-calibration-guide.md](pm-calibration-guide.md).

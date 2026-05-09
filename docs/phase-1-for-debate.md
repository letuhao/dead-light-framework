# Phase 1 — The Astronomican (For Debate)

> **Status:** Draft, not final. To be refined through debate against the LoreWeave case study and from multiple critical angles before any element is canonized.
>
> **Purpose:** Lay out a complete first-cut definition of Phase 1 — its goal, prerequisites, activities, outputs, gates, failure modes, anti-patterns, and roles — so the structure can be argued with as a whole rather than discussed piece by piece in chat.

---

## 1. Goal (one sentence)

Phase 1 is complete when a sealed Astronomican exists that every participant — human or agent — can navigate by, and a Re-consecration process has been defined for any future change.

---

## 2. Inputs / Prerequisites

Before convening the Ascension Council:

- **Project mandate** — the problem to solve and who it is for, in 1–2 paragraphs.
- **Candidate Council list** — 3–7 people, each authorized to bind the project on behalf of their constituency.
- **Prior context** — what has already been built, what has failed, what is in flight. **For retrofit projects, this comes from the Reckoning Record produced by Phase 0; see section 10.**
- **Facilitator** — has no voting power; runs the process.
- **Scribe** — records discussion and drafts the document; does not debate.

---

## 3. Activities (sequence)

### Pre-work (1–2 weeks before the session)

- Each Council member independently answers five open questions:
  1. Why does this project exist?
  2. What must always be true?
  3. What must never be true?
  4. What is explicitly out of scope?
  5. What does failure look like?
- Facilitator aggregates answers, marks overlap and disagreement.

### Session (1–2 days, intensive)

1. **Read prior context.** Council reads the Project mandate together, plus a record of what has previously failed (if any).
2. **Define The Purpose.** One sentence, by full consensus. If consensus fails, Phase 1 stops here — the project itself is not aligned, and that is the real problem to solve first.
3. **Draft Immutable Laws.** Propose, stress-test, prune. **Hard cap 9; target ~7** (Miller 7±2 working-memory range; see [debate 004](debates/004-cap-revision-miller-correction.md)). Below 5 is permitted for narrowly-scoped projects but is reviewed by the Council, not auto-padded.
4. **Draft Guiding Principles.** Propose, stress-test, prune. **Hard cap 9; target ~7** (same anchor as Laws).
5. **Define Boundaries.** Concrete list of what the project is NOT.
6. **Stress test the whole.** Run 5–10 hard scenarios. Each Council member decides independently using the Astronomican, then results are compared. Divergence is a signal of remaining vagueness — fix immediately.
7. **Sealing ceremony.** All Council members sign. The document is committed to immutable storage (signed git tag or equivalent).

### Post-session

- **Public proclamation.** Astronomican v1.0 broadcast to every participant.
- **Setup runtime references.** Agents load the Astronomican into their system prompt; humans reference it in every review and decision.

---

## 4. Outputs / Artifacts

| Artifact | Format | Status after Phase 1 |
|---|---|---|
| **The Astronomican v1.0** | Markdown, ≤ 2 pages | Sealed, immutable |
| **Ascension Council Record** | Names + roles + date + signatures | Append-only |
| **Re-consecration Playbook** | Markdown, defines when and how to amend | Living document |
| **Stress Test Log** | Scenarios run + results per Council member | Reference only |
| **Codex Slot Placeholders** | One stub file per planned Chapter | Empty, filled in later phases |

---

## 5. Quality Gates — when is Phase 1 actually done?

Phase 1 is NOT done until all of the following are true:

- [ ] Every Council member can articulate The Purpose **without reading** the document.
- [ ] Every Immutable Law has at least one example of violation and one of compliance.
- [ ] Every Guiding Principle has both an Intent statement and a Direction statement.
- [ ] Boundaries contains at least three explicit items (guards against vagueness).
- [ ] Stress test covers ≥ 5 scenarios; divergence rate between Council members < 20%.
- [ ] All Council members have signed.
- [ ] Document exists in immutable storage (signed git tag, hash-pinned commit, or equivalent).
- [ ] At least one agent has been test-run with the Astronomican as system prompt and produced output consistent with the Laws.

---

## 6. Failure Modes — signals Phase 1 has gone off-track

| Signal | Diagnosis |
|---|---|
| Council cannot agree on Purpose after two rounds | Disagreement is upstream of Phase 1 — the project itself is not aligned. Stop and resolve before continuing. |
| Laws read as platitudes ("good code", "best UX") | Too vague — will not be enforceable. |
| Laws read as coding instructions ("use PostgreSQL", "use React") | Too specific — belong in Codex or ADR, not the Astronomican. |
| More than 9 Laws or 9 Principles | Bloat — past Miller's upper bound (7±2). Each extra item adds an interpretation surface and breaks the recall premise. Force a cut. (Cap revised in [debate 004](debates/004-cap-revision-miller-correction.md).) |
| Document keeps being edited after "sealing" | The seal was symbolic only — either ceremony was skipped or the Council lacked binding authority. |
| Stress-test divergence > 20% | Wording is still ambiguous; humans and agents will interpret differently at runtime. |
| Boundaries section is empty | The project will scope-creep. Boundaries are the vaccine; an empty list means no immunity. |

---

## 7. Anti-patterns — what NOT to do

- **Skip the ceremony.** "The team is already aligned, we don't need a meeting." Six months later, every member remembers something different.
- **Single-author draft with rubber-stamp approval.** Bypasses collective sealing; produces no psychological commitment.
- **Mix Laws and Principles in one tier.** Loses the hard/soft distinction — the whole point of two tiers.
- **Write Laws before agreeing on Purpose.** Building principles without a north star.
- **Seal before stress-testing.** Vagueness is found after immutability — forces immediate Re-consecration, which destroys the credibility of sealing.
- **Council with uniform background.** Loses the diversity that catches blind spots; consensus arrives faster but is weaker.
- **Council too large (> 7).** Past the Dunbar threshold for small-group decision quality.
- **Treat the Astronomican as marketing.** Written to impress rather than to bind.
- **Use small team size as an excuse to skip Phase 1 or violate the Council minimum-diversity rule.** Where literal humans cannot fill three distinct functional perspectives, AI assistants — invoked as specific Chapters with explicit Codex — can serve as **aides** to the absent functional roles. Aides surface arguments, stress-test proposals, and provide the perspective the missing role would have offered; they do not vote, do not sign the seal, and are not Council members in any voting sense. Voting authority remains exclusively with named humans. Their use is **named in the Ascension Council Record** (which Chapter and Codex stood in for which functional perspective). The specific Chapters and their Codexes are deferred to **Phase 2 (Codex per Chapter)** — the framework's planned next phase — and are not yet defined here.

---

## 8. Roles in Phase 1

### 8.1 Council composition (multi-role)

The Ascension Council is **not a single-role body**. It is a small assembly of people, each bringing a distinct functional perspective. Voting authority is held collectively, but the *quality* of decisions depends on the diversity of perspectives present.

| Role on the Council | What this role contributes |
|---|---|
| **Sponsor / Mandate holder** | Mandate, business context, ultimate accountability |
| **PM (Product Manager / Owner)** | Scope, customer needs, market reality. In retrofit projects, also owns the Phase 0 threshold decisions (significance, materiality, scope, time-budget, re-reckoning cadence). |
| **Tech Lead / Architect** | Technical direction, system-level constraints |
| **Senior IC / Maintainer** | Code-level perspective, bottom-up signal, reality-check on technical proposals |
| **Domain Expert / SME** | Subject-matter authority for the project's domain (legal, security, ML, regulated industries — when applicable) |
| **Other functional perspectives** | As the project requires — UX, security, data, ops, compliance, etc. |

**Minimum-diversity rule.** A valid Council must include at least **three distinct functional perspectives** drawn from the list above — typically product/scope, technical direction, and operational/code. A Council composed entirely of one functional type (all architects, all PMs, all senior managers) is structurally one-sided and produces single-perspective Astronomicans.

Council size remains **3–7 members** (within the existing framework constraint). The minimum-diversity rule applies regardless of size.

This composition rule has direct precedent in real-world boards: corporate boards of directors prescribe role diversity (independent + executive + functional specialists); IETF working groups balance vendor + operator + academic; the Federal Reserve Board of Governors balances geographic + economic perspectives. The pattern is consistent: governance bodies that are functionally homogeneous produce one-sided outputs.

**Small-team accommodation.** Where literal humans cannot fill three distinct functional perspectives, AI assistants — invoked as specific Chapters with explicit Codex — may serve as **aides** to the missing perspectives. Aides surface arguments and analysis; they do not vote and do not sign. The Chapter and Codex specifications for this purpose are deferred to **Phase 2 (Codex per Chapter)**. This accommodation is on-thesis with Dead Light Framework's foundational stance: humans + agents collaborate, but humans alone hold binding authority.

### 8.2 Supporting roles (not Council)

| Role | During Phase 1 | After Phase 1 |
|---|---|---|
| **Facilitator** | Runs the process; no vote | May become a High Lord, or step aside |
| **Scribe** | Records discussion; drafts the document | May become the document steward |

### 8.3 Future roles (post-Phase 1)

| Role | Source | Authority |
|---|---|---|
| **High Lord** | Typically subset of Council | Interpretation authority over the Astronomican |
| **Planetary Governor** | From Council or appointed later | Module-level application |

> **Critical detail:** the Ascension Council **disbands** after sealing. It is not a standing body. Any future change to the Astronomican requires convening a *new* Council via the Re-consecration process — this is a feature, not a bug. It creates a *psychological cost* for change that defends against drift.

---

## 9. Scaling — Imperial Astronomican and Sector Astronomicans

Phase 1 produces a **single Astronomican** by default. For projects spanning multiple repositories or services with dedicated teams, an Imperial + Sector tier may be required. This decision was reached in [debate 001](debates/001-laws-count-and-multirepo-scaling.md).

### Trigger — when to split

Adopt Sector Astronomicans only when **all** of the following are true:

- ≥ 2 repositories or services that deploy independently
- Each has a dedicated team or on-call rotation
- Cross-team contracts (API, schema) exist and must be negotiated
- Genuinely local decisions exist that the Imperial Council should not be making

Below this threshold: keep a single Astronomican. Use Codex per Chapter for agent governance and ADRs for tech specifics.

### Imperial Astronomican

- Same structure as the default Astronomican (Purpose / Immutable Laws / Guiding Principles / Boundaries).
- Binds every Sector below.
- Sealed at Imperial Phase 1; this always runs first when Sectors are planned.

### Sector Astronomican

- **Inherits all Imperial Laws** — they cannot be relaxed, only tightened.
- Adds up to 9 local Laws and 9 local Principles (target ~7) within Imperial bounds. Same Miller-7±2 anchor as the Imperial cap; see [debate 004](debates/004-cap-revision-miller-correction.md).
- Has its own Boundaries.
- Sealed by a Sector Ascension Council (subset of Imperial Council + local leads).
- Re-consecration scope is local; Imperial-level Re-consecration invalidates all Sector inheritance and forces every Sector to re-review.

### Ordering rule

Imperial Phase 1 must complete before any Sector Phase 1 begins. This is non-negotiable — without it, Sectors would define Laws against a moving target and inheritance breaks.

### Real-world precedent

The Imperial + Sector pattern is borrowed directly from constitutional federalism (US, Germany), the Catholic Church's Canon Law plus diocesan customs, the Linux kernel's whole-tree standards plus subsystem rules, Toyota's TPS plus plant-level kaizen, and AWS Leadership Principles plus team Tenets. The framework is not inventing a new structure — it is adopting a structure with multiple multi-decade-to-multi-century track records.

---

## 10. Retrofit — Phase 0 Reckoning and Phase 1 Additions

Most real-world adoptions of the framework are not greenfield. The framework distinguishes:

- **Greenfield** — fresh project, no prior code, no prior architectural decisions. Default Phase 1 applies as written in sections 1–9.
- **Retrofit** — project already in flight, with existing code, decisions, and team habits. Requires a preceding **Phase 0: Reckoning** plus the additions described in this section.

This decision was reached in [debate 002](debates/002-retrofit-vs-greenfield.md). Phase 0 itself will be defined in a separate document (`phase-0-for-debate.md`); only the interface with Phase 1 is summarized here.

### 10.1 Phase 0 prerequisite (retrofit-only)

Phase 0 produces a **Reckoning Record draft** (inventory portion) as input to Phase 1. Phase 1 cannot begin until this draft exists and the Council has reviewed it. The full Reckoning Record reaches v1.0 only when Phase 1 seals the Astronomican — Phase 1's Reckoning step adds the classification section to the same document. This is non-negotiable: without the inventory, the session would proceed against an unsurfaced past and seal hollowly.

Phase 0 is defined in detail in [phase-0-for-debate.md](phase-0-for-debate.md). For Phase 1's purposes, the inputs from Phase 0 are:

- **Current state audit** — services, deployments, contracts as they actually exist (not as planned).
- **Past decisions catalog with attribution** — significant scope changes, architectural pivots, abandoned directions, named decision-makers, with date and context.
- **Failure inventory with attribution** — concrete past failures with dates, blast radius, named participants, and root cause where known. Blameless framing.
- **Implicit principles surface** — independent contributions from each Reckoning Team member naming what they believe the team has been operating under, with contradictions preserved (not smoothed).

The Reckoning Team that produces this inventory is **not** the Council — it is a smaller bottom-up team (2–5 people including ICs who maintain the code), reflecting the principle that the Council does not have bandwidth to review massive existing codebases.

### 10.2 Session additions (retrofit-only)

A **Reckoning step** is inserted between Boundaries (activity 5) and Stress Test (activity 6). The Council classifies each significant past decision under the proposed Astronomican into one of four buckets:

- **Keep** — consistent with the proposed Astronomican; no action.
- **Fix-now** — violates an Immutable Law and must be fixed before sealing.
- **Fix-by-date** — violates but is recognized; recorded with named owner and sunset date in the Reckoning Record.
- **Reconsider Law** — the proposed Law is too strict for project reality; weaken it, soften it to a Guiding Principle, or remove it.

Stress test scenarios (activity 6) are drawn from the actual past failure inventory, not hypotheticals. The test asks: *would the proposed Astronomican have prevented this?* If the answer is "nothing different" or "permitted it," the Astronomican is reworked.

### 10.3 Output additions (retrofit-only)

In addition to the standard outputs of section 4:

- **Reckoning Record** — carried forward from Phase 0; amended during the session with classifications. Lives outside the Astronomican as a living document.
- **Migration Plan** — extraction of Fix-now and Fix-by-date items as actionable backlog with named owners and explicit dates.

### 10.4 Quality-gate additions (retrofit-only)

All gates from section 5 apply, plus:

- [ ] Reckoning is complete — every significant past decision is classified.
- [ ] Migration plan has named owners and explicit dates, not aspirational language.
- [ ] At least one prior failure is explicitly addressed by a proposed Immutable Law (proves the Law has historical teeth, not abstract aspiration).

### 10.5 Failure-mode additions (retrofit-only)

In addition to the failure modes of section 6:

| Signal | Diagnosis |
|---|---|
| Reckoning paralysis — Council cannot agree on past classifications | The real operating principles are unspoken and the team is divergent on them. Surface that divergence first, then return to the proposed Astronomican. |
| Mass grandfathering — too many items in Fix-by-date with vague dates | Council is avoiding hard tradeoffs. Cap grandfather count or require sunset within a fixed horizon. |
| Past-blame dynamics — past decision-makers feel personally attacked | Facilitator must reframe reckoning as architectural learning, not personal review. Adopt a "no fault, just facts" tone — only decisions and outcomes are reviewed, not the people who made them. |

### 10.6 Effective-date semantics

When the Astronomican is sealed in a retrofit Phase 1:

- All future decisions are bound immediately upon sealing.
- Past decisions classified **Keep** stand as-is.
- Past decisions classified **Fix-now** have already been resolved as a precondition for sealing.
- Past decisions classified **Fix-by-date** are tracked in the Reckoning Record with explicit sunset dates; the Reckoning Record is a living document outside the Astronomican.
- Past decisions classified **Reconsider Law** indicate the Astronomican itself was weakened during the session; the final sealed Astronomican already reflects this.

This produces a hybrid effective-date model: reckoning-first determines status at sealing, sunsets carry forward through the Reckoning Record. The Astronomican itself stays clean and stable.

### 10.7 Open questions — resolved

The six open questions carried forward from [debate 002](debates/002-retrofit-vs-greenfield.md) were answered by the project owner and baked into [phase-0-for-debate.md](phase-0-for-debate.md):

| Question | Decision |
|---|---|
| Phase 0 sealing | No sealing. Output is input to Phase 1; the full Reckoning Record is completed by Phase 1's Reckoning step. |
| Reckoning quorum | Smaller Reckoning Team produces; Council reviews. Bottom-up because Council cannot review massive existing codebases. |
| Past-blame protection | Full attribution. History is a valuable lesson; git commits already record names; hiding actors hides social structure. Blameless framing, not anonymous. |
| Cap on grandfather count | No fixed cap. PM decides per project scale and complexity. |
| Sunset horizon | No fixed horizon. PM decides per item and project. |
| Re-reckoning cadence | PM-defined cadence committed in writing inside the Reckoning Record. |

Questions 4–6 manifest operationally in this Phase 1 section: the Reckoning step accepts the PM's policies as inputs and applies them when classifying past decisions.

---

## 11. What is borrowed vs novel

| Component | Source |
|---|---|
| Five pre-work questions | Borrowed from Agile Inception Deck |
| NOT list / Boundaries | Borrowed from Agile Inception Deck |
| Sign-off ceremony | Borrowed from RUP Lifecycle Objective Milestone + PRINCE2 PID approval |
| Re-consecration playbook structure | Borrowed from PRINCE2 Change Control, with stricter cost |
| Stakeholder register pattern | Borrowed from PMBOK |
| **Two-tier hardness (Laws / Principles)** | Novel |
| **Sealing as one-shot, Council disbands** | Novel |
| **Stress test with divergence threshold** | Novel |
| **Format constraint for agent recital (ID-addressable, system-prompt-able)** | Novel |
| **Quality gate "recite without reading"** | Borrowed in spirit from military doctrine drilling; novel applied to software |
| **Imperial + Sector tier with inherit-and-add rule** | Borrowed from constitutional federalism, Catholic Church canon law plus diocesan customs, Linux kernel maintainer tree, Toyota TPS plus plant kaizen |
| **Phase 0: Reckoning + retrofit-aware Phase 1** | Borrowed from constitutional retrofit precedents (Japan 1947, Spain 1978, South Africa TRC 1996), corporate transformation patterns (Microsoft / Nadella, Apple / Jobs 1997), Toyota's Ohno-circle exercise, Linux kernel CoC effective-date model, and the Strangler Fig refactoring pattern (Fowler) |

---

## Note on Method

This draft is intentionally specific — it commits to numbers (5 Laws max, 7 Council members max, 20% divergence threshold, 1–2 day session), to ordering (Purpose before Laws), and to ceremony design (Council disbands). Specificity is a debate aid: it is easier to argue against a number than against a vague stance.

The numbers and rules will move. The structure of the phase — pre-work, intensive session, sealing, post-session — is the part most likely to survive intact.

Outstanding open questions (carry into debate):

- **Council size lower bound** — is 3 truly enough, or is it too few for diversity?
- **Pre-work depth** — five questions sufficient, or do agentic projects need a sixth on agent boundaries?
- **Session format** — co-located vs distributed; impact on sealing ritual.
- **Storage of seal** — is signed git tag enough, or is something stronger needed (notarized hash, multi-sig commit)?
- **First-time vs retrofit** — applying Phase 1 to a fresh project vs to an existing project mid-rot (the LoreWeave case). Same activities, different inputs and risks.
- **Failure of sealing** — what happens when stress test divergence > 20% on the day of sealing? Postpone? Reduce scope of Astronomican? Disband and start over?

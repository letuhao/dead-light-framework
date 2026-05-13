# Glossary — For Debate

> **Status:** Working document, not final. The official glossary will be assembled bottom-up while we define each phase of the framework against the LoreWeave case study.
>
> **Purpose:** Capture all candidate concepts in one place so we can debate them from multiple angles (necessity, naming, redundancy, scope) before any term is canonized.

---

## Scoping Principle

Dead Light Framework is **agentic AI governance focused**. It does not replace existing software development processes (Agile, Scrum, RUP, …). It composes on top of them.

A concept enters the glossary only if at least one is true:

1. **Genuinely new** — no traditional analog; without defining it the framework cannot be discussed.
2. **Redefined deeply enough** — reusing the existing name would mislead.
3. **Names a governance failure mode** the framework explicitly defends against.

If a concept already exists fine in Scrum / Agile / RUP / DevOps and Dead Light does not change its meaning, it stays out — we reference it externally instead.

---

## Candidate Concepts (25)

Status legend:
- **strong-keep** — high confidence the concept must be defined.
- **needs-debate** — has a reason to exist but warrants critique (necessity, naming, overlap, scope).

### Group A — The Beacon (frozen authority artifact)

| # | Term | Status | Rationale |
|---|------|--------|-----------|
| 1 | **The Astronomican** | strong-keep | Central artifact of the framework; immutability semantics have no traditional analog. |
| 2 | **Immutable Law** | strong-keep | Top tier of the Astronomican. Name distinguishes hard commitment from soft guidance. |
| 3 | **Guiding Principle** | strong-keep | Interpretable tier (intent fixed, implementation flexible). Pairs with Immutable Law. |
| 4 | **The Purpose** | needs-debate | Single-sentence north star. Used as "recital test" — but might be a subsection of Astronomican rather than a glossary entry. |
| 5 | **The Boundaries** | needs-debate | Explicit out-of-scope statements. Same edge case — could be subsection only. |

### Group B — Ceremonies (governance events)

| # | Term | Status | Rationale |
|---|------|--------|-----------|
| 6 | **The Ascension Council** | strong-keep | One-time gathering that seals the Astronomican. Specific composition + one-shot semantics. |
| 7 | **The Sealing** | needs-debate | The act of finalization. Possibly redundant with Ascension Council. |
| 8 | **Re-consecration** | strong-keep | Process to amend a sealed Astronomican. Without this, framework is brittle — either rigid or silently mutable. |

### Group C — Human governance roles

| # | Term | Status | Rationale |
|---|------|--------|-----------|
| 9 | **High Lord (of Terra)** | strong-keep | Interpretation authority over the Astronomican. Does not map cleanly to PM / TL / Architect — sole job is interpretation, not delivery. |
| 10 | **Planetary Governor** | strong-keep | Human leading a module, applies Astronomican locally. Distinct from Tech Lead — authority comes from stewarding the beacon locally, not engineering seniority. |
| 11 | **Inquisitor** | needs-debate | Drift detection / enforcement role. Tightly linked to Heresy. Question: does this need to be a role, or a function performed by High Lords / Planetary Governors? |

### Group D — Agent concepts (the genuinely new layer)

| # | Term | Status | Rationale |
|---|------|--------|-----------|
| 12 | **Chapter** | strong-keep | A class/type of agent (e.g., the CodeReview Chapter). "Agent" alone is too generic — needs a unit name. |
| 13 | **Codex** | strong-keep | The document defining a Chapter's bounds, hard stops, autonomy threshold, output contract. No traditional analog. |
| 14 | **Operational Bounds** | strong-keep | What an agent CAN do. "Permissions" is technical; "bounds" is governance-level. |
| 15 | **Hard Stop** | strong-keep | Conditions forcing an agent to halt and escalate. Distinct from generic error handling. |
| 16 | **Autonomy Threshold** | strong-keep | Confidence/risk level above which an agent acts solo. Parametrizes the human-in-the-loop decision. |
| 17 | **Tithe** | needs-debate | Mandated output contract format. Strong 40k flavor — debate whether to use plain "Output Contract". |
| 18 | **Battle Brother** | needs-debate | An instance of a Chapter (one running agent). Question: does class-vs-instance distinction matter at governance level? Probable cut. |

### Group E — Failure modes (The Chaos)

| # | Term | Status | Rationale |
|---|------|--------|-----------|
| 19 | **The Chaos** | strong-keep | Umbrella term for failure modes the framework defends against. Lets us talk about defense holistically. |
| 20 | **Heresy** | strong-keep | A specific deviation from the Astronomican. Has a defined governance response (investigation, possibly Re-consecration). |
| 21 | **Corruption** | needs-debate | Gradual drift in agent behavior or codebase. Possibly redundant with Heresy. Question: is the distinction "Heresy = single sharp violation, Corruption = accumulated drift" worth two terms? |
| 22 | **Schism** | needs-debate | Irreconcilable interpretation conflict between High Lords. Distinct governance event needing a tiebreaker process. |

**Cross-reference to current AI-dev discourse.** The pattern The Chaos (#19) names — particularly its accumulated-drift sub-modes — is widely called **"vibe coding"** in current community usage (term popularized by Andrej Karpathy, 2025). The framework's vocabulary is more precise (separates Heresy = sharp violation, Corruption = accumulated drift, Chaos = umbrella; vibe coding sits closest to Corruption + Chaos), but "vibe coding" is the natural external bridge when explaining the framework to readers outside this vocabulary. Not a glossary entry on its own — referenced for outward-facing communication only.

### Group F — Detection & feedback

| # | Term | Status | Rationale |
|---|------|--------|-----------|
| 23 | **Heresy Detection** | needs-debate | Sensors/processes that flag drift. Question: is this a concept or just an activity? Maybe describable without a glossary entry. |
| 24 | **Astropathic Signal** | needs-debate | Bottom-up escalation channel to High Lords. Fixes the upward-signal failure of the canonical Imperium. Strong 40k flavor — alternative name possible. |
| 25 | **Astronomican Reading** | needs-debate | Periodic re-read ceremony to keep team aligned. Anti–context-rot mechanism. Question: ceremony vs habit — does it deserve a named term? |

---

## Concepts Considered but Excluded (Out of Scope)

| Concept | Reason for exclusion |
|---|---|
| Sprint, Iteration, Velocity | Scrum / Agile owns these. |
| Backlog, Story, Epic | Agile owns these. |
| ADR (Architecture Decision Record) | Exists fine. Immutable Laws may *be expressed as* ADRs, but the ADR concept itself is not ours. |
| Code Review | Existing engineering process. |
| Definition of Ready / Definition of Done | Delivery process owns these. |
| Postmortem | Exists fine. Heresy investigation may use postmortem format without redefining the term. |
| RACI matrix | Exists fine. We may publish a Dead Light–shaped RACI variant in a separate doc, but the concept itself stays. |
| Sprint planning, Retrospective | Delivery process owns these. |
| Release management | Existing process. |
| Incident, On-call | Operations owns these. |

---

## Summary

- **25 candidates** across 6 groups.
- **14 strong-keep** — high confidence inclusion.
- **11 needs-debate** — concept has a reason to exist but warrants critique.

### Strong-keep (14)
#1, #2, #3, #6, #8, #9, #10, #12, #13, #14, #15, #16, #19, #20

### Needs-debate (11)
#4, #5, #7, #11, #17, #18, #21, #22, #23, #24, #25

---

## Note on Method

The final glossary will not be authored upfront from this list. Instead, it will be assembled **bottom-up while defining each phase of the framework against the LoreWeave case study**. This mirrors how I understand mature software methodologies to have been distilled — from accumulated mistakes and concrete lessons, not from speculative taxonomy.

This document exists to be argued with, pruned, renamed, and partially abandoned as the phases force real definitions into the open.

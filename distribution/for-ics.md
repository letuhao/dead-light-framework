---
title: Reading guide for ICs
status: working
version: 0.6.0
audience: human
type: readme
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Reading guide for Individual Contributors / engineers / maintainers.
> **Audience:** Human — ICs.
> **Purpose:** Understand what your role looks like when your team adopts Dead Light.
> **Read next if:** you're an engineer / maintainer and your team is adopting Dead Light.

# For ICs / Engineers — How Dead Light affects your work

## What you need to know

Dead Light is a **governance layer on top of your existing development methodology** (Scrum / Kanban / your delivery framework). It does not replace Scrum or any delivery rhythm. It adds:

- A **sealed source of authority** (the Astronomican) that no participant — including AI agents you work with — can rewrite at will.
- **Continuous principle-referenced decision-making** instead of after-the-fact correction.
- **Codex per Chapter** — explicit operational bounds for AI agent types working alongside you.

## Read these (light reads)

1. **`framework/phases/phase-0.md` §3 Activities** — what the Reckoning Team produces. If you're an active maintainer ("active IC who maintains code in scope"), you're a likely Reckoning Team member.
2. **`framework/phases/phase-0.md` §6 Failure Modes** — the anti-patterns to watch for if you participate.
3. **`framework/chapters/adeptus-administratum/codex.md`** — when an AI aide is working alongside you, this is the bounds it operates under. The §3 Hard Stops + §7 Authority bounds are what to expect.

## Your role specifically

You're typically:

- **A Reckoning Team member during Phase 0** — produce inventory content for your area (current state, past decisions you remember, failures you witnessed, implicit principles you operate under).
- **A possible Council member during Phase 1** — depends on your role + the project's minimum-diversity rule (per phase-1 §8.1).
- **A consumer of the sealed Astronomican post-Phase 1** — your work is bound by it; you flag heresies; you propose Re-consecration if a Law no longer fits reality.

## What changes vs traditional development

- Decisions you contribute (architectural pivots, scope changes, technical choices) get **attribution** in the Past Decisions Catalog. Per the framework's "names are kept, blame is not assigned" framing (debate 002 Q3), this is institutional learning, not personal review.
- AI agents working with you have **explicit bounds** (the Codex). If an agent does something it shouldn't, it's a Codex §5 N-1/N-2 notify; you raise it.
- Refactors that contradict prior decisions trigger **architect-rot detection** (framework's central concern per README anchors on Bommasani 2021 / Park 2023).

## Example to learn from

`examples/lore-weave-snapshot/methodology-notes.md` — see the spec departures (D-1, D-2, D-3) the LoreWeave project recorded when applying the framework. Real engagement, real friction, real outcomes.

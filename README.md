# Dead Light Framework

> *The Emperor is all but dead. The light remains.*

An experimental development process for projects where humans and AI agents build together.

---

## Who is writing this

I am a working developer with roughly ten years of experience across a range of projects. I am not an academic, not an industry authority on software methodology, not a methodologist of any kind. I do not have a chair, a certification body, or a track record of published frameworks behind me.

What follows is a personal exploration: one practitioner's attempt at finding methods that hold up when AI agents become full-time teammates. It is published openly so the assumptions can be tested by people who have stood in front of the same problems.

If anything in this document sounds certain, treat that as a slip in tone, not a claim of authority. The framework is at hypothesis stage. Everything is in scope to be argued with.

---

## The Problem

Software methodologies — from Waterfall through Agile, Scrum, SAFe, RUP — were developed in eras when teams were entirely human. They implicitly assume:

- a stable group of decision-makers,
- shared memory across days, weeks, and meetings,
- correction in real time when scope or direction drifts.

When AI agents join the team as co-developers, those assumptions may not hold automatically. Not because the methodologies fail — but because they were never asked to design for participants whose memory and identity properties differ from a human teammate's:

- **Context rot** — agents lose the *why* behind past decisions and re-invent or contradict prior choices across sessions.
- **Architect rot** — without a fixed reference, refactors land in incompatible directions; both humans and agents drift.
- **Authority drift** — when many actors (humans + agents) can each "decide", nothing sticks.
- **Scope chaos** — agents amplify whatever the latest prompt suggests, including the wrong directions.

In recent AI-dev discourse this pattern has been called **"vibe coding"** — shipping code by feel with agents steering. It is wonderful for prototypes; it tends to compound rot when extended beyond them.

These are not coding bugs. They are *governance* gaps wearing technical disguises.

> **Empirical anchors for the AI-agent properties above.** The "stateless / context-bounded decision-maker" property of foundation-model agents is documented in Bommasani et al. 2021 (*On the Opportunities and Risks of Foundation Models*, Stanford CRFM, [arXiv:2108.07258](https://arxiv.org/abs/2108.07258)). Memory and identity limitations across sessions, and the resulting drift, are explored in Park et al. 2023 (*Generative Agents: Interactive Simulacra of Human Behavior*, UIST 2023). The framing of these as *governance* rather than *capability* problems aligns with practitioner observability literature on agentic systems published 2024–2026 by Anthropic, OpenAI, and Google. The piece Dead Light is *trying* to add is not the observation that agents lose context — that is already documented — but a hypothesis about what an authority layer that *survives* the loss could look like.

## The Thesis

Existing methodologies are not wrong. They were simply not designed with AI agents as first-class participants in scope.

Dead Light Framework is a **development process** that builds on top of those methodologies and tries to add one element they were not designed to include:

> **A frozen source of authority that no participant — human or agent — can rewrite at will.**

The project's founding principles are codified once by a small council, then *sealed*. Humans interpret and decide. Agents execute within bounds. Neither group obeys a person — both navigate by the same fixed light.

The metaphor is borrowed from Warhammer 40,000: the *Astronomican* is a beacon that still shines after its god-emperor has all but died, and the entire civilization steers by it. We use the metaphor because it names something real — *authority detached from any living agent* — that traditional methodologies were not designed to embed.

## How It Relates to Existing Methodologies

Dead Light is **not** a replacement for Agile, Scrum, or any delivery framework. It composes on top of them.

| Concern              | Where existing methodologies focus | What Dead Light tries to add as a layer |
|----------------------|------------------------------------|------------------------------------------|
| Vision               | Evolving by team consensus         | Codified, sealed, immutable              |
| Decision authority   | Distributed by role                | Anchored to principles, not people       |
| Agent participation  | Not addressed                      | Codex per agent type                     |
| Drift detection      | Retrospective via ceremony         | Continuous, principle-referenced         |
| Conflict resolution  | Hierarchy                          | Re-interpret the beacon                  |

If you adopt this, run Scrum or Kanban for delivery rhythm and use Dead Light for the layer above: who decides what, why, and how the answer survives both staff turnover and agent context loss.

## Core Concepts

> Each concept gets its own document. This README is only a map.

- **The Astronomican** — the sealed document of project purpose, immutable laws, and guiding principles.
- **The Ascension Council** — the one-time meeting of humans who seal the Astronomican before kickoff.
- **High Lords** — humans with interpretation authority over the Astronomican.
- **Planetary Governors** — humans leading individual modules of work.
- **Chapters** — agent types, each governed by its own *Codex* (operational bounds, hard stops, autonomy thresholds, output contracts).
- **The Chaos** — the failure modes the framework defends against: scope creep, architect rot, context drift, accumulated technical debt.

Full glossary: [framework/glossary.md](framework/glossary.md) *(planned)*

## The Astronomican Protocol

The framework is delivered as a sequence of phases. Earlier phases produce artifacts that later phases depend on.

| Phase | Name              | Produces                          |
|-------|-------------------|-----------------------------------|
| 1     | The Astronomican  | Sealed vision document            |
| 2     | *(planned)*       | Codex per agent Chapter           |
| 3     | *(planned)*       | Heresy detection / drift sensors  |
| 4     | *(planned)*       | Re-consecration process           |

Detailed protocol: [framework/phases/](framework/phases/) *(in flight; Phase 0 sealed, Phase 1 partial)*

## Case Study — LoreWeave

This framework was distilled from a working project: **LoreWeave**, a multi-agent platform for multilingual novel workflows. LoreWeave hit the failure modes Dead Light aims to mitigate — conflicting refactors, scope drift between human contributors and AI agents, accumulated context rot.

The lessons that motivated the framework's laws and principles are documented as a case study, covering what went wrong before any sealing process existed and what we hope to learn from applying it.

Case study: [case-studies/lore-weave/](case-studies/lore-weave/) *(Phase 0 in flight; folder skeleton drafted 2026-05-11)*

## Status

**Phase 1: Drafting.** Active work-in-progress. Concepts may change until the framework itself is sealed.

## Acknowledgment

Conceptual references to the Imperium of Mankind, the Emperor of Mankind, the High Lords of Terra, the Astronomican, and the Space Marine Chapters are inspired by Warhammer 40,000, a setting created by Games Workshop. Dead Light Framework is an independent practitioner exploration with no commercial intent and no affiliation with Games Workshop.

## License

MIT — see [LICENSE](LICENSE).

# Dead Light Framework

> *The Emperor is dead. The light remains.*

A software development process for the era when humans and AI agents build together.

---

## The Problem

Software methodologies — from Waterfall through Agile, Scrum, SAFe, RUP — were designed for teams of humans. They quietly assume:

- a stable group of decision-makers,
- shared memory across days, weeks, and meetings,
- correction in real time when scope or direction drifts.

When AI agents join the team as co-developers, those assumptions break:

- **Context rot** — agents lose the *why* behind past decisions and re-invent or contradict prior choices across sessions.
- **Architect rot** — without a fixed reference, refactors land in incompatible directions; both humans and agents drift.
- **Authority drift** — when many actors (humans + agents) can each "decide", nothing sticks.
- **Scope chaos** — agents amplify whatever the latest prompt suggests, including the wrong directions.

These are not coding bugs. They are *governance* failures wearing technical disguises.

## The Thesis

Existing methodologies are not wrong. They are *incomplete* for human + AI collaboration.

Dead Light Framework is a **development process** that builds on top of those methodologies and adds one missing element:

> **A frozen source of authority that no participant — human or agent — can rewrite at will.**

The project's founding principles are codified once by a small council, then *sealed*. Humans interpret and decide. Agents execute within bounds. Neither group obeys a person — both navigate by the same fixed light.

The metaphor is borrowed from Warhammer 40,000: the *Astronomican* is a beacon that still shines after its god-emperor has all but died, and the entire civilization steers by it. We use the metaphor because it names something real — *authority detached from any living agent* — that traditional methodologies do not address.

## How It Relates to Existing Methodologies

Dead Light is **not** a replacement for Agile, Scrum, or any delivery framework. It composes on top of them.

| Concern              | Existing methodologies   | Dead Light adds                    |
|----------------------|--------------------------|------------------------------------|
| Vision               | Often implicit, evolving | Codified, sealed, immutable        |
| Decision authority   | Distributed by role      | Anchored to principles, not people |
| Agent participation  | Not addressed            | Codex per agent type               |
| Drift detection      | Retrospective            | Continuous, principle-referenced   |
| Conflict resolution  | Hierarchy                | Re-interpret the beacon            |

Use Scrum or Kanban for delivery rhythm. Use Dead Light for the layer above: who decides what, why, and how the answer survives both staff turnover and agent context loss.

## Core Concepts

> Each concept gets its own document. This README is only a map.

- **The Astronomican** — the sealed document of project purpose, immutable laws, and guiding principles.
- **The Ascension Council** — the one-time meeting of humans who seal the Astronomican before kickoff.
- **High Lords** — humans with interpretation authority over the Astronomican.
- **Planetary Governors** — humans leading individual modules of work.
- **Chapters** — agent types, each governed by its own *Codex* (operational bounds, hard stops, autonomy thresholds, output contracts).
- **The Chaos** — the failure modes the framework defends against: scope creep, architect rot, context drift, accumulated technical debt.

Full glossary: [docs/glossary.md](docs/glossary.md) *(planned)*

## The Astronomican Protocol

The framework is delivered as a sequence of phases. Earlier phases produce artifacts that later phases depend on.

| Phase | Name              | Produces                          |
|-------|-------------------|-----------------------------------|
| 1     | The Astronomican  | Sealed vision document            |
| 2     | *(planned)*       | Codex per agent Chapter           |
| 3     | *(planned)*       | Heresy detection / drift sensors  |
| 4     | *(planned)*       | Re-consecration process           |

Detailed protocol: [docs/protocol/](docs/protocol/) *(planned)*

## Case Study — LoreWeave

This framework was distilled from a working project: **LoreWeave**, a multi-agent platform for multilingual novel workflows. LoreWeave hit the failure modes Dead Light is designed to prevent — conflicting refactors, scope drift between human contributors and AI agents, accumulated context rot.

The lessons that became the framework's laws and principles are documented as a case study, including what went wrong before any sealing process existed and what changed after one was applied.

Case study: [docs/case-study-lore-weave.md](docs/case-study-lore-weave.md) *(planned)*

## Status

**Phase 1: Drafting.** Active work-in-progress. Concepts may change until the framework itself is sealed.

## Acknowledgment

Conceptual references to the Imperium of Mankind, the Emperor of Mankind, the High Lords of Terra, the Astronomican, and the Space Marine Chapters are inspired by Warhammer 40,000, a setting created by Games Workshop. Dead Light Framework is an independent academic work with no commercial intent and no affiliation with Games Workshop.

## License

MIT — see [LICENSE](LICENSE).

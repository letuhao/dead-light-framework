---
title: The Emperor Is All But Dead. The Light Remains.
date: 2026-05-11
tags: [ai-agents, human-ai-collaboration, software-governance, methodology, experimental, frozen-authority, software-architecture, debate]
---

# The Emperor Is All But Dead. The Light Remains.

### An experimental governance framework for software teams of humans and AI agents — and a request to be argued with

> **Status: experimental. Unverified in the field. Looking for sparring partners more than followers.**
>
> **By:** a developer with ~10 years across many projects, not an academic or industry authority — full bio at [the bottom](#about-the-author).
>
> **Published:** 2026-05-11 · **~8 min read** · **Repository:** [github.com/letuhao/dead-light-framework](https://github.com/letuhao/dead-light-framework)

---

## TL;DR

I have been building software with AI agents long enough to see the same governance failure mode appear over and over: agents and humans contradicting Monday's decisions on Wednesday, layers leaking into each other, no anchor to navigate by. I am testing the hypothesis that **human + AI software projects need a frozen source of authority that no participant — including the author — can rewrite at will.** This post is the opening of an open debate; sharper arguments against it would help me more than agreement.

> **One question I most want to be wrong about:** Is "frozen authority" actually compatible with "evolutionary architecture"? I think yes — argue with me.

---

## The pain I keep running into

I have been building software with AI agents long enough — daily, across multiple projects — to recognize a pattern that does not look like a bug.

On Monday, an agent and I agree that the auth layer should not know about billing. On Wednesday, a different session of the same agent cheerfully imports a billing helper into the auth module, because the prompt of the day made it convenient. The change passes review, because the human reviewer has also forgotten the Monday conversation. By the time anyone notices, the layering decision has been quietly inverted in three places.

Another version of the same story: I commit a fix with a comment explaining *why* a specific branch of code must stay. Two days later, a fresh agent session is sent in to clean up TODOs and reads the comment as a TODO. By morning the carefully-preserved branch is gone, and the previous session's reasoning died with the previous session.

This is not a model failure. It is not a human failure either. It is the predictable result of a team in which:

- **Some members are stateless.** Foundation-model agents have well-documented memory and identity limits across sessions (see Bommasani et al. 2021, *On the Opportunities and Risks of Foundation Models*; Park et al. 2023, *Generative Agents*).
- **The "why" behind past decisions is in nobody's working memory.** Humans forget. Agents don't even start with the context.
- **Many actors can each "decide".** When everyone has authority to nudge a direction, nothing actually sticks.
- **Latest input dominates.** Agents will amplify whatever the most recent prompt suggests, including the wrong directions.

I have come to think of these as **governance gaps wearing technical disguises.** No amount of better prompts, better tests, or better refactor discipline patches them. They are properties of the *team shape*, not of any single contributor.

---

## What we're fighting against — "The Chaos"

The failure pattern above has a name in this framework: **The Chaos.** It is the umbrella for four specific drift modes that tend to compound:

- **Context rot** — agents lose the *why* behind past decisions and re-invent or contradict prior choices across sessions (the Monday/Wednesday and TODO-misread stories above).
- **Architect rot** — without a fixed reference, refactors land in incompatible directions. Humans and agents drift further apart from any earlier coherent design.
- **Scope creep** — the project keeps absorbing new concerns. Agents amplify it because the latest prompt is always more vivid than the original mandate.
- **Accumulated technical debt** — local conveniences that, once normal, are hard to undo. Humans and agents together can ship more of it, faster than a single human could.

This is roughly what the AI-dev community has lately started calling **"vibe coding"**: shipping code by feel, with agents steering, no anchor strong enough to make Monday's promise survive into Wednesday's commit. Vibe coding is wonderful for prototypes. It is brutal for anything that has to outlive a single session.

The framework's job is not to forbid vibe coding. It is to give a project enough of a fixed backdrop that, when it graduates from prototype to *thing-people-rely-on*, decisions can be made against something stable instead of against the void.

---

## Where existing methodologies leave a design slot empty

I want to be careful here, because this is the easiest place to overreach.

Waterfall, Agile, Scrum, SAFe, RUP — these work. I am not in a position to grade them. If an AI agent shows up to a stand-up the way a competent teammate does — persistent role, accountable for decisions, reads the working agreements, follows what was decided yesterday — Scrum runs the same as it always has. Sometimes better, frankly, because the agent does not forget the meeting on the drive home.

So I do not want to claim the methodologies "fail" or "stop covering" anything when agents join. That would be both arrogant and inaccurate.

What I do think is narrower: **none of these methodologies were designed with AI agents as first-class participants in mind.** They do not specify what an "agent role" looks like — its memory model, its onboarding procedure, its authority bounds, its drift profile, how its decisions are attributed across sessions. That is an unfilled design slot, not a coverage failure.

The Dead Light Framework is one attempt at filling that slot. It sits *on top of* whatever delivery framework you already run, not in place of it. If your Scrum is well-disciplined and your reviews are tight, you will catch some of the failure modes I described above without any of this. The framework is for the parts your existing process was never asked to handle in the first place.

---

## The hypothesis (the part you should attack)

The thing I am testing is one sentence:

> **A software project for humans + AI agents needs a frozen source of authority that no participant — human or agent — can rewrite at will.**

Codified once by a small council. Sealed before kickoff. Humans interpret it. Agents execute within it. Neither group obeys a *person* — both navigate by the same fixed light.

This is not a radical idea outside software. It is roughly how constitutional federalism works (the U.S. Constitution constrains every subsequent administration), how religious institutional canon works (the Nicene Creed is older than any living interpreter), how central-bank mandates work (a price-stability mandate outlasts any single governor), and how RFC-driven protocol governance works (TCP/IP does not get rewritten because a vendor finds it inconvenient).

What is novel — *if anything* — is applying this pattern at the level of an individual software project, with AI agents as first-class participants whose context windows guarantee the authority cannot live in their heads.

I call the sealed document the **Astronomican**. I call the sealing meeting the **Ascension Council**. I call the agent-type rulebooks **Codices**. The names are borrowed from Warhammer 40,000.

---

## About the metaphor (important)

I want to be honest about this up front, because it is the obvious objection.

The Imperium of Mankind in Warhammer 40,000 is a *cautionary tale*. It is grimdark by design: a bureaucratic, paranoid, ossified empire that fails spectacularly across ten thousand years. Picking it as a governance metaphor without acknowledging that is internally contradictory.

So I do not use it as evidence. The framework's policy, written into its own rules, is:

> **40k vocabulary is naming and shared metaphor only.** Every load-bearing argument must rest on a real-world system with an observable track record: constitutional federalism, military command-and-control doctrine, central-bank mandates, religious canon, established corporate practice (Toyota Production System, Amazon two-pizza teams), open-source governance, established software methodologies.

When the 40k name and the real-world precedent disagree, the real-world precedent governs. The Imperium provides memorable names. Toyota's Andon Cord, the U.S. military's C2/SIGINT loop, and Bezos-era Amazon's API mandate provide the actual design lessons — particularly on the hardest problem the Imperium itself failed at: **centralized authority combined with distributed sensing**.

If you find a place in the framework where I leaned on 40k *as an argument* rather than as a name, that is a finding. Please file it.

---

## Glossary — 40k terms used above

For readers who do not know Warhammer 40,000 — one-liners on each term used in this post.

> - **Astronomican** — In W40k, the psychic beacon that guides the Imperium's space travel after its god-emperor has all but died. **In this framework:** the name for the sealed project document of purpose, immutable laws, and guiding principles.
> - **Imperium of Mankind** — The fictional galactic empire in W40k. Used here only as a memorable source of names; *not* as a governance role model (the empire fails spectacularly in canon — that is part of why I quote it carefully).
> - **Codex / Codices** — In W40k, the rulebook each Space Marine Chapter operates under. **In this framework:** the rulebook each AI agent type operates under (operational bounds, hard stops, output contract, notify triggers).
> - **Adeptus Administratum** — In W40k, the Imperial bureau of records, taxation, and administrative logistics — the empire's "chief of paperwork." **In this framework:** the first sealed Chapter — a PM / High-Lord aide role.
> - **Ascension Council** — *Not* from canon. The framework's name for the one-time small group of humans who seal the project's founding document before kickoff and then disband.
> - **Chapter / Chapters** — In W40k, a self-contained battle order of Space Marines, each with its own Codex. **In this framework:** an agent *type*, each with its own Codex.
> - **The Chaos** — In W40k, the warp-based corrupting forces the Imperium fights eternally. **In this framework:** the umbrella failure mode the framework tries to defend against — context rot, architect rot, scope creep, accumulated technical debt; roughly the kind of drift "vibe coding" produces when extended beyond prototyping.

---

## What this is and is not

**This is:**
- A *composition layer* that sits on top of Agile / Scrum / Kanban / whatever you already run. It does not replace delivery rhythm.
- An attempt to give projects a constitution-like artifact and an explicit protocol for agent participation.
- A working hypothesis with a documented audit trail (38 findings against my own claims, all remediated, still openly listed).

**This is not:**
- Proven. I have one in-flight case study (a 358-KLOC project called LoreWeave). One case is not evidence. It is a smoke test.
- A productivity tool. It will add overhead before it removes any.
- A claim that you should run your project this way. It is a claim that the failure modes are real, that existing methodologies were simply not designed with agent participants in scope, and that *some* framing in this neighborhood is probably needed to fill that slot.

---

## Where this stands today

- Phase 0 (the calibration/audit phase for retrofit projects) — **sealed**.
- Phase 1 (the Astronomican itself) — partial. Six known open questions, listed publicly.
- Phase 2 (Codex per Chapter) — first Chapter sealed (a PM/High-Lord aide called the Adeptus Administratum). Others wait for real-project triggers.
- Phase 3 (drift detection) and Phase 4 (re-consecration) — not started.
- One case study (LoreWeave) — Phase 0 Pass 1 about to begin.
- Internal audit (Independent Verification Pass) — five of seven phases complete. The audit is public, including the times the framework failed its own audit.

Everything is in the open. The framework is being built in a single repo with full debate history.

Repository: [github.com/letuhao/dead-light-framework](https://github.com/letuhao/dead-light-framework)

---

## What I want from readers

Not converts. Arguments.

Specifically, I want people to attack these:

1. **Is "frozen authority" actually compatible with "evolutionary architecture"?** I think yes, with a re-consecration ceremony. But that ceremony is unsealed and you might convince me it is impossible.
2. **Does the 40k vocabulary do more harm than good?** I find it useful as memorable scaffolding for a debate-driven team. But it may be repelling readers who would otherwise engage.
3. **Where does an industry standard already do this job?** If COCOMO II / CMMI v3.0 / ITIL 4 / DORA already cover one of the gaps I think I am filling, I want to know before adding another box.
4. **What is the smallest experiment that would falsify the framework?** I am genuinely unsure how to design this. A failed retrofit on one project is suggestive, not conclusive.
5. **What did I import from the Imperium that I should not have?** I keep finding things. Help me find more.

---

## What's coming next

A short series of posts will work through:

- The case study in detail (where it hurt, with numbers).
- Why Agile/Scrum specifically do not cover this gap.
- The mechanics of sealing an Astronomican.
- The Codex pattern for AI agents.
- How the framework audits itself (and the times it has failed).
- The anti-patterns I knowingly imported from a fictional dying empire, and how I compensate.
- Open questions where the framework could still be wrong.
- A practical adoption sketch — without promising it works.

If any of the failure modes I described sound like the project you are in right now, I would especially like to hear from you. The framework is far more useful as a piñata than as a manifesto.

---

## About the author

A working developer with roughly ten years of experience across a range of projects. Not an academic, not an industry authority on software methodology, not a methodologist of any kind. No chair, no certification body, no track record of published frameworks behind me.

The Dead Light Framework — the subject of this post and the series it opens — is a personal exploration: one practitioner's attempt at finding methods that hold up when AI agents become full-time teammates. I publish it openly because I would rather be told I am wrong by people who have stood in front of the same problems than be politely ignored.

If I sounded certain anywhere above, treat that as a slip in tone, not a claim of authority. The framework is at hypothesis stage. Everything is in scope to be argued with.

---

> *The Emperor is all but dead. The light remains.*

**Repository:** [github.com/letuhao/dead-light-framework](https://github.com/letuhao/dead-light-framework)

*Independent practitioner exploration. No affiliation with Games Workshop. Repository MIT-licensed.*

---

#AIAgents #VibeCoding #HumanAICollaboration #SoftwareGovernance #Methodology #Experimental #FrozenAuthority #SoftwareArchitecture #Debate

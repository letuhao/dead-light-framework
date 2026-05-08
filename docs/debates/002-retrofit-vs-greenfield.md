# Debate 002 — Retrofit vs Greenfield Application of Phase 1

> **Status:** decided.
> **Opened:** 2026-05-08
> **Decided:** 2026-05-08
> **Decided by:** project owner
> **Affects:** [phase-1-for-debate.md](../phase-1-for-debate.md). Produces a new `phase-0-for-debate.md` as a follow-up artifact.
> **Raised by:** project owner — priority #1 in open-questions triage.

---

## The Question

Phase 1 as drafted assumes a fresh project: the Ascension Council convenes before kickoff, with no prior code, no prior architectural decisions, no formed habits. Most real adoptions — including LoreWeave — will instead be **retrofit**: applying Dead Light to a project already in flight, with existing code, accumulated decisions, and a team carrying both context and inertia.

What does Phase 1 need so that retrofit is neither silently inapplicable nor so lenient that the seal loses meaning?

---

## Why this matters now

LoreWeave is the framework's primary case study. It already has six service contracts, an extensive `docs/` tree spanning foundation through planning, and (per project owner) **multiple scope changes** prior to any sealing. If Phase 1 does not address retrofit, the framework cannot be applied to the project that motivated it — making Dead Light a thought experiment rather than a usable methodology.

---

## Key differences — greenfield vs retrofit

| Dimension | Greenfield | Retrofit |
|---|---|---|
| Existing code | None | Significant, often in production |
| Prior architectural decisions | None | Many, some implicit, some contradictory |
| Team habits and assumptions | Forming | Formed and load-bearing |
| Stakeholder commitments | Open | Customers, roadmap, integrations exist |
| Sunk cost | Zero | High; influences willingness to break things |
| Time pressure | Often deliberate | Often acute — rot is already hurting |
| Implicit operating principles | None to inherit | Many, usually unspoken |

Two of these dominate the design challenge for Phase 1:

- **Implicit principles already in use.** The team has been operating *as if* certain principles applied. Retrofit must surface these before formalizing new ones, or the new Astronomican will be talked about while the old implicit one is followed.
- **Past violations are inevitable.** Any meaningful Astronomican will be violated by some accumulated decisions. Phase 1 must say what happens to those, or sealing is hollow.

---

## Real-world precedents for retrofit governance

| Domain | Case | Lesson for Phase 1 |
|---|---|---|
| Constitutional law | Japan post-WWII (1947), Spain post-Franco (1978), South Africa post-apartheid (1996) | Retrofit constitutions need an explicit mechanism to handle past violations. South Africa's Truth & Reconciliation Commission is the strongest example. Without such a mechanism the new charter floats over an unaddressed history and erodes. |
| Corporate transformation | Microsoft under Satya Nadella (post-2014), Apple under Jobs's return (1997) | Both started by *cutting scope* before reaffirming principles. Apple killed ~70% of its product lines; Microsoft explicitly retired the "know-it-all" culture before declaring "learn-it-all". Retrofit governance often begins with destruction, not declaration. |
| Manufacturing | Toyota's TPS introduction to existing plants under Taiichi Ohno | Pattern: identify ONE concrete deviation as the starting wedge ("Ohno's circle" exercise), fix it visibly, then expand. Did not attempt wholesale retrofit. Useful when the team is overwhelmed by the scale of change needed. |
| Open source governance | Linux kernel Code of Conduct adoption (2018), Rust Foundation creation (2021), Docker → Moby split | "Effective date" with grandfathering of prior code and community behavior is universal. Retroactive enforcement of new rules on past behavior is universally rejected and creates lasting damage when attempted. |
| Software practice | ADR adoption mid-project | Common pattern: document existing decisions retroactively as ADRs *first*, then start writing new ones for future decisions. Surfacing the implicit precedes constraining the explicit. |
| Refactoring discipline | Strangler fig pattern (Martin Fowler, 2004) | Retrofit works as gradient, not flag-flip. New regime wraps old, gradually replaces. Big-bang rewrites correlate strongly with project death (Joel Spolsky, 2000). |

**Common pattern across all six precedents:** retrofit governance succeeds when it includes (a) explicit reckoning with the past, (b) clear effective-date semantics, (c) gradual rather than flag-flip transition.

---

## Design implications — what Phase 1 needs that it currently lacks

### Pre-work additions (retrofit-only)

- **Current state audit.** What is the codebase actually doing? Active services, deployments, contracts, integrations. Not what was planned — what exists.
- **Implicit principles surface.** Council members independently list the principles they think the team has been operating under. Aggregated, contradictions are usually visible — that is the point.
- **Past decisions catalog.** Significant scope changes, architectural pivots, abandoned directions. Each summarized in 1–3 sentences with date and rough cause.
- **Failure inventory.** Concrete past failures with dates, blast radius, and root cause where known. These become the most authoritative stress-test scenarios.

### Session additions (retrofit-only)

- **Reckoning step,** inserted between Boundaries and Stress Test. The Council classifies each significant past decision under the proposed Astronomican into one of four buckets:
  - **Keep** — consistent with the proposed Astronomican; no action.
  - **Fix-now** — violates an Immutable Law and must be fixed before sealing.
  - **Fix-by-date** — violates but is recognized; recorded with named owner and sunset date.
  - **Reconsider Law** — the proposed Law is too strict for the project's reality; weaken it, soften it to a Guiding Principle, or remove it.
- **Stress test on real past failures,** not hypotheticals. The Council walks the most damaging past failures and asks "would this Astronomican have prevented this?" If the answer is "nothing different" or "permitted it", the Astronomican is too lax and gets reworked.

### Output additions (retrofit-only)

- **Reckoning Record** — table of past decisions, classifications, owners, sunset dates. Lives outside the Astronomican (so the Astronomican stays stable; the Reckoning Record evolves as items are resolved).
- **Migration Plan** — extraction of Fix-now and Fix-by-date items into actionable backlog with named owners and explicit dates.

### Quality gate additions (retrofit-only)

All greenfield gates apply. Plus:
- Reckoning is complete — no significant past decision left unclassified.
- Migration plan has named owners and dates, not aspirational language.
- **At least one prior failure is explicitly addressed by a proposed Immutable Law.** This proves the Law has historical teeth and is not abstract aspiration.

### Failure-mode additions (retrofit-only)

- **Reckoning paralysis.** Council cannot agree on past classifications. Diagnosis: the *real* operating principles are unspoken and the team is divergent on them. Resolution: surface that divergence as the first agenda item, then return to the proposed Astronomican.
- **Mass grandfathering.** Too many items land in Fix-by-date with vague dates. Diagnosis: Council is avoiding hard tradeoffs. Resolution: cap grandfather count or require sunset dates within a fixed horizon.
- **Past-blame dynamics.** Past decision-makers feel personally attacked, withdraw support. Resolution: facilitator must frame reckoning as architectural learning, not personal review. The framework adopts a "no fault, just facts" tone — only decisions and outcomes are reviewed, not the people who made them.

---

## Sub-decision A — Process structure

How should the retrofit work be structured relative to greenfield Phase 1?

| Option | Structure | Pros | Cons |
|---|---|---|---|
| **A1.** Single Phase 1 with retrofit-specific sections | One phase, conditional sections | Framework appears unified | Greenfield and retrofit Phase 1s are different enough that conditional content gets ignored or skipped; no clear signal that the retrofit work is mandatory |
| **A2.** New Phase 0: Reckoning, before Phase 1 | Phase 0 mandatory for retrofits, optional/lightweight for greenfield | Surveying the past is genuinely different work from drafting forward principles; explicit naming forces it to be done | One more phase to learn |
| **A3.** Phase 1 (Greenfield) and Phase 1′ (Retrofit) as parallel variants | Two flows documented separately | No greenfield bloat | Doc duplication; risk of drift between the two |

**Recommendation: A2 — introduce Phase 0: Reckoning.**

Rationale:
- Surveying the past is genuinely different work from drafting forward principles. Conflating them dilutes both.
- Naming the work as a phase signals to teams that it must be done; teams cannot speed-run it inside an already-heavy Phase 1 session.
- Greenfield Phase 1 stays clean and identical to the current draft.
- Phase 0 can also serve a lightweight role for greenfield projects (mandate audit, stakeholder map) without being forced.
- This implies a future artifact: `phase-0-for-debate.md`. That is the next natural document, but its detailed content is out of scope for *this* debate.

---

## Sub-decision B — Effective-date model

When does the sealed Astronomican become binding on existing decisions?

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **B1.** Immediate binding | Future decisions bound on seal; past decisions stand unless explicitly migrated | Simple; doesn't dilute the seal | Codebase remains in known violation; team carries cognitive load of "old vs new" code permanently |
| **B2.** Grandfather with sunset | Past violations identified, given sunset dates | Bridges past to future; gives team time | Deadlines slip; framework relies on follow-through that may never come |
| **B3.** Reckoning-first, seal-after | Identify all violations *before* sealing; resolve each one's status as part of sealing | Codebase is consistent (or explicitly inconsistent with rationale) at moment of seal | Most rigorous; can block sealing for months on large projects |

**Recommendation: B3 hybridized with B2.**

Concretely:
- Reckoning identifies everything before sealing.
- Each item classified Keep / Fix-now / Fix-by-date / Reconsider-Law during the session.
- **Fix-now** items completed before sealing — typically narrow, high-leverage fixes.
- **Fix-by-date** items recorded with named owner and sunset date in the **Reckoning Record** (not in the Astronomican itself — the Astronomican stays stable; the Reckoning Record is the living migration document).
- Sealing proceeds as soon as all items have a classification, even if Fix-by-date work is still in flight.

Rationale:
- Pure immediate binding (B1) leaves the codebase in a known violation state on day one, eroding the seal's authority before it has any.
- Pure grandfather (B2) tempts teams to grandfather everything; the seal becomes a wish list.
- Pure reckoning-first (B3 alone) is impractical for large existing projects — would block sealing for months and the rot continues meanwhile.
- The hybrid keeps the Astronomican clean and the migration honest.

---

## Application to LoreWeave (sketch)

Detailed mapping comes after this debate is decided. As a sketch, retrofit Phase 1 applied to LoreWeave would:

1. **Phase 0: Reckoning.** Audit current state of `contracts/`, `docs/01_foundation/` through `docs/03_planning/`, deployed-vs-documented services. Catalog the scope changes the project owner has indicated occurred.
2. **Pre-work.** Council members independently surface implicit principles they believe LoreWeave has been operating under so far. Build the past-failure inventory — each scope change gets a 1–3 sentence summary with what triggered it.
3. **Session.** Explicit reckoning step. Each scope change classified: was it serving a principle that should become an Immutable Law? Was it scope creep that Boundaries should now forbid? Was it a real shift in understanding that should be honored and documented?
4. **Stress test using real past failures.** "When we changed scope from X to Y, what would the proposed Astronomican have done?" If the answer is "nothing different" or "permitted it", the Astronomican is reworked.
5. **Outputs.** Astronomican v1.0, Reckoning Record, and Migration Plan as required artifacts.

LoreWeave thus becomes the framework's first genuine retrofit run, generating real evidence to refine Phase 0 and Phase 1.

---

## Open questions remaining

1. **Phase 0 sealing** — does Phase 0 itself need a sealing ceremony for its outputs (Reckoning Record), or is its output simply an input to Phase 1's session?
2. **Reckoning quorum** — must all Council members participate in reckoning work, or can a smaller team produce a Reckoning Record for full Council review?
3. **Past-blame protection** — should the Reckoning Record include attribution (who decided what) for institutional memory, or stay anonymized for psychological safety? Tradeoff is real.
4. **Cap on grandfather count** — should there be a hard limit (e.g., max 10 Fix-by-date items) to prevent dilution? What number?
5. **Sunset horizon** — what is a reasonable upper bound for Fix-by-date sunset? Fixed (e.g., 90 days) or scaled with project size?
6. **Re-reckoning cadence** — does the Reckoning Record need periodic re-review (quarterly?) or only on Re-consecration events?

These do not need to be resolved in this debate but are flagged as the natural next debates if Phase 0 is adopted.

---

## Recommendation (TL;DR)

- **Yes — support retrofit explicitly.** Without it, the framework cannot be applied to its own primary case study.
- **A2 — introduce Phase 0: Reckoning** as a prerequisite to Phase 1 for retrofit projects. Greenfield projects skip it or run a lightweight version.
- **B3 hybrid — reckoning before sealing**, with classification into Keep / Fix-now / Fix-by-date / Reconsider-Law. Fix-now resolved before seal; Fix-by-date recorded with owners and dates in a Reckoning Record outside the Astronomican.
- **Add a retrofit-specific section to Phase 1 draft** capturing the additions to pre-work, session, outputs, quality gates, and failure modes.
- **Plan `phase-0-for-debate.md`** as the next major artifact once this debate is decided.

---

## Decision

- **Sub-decision A:** Approved — adopt **A2: introduce Phase 0: Reckoning** as a prerequisite to Phase 1 for retrofit projects. Greenfield projects skip it (or run a lightweight version).
- **Sub-decision B:** Approved — adopt **B3 hybrid**: reckoning-first classification (Keep / Fix-now / Fix-by-date / Reconsider-Law) before sealing; Fix-now resolved before seal; Fix-by-date recorded in a Reckoning Record outside the Astronomican.
- **Open questions:** carried forward — to be addressed in subsequent debates rather than blocking this one.
- **Decided on:** 2026-05-08
- **Decided by:** project owner

### Follow-up actions

- [x] Update [phase-1-for-debate.md](../phase-1-for-debate.md) with a Retrofit section covering Phase 0 prerequisite, session additions, output additions, quality-gate additions, failure-mode additions, and effective-date semantics.
- [x] Update Inputs/Prerequisites in Phase 1 to reference the Phase 0 Reckoning Record for retrofit projects.
- [x] Add the retrofit pattern to the Borrowed-vs-Novel table.
- [x] Update [debates/README.md](README.md) index to status `decided`.
- [x] Create [phase-0-for-debate.md](../phase-0-for-debate.md) defining Phase 0: Reckoning in detail.
- [x] Resolve the six carried-forward open questions (answered by project owner; baked into `phase-0-for-debate.md`):
  1. Phase 0 sealing → No sealing; output is input to Phase 1.
  2. Reckoning quorum → Smaller Reckoning Team produces; Council reviews.
  3. Past-blame protection → Full attribution with blameless framing.
  4. Cap on grandfather count → No fixed cap; PM decides per project.
  5. Sunset horizon → No fixed horizon; PM decides per item.
  6. Re-reckoning cadence → PM-defined cadence committed inside the Reckoning Record.

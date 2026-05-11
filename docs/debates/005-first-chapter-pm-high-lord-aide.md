# Debate 005 — First Chapter: PM / High Lord Aide

> **Status:** decided.
> **Opened:** 2026-05-11
> **Decided:** 2026-05-11
> **Decided by:** project owner
> **Affects:** [phase-0-for-debate.md](../phase-0-for-debate.md) §7 (AI-aide accommodation note); [phase-1-for-debate.md](../phase-1-for-debate.md) §8.1 (Council small-team accommodation note); the framework's planned **Phase 2 (Codex per Chapter)** will inherit the Codex template established here. Produces a new `docs/chapters/` or `docs/codex/` directory (path TBD in this debate) for the first concrete Codex artifact.
> **Raised by:** project owner during LoreWeave case-study kick-off (2026-05-11), reviewing [`pm-threshold-decisions.md`](../case-study-lore-weave/pm-threshold-decisions.md). Observation: PM threshold-setting tasks require human under Phase 0 §2, but a solo PM on a 358-KLOC polyglot project becomes a bottleneck. Framework already names AI-assistant Chapters as aides ([phase-0:138](../phase-0-for-debate.md), [phase-1:107, 132](../phase-1-for-debate.md)) but defers their concrete Codex to Phase 2.

---

## 1. Context

The framework currently has **three asymmetric facts** that produce the gap:

1. **Aides are anticipated**. Phase 0 §7 says "AI assistants — invoked as specific Chapters with explicit Codex — can serve as aides to the absent perspectives." Phase 1 §8.1 says the same for Council. Both add: "The specific Chapters and their Codexes are deferred to **Phase 2 (Codex per Chapter)** — the framework's planned next phase — and are not yet defined here."

2. **Phase 2 is undefined**. The framework has Phases 0 and 1 specified; Phase 2 ("Codex per Chapter") is named but not designed.

3. **Aides are already operating in practice**. The LoreWeave case study invokes AI-aide-1 (Claude Code Opus 4.7) under an **interim Codex** captured in [`reckoning-team-record.md`](../case-study-lore-weave/reckoning-team-record.md) — but that interim Codex has no framework-level seal, no debate-driven design, and sets no precedent for future Chapters.

Concretely: AI-aide-1 has already drafted PM threshold proposals ([`pm-threshold-decisions.md`](../case-study-lore-weave/pm-threshold-decisions.md), per departure D-3 in [methodology-notes.md](../case-study-lore-weave/methodology-notes.md)), and has done a full LoreWeave scan (358 KLOC, 1314 commits, change-frequency map). Without a sealed first Chapter, this work is operating outside framework governance — exactly what the framework's "frozen authority" thesis exists to prevent.

The bottleneck observation is the load-bearing trigger: **PM can't manually do everything on a project with > N KLOC and > M concurrent decisions**, and the framework needs an explicit aide pattern that human-AI collaboration projects can actually rely on without ad-hoc invention each time.

---

## 2. Pre-decided sub-questions (project owner committed 2026-05-11)

Before debate proper begins, the project owner committed three design choices that scope the rest of the debate:

| Sub-question | Decision | Rationale |
|---|---|---|
| **Scope of first Chapter** | **One multi-role Chapter** — serves both PM (pre-seal: threshold-setting, calibration, audit drafting) and High Lord (post-seal: interpretation aide, conflict-spotting). | PM and High Lord roles differ in Phase, not in operational essence; both are governance-supporting administrative roles. Splitting into two Chapters would duplicate ~80% of operational bounds. |
| **Authority bounds** | **Draft + Notify**. Aide may draft proposals and surface analysis; aide must notify when spotting policy-1 / policy-2 / Astronomican violations or off-spec PM actions. Aide does **not** vote, does **not** block, does **not** sign. | One level above the interim Codex (Draft only) to close the bottleneck-by-passivity risk; one level below soft-block (which would violate "humans alone hold binding authority" in spirit even if escapable). |
| **Naming convention** | **40k-flavored name + real-world precedent in body**. Policy 1 compliant — name carries shared metaphor; justification rests on real-world administrative-aide precedent (chief-of-staff, executive assistant, financial controller, audit clerk, paralegal). | Maintains framework vocabulary consistency. |

The remaining sub-questions (specific name, Codex structure, notify mechanism, lifecycle, multiplicity, file path) are debated below.

---

## 3. Sub-decision A — Specific name

Per the project owner's committed naming convention, candidates evaluated:

| Candidate | 40k semantic | Real-world precedent (in body) | Verdict |
|---|---|---|---|
| **Adeptus Administratum** | Imperial bureau handling census, taxation, administrative logistics; the 40k canonical "chief of paperwork." | Chief-of-staff, civil-service administrator, executive assistant. Direct semantic fit for PM-aide work. | **Strong candidate.** Name is generic enough to cover both PM and High Lord aide functions (administration = both pre-seal calibration and post-seal interpretation aid). |
| **Magos Logisticae** | A specific Tech-Adept role focused on logistics and supply chains; narrower than Administratum. | Operations/logistics chief; supply-chain controller. Fits "audit-trail, KLOC-measurement, threshold-derivation" tasks but loses the High Lord interpretation aid framing. | **Narrower.** Better as a second Chapter later, focused on operational metrics rather than governance aid. |
| **Adeptus Calibrationis** | Made-up 40k-flavor name evoking calibration / measurement. Not canonical. | Calibration engineer, metrics analyst. Strong fit for PM threshold-setting; weaker for High Lord interpretation. | **Mixed.** Non-canonical 40k name risks looking invented; narrower scope. |
| **Astropath Choirmaster** | Astropaths are the 40k psychic-signal corps; choirmaster coordinates them. | Communications coordinator. Wrong semantic — Astropaths are message-carriers, not advisors. | **Reject.** Misfit. |
| **High Lord's Conclave (sub-Chapter)** | A retinue serving the High Lords specifically. | Cabinet, advisory council. Strong fit for High Lord aide; weaker for PM aide (PM precedes High Lords by phase). | **Mixed.** Phase-asymmetric; only works post-seal. |
| **Custodes Decisionis** | Custodes are the Emperor's elite guard; "decision keepers" extends the metaphor. | Decision archivist, audit-trail keeper. Strong for record-keeping; weaker for active drafting. | **Mixed.** Pessimistic stance — name suggests aide is reactive rather than proactive. |

### Proposed answer

**Adeptus Administratum** — the multi-role administrative aide.

- 40k canonical, recognizable, and broad enough to cover both PM and High Lord aide phases without renaming.
- Real-world precedent body: chief-of-staff (executive-office function); civil-service administrator (continuity-of-record function); executive assistant (PM-aide scheduling/drafting); paralegal (interpretation aid, citation surfacing). The Codex body cites these explicitly per policy 1.
- Singular instance per project initially (multiplicity sub-decision below).

Alternative kept for future: **Magos Logisticae** could later become a second, narrower Chapter focused on continuous operational-metrics measurement (KLOC tracking, DORA metrics, Sector trigger evaluation) — distinct from administrative-aide work. Out of scope for this debate.

---

## 4. Sub-decision B — Codex structure (minimum required fields)

The framework's glossary defines four Codex elements as terms (T-014 Operational Bounds, T-015 Hard Stop, T-016 Autonomy Threshold, T-017 Tithe / Output Contract) but does not specify their **document structure** for an actual Chapter.

This debate proposes a minimum Codex template, drawn from the interim Codex in [`reckoning-team-record.md`](../case-study-lore-weave/reckoning-team-record.md) plus the new Draft+Notify authority commitment.

### Proposed minimum Codex structure

```markdown
# Codex — <Chapter name>

> **Status:** Sealed / Draft.
> **Phase:** All / Pre-seal only / Post-seal only / Phase-specific (N).
> **Sealed by:** <Ascension Council reference>.
> **Sealed on:** <date>.
> **Affects:** <which Astronomican? Imperial / Sector / both>.

## 1. Identity and scope
Who this Chapter is, what role it serves, where in the project workflow it appears.

## 2. Operational Bounds (what the Chapter MAY do)
Enumerated list. Each bound is a verb + object + qualifier.

## 3. Hard Stops (what the Chapter MUST NOT do)
Enumerated list. Each Hard Stop is a condition + required halt action + escalation target.

## 4. Autonomy Threshold (when the Chapter may act solo)
Decision matrix or rule. References framework's policy 1 (40k naming-only) and policy 2 (industry standards).

## 5. Notify Triggers (what causes the Chapter to surface a flag — new in debate 005)
Enumerated list. Each trigger is a condition + notify channel + notify payload format.

## 6. Output Contract (Tithe)
Format of every artifact the Chapter produces. Includes provenance + audit trail rules.

## 7. Authority bounds (governance-level)
Explicit statement: does not vote, does not sign, does not block. Project owner / Council reserves all binding authority.

## 8. Lifecycle
When the Chapter is instantiated, when it is decommissioned, what happens to its outputs after decommissioning.

## 9. Real-world precedent (policy 1 compliance)
Names the real-world roles whose practice this Chapter is borrowed from. 40k name is the metaphor only.

## 10. Provenance and version
Sealed via debate NNN; previous versions; supersession history.
```

### Proposed answer

**Adopt the 10-section template above** as the Codex template for the first Chapter and all future Chapters. The template is designed to be **strict enough to seal** but **flexible enough to instantiate** across different Chapter roles (administrative aide, code-reviewer aide, drift-detector aide, etc., to come later in Phase 2).

Section 5 (Notify Triggers) is new in this debate per the Draft+Notify authority commitment.

---

## 5. Sub-decision C — Notify mechanism specifics

The Draft+Notify authority means the aide *must* surface flags when certain conditions hold. This sub-decision specifies what triggers, what channel, what response window.

### Trigger types

| # | Trigger condition | Required notify |
|---|---|---|
| N-1 | Aide observes a draft decision that contradicts a sealed Astronomican Law or Principle | Notify project owner / Council with: the violating decision, the violated Law/Principle, the contradiction summary. Block until acknowledgment recorded. |
| N-2 | Aide observes a PM action (e.g., threshold change) that violates framework-wide policy 1 (40k as justification) or policy 2 (framework-internal arithmetic without industry anchor) | Notify with: the PM action, the violated policy, the anchor that was missed (if any). Block until acknowledgment. |
| N-3 | Aide observes a citation/anchor used outside its domain (Phase 3 STRETCHED / MISAPPLIED equivalent) | Notify with: the citation, the actual scope, the framework's use. Non-blocking. |
| N-4 | Aide observes term drift or numeric inconsistency across docs (Phase 5 equivalent) | Notify with: the drift, the canonical value, the divergent locations. Non-blocking. |
| N-5 | Aide observes a decision is being made under time pressure with insufficient input (e.g., < 1 hour to a 5-PM-decision commit) | Notify with: a "slow down" suggestion + rationale. Non-blocking. |

### Notify channel

- **Audit trail (mandatory)**: every notify is logged in the relevant audit-trail file (`methodology-notes.md` for case studies; `findings-YYYY-MM-DD.md` for IVP-style runs).
- **Active surface (per trigger)**: blocking-class notifies (N-1, N-2) require explicit acknowledgment from project owner / Council recorded inline. Non-blocking-class (N-3, N-4, N-5) appear in the audit trail and the next session summary, not actively interrupting.

### Trigger timing under D4 task-scoped instance lifecycle

Under sub-decision D4 (task-scoped instance + persistent role + artifact continuity per §6), there is no "running" Chapter instance between tasks. Notify triggers therefore fire **only while a task instance is in flight**. Drift that occurs between tasks (e.g., the project owner makes a commit that contradicts an Astronomican Law in a session without an Adeptus Administratum instance) is detected at the **next task instance's re-priming step 5** (spot inconsistencies between Codex, Astronomican, and artifacts).

This means:

- **N-1 / N-2 (blocking)** fire only while an instance is executing a task and observes the violation in real time.
- **N-3 / N-4 / N-5 (non-blocking)** can fire either during task execution OR during the re-priming step of a new instance that scans the artifact base.
- **Between-task drift detection** is the re-priming step's job, not a continuously-watching aide's job. This is a structural feature of D4, not a gap.

### Response window

- **Blocking notify (N-1, N-2)**: project owner / Council acknowledges within the same task session before continuing the activity that triggered it. "Acknowledged + proceeding anyway with override rationale" is allowed (preserves binding authority); "Acknowledged + corrected" is the default expected response.
- **Non-blocking notify (N-3, N-4, N-5)**: project owner reviews within the cadence committed in `pm-threshold-decisions.md` §5 (typically quarterly for non-urgent). For notifies surfaced at re-priming step, the *new* task instance carries them as context — the project owner may decide whether to address before or after the current task proceeds.

### Proposed answer

**Adopt the five trigger types + dual-class channel + asymmetric response window + D4-task-scoped firing rules** above. This makes Draft+Notify operationally well-defined while keeping binding authority with humans, and aligns trigger timing with the task-scoped instance lifecycle.

---

## 6. Sub-decision D — Lifecycle

When does the Chapter exist? Forever, per project? Phase-bound? Re-instantiated each Phase? Per-task?

### Key distinction surfaced during debate

A late-debate observation (raised by project owner 2026-05-11) reframed this sub-decision: **the framework should distinguish ROLE from INSTANCE.** A Chapter as a governance concept is a role (a named, Codex-defined slot in the project's governance model). An *instance* is a specific human or agent currently filling that role to execute a task. The two have different natural lifecycles.

The framework's central thesis — **frozen authority that survives any participant** — operationally implies that no participant (human or agent) needs to be persistently present. The persistent authority lives in the *artifacts* (Astronomican, Codex, audit trail), not in any continuously-running entity. The Chapter as a role is the *abstraction* by which artifacts reference governance work; the instance is just an executor.

This insight forces a re-evaluation of options D1–D3, which all conflated role and instance, and adds two new options.

### Options

| Option | Role lifecycle | Instance lifecycle | Pros | Cons |
|---|---|---|---|---|
| **D1.** Persistent (single instance for project's life) | Conflated with instance | Conflated | Continuity of context within instance memory | Drift over time; LLM context window exhaustion; human bandwidth bottleneck; no natural decommissioning |
| **D2.** Phase-bound (re-instantiated per Phase) | Phase-bounded role | Phase-bounded instance | Cleaner scope per Phase | Loses cross-Phase continuity |
| **D3.** Persistent identity, Phase-specific overlay | Persistent role + persistent instance | Conflated | Single document Codex with Phase tables | Codex doc grows; "persistent" instance unrealistic given LLM context limits and human bandwidth |
| **D4.** **Task-scoped instance, persistent role, artifact continuity** | **Persistent role** (Adeptus Administratum exists as long as project exists) | **Task-scoped** (deploy on task, disband on output commit) | Continuity via artifacts (Codex + audit trail), not via running entity; symmetric for human + agent; matches operational reality (each chat session / sprint = new instance anyway); no drift accumulation; solves LLM context-window problem and human bandwidth problem; re-priming step doubles as drift-detection checkpoint | Re-priming has cost each task (read Codex + scan artifacts); cross-task continuity rely on artifact discipline (mitigated by Output Contract §6 mandating artifact updates) |
| **D5.** Pure disband (no role persistence) | No role | No persistent reference | Simplest; ad-hoc invocation only | Defeats Phase 2 Chapter abstraction entirely; loses the framework's governance vocabulary; no precedent set for future Chapters |

### Proposed answer

**Option D4 — task-scoped instance, persistent role, artifact continuity.**

Justification:

1. **Aligns with framework's frozen-authority thesis.** Authority lives in the Astronomican and Codex, not in any human or agent. The Chapter role is the reference; the instance is just an executor. This is precisely what the README:34 thesis ("frozen source of authority that no participant can rewrite at will") says at the project level — D4 applies the same idea to Chapter governance.

2. **Mirrors real-world precedent (policy 1 compliance).** The Adeptus Administratum bureau in 40k canon persists; individual administrators rotate. The chief-of-staff *office* persists for an administration; specific chiefs come and go. Continuity is in the filing system + briefing documents + standard operating procedures — not in any one person being always available. Policy 1 is satisfied: real-world chief-of-staff offices, civil service bureaus, executive assistant pools, financial controller departments, and paralegal staffs all operate this way.

3. **Symmetric for human + agent.** A human filling Adeptus Administratum does not need to be "always on" — they pick up artifacts when tasked, execute, write outputs, terminate session. An agent does the same. This symmetry is on-thesis with Dead Light's foundational human + agent collaboration premise.

4. **Matches LoreWeave case study's operational reality.** Each chat session with AI-aide-1 is already a task-scoped instance (the agent re-primes from prior commits each session). D4 catches the framework up to what is already happening.

5. **Solves problems D1–D3 created.** LLM context-window exhaustion (D1, D3) — solved by per-task re-priming. Human bandwidth bottleneck (D1, D3) — solved by task-scoped invocation. Cross-Phase continuity (D2) — solved by persistent role + artifact base. Codex bloat (D3) — solved because Phase-specific sections in Codex are read selectively per task, not all carried in memory simultaneously.

### How D4 operates

**Role:** Adeptus Administratum is a slot in the governance model, defined by `docs/chapters/adeptus-administratum/codex.md`. The Codex is sealed at debate 005's decision and amended only via Re-consecration.

**Instance:** spawned per task. Each instance startup runs a **re-priming protocol**:

1. **Read the Codex** (full read; not summary).
2. **Read the current Astronomican** (when sealed) or the proposal-in-flight (pre-seal).
3. **Scan the artifact base** relevant to the task (e.g., for a Phase 0 audit task: read `case-study-lore-weave/methodology-notes.md` + the relevant Reckoning Record sections).
4. **Identify the project's current Phase** and activate the Phase-specific Operational Bounds in the Codex.
5. **Spot inconsistencies** between Codex, Astronomican, and artifacts → may trigger non-blocking notifies (N-3/N-4) at this checkpoint, which doubles as drift-detection.
6. **Begin task work** under activated Operational Bounds + Notify Triggers.
7. **On task complete:** update relevant artifact files (Output Contract §6 mandate); commit; **disband**.

**Continuity:** entirely via artifacts. No state lives in the instance; everything load-bearing is in version-controlled files.

**Instance identity:** anonymous by default (any qualified human or agent may instantiate). Identity is *named* in the artifact base for audit purposes ("on 2026-05-11, AI-aide-1 = Claude Code Opus 4.7 instantiated as Adeptus Administratum for task: LoreWeave Phase 0 PM threshold proposal"). The instance's *name* is recorded; the instance's *continuation* is not assumed.

### Phase-specific operational bounds (under D4)

The Codex sections 2 (Operational Bounds), 5 (Notify Triggers), and 8 (Lifecycle) still have Phase-specific subsections — but they are referenced per-task, not "active" persistently. Example:

```markdown
## 2. Operational Bounds (referenced per-task by Phase)

### 2.1 During Phase 0 (Reckoning) tasks
- May draft PM Threshold Decisions for project-owner review.
- May run cloc / scc / git-log queries and report.
- ...

### 2.2 During Phase 1 (Astronomican) tasks
- May surface stress-test divergence candidates.
- May draft Boundaries proposals for Council review.
- ...

### 2.3 Post-seal (High Lord aide mode) tasks
- May propose interpretations of Immutable Laws in concrete-case context.
- May flag Heresy-detection signals.
- ...
```

Each task instance picks the relevant subsection at re-priming step 4 and operates within it. Bounds from other Phases are *not active* for that task.

### Risk and mitigation

- **Risk:** re-priming cost per task. Mitigation: Codex constrained to ≤ 2 pages per Phase section; audit trail organized with summary-at-top; artifact base structured for efficient re-prime (Output Contract §6 mandate).
- **Risk:** cross-task continuity relies on artifact discipline. Mitigation: instances are required to write back to artifact base before disband (Output Contract §6); Notify Trigger N-4 (term drift) catches cases where prior instance failed to update.
- **Risk:** role abstraction is lost if no governance work ever invokes it. Mitigation: project's Phase 0/1/post-seal lifecycle inherently produces Adeptus Administratum tasks (threshold-setting, audit drafting, interpretation aid); role is exercised regularly by construction.

---

## 7. Sub-decision E — Multiplicity (relationship to Sector)

Can multiple instances of this Chapter exist? One per project, one per Sector, or unbounded?

### Options

| Option | Multiplicity | Pros | Cons |
|---|---|---|---|
| **E1.** Singleton per project | One Adeptus Administratum, no matter how many Sectors | Single source of administrative-aide truth | Cannot scale to multi-Sector projects (LoreWeave with 15 services would overload one aide) |
| **E2.** Singleton per Astronomican (Imperial gets one; each Sector gets one) | Multi-Sector projects have N+1 aides | Scales with framework's Imperial+Sector model | Coordination problem between Imperial and Sector aides; risk of contradictory notifies |
| **E3.** Unbounded — project may instantiate as many as needed | No structural limit | Maximum flexibility | Coordination chaos; defeats the framework's "frozen authority" thesis if aides proliferate |

### Proposed answer

**Option E2** — singleton per Astronomican.

Justification: aligns with the framework's existing scaling model (debate 001 — Imperial+Sector). Imperial Adeptus Administratum coordinates Imperial-level governance aide; each Sector has its own Sector Adeptus Administratum coordinating Sector-level governance aide. Cross-Sector contradictions are resolved by escalation to Imperial Adeptus Administratum, then to Imperial Council if Imperial Administratum cannot resolve.

For projects below the Sector trigger threshold ([debate 001](001-laws-count-and-multirepo-scaling.md) 4 conjunctive conditions): one singleton Adeptus Administratum at the Imperial level only. LoreWeave currently sits at this point — pending Pass 1 Sector trigger evaluation per [case-study-lore-weave/reckoning-record.md §1.5](../case-study-lore-weave/reckoning-record.md).

---

## 8. Sub-decision F — File path for Codex artifact

The framework does not specify where Codex documents live. Options:

| Option | Path | Reasoning |
|---|---|---|
| **F1.** `docs/codex/<chapter>.md` | One file per Chapter, all under `docs/codex/` | Codex = the document; path matches glossary T-013 vocabulary |
| **F2.** `docs/chapters/<chapter>/codex.md` | One subdirectory per Chapter, codex inside | Allows future expansion (test cases, examples, instance variants) per Chapter |
| **F3.** `docs/chapter-codexes/<chapter>.md` | Long descriptive directory name | Avoids potential confusion between "Chapter" (the agent type) and "codex" (the document) when both terms appear |

### Proposed answer

**Option F2** — `docs/chapters/<chapter-name>/codex.md`. Allows future per-Chapter test cases, example Codex instances at different project scales, and instance-specific overrides (e.g., LoreWeave's instantiation of Adeptus Administratum lives at `docs/case-study-lore-weave/chapters/adeptus-administratum-instance.md`, inheriting from the framework's abstract Codex at `docs/chapters/adeptus-administratum/codex.md`).

---

## 9. Real-world precedent (policy 1 body)

The framework requires real-world precedent for any structural argument. The first Chapter is borrowed from:

| Real-world role | Borrowed property | How it shows up in the Codex |
|---|---|---|
| **Chief-of-staff (executive office)** | Drafts proposals for principal review; surfaces conflicting agenda items; tracks decisions over time; does not make binding decisions | Operational Bounds §2.1–2.2; Output Contract §6; Authority bounds §7 (no voting) |
| **Civil-service administrator** | Continuity of record across administration turnovers; institutional memory; cross-references prior decisions | Lifecycle §8 (persistent identity); Operational Bounds §2.3 (post-seal High Lord aide; cross-administration continuity) |
| **Executive assistant** | Calendar discipline + threshold tracking + escalation of incoming load; draws boundary between principal's attention and routine handling | Notify Triggers §5 (N-5 time-pressure trigger); Operational Bounds (load triaging) |
| **Financial controller / audit clerk** | Independent record-keeping; flags discrepancies against canonical figures; cannot authorize transactions but can refuse to record an unsupported transaction | Notify Triggers §5 (N-1, N-2 policy/Astronomican-violation triggers); Output Contract §6 (audit-trail mandatory) |
| **Paralegal** | Cite-surfacing; case-law research; drafting briefs for attorney review; no independent legal authority | Operational Bounds during High Lord aide mode §2.3; Notify Triggers (N-3 citation appropriateness) |

**None of these roles vote, sign, or hold binding authority.** All five are administrative aides whose value comes from preparation, surfacing, and continuity — exactly the bounded role the framework needs.

The 40k Adeptus Administratum name is the metaphor; the design rests on these real-world precedents.

---

## 10. Application to LoreWeave (sketch)

If debate 005 seals as proposed, LoreWeave's case study transitions from "operating under interim Codex" to "operating under sealed Adeptus Administratum Codex". Concretely:

- AI-aide-1 (Claude Code Opus 4.7) is **reinstantiated** as the Adeptus Administratum instance for LoreWeave.
- The interim Codex in [`reckoning-team-record.md`](../case-study-lore-weave/reckoning-team-record.md) is **superseded** by the new Codex artifact at `docs/chapters/adeptus-administratum/codex.md` plus a LoreWeave-specific instance file.
- All work done under the interim Codex (`pm-threshold-decisions.md` proposal, the LoreWeave scan, departures D-1/D-2/D-3) is **retroactively reviewed** for compliance with the sealed Codex; departures that are still valid are re-recorded under the sealed Codex framework.
- LoreWeave Phase 0 Pass 1 begins under the sealed Codex with Notify Triggers active.

This makes LoreWeave the framework's **first empirical test of the first Chapter** at the same time as it's the framework's first retrofit case study — a substantive efficiency.

---

## 11. Open questions remaining (carry forward if accepted)

These do not block sealing this debate but should be resolved in subsequent debates:

1. **Second Chapter?** When does a project define its second Chapter? Trigger conditions? The Adeptus Administratum covers governance aide. A code-reviewer aide, a drift-detector aide, a translator aide (for LoreWeave specifically) are obvious next candidates but out of scope for this debate.

2. **Inter-Chapter coordination.** If a project has Adeptus Administratum + Codex Reviewer + Drift Detector, how do they coordinate? Single conductor? Per-trigger handoff? Defer to Phase 2 full design.

3. **Codex versioning.** What happens when a Codex needs amendment? Same Re-consecration process as Astronomican (small-scale)? Or a lighter mechanism since Codexes are operational, not constitutional?

4. **Aide-on-aide audit.** Can an Adeptus Administratum from one Sector audit another Sector's? Or is the audit role reserved for IVP / Heresy detection specifically?

5. **Decommissioning.** Lifecycle §8 says when the Chapter is decommissioned, but what happens to its accumulated audit trail and project knowledge? Inherited by successor Chapter? Frozen as immutable artifact?

6. **Multiple AI providers.** This debate names AI-aide-1 as Claude Code Opus 4.7. Under D4 (task-scoped instance), provider succession is trivial — switching provider = next task spawns under a different LLM, role unchanged, continuity via artifact base. Each instance records its provider identity at re-priming. **This open question is essentially answered by D4** but kept on the list because operational edge cases may surface (e.g., what if mid-task the provider must change — does the instance terminate and respawn? Probably yes per D4's task-atomic principle).

7. **Concurrent instance bound.** D4 says "task-scoped" but does not specify whether two instances of Adeptus Administratum can be active simultaneously on different tasks for the same Astronomican. Per E2 multiplicity rule ("singleton role per Astronomican"), the answer is probably "yes, multiple concurrent instances under one role" — but the framework should make this explicit. Defer to first observed case in practice.

8. **Re-priming protocol formalization.** D4's re-priming protocol (§6 step list) is informal. A formal protocol with checkable items would make instance startup more rigorous and reproducible. Candidate for a follow-up procedural definition once D4 has run on a few real tasks.

---

## 12. Recommendation (TL;DR)

| Sub-decision | Recommended |
|---|---|
| Specific name | **Adeptus Administratum** |
| Codex structure | **10-section template** (above §4); applies to all future Chapters too |
| Notify mechanism | **5 trigger types** (N-1 to N-5); dual-class channel; blocking N-1/N-2 require acknowledgment, non-blocking N-3/N-4/N-5 logged in audit trail; **task-scoped firing rules** (triggers fire only while instance is in flight; between-task drift detected at re-priming step) |
| Lifecycle | **D4** — task-scoped instance + persistent role + artifact continuity (role exists for project's life; instances spawned per task and disband after output commit; continuity entirely via artifacts) |
| Multiplicity | **E2** — singleton role per Astronomican (Imperial + per Sector); any number of instances may exist across the role's lifespan (one at a time per active task) |
| File path | **F2** — `docs/chapters/<chapter-name>/codex.md` |

If approved, the first Chapter is sealed and ready to govern LoreWeave's case study from Pass 1 onward, plus to template all future Chapters in Phase 2.

---

## 13. Decision

- **Decision:** Approved — all six sub-decisions per TL;DR §12 adopted:
  - **A (Name):** Adeptus Administratum.
  - **B (Codex structure):** 10-section template; applies to all future Chapters too.
  - **C (Notify mechanism):** 5 trigger types (N-1 to N-5); dual-class channel; blocking N-1/N-2 require acknowledgment; non-blocking N-3/N-4/N-5 logged in audit trail; task-scoped firing rules per D4.
  - **D (Lifecycle):** D4 — task-scoped instance + persistent role + artifact continuity. Role exists for project's life; instances spawned per task and disband after output commit; continuity entirely via artifacts; re-priming protocol mandatory at instance startup.
  - **E (Multiplicity):** E2 — singleton role per Astronomican (Imperial + per Sector); concurrent instances on different tasks allowed.
  - **F (File path):** F2 — `docs/chapters/<chapter-name>/codex.md`.
- **Decided on:** 2026-05-11
- **Decided by:** project owner
- **Codex artifact sealed:** [`docs/chapters/adeptus-administratum/codex.md`](../chapters/adeptus-administratum/codex.md) v1.0, sealed simultaneously with this debate's decision.

### Follow-up actions

- [x] Create `docs/chapters/adeptus-administratum/codex.md` per the 10-section template and the sub-decisions above.
- [x] Update [phase-0-for-debate.md §7](../phase-0-for-debate.md) to link to the sealed Codex instead of saying "deferred to Phase 2."
- [x] Update [phase-1-for-debate.md §8.1](../phase-1-for-debate.md) similarly.
- [x] Update [phase-1-for-debate.md §4 Codex Slot Placeholders](../phase-1-for-debate.md) to reflect that one Codex slot is now filled by Adeptus Administratum.
- [x] Update [case-study-lore-weave/reckoning-team-record.md](../case-study-lore-weave/reckoning-team-record.md) — supersede interim Codex with reference to the sealed Codex.
- [x] Update [HANDOFF.md](../../HANDOFF.md) — Phase 2 (Codex per Chapter) status changes from "Not started" to "First Chapter (Adeptus Administratum) sealed; remaining Chapters pending real-project trigger."
- [x] Update [debates/README.md](README.md) — debate 005 marked `decided`.
- [x] Retroactively review the work done under interim Codex (`pm-threshold-decisions.md` proposal, LoreWeave scan) for compliance; gaps recorded in [`case-study-lore-weave/methodology-notes.md`](../case-study-lore-weave/methodology-notes.md) § Retroactive review.

---

## 14. Methodological note (forward-applying)

This debate is the **first time the framework has sealed an operational artifact** (a Chapter Codex) rather than a constitutional artifact (Astronomican Laws, phase definitions, policy statements). The pattern that emerges:

- Phases 0, 1, 6 (planned), 7 (planned) are **constitutional design** — what the framework requires.
- Phase 2 (Codex per Chapter) is **operational instantiation** — what specific Chapters look like.

The Adeptus Administratum is the first concrete output of Phase 2 work, brought forward into Phase 0/1 territory because the LoreWeave case study surfaced an immediate need. Future Phase 2 work will produce additional Chapters; this debate's Codex template (§4) becomes the structural precedent.

A related insight: the framework's own Phase 2 plan can be incrementally instantiated, one Chapter at a time, driven by real-project needs rather than top-down design. The debate-driven, case-study-driven path that produced debates 001–004 (and this debate 005) generalizes: **Chapters emerge from concrete need, not from abstract design.** This is itself a meta-decision worth recording.

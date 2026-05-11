# Debate 005 — First Chapter: PM / High Lord Aide

> **Status:** open.
> **Opened:** 2026-05-11
> **Decided:** —
> **Decided by:** project owner (pending)
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

### Response window

- **Blocking notify (N-1, N-2)**: project owner / Council acknowledges within the same session before continuing the activity that triggered it. "Acknowledged + proceeding anyway with override rationale" is allowed (preserves binding authority); "Acknowledged + corrected" is the default expected response.
- **Non-blocking notify (N-3, N-4, N-5)**: project owner reviews within the cadence committed in `pm-threshold-decisions.md` §5 (typically quarterly for non-urgent).

### Proposed answer

**Adopt the five trigger types + dual-class channel + asymmetric response window** above. This makes Draft+Notify operationally well-defined while keeping binding authority with humans.

---

## 6. Sub-decision D — Lifecycle

When does the Chapter exist? Forever, per project? Phase-bound? Re-instantiated each Phase?

### Options

| Option | Lifecycle | Pros | Cons |
|---|---|---|---|
| **D1.** Persistent — once instantiated, exists for the life of the project | Same Codex applies across all Phases | Continuity of context; aide accumulates project-specific knowledge | Risk: aide drifts as project context grows; no natural decommissioning event |
| **D2.** Phase-bound — re-instantiated per Phase with Phase-specific Codex | Cleaner scope per Phase; explicit decommissioning at Phase boundaries | Loses cross-Phase continuity; PM aide doesn't carry into High Lord aide easily |
| **D3.** Persistent identity, Phase-specific operational overlay | Single Chapter exists for life of project; Codex has Phase-specific Operational Bounds + Notify Triggers within a single document | Continuity preserved; Phase-bound bounds preserved; complexity of Codex grows | Codex doc longer; possible internal contradictions if Phase overlays drift |

### Proposed answer

**Option D3** — persistent identity, Phase-specific operational overlay.

Justification: the multi-role-single-Chapter commitment (§2 pre-decided) implies one identity carrying through Phases. The Codex sections 2 (Operational Bounds), 5 (Notify Triggers), and 8 (Lifecycle) become Phase-aware tables rather than monolithic enumerations. Example structure for Operational Bounds:

```markdown
## 2. Operational Bounds

### 2.1 During Phase 0 (Reckoning)
- May draft PM Threshold Decisions for project-owner review.
- May run cloc / scc / git-log queries and report.
- ...

### 2.2 During Phase 1 (The Astronomican)
- May surface stress-test divergence candidates.
- May draft Boundaries proposals for Council review.
- ...

### 2.3 Post-seal (High Lord aide mode)
- May propose interpretations of Immutable Laws in concrete-case context.
- May flag Heresy-detection signals.
- ...
```

This keeps a single Codex document while making Phase-bounded operational behavior explicit.

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

6. **Multiple AI providers.** This debate names AI-aide-1 as Claude Code Opus 4.7. If a project's Adeptus Administratum is later instantiated under a different LLM (GPT-5, Gemini-X), is that a new instance or a continuation? Need explicit rule for provider succession.

---

## 12. Recommendation (TL;DR)

| Sub-decision | Recommended |
|---|---|
| Specific name | **Adeptus Administratum** |
| Codex structure | **10-section template** (above §4); applies to all future Chapters too |
| Notify mechanism | **5 trigger types** (N-1 to N-5); dual-class channel; blocking N-1/N-2 require acknowledgment, non-blocking N-3/N-4/N-5 logged in audit trail |
| Lifecycle | **D3** — persistent identity, Phase-specific operational overlay |
| Multiplicity | **E2** — singleton per Astronomican (Imperial + per Sector) |
| File path | **F2** — `docs/chapters/<chapter-name>/codex.md` |

If approved, the first Chapter is sealed and ready to govern LoreWeave's case study from Pass 1 onward, plus to template all future Chapters in Phase 2.

---

## 13. Decision

_(Empty — to be filled when project owner decides.)_

- **Decision:** _(pending)_
- **Decided on:** _(pending)_
- **Decided by:** _(pending)_

### Follow-up actions (will be checked on seal)

- [ ] Create `docs/chapters/adeptus-administratum/codex.md` per the 10-section template and the sub-decisions above.
- [ ] Update [phase-0-for-debate.md §7](../phase-0-for-debate.md) to link to the sealed Codex instead of saying "deferred to Phase 2."
- [ ] Update [phase-1-for-debate.md §8.1](../phase-1-for-debate.md) similarly.
- [ ] Update [phase-1-for-debate.md §4 Codex Slot Placeholders](../phase-1-for-debate.md) to reflect that one Codex slot is now filled by Adeptus Administratum.
- [ ] Update [case-study-lore-weave/reckoning-team-record.md](../case-study-lore-weave/reckoning-team-record.md) — supersede interim Codex with reference to the sealed Codex; create LoreWeave-specific instance file.
- [ ] Update [HANDOFF.md](../../HANDOFF.md) — Phase 2 (Codex per Chapter) status changes from "Not started" to "First Chapter sealed; remaining Chapters pending real-project trigger."
- [ ] Update [debates/README.md](README.md) — add debate 005 as `decided`.
- [ ] Retroactively review the work done under interim Codex (pm-threshold-decisions.md proposal, LoreWeave scan) for compliance; record any gaps in `case-study-lore-weave/methodology-notes.md`.

---

## 14. Methodological note (forward-applying)

This debate is the **first time the framework has sealed an operational artifact** (a Chapter Codex) rather than a constitutional artifact (Astronomican Laws, phase definitions, policy statements). The pattern that emerges:

- Phases 0, 1, 6 (planned), 7 (planned) are **constitutional design** — what the framework requires.
- Phase 2 (Codex per Chapter) is **operational instantiation** — what specific Chapters look like.

The Adeptus Administratum is the first concrete output of Phase 2 work, brought forward into Phase 0/1 territory because the LoreWeave case study surfaced an immediate need. Future Phase 2 work will produce additional Chapters; this debate's Codex template (§4) becomes the structural precedent.

A related insight: the framework's own Phase 2 plan can be incrementally instantiated, one Chapter at a time, driven by real-project needs rather than top-down design. The debate-driven, case-study-driven path that produced debates 001–004 (and this debate 005) generalizes: **Chapters emerge from concrete need, not from abstract design.** This is itself a meta-decision worth recording.

# Independent Verification Pass (IVP) — Audit Workflow (For Debate)

> **Version:** v0.2 (2026-05-09). Refined after the 2026-05-08 rodage execution against the existing repository. See [§ 11 Changelog](#11-changelog) for what changed and why; rodage findings in [`findings-2026-05-08.md`](findings-2026-05-08.md).
>
> **Status:** Draft, not final. To be refined after each execution against the repository; spec changes go between passes, not during.
>
> **Purpose:** Define a repeatable workflow that an *outside reviewer* can run against the Dead Light Framework documents to verify (a) the existence and accuracy of cited sources, (b) the appropriateness of those sources for the claims they support, (c) the soundness of arguments, (d) the internal consistency of the framework, and (e) the framework's standing relative to external literature.
>
> **Scope:** All documents under `docs/`, plus `README.md` and `HANDOFF.md`. Out of scope: `chat.txt` (raw history), `LICENSE` (legal boilerplate).
>
> **Non-goals:** IVP **does not** produce new framework content, redesign existing sections, or rewrite weak passages. Findings are *reported*; remediation is a separate, downstream activity.
>
> **Calibration:** Industry-pragmatic. Grey literature (vendor whitepapers, major consultancy reports, well-known practitioner books, citable blog posts from recognized authors) is admissible as evidence, with flagging. Strict peer-review-only thresholds are not used.

---

## 1. Why this exists

Dead Light Framework is an academic-style governance methodology. Two policies bind it:

1. *40k vocabulary is naming and shared metaphor only* — real-world precedent governs the design.
2. *Industry standards over framework-invented formulas* — calibration anchors to documented external practice.

Both policies are testable: either a citation matches the precedent it claims, or it does not. Either the argument bridge from data to claim holds, or it does not. IVP exists to perform that test independently of the authors, with a pre-registered rubric, so the result is reproducible and not a matter of taste.

---

## 2. Pre-registered design principles (anti-bias)

These principles must be honoured by anyone executing IVP. They are deliberately strict to prevent the audit from drifting into editorial review.

1. **Pre-registration of rubric.** The rubric tables in section 4 are fixed *before* the auditor opens any framework document. The auditor may not modify the rubric mid-pass. If a rubric flaw is found, log it under "Limitations of this audit" and continue with the existing rubric; revise only between passes.
2. **Symmetric search (mandatory for load-bearing).** For every **load-bearing** citation or claim sent to external search, the auditor MUST run both a confirming query *and* a disconfirming query, and record the disconfirming result with the same weight as the confirming one. For non-load-bearing items, disconfirming search is recommended but optional. Disconfirming-query templates appear in [§ 5 Phase 2 procedure](#phase-2--citation-verification-factual). The 2026-05-08 rodage held this loosely (~6 of 30 verifications had disconfirming counterparts) and was identified as a coverage gap; this revision closes it.
3. **Audit trail mandatory.** Every verdict is backed by: (a) the file:line of the claim, (b) the search query or read action performed, (c) the source consulted including URL and access date, (d) the excerpt or summary supporting the verdict. No verdict without trail.
4. **Falsifiability check.** For each load-bearing claim, the auditor states what evidence would falsify it. A claim with no conceivable disconfirming evidence is flagged `UNFALSIFIABLE` regardless of its plausibility.
5. **Separation of concerns.** During an IVP run the auditor must not modify the framework documents themselves. Findings go to `docs/audit/findings-YYYY-MM-DD.md`. Remediation is a separate authoring pass after the project owner reviews findings.
6. **Stop-on-trail-break.** If audit trail cannot be established for a verdict (e.g., source paywalled, archive offline), the verdict is `UNVERIFIABLE`, not a guess. Continuing with a guess corrupts the pass.
7. **Industry-pragmatic, not lax.** Grey literature is admissible, but tier matters (section 5). A grey-literature-only basis for a load-bearing claim is itself a finding (severity MEDIUM or higher depending on the claim's role).
8. **No early termination on CRITICAL findings.** Per project owner decision, run all seven phases to completion regardless of severity encountered. A single critical finding is not allowed to short-circuit later phases that may surface independent issues.

---

## 3. Source authority hierarchy (industry-pragmatic)

Used by phases 2, 3, and 6 to weigh sources.

| Tier | Examples | Treatment |
|---|---|---|
| **T1 — Primary standards / peer-reviewed** | Three sub-categories, all treated as T1 for verdicts: (a) **International / governmental standards bodies** — ISO/IEC, IEEE, IAASB (ISA), NIST. (b) **Standards-body-owned commercial publishers (de-facto standards)** — AXELOS / PeopleCert (ITIL), PMI (PMBOK), CMMI Institute / ISACA (CMMI), IFPUG (Function Points), SEI (CMMI legacy v1.x–v2.x). These are commercial publishers but own the de-facto standard for their domain. (c) **Peer-reviewed venues** — ACM and IEEE conference proceedings, peer-reviewed journals (e.g., *IEEE Computer*, *IEEE Trans. SE*, *Behavioral and Brain Sciences*). | Strongest. Use when available; cite directly. The 2026-05-08 rodage exposed ambiguity in earlier wording (T1 vs T2 for AXELOS/PMI); category (b) is now explicit. |
| **T2 — Recognized practitioner texts and standards-adjacent** | Established textbooks (Boehm COCOMO II, Putnam SLIM, Fowler refactoring, Nygard *Release It!*), DORA *Accelerate*/*State of DevOps* reports, NIST publications, ISACA/COBIT guidance, OWASP project outputs | Strong. Treat as primary for industry questions. Note edition. |
| **T3 — Major-vendor / major-consultancy grey literature** | Microsoft/Google/AWS architecture papers, Big-4 consulting whitepapers, Gartner / Forrester reports (when accessible), Martin Fowler's bliki, well-known engineering blogs from FAANG-tier engineering teams | Admissible. Flag as grey-tier. Triangulate with at least one T1/T2 source for load-bearing claims. |
| **T4 — Practitioner blogs, conference talks (no proceedings), podcasts** | Individual practitioner posts, recorded conference talks without papers, podcast interviews | Admissible only as colour or as illustrative example. Cannot be sole basis for a load-bearing claim. |
| **T5 — Unsourced web content, AI-generated text, anonymous wiki** | Any content without verifiable authorship, ChatGPT-style outputs, anonymous wikis with no editorial process | Inadmissible as evidence. Flag any framework citation that resolves only to T5. |

**Recency policy:** For technology/practice claims, prefer sources from the last 5 years. For governance/audit/measurement claims, last 10 years. Older sources admissible if cited as foundational (e.g., COCOMO 1981, Brooks 1975) or if no superseding source exists; record the choice in the trail.

**Edition currency:** Where standards are versioned (ISA, ITIL, PMBOK, ISO), confirm the cited edition is current or that the framework's claim is edition-stable.

---

## 4. Pre-registered rubric

These four tables are the operational rubric. Auditor maps every item to one row in the relevant table.

### 4.1 Severity scale (applies to every finding)

| Code | Definition | Examples |
|---|---|---|
| **CRITICAL** | Falsifies a load-bearing decision, violates a framework-level policy, or makes the framework's central claim unsupportable. | Cited standard does not exist; Council minimum-diversity rule rests on a fallacy; 40k metaphor used as primary justification (policy-1 violation). |
| **HIGH** | Cited source exists but does not say what is claimed; argument has a missing or implausible warrant on a sealed decision; cross-document contradiction in a sealed phase. | "ISA 320 prescribes 5-10%" claim where ISA 320 actually says materiality is qualitative + quantitative; "Council ≥ 3" justified solely by 40k analogy; Miller cited as "5±2" when actual is 7±2 (rodage F-01). |
| **MEDIUM** | Stretched citation, missing qualifier, partial verification, weak warrant on an open question, terminology drift between drafts. | Source cited from secondary text without primary check; PMBOK threshold given without edition; "Council" in phase-0 vs phase-1 used with subtle scope difference. |
| **LOW** | Citation-style or hygiene issues that do not affect the substance. | Missing access date, link rot, inconsistent reference formatting, missing edition number where edition is stable. |

**Cross-cutting rules (apply on top of the row classification):**

- **`UNFALSIFIABLE` escalation.** Any claim flagged `UNFALSIFIABLE` by Phase 4 escalates by **one severity level above its rubric base**, unless the claim is explicitly *definitional* or *conventional* (per § 7 limitations: definitional claims are not falsifiable in the empirical sense and the verdict is informational for them, not penal). Resolved from § 9 open question.
- **Load-bearing weighting.** Findings on load-bearing items (LB=Y in inventory) are reported first and never bumped down for brevity.
- **Tier-floor rule.** A load-bearing claim resting solely on T3 grey literature, with no T1/T2 triangulation, is flagged at minimum `MEDIUM` regardless of whether the T3 source itself is accurate. Industry-pragmatic mode admits T3, but unanchored T3 is itself a finding.

### 4.2 Citation verification verdict (Phase 2)

| Verdict | Definition |
|---|---|
| **VERIFIED** | Source exists; identity (author/publisher/year/edition) matches; if a quote or number is given, it matches the primary source. |
| **PARTIAL** | Source exists and identity matches, but quote/number/attribute could only be confirmed via T2/T3 secondary, or one sub-element is unconfirmed. |
| **UNVERIFIABLE** | Source could not be located within reasonable effort, or all paths terminate at T5. Distinct from `CONTRADICTED`. |
| **CONTRADICTED** | Source exists and clearly does *not* say what the framework attributes to it. |

### 4.3 Citation appropriateness verdict (Phase 3)

| Verdict | Definition |
|---|---|
| **APPROPRIATE** | Source's domain, scope, and authority match the claim being supported. |
| **STRETCHED** | Source is in adjacent domain or covers narrower scope than the claim suggests; transfer is plausible but should be qualified in the framework. |
| **MISAPPLIED** | Source is being asked to support a claim it does not address (e.g., cost-estimation source supporting a governance threshold). |
| **UNSUPPORTED-LEAP** | Source is real and respected, but the inferential gap from source to claim is unbridged in the framework text. |

### 4.4 Argument verdict (Phase 4)

| Verdict | Definition |
|---|---|
| **SOUND** | Toulmin decomposition is complete and each element is supported. |
| **WEAK-WARRANT** | Warrant (the bridge from data to claim) is implicit, missing, or backed only by analogy. |
| **FALLACIOUS** | Argument relies on a named fallacy (false analogy, hasty generalization, equivocation, circular definition, appeal to authority where authority does not speak to the question, no-true-Scotsman). |
| **UNFALSIFIABLE** | No statable evidence would change the claim. |

---

## 5. The seven phases

Each phase has a fixed structure: Goal · Inputs · Procedure · Output · Acceptance criteria · Tools.

### Phase 1 — Inventory (extract; no judgement)

**Goal.** Produce a flat catalog of everything that will be audited so later phases operate on a stable list.

**Inputs.** All `docs/**/*.md`, `README.md`, `HANDOFF.md`.

**Procedure.**
1. Read each in-scope file end-to-end.
2. Extract into four tables in `audit/inventory.md`:
   - **Claims** — every assertive proposition. Columns: id (`C-NNN`), file:line, claim text (≤ 30 words), type (`descriptive` | `normative` | `causal` | `definitional`), load-bearing (`Y`/`N`).
   - **Citations** — every reference to an external entity. **Deduplication rule (mandatory):** each *distinct entity* gets exactly one row; if the same entity is cited in multiple files, list every file:line in a single **Locations** column. Phase 2 verifies the entity once and applies the verdict to every location. Columns: id (`R-NNN`), cited entity (e.g., "COCOMO II", "ITIL 4 (2019)"), **Locations** (file:line list), claimed attribute(s) (e.g., "5–10% materiality", "Sev1/Sev2/Sev3 tiers"), type (standard | book | report | doctrine | historical fact). The 2026-05-08 rodage already followed this convention informally; this revision makes it explicit.
   - **Defined terms** — every framework term defined or used as if defined. Columns: id (`T-NNN`), term, file:line of first definition, occurrences elsewhere.
   - **Analogies** — every 40k metaphor invoked. Columns: id (`A-NNN`), file:line, metaphor, role (naming-only | risks-becoming-justification).

**Output.** `audit/inventory.md`.

**Acceptance.** No file in scope is unread. All four tables non-empty. Spot-check: pick three random claims, three random citations; confirm presence in tables.

**Tools.** `Read` for full files, `Grep` for term occurrences, optionally `Agent (Explore)` to parallelize across files.

---

### Phase 2 — Citation Verification (factual)

**Goal.** Determine whether each citation's source exists and is being identified correctly.

**Inputs.** Citations table from Phase 1.

**Procedure.** For each citation `R-NNN`:

1. Run **confirming query** to locate primary source. Prefer publisher's official site, standards-body site, or an indexed bibliographic database.
2. **For load-bearing citations (LB=Y in any of the citation's claim references): primary-source read is MANDATORY.** A T2 textbook summary or T3 grey-literature secondary is *insufficient* grounds for a `VERIFIED` verdict on a load-bearing item — the auditor must reach the standard's text, the paper's PDF, or the publisher's official documentation page. If the primary source cannot be reached within reasonable effort (paywall, archive offline, language barrier), the verdict is `UNVERIFIABLE` until a future pass with better access — no guess from secondary.
3. **For non-load-bearing citations:** if primary not directly accessible, climb tier ladder (T1 → T2 → T3) and record the tier reached.
4. Run **disconfirming query** — **MANDATORY for load-bearing** items, recommended for others — to find any source asserting the framework's claim is wrong about the citation's content (e.g., "ISA 320 materiality is qualitative not 5%", "Miller's number is 7 not 5", "CMMI v3.0 is current not v2.0", "two-pizza team origin is late 1990s not 2002").
5. Compare attribute claimed in framework against source. For numeric claims, the number must match within stated precision. For doctrine claims, the source must explicitly support the doctrine being attributed.
6. Assign verdict from rubric 4.2.

**Output.** Table appended to `audit/findings-YYYY-MM-DD.md`:

| R-id | Claim location | Cited entity | Attribute claimed | Verdict | Tier reached | Trail |

**Acceptance.** Every `R-NNN` has a verdict and an audit trail. No `VERIFIED` without a citable source URL or stable identifier.

**Tools.** `WebSearch` (both directions), `WebFetch` for primary sources.

**Query templates.**
- Confirming: `"<entity>" <attribute> <year>` and `<publisher> <entity>` and `site:<publisher-domain> <entity>`
- Disconfirming: `<entity> NOT <attribute>` and `<entity> myth misconception` and `<entity> common misuse`
- Bibliographic: `Google Scholar / Semantic Scholar` for academic; standards-body catalog for standards.

---

### Phase 3 — Citation Appropriateness (logical)

**Goal.** Determine whether each verified citation is being used to support a claim its source can actually support.

**Inputs.** Verified citations from Phase 2 (verdicts `VERIFIED` or `PARTIAL`).

**Procedure.** For each:
1. State the source's *actual scope* (one sentence) from the source's own framing.
2. State the framework's *use* of the source (one sentence).
3. Apply the four sub-checks:
   - **Scope match** — does the source's domain include the framework's question?
   - **Authority in context** — within the framework's question, is this source authoritative? (E.g., COCOMO II is authoritative for *cost*; not for *governance threshold*.)
   - **Generalization burden** — how many inferential steps separate source statement from framework claim?
   - **Anachronism / cherry-pick** — is the source from a meaningfully different era or context? Has any in-domain counter-source been ignored?
4. Assign verdict from rubric 4.3.

**Output.** Table appended to `audit/findings-YYYY-MM-DD.md`:

| R-id | Source actual scope | Framework use | Scope match | Authority | Gen-burden | Anachronism/cherry | Verdict | Trail |

**Acceptance.** Every verified citation reviewed. Each `STRETCHED` / `MISAPPLIED` / `UNSUPPORTED-LEAP` has a stated reason and at least one suggested narrower alternative source if one exists.

**Tools.** `WebSearch` for in-domain alternative sources; `WebFetch` to read source framing; `Read` for the framework's own use.

---

### Phase 4 — Argument Analysis (Toulmin + fallacy check)

**Goal.** Decompose each load-bearing argument and test it.

**Inputs.** Load-bearing claims from Phase 1 (load-bearing = `Y`), plus all decisions in `docs/debates/`.

**Procedure.** For each load-bearing argument:
1. Extract Toulmin elements:
   - **Claim** — what is asserted.
   - **Data** — evidence offered.
   - **Warrant** — bridge from data to claim.
   - **Backing** — what supports the warrant.
   - **Qualifier** — scope-limiting language ("usually", "in retrofit", "for teams ≥ 5").
   - **Rebuttal** — acknowledged conditions where the claim would fail.
2. Test for missing elements. Implicit warrants must be made explicit by the auditor and assessed.
3. Run the fixed fallacy checklist:
   - False analogy (especially: 40k metaphor used as substantive support — policy-1 violation).
   - Hasty generalization (n=1 case study → universal rule).
   - Appeal to authority where the cited authority does not address the question.
   - Equivocation (the same term shifting meaning between phases or sections).
   - Circular definition (term defined using itself or its near-synonym).
   - No-true-Scotsman (definition narrowed mid-debate to exclude counterexamples).
   - Begging the question (premise restates the conclusion).
   - Survivorship bias (only successful cases informed the rule).
4. Apply falsifiability test: state what evidence would prove the claim wrong. If none can be stated, mark `UNFALSIFIABLE`.
5. Assign verdict from rubric 4.4.

**Output.** Table appended to `audit/findings-YYYY-MM-DD.md`:

| C-id | Claim | Data | Warrant (explicit?) | Backing | Qualifier | Rebuttal | Fallacy check | Falsifiability test | Verdict | Trail |

**Acceptance.** Every load-bearing claim and every sealed debate decision has a row. Implicit warrants are surfaced.

**Tools.** `Read` (deep), `Grep` (cross-doc term tracking for equivocation check).

---

### Phase 5 — Internal Consistency

**Goal.** Detect contradictions, term drift, and unreflected decisions across the document set.

**Inputs.** All Phase 1 outputs; all `docs/debates/*.md` decision sections.

**Procedure.**
1. **Term drift.** For each defined term `T-NNN`, list every occurrence in non-defining files. Compare against the definition. Flag scope shifts, role shifts, or quietly added/removed attributes.
2. **Decision-to-doc reflection.** For each `decided` debate, verify each decision element is reflected in the relevant phase doc(s). Missing reflections are MEDIUM or HIGH depending on whether the decision is load-bearing.
3. **Quantitative consistency.** Every numeric threshold (sizes, percentages, durations) must match across all docs that mention it. Flag mismatches.
4. **Policy compliance.** Re-check every justification segment against the two framework-wide policies. A justification resting on 40k metaphor (policy-1) or on framework-internal arithmetic with no industry anchor (policy-2) is a CRITICAL finding.
5. **README link integrity.** Verify "planned" links in README do not assert content; verify existing links resolve.

**Output.** Table appended to `audit/findings-YYYY-MM-DD.md`:

| Issue type | Locations | Detail | Severity | Trail |

**Acceptance.** Every defined term, every decision, every numeric threshold, every justification touched at least once.

**Tools.** `Grep` (heavy use for cross-file term and number searches), `Read`.

---

### Phase 6 — External Benchmarking

**Goal.** Place the framework in the broader literature on AI-agent governance, software governance, frozen-specification patterns, and human-AI collaboration. Identify both supporting precedent and direct counter-arguments the framework has not addressed.

**Inputs.** Framework's central claims and policies from Phase 1; sealed decisions from Phase 5.

**Procedure.**
1. **Adjacent-frameworks search.** For the framework's core ideas (frozen authority, retrofit-then-build, multi-role council, AI-agent-as-Chapter), search for prior art and parallels. Tag by relationship: `precedent` (came first, similar) | `convergent` (independent, similar) | `counter` (argues against this approach).
2. **Empirical evidence search.** For each major design choice, search for empirical studies, postmortems, or longitudinal reports that bear on it. Industry-pragmatic: DORA reports, GitHub State of the Octoverse, Stack Overflow surveys, Google re:Work, Atlassian's team-collaboration research are admissible at T2/T3.
3. **Counter-framework search.** Identify methodologies whose first principles oppose Dead Light's (e.g., agile manifesto's "responding to change over following a plan" vs frozen authority). For each, evaluate whether Dead Light has addressed the counter-argument or evaded it.
4. **Gap matrix.** Produce a comparison matrix: rows = Dead Light's load-bearing choices, columns = adjacent frameworks, cells = `same` / `different` / `silent` / `incompatible`.

**Output.** `audit/benchmark.md` with:
- Adjacent-frameworks table with relationship tag and one-line summary.
- Empirical-evidence table with source, finding, supports/contradicts column.
- Counter-frameworks table with their core counter-argument and Dead Light's response status (`addressed` / `partially-addressed` / `unaddressed` / `evaded`).
- Gap matrix.

**Acceptance.** At least three precedents, three convergent items, three counter-arguments documented. Industry-pragmatic tier of every source recorded.

**Tools.** `WebSearch` (broad), `WebFetch`, optionally `Agent` for parallel investigation by topic. (Do not use `Agent` to *form opinions*; only to gather and summarize literature with audit trail.)

---

### Phase 7 — Synthesis Report

**Goal.** Compose a single artifact that an outside reviewer can read end-to-end to understand the framework's current evidentiary standing.

**Inputs.** All Phase 1–6 outputs.

**Procedure.**
1. Aggregate all findings into one table.
2. Compute summary statistics.
3. Write the executive verdict (≤ 300 words). State only what the evidence supports; no editorial.
4. List CRITICAL and HIGH findings in dedicated sections, each with a *recommended action* slot (filled either `defer to project owner` or `obvious fix: <one sentence>`).
5. Write **Limitations of this audit** — what was *not* checked and why (paywalled sources, language coverage, time spent, rubric flaws encountered).
6. Append complete audit trail.

**Output.** `audit/findings-YYYY-MM-DD.md`. Fixed structure:

```markdown
# IVP Findings — YYYY-MM-DD

## Executive verdict
<≤ 300 words>

## Aggregate stats
- Citations: V verified / P partial / U unverifiable / C contradicted (total N)
- Citations appropriateness: A appropriate / S stretched / M misapplied / L unsupported-leap
- Arguments: S sound / W weak-warrant / F fallacious / U unfalsifiable
- Consistency: N findings (severity histogram)
- Benchmarking: P precedents / V convergent / X counter / unaddressed counter-arguments: K

## CRITICAL findings
<table>

## HIGH findings
<table>

## MEDIUM findings
<table>

## LOW findings
<table>

## Disconfirming evidence found (Phase 6)
<list>

## Limitations of this audit
<list>

## Audit trail
<all queries with date, all URLs accessed with date, all read actions>
```

**Acceptance.** Report is self-contained; an outsider with no prior context can read this single file and understand the framework's current evidentiary state. No verdict in the report lacks a corresponding trail entry.

---

## 6. Re-run procedure

IVP is designed to be repeated as the framework evolves.

1. Create a new branch (e.g., `audit/ivp-YYYY-MM-DD`).
2. Copy the rubric tables from this document into a fresh working file. **Do not modify the rubric** during the run.
3. Run phases 1–7 in order. Each phase writes to its own file under `audit/`. Do not modify framework documents during the run.
4. On completion, file the report at `audit/findings-YYYY-MM-DD.md`, commit, and open a PR for project-owner review.
5. Project owner reviews, decides remediation actions, and authorises a *separate* authoring branch. The remediation branch may modify framework documents; the audit branch may not.
6. Diff between consecutive IVP runs goes in `audit/diff-PREV-to-CURRENT.md` to track whether prior findings were resolved.

**Cadence guidance (event-driven primary; calendar fallback).** Run IVP after any of:

- a sealed decision being added or a sealed decision being amended;
- a new phase being drafted;
- a case study being introduced or substantially revised (e.g., LoreWeave application);
- an external standard being updated or superseded that the framework depends on (e.g., CMMI v2.0 → v3.0 in 2023, ITIL 4 → ITIL 5 in 2026);
- significant external academic findings on the framework's anchored concepts (e.g., a major working-memory or organizational-governance result that affects citations).

**Calendar fallback:** at most **12 months** between runs even if no events have triggered. The earlier draft suggested 90 days; the 2026-05-08 rodage experience indicates event-driven is more useful and the calendar exists only as a safety net. Resolved from § 9 open question.

---

## 7. Limitations of this methodology

Stated up front so they cannot be raised post-hoc as defences against findings.

- **Reviewer model dependency.** When IVP is run by an AI agent, the agent's training data and search effectiveness bound what it can find. This biases toward English-language, web-indexed sources. A human reviewer with library access to non-indexed academic literature may surface more.
- **Recency bias of search engines.** Search engines down-rank older content, which can hide foundational sources. The recency policy in section 3 partly compensates.
- **Grey-literature admission.** Industry-pragmatic mode admits T3 sources for load-bearing claims when triangulated; a stricter pass would not. This is a deliberate trade-off, declared.
- **Single-pass single-reviewer risk.** Inter-rater reliability cannot be measured from one pass by one reviewer. Repeated runs by different reviewers (or different agents) are the only mitigation.
- **Falsifiability test is itself imperfect.** Some legitimately useful framework concepts (definitional, conventional) are not falsifiable in the empirical sense. The rubric's `UNFALSIFIABLE` verdict is informative, not condemning.
- **No experimental component.** IVP does not run the framework on a project to test it; that is the LoreWeave case study's job. IVP audits only the *texts*.
- **Same-reviewer classification bias.** When a single reviewer (human or agent) does both Phase 1 inventory (which includes the load-bearing classification) and Phase 2 verification, the load-bearing decision and the verification effort are correlated. A load-bearing item misclassified as non-load-bearing receives less rigour and may hide a finding. Mitigations: (a) a second-pass independent re-classification by a different reviewer, or (b) for single-reviewer runs, the classifications themselves are explicitly subject to audit and listed as a known risk in the limitations of the report. The 2026-05-08 rodage was a single-reviewer run; the limitation was acknowledged in [`findings-2026-05-08.md`](findings-2026-05-08.md) § 8 and is now formalized here.
- **Non-Latin and paywalled sources under-sampled.** A reviewer running IVP via web search alone will miss content not indexed by major engines (older standards PDFs behind login, non-English methodology literature, internal corporate documents). State this explicitly in any finding that depended on a single-tier reach.

---

## 8. Glossary of audit terms used in this document

| Term | Meaning |
|---|---|
| Audit trail | The ordered record of every search query, fetch action, and read action backing a verdict. |
| Backing | (Toulmin) The support that legitimizes the warrant. |
| Claim (Toulmin) | The assertion the argument intends to establish. |
| Data (Toulmin) | The evidence offered in support of the claim. |
| Falsifiability | The property that some conceivable observation could prove the claim wrong. |
| Grey literature | Sources outside formal peer review or standards bodies (vendor papers, industry reports, recognized practitioner blogs). |
| Load-bearing claim | A claim whose removal or refutation would change a sealed decision or a phase's design. |
| Qualifier (Toulmin) | Scope- or strength-limiting language attached to a claim. |
| Rebuttal (Toulmin) | Conditions explicitly acknowledged under which the claim would not hold. |
| Toulmin model | Stephen Toulmin, *The Uses of Argument* (1958), six-element structure for argument analysis. |
| Triangulation | Confirming a claim by independent sources from at least two tiers. |
| Warrant (Toulmin) | The general principle that bridges data to claim. |

---

## 9. Open questions about this methodology — status after rodage

Status legend: ✅ resolved (decision baked into v0.2 spec); ⏳ still open (carry to next debate cycle).

- ✅ **Is the load-bearing classification reliable?** Single-reviewer classification has correlation risk (resolved as a § 7 limitation; mitigation = second-pass independent classification or explicit risk-listing). Not a hard rubric requirement, since requiring two independent reviewers is impractical for many runs.
- ✅ **Should `UNFALSIFIABLE` automatically escalate severity, or informational only?** Resolved: escalates by one severity level above rubric base, except for definitional/conventional claims (§ 4.1 cross-cutting rule).
- ✅ **Industry-pragmatic admits T3; hard cap on the fraction of T3-only?** Resolved: not a hard fractional cap; instead a *tier-floor rule* — load-bearing claims resting solely on T3 are flagged at minimum MEDIUM regardless of T3 source accuracy (§ 4.1 cross-cutting rule).
- ✅ **Phase 6's gap matrix — own debate document or part of audit?** Resolved: stays as part of audit, lives in `docs/audit/benchmark.md` (§ 5 Phase 6 unchanged).
- ✅ **Re-run cadence — 90 days vs event-driven?** Resolved: event-driven primary, 12-month calendar fallback (§ 6 Cadence guidance).

⏳ **Carried open into next cycle:**

- Should the IVP spec itself be subject to a "meta-IVP" pass periodically? (Today the spec excludes itself from scope to avoid self-reference; a separate reviewer running IVP on the spec would be the cleanest answer.)
- For multi-reviewer runs, what inter-rater-reliability metric is reported (Cohen's κ on classification, agreement rate on verdicts)?
- For frameworks that themselves cite *other governance frameworks* (Dead Light citing PRINCE2, ITIL, CMMI), is there a recursion risk — does the framework inherit the cited framework's evidentiary issues? When and how should this be flagged in Phase 6?
- Should Phase 4 fallacy checklist be expanded based on which fallacies actually surface in real runs? (Add only after a fallacy has been observed to surface; do not pre-emptively bloat the checklist.)

---

## 10. References used to design this methodology

These are the methodology's own citations and are themselves subject to a future IVP pass.

- Stephen Toulmin, *The Uses of Argument* (Cambridge University Press, 1958; rev. ed. 2003) — argument decomposition.
- IIA, *International Standards for the Professional Practice of Internal Auditing* — independence and audit-trail principles.
- IAASB, ISA 200 / ISA 230 — audit documentation and professional skepticism.
- PRISMA 2020 statement (Page et al., *BMJ* 2021) — systematic review reporting structure (informs Phase 6 search rigour).
- Cochrane Handbook for Systematic Reviews of Interventions (current edition) — search-strategy and bias-assessment patterns.
- COSO Internal Control — Integrated Framework (2013) — control-environment framing.
- Karl Popper, *The Logic of Scientific Discovery* (Hutchinson, 1959) — falsifiability.
- DORA, *Accelerate: State of DevOps* (annual) — exemplar of industry-pragmatic empirical evidence.

---

## 11. Changelog

### v0.2 — 2026-05-09 (post-rodage refinement)

Driven by lessons from the 2026-05-08 rodage execution against the existing repository ([`findings-2026-05-08.md`](findings-2026-05-08.md)). Each change cites the specific gap the rodage exposed.

| § | Change | Why |
|---|---|---|
| Status header | Added `Version: v0.2` and pointer to changelog | Spec is now versioned; future revisions accumulate visibly. |
| § 2 principle 2 (Symmetric search) | Made disconfirming queries **mandatory** for load-bearing claims (was "for every citation"). | Rodage held the principle loosely — only ~6 of 30 verifications had disconfirming counterparts (§ 2 Pre-registered methodology checks in findings file). |
| § 3 source authority hierarchy (T1 row) | Split T1 into three sub-categories: international/governmental standards bodies, standards-body-owned commercial publishers (AXELOS / PMI / CMMI Institute / IFPUG / SEI), and peer-reviewed venues. | Rodage exposed ambiguity over whether AXELOS-style commercial-publishers-of-de-facto-standards counted as T1 or T2 (limitation surfaced around F-13 ITIL edition currency). |
| § 4.1 severity scale | Added three cross-cutting rules: `UNFALSIFIABLE` escalation by one level (resolved from § 9); load-bearing weighting (LB findings reported first, never bumped down); tier-floor rule (LB on T3-only flagged ≥ MEDIUM). | Resolves three open questions from § 9 v0.1. |
| § 5 Phase 1 Citations table | Citation deduplication is now an **explicit mandatory rule** with a `Locations` column (was implicit). | Rodage already followed this convention informally; now formalized so future runs do not drift. |
| § 5 Phase 2 procedure | Added: primary-source read **MANDATORY** for load-bearing citations (T2/T3 secondary insufficient for `VERIFIED`); disconfirming search **MANDATORY** for load-bearing; explicit step-numbered procedure (1–6). | Rodage limitation § 8.3: "No primary-source PDFs read in full" — would have caught F-01 (Miller) and F-03 (ISA 320) faster, and may have caught additional issues. |
| § 6 Re-run procedure (Cadence) | Replaced "every 90 days regardless" with event-driven primary triggers + 12-month calendar fallback. | Resolves § 9 open question; calendar-only cadence is a poor fit for a documentation framework. |
| § 7 Limitations | Added "Same-reviewer classification bias" and "Non-Latin and paywalled sources under-sampled". | First was acknowledged in [`findings-2026-05-08.md`](findings-2026-05-08.md) § 8.8; second was implicit and is now explicit. |
| § 9 Open questions | Updated with status legend (✅ resolved / ⏳ open). Five v0.1 questions resolved; four new questions surfaced from rodage carry into v0.3 cycle. | Standard housekeeping. |
| § 11 (this section) | Added. | Versioning hygiene. |

### v0.1 — 2026-05-08 (initial draft)

Initial specification — written before the rodage. Authored by Claude Code (Opus 4.7) at the project owner's request to define a repeatable workflow for outside-reviewer verification of Dead Light Framework documents. Industry-pragmatic mode, separate audit-from-authoring, pre-registered rubric.

### Out-of-scope-for-this-revision (carried forward)

These were considered for v0.2 but deferred:

- A formal *meta-IVP* pass over this spec (the audit doc auditing itself is excluded from scope to avoid self-reference; a separate reviewer is the cleanest path).
- Inter-rater-reliability formalism (Cohen's κ etc.) for multi-reviewer runs — not yet needed because all runs to date have been single-reviewer.
- Recursion-risk handling for governance-framework-citing-other-governance-frameworks (open in § 9).

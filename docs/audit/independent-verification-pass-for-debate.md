# Independent Verification Pass (IVP) — Audit Workflow (For Debate)

> **Status:** Draft, not final. To be refined after first execution against the existing repository.
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
2. **Symmetric search.** For every citation or claim sent to external search, the auditor runs both a confirming query *and* a disconfirming query. The disconfirming result, if any, is recorded with the same weight.
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
| **T1 — Primary standards / peer-reviewed** | ISO/IEC standards, IEEE standards, IAASB (ISA), SEI CMMI publications, peer-reviewed journal articles, ACM/IEEE conference proceedings, ITIL official publications, official PMBOK / PRINCE2 manuals | Strongest. Use when available; cite directly. |
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
| **HIGH** | Cited source exists but does not say what is claimed; argument has a missing or implausible warrant on a sealed decision; cross-document contradiction in a sealed phase. | "ISA 320 prescribes 5-10%" claim where ISA 320 actually says materiality is qualitative + quantitative; "Council ≥ 3" justified solely by 40k analogy. |
| **MEDIUM** | Stretched citation, missing qualifier, partial verification, weak warrant on an open question, terminology drift between drafts. | Source cited from secondary text without primary check; PMBOK threshold given without edition; "Council" in phase-0 vs phase-1 used with subtle scope difference. |
| **LOW** | Citation-style or hygiene issues that do not affect the substance. | Missing access date, link rot, inconsistent reference formatting, missing edition number where edition is stable. |

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
   - **Citations** — every reference to an external entity. Columns: id (`R-NNN`), file:line, cited entity (e.g., "COCOMO II", "ITIL 4 (2019)"), claimed attribute (e.g., "5–10% materiality", "Sev1/Sev2/Sev3 tiers"), type (standard | book | report | doctrine | historical fact).
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
2. If primary source not directly accessible, climb tier ladder (T1 → T2 → T3) and record the tier reached.
3. Run **disconfirming query** to find any source asserting the framework's claim is wrong about the citation's content (e.g., "ISA 320 materiality is qualitative not 5%").
4. Compare attribute claimed in framework against source. For numeric claims, the number must match within stated precision. For doctrine claims, the source must explicitly support the doctrine being attributed.
5. Assign verdict from rubric 4.2.

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

**Cadence guidance.** Run IVP after any of: a sealed decision being added, a new phase being drafted, a case study being introduced, or every 90 days regardless. The 90-day default mirrors typical audit-recurrence practice (internal audit annual + quarterly check-ins).

---

## 7. Limitations of this methodology

Stated up front so they cannot be raised post-hoc as defences against findings.

- **Reviewer model dependency.** When IVP is run by an AI agent, the agent's training data and search effectiveness bound what it can find. This biases toward English-language, web-indexed sources. A human reviewer with library access to non-indexed academic literature may surface more.
- **Recency bias of search engines.** Search engines down-rank older content, which can hide foundational sources. The recency policy in section 3 partly compensates.
- **Grey-literature admission.** Industry-pragmatic mode admits T3 sources for load-bearing claims when triangulated; a stricter pass would not. This is a deliberate trade-off, declared.
- **Single-pass single-reviewer risk.** Inter-rater reliability cannot be measured from one pass by one reviewer. Repeated runs by different reviewers (or different agents) are the only mitigation.
- **Falsifiability test is itself imperfect.** Some legitimately useful framework concepts (definitional, conventional) are not falsifiable in the empirical sense. The rubric's `UNFALSIFIABLE` verdict is informative, not condemning.
- **No experimental component.** IVP does not run the framework on a project to test it; that is the LoreWeave case study's job. IVP audits only the *texts*.

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

## 9. Open questions about this methodology (for first-pass debate)

These should be revisited *after* the first IVP run, not before — initial answers are first guesses.

- Is the load-bearing classification reliable? A claim's load-bearing status is itself a judgement; should the rubric require triangulation by two independent passes?
- Should `UNFALSIFIABLE` automatically escalate severity, or is it informational only?
- Industry-pragmatic admits T3; should there be a hard cap on the *fraction* of citations that can rest on T3 alone?
- Should Phase 6's gap matrix be its own debate document, or remain part of the audit?
- Re-run cadence — 90 days is a guess; should it be tied to events only, not calendar?

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

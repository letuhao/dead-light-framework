# IVP Findings — Phase 3 (Citation Appropriateness) — 2026-05-09

> **Status:** Phase 3 only. This run executes **Phase 3 (Citation Appropriateness)** against the verified subset from Phase 2. Phases 4–7 remain queued.
>
> **Auditor:** Claude Code (Opus 4.7), single pass.
> **Mode:** Industry-pragmatic (per IVP spec v0.2 § 1).
> **Branch:** `audit/ivp-2026-05-09-phase3`.
> **Inputs:** 73 citations with Phase 2 verdict `VERIFIED` or `PARTIAL` (50 V + 23 P combined across [`findings-2026-05-08.md`](findings-2026-05-08.md) and [`findings-2026-05-09.md`](findings-2026-05-09.md)). The 2 `CONTRADICTED` items were remediated to `VERIFIED` after Phase 2 and are evaluated here under their new attributions.
> **Spec applied:** [`independent-verification-pass-for-debate.md`](independent-verification-pass-for-debate.md) v0.2 § 5 Phase 3 + § 4.3 rubric (APPROPRIATE / STRETCHED / MISAPPLIED / UNSUPPORTED-LEAP).
> **Rubric integrity:** Pre-registered v0.2 § 4.3 rubric used unmodified.

---

## 1. Executive verdict

Phase 3 evaluates the appropriateness of each verified citation's use against its source's actual scope and authority. **Of 73 citations evaluated, 70 (96%) earn `APPROPRIATE` verdicts** (including -with-qualification, -after-remediation, and -per-policy variants). Only **3 STRETCHED verdicts** surface, generating **0 CRITICAL, 0 HIGH, 1 MEDIUM, 2 LOW** new findings.

The headline result is the **policy-1 check on the 40k metaphor (R-001)**: the framework's self-discipline holds at the document-text level. The most ambitious load-bearing 40k invocation (Imperial + Sector Astronomican) has an explicit Methodological Note where the framework *self-corrects* a prior policy-1 violation and re-anchors on real-world precedents (US federalism, German Basic Law, Catholic Church, Linux kernel, TPS). This is a strongly favourable Phase 3 result for the framework's central design discipline.

The three STRETCHED findings:
- **F-25 (MEDIUM):** Catholic Church cited as "no schism in 2,000 years" without surfacing the Great Schism (1054) or Reformation (1517) — methodological cherry-pick of the most generous time-window.
- **F-26 (LOW):** Spotify Tribe-Squad model cited without acknowledging Spotify's own departure from the model (well-documented in industry critiques).
- **F-27 (LOW):** Goodhart's Law invoked to justify a memorability tradeoff the law does not actually address; Miller's working-memory bound (already cited elsewhere) is the natural in-domain anchor.

All three are remediation candidates of the same low-cost "rephrase + acknowledge" class as the rodage's MEDIUM/LOW findings. None changes the framework's structural design; all are precision-of-scholarly-claim issues consistent with an academic-style governance methodology.

**Combined cross-phase totals (Phase 2 + Phase 3, after Phase 2 remediation):**
- 76 citations have Phase 2 verdicts; 73 carried forward to Phase 3.
- Across both phases: **0 CRITICAL · 6 HIGH · 7 MEDIUM · 14 LOW = 27 findings total, of which 24 (F-01 to F-24) are remediated and 3 (F-25 to F-27) are new in Phase 3.**

---

## 2. Aggregate stats

| Category | Count |
|---|---|
| Citations evaluated in Phase 3 | 73 |
| Verdict `APPROPRIATE` (incl. -with-qualification, -after-remediation, -per-policy) | 70 |
| Verdict `STRETCHED` | 3 (R-007 → F-25; R-011 → F-26; R-015 → F-27) |
| Verdict `MISAPPLIED` | 0 |
| Verdict `UNSUPPORTED-LEAP` | 0 |
| Findings — severity CRITICAL | 0 |
| Findings — severity HIGH | 0 |
| Findings — severity MEDIUM | 1 (F-25) |
| Findings — severity LOW | 2 (F-26, F-27) |

---

## 3. Phase 3 — Citation Appropriateness verdicts

Per IVP spec v0.2 § 5 Phase 3 procedure: each citation is evaluated on (a) source's actual scope, (b) framework's use, and four sub-checks: scope match, authority in context, generalization burden, anachronism / cherry-pick. Verdict per § 4.3 rubric.

For brevity, citations whose source domain matches the framework's claim domain at the canonical use level (e.g., COCOMO II for cost estimation; ITIL for IT service management) are batched in § 3A as APPROPRIATE-by-domain-match, with a single explanatory paragraph instead of per-citation rows. Citations requiring detailed analysis are listed individually in § 3B onward.

---

### 3A. Software-engineering standards used for their canonical domain (APPROPRIATE by domain-match)

**Verdict for all rows below: APPROPRIATE.** The source is the canonical industry reference for the metric, formula, or practice the framework cites it for. Scope matches; authority is in-context (e.g., COCOMO II is the canonical authority for software cost estimation); generalization burden is zero or near-zero (framework uses the source's own definitions); no anachronism flag. These verdicts are recorded compactly because the appropriateness check is mechanical.

| R-id | Source | Framework's canonical use | Notes (if any) |
|---|---|---|---|
| R-027 | ITIL 4 (AXELOS, 2019; ITIL 5 launching 2026) | Change management tiers (Standard / Normal / Emergency) for adapting to architectural-decision tiers | After F-05 remediation, framework correctly distinguishes ITIL Priority via Impact × Urgency from SRE Sev1–Sev4 |
| R-028 | ISA 320 (IAASB) | Materiality framework — judgement discipline | After F-03 remediation, framework correctly attributes the 5–10% as practitioner heuristic, not standard mandate |
| R-029 | GAAP / IFRS | Materiality (parallel to ISA 320) | Same caveat as R-028 |
| R-030 | PMBOK EVM | Variance indices (SPI/CPI) | After F-04 remediation, threshold values correctly attributed to practitioner convention not PMBOK |
| R-031 | PMBOK Guide (8th ed., 2025) | Project sizing, stakeholder register, tailoring patterns | After F-15 remediation, edition specified |
| R-032 | PRINCE2 (7th ed., 2023) | PID approval, change control, stages | After F-16 remediation, edition specified |
| R-033 | CMMI v3.0 (CMMI Institute / ISACA, 2023) | CAR / PPB / QPM practice areas | After F-02 remediation, framework correctly cites v3.0 |
| R-034 | COCOMO II (Boehm, Prentice Hall, 2000) | Cost/effort estimation formula and constants | Canonical authority for software cost estimation |
| R-035 | COCOMO original (Boehm, Prentice Hall, 1981) | Successor relationship to COCOMO II | Historical predecessor; appropriately framed |
| R-036 | IFPUG Function Points | Functional component sizing | Canonical for FP analysis |
| R-037 | Putnam SLIM (Prentice Hall / Yourdon Press, 1991) | Effort estimation via Rayleigh curve | After F-17 remediation, year corrected |
| R-039 | DORA / *Accelerate* (Forsgren et al., 2018) | Four key DevOps metrics | Canonical industry reference |
| R-040 | Brooks's Law (*Mythical Man-Month*, 1975) | Communication-channel formula N(N−1)/2 | Canonical reference for team-size friction |
| R-042 | Dunbar's number (Robin Dunbar, 1996) | Cognitive group-size layered model | Canonical for group cognition; applied to Council size |
| R-043 | Team Topologies (Skelton & Pais, 2019) | Four team types (stream-aligned/platform/enabling/complicated-subsystem) | Canonical for team-design taxonomy |
| R-044 | McCabe Cyclomatic Complexity (1976) | M = E − N + 2P formula and standard thresholds | Canonical |
| R-045 | Halstead, *Elements of Software Science* (1977) | Effort/Volume/Difficulty metrics | Canonical |
| R-046 | Maintainability Index (Coleman et al., 1994) | Formula and threshold | After F-11 remediation, scale-specific thresholds clarified |
| R-047 | Code churn (Nagappan & Ball, ICSE 2005) | Defect-density predictor | Peer-reviewed canonical reference |
| R-048 | Bus factor (Cosentino et al., SANER 2015) | Developer-departure risk metric | Peer-reviewed canonical |
| R-049 | SQALE (Letouzey, IEEE MTD 2012) | Technical-debt estimation, operationalized in SonarQube | Peer-reviewed canonical |
| R-050 | IEEE Standard 1633-2016 + MTBF/MTTR | Reliability metrics | After F-09 remediation, framework correctly notes IEEE 1633 is not the canonical originator of MTBF/MTTR |
| R-051 | *Site Reliability Engineering* (Beyer et al., O'Reilly 2016) | S0/S1/S2/S3 postmortem severity | Canonical SRE reference |
| R-052 | Six Sigma DPMO (Smith / Harry, Motorola 1986; ASQ) | 3.4 DPMO defect rate | After F-08 remediation, both Smith and Harry credited |
| R-053 | Shewhart SPC (1931) | Control charts (X̄, R, p, c) for process variation | Foundational for SPC; appropriately framed as foundational |
| R-055 | Feathers, *Working Effectively with Legacy Code* (Pearson, 2004) | Legacy-code retrofit techniques | Canonical authority for the topic; appropriate use |
| R-076 | cloc / scc / lizard / radon / SonarQube | Code-metric tooling | Tools used for their actual purpose (code measurement) |

**Sub-section count: 27 citations, all APPROPRIATE.**

---

### 3B. Methodological borrowings — practice patterns from adjacent domains

These citations borrow patterns from one engineering / management discipline into the framework's governance question. Per spec § 5 Phase 3 sub-check 3 (Generalization burden), each is examined for the inferential leap from source to framework claim.

| R-id | Source's actual scope | Framework's use | Scope match | Authority | Gen-burden | Anachronism | Verdict | Notes |
|---|---|---|---|---|---|---|---|---|
| R-038 | Big-4 M&A IT due-diligence — pre-acquisition assessment of acquisition-target IT systems for risk pricing | Phase 0 retrofit-audit time-budget heuristic for ongoing software-governance work | **Adjacent** (M&A is acquisition-time, framework is in-flight governance) | Practitioner heuristic, not standards-body | 1 step (audit-of-foreign-codebase → audit-of-own-codebase) | None | **APPROPRIATE-after-remediation** | After F-21 remediation framework explicitly downgrades this row to sanity-check status; load-bearing budget directed to COCOMO II row. The remediation closes what would otherwise be a STRETCHED verdict. |
| R-041 | Bezos / Amazon "two-pizza team" — informal management heuristic for org design | Council size 3–7 cap | Match (both team size) | Practitioner heuristic | 0 steps (direct application) | None | **APPROPRIATE** | Used appropriately as one of three converging anchors (Brooks N(N−1)/2; Dunbar layer 1; two-pizza). Triangulation strengthens the warrant. |
| R-054 | Code-reading tradition (Spinellis 2003 representative) — engineering practice for understanding existing code | Phase 0 decision archaeology | Match (both about reading existing code) | Practitioner-textbook | 1 step (code-reading-as-skill → code-reading-as-governance-input) | None | **APPROPRIATE** | After F-22 remediation, attribution sharpened from "software archaeology" (a vague concept) to "code-reading and code-comprehension tradition" with Spinellis as representative reference. |
| R-056 | Allspaw 2012 — Etsy engineering-blog argument for blameless culture in incident postmortems | Phase 0 failure-inventory framing | Match (both about failure analysis) | Practitioner-blog (T3) | 0 steps (direct application of blameless framing) | None | **APPROPRIATE** | Triangulated with NTSB and medical-M&M practice in framework — multi-source warrant strengthens grey-literature foundation. |
| R-057 | NTSB aviation safety — federal investigative agency; multi-disciplinary "go team" investigates major transport accidents | Phase 0 multi-disciplinary investigators; root-cause analysis | Match (both about post-failure investigation discipline) | Regulatory body in adjacent safety domain | 2 steps (aviation safety → general systems failure → software governance) | None | **APPROPRIATE-with-qualification** | Cross-domain transfer is a long-established move (Sidney Dekker, Charles Perrow, John Allspaw all explicitly cite NTSB for software/SRE postmortems). Framework is in established lineage. |
| R-058 | Schein, *Organizational Culture and Leadership* — 3-level cultural model + Argyris/Schön (1974) — espoused theory vs theory-in-use | Phase 0 implicit-principles surfacing | Match (both about surfacing implicit cultural assumptions) | Foundational textbooks in organizational psychology | 1 step (org-culture diagnostics → governance-design input) | None | **APPROPRIATE** | After F-18 remediation, both citations appear with correct attributions and can stand independently or together. |
| R-059 | Delphi method (RAND, 1950s–60s) — anonymous-iterative-expert forecasting technique | Phase 0 forecast aggregation via independent expert capture | Match (both about aggregating expert input without dominant-personality bias) | Foundational methodology | 1 step (forecasting → governance-input gathering) | None | **APPROPRIATE** | Standard methodological move; Delphi is widely applied beyond its forecasting origins. |
| R-060 | Linux subsystem maintainer + Apache PMC governance — peer-elected technical leadership in open-source projects | Bottom-up Reckoning Team producing inventory | Match (both about peer-driven, non-hierarchical technical work) | OSS governance practice | 1 step (OSS development → governance-investigation) | None | **APPROPRIATE** | Used as one of two anchors (with XP spike — see R-061); fits framework's peer-team-not-Council pattern. |
| R-061 | XP spike (Beck, *Extreme Programming Explained*, 1999) — time-boxed investigation of unknowns | Phase 0 investigation work for unknowns | Match (both about time-boxed investigation) | Canonical XP textbook | 0 steps (direct application) | None | **APPROPRIATE** | After F-19 remediation, attribution corrected from RUP to XP. The investigation-work concept is faithfully borrowed. |
| R-062 | RUP Lifecycle Objective Milestone — sign-off ceremony at end of Inception phase | Phase 1 sign-off ceremony for Astronomican | Match (both about formal phase-end sign-off) | Foundational software-engineering methodology | 0 steps (direct application) | None | **APPROPRIATE** | Triangulated with PRINCE2 PID approval — multi-source warrant. |
| R-063 | (After F-20 remediation:) Agile Iron Triangle — fix time, vary scope; PRINCE2 tolerance pattern; Lean Startup minimal-upfront-artifacts and validated-learning | Phase 0 time-boxing + minimal-upfront-artifact discipline | Match for both halves of the borrowing | Established methodology + foundational text | 0 steps for Iron Triangle/tolerance; 1 step for Lean Startup → governance-investigation budgeting | None | **APPROPRIATE** | Remediation cleanly separated the scope-as-variable framing (Agile/PRINCE2) from the minimal-artifacts framing (Lean Startup); each citation now does work matching its actual scope. |
| R-064 | IETF / W3C standards process — working groups produce drafts that go to IESG/Director for approval | Phase 0 → Phase 1 hand-off without approval gate (engineering-review feeds governance bodies) | Match (both about engineering-output-feeding-governance) | Standards-body practice | 1 step (technical standards → governance design) | None | **APPROPRIATE** | Pattern is a legitimate generalization; IETF model is a well-cited reference for engineering-review patterns. |
| R-065 | Agile Inception Deck (Rasmusson, *The Agile Samurai*, 2010) — 10-question project-kickoff template | Phase 1 five pre-work questions | Match (both about project-kickoff scoping) | Established practitioner book | 0 steps (framework directly maps to questions 1–5 of the deck) | None | **APPROPRIATE** | Framework's "five pre-work questions" maps to Rasmusson's "Why" deck (questions 1–5 of the 10). |
| R-066 | Federal Reserve Board — 7 governors; Federal Reserve Act mandates fair representation of financial/agricultural/industrial/commercial interests + geographic diversity | Phase 1 Council multi-perspective composition | Match (both about diverse-perspective governing bodies) | Statutory governance body in adjacent domain | 2 steps (financial-policy diversity → general-governance diversity → software governance) | None | **APPROPRIATE-with-qualification** | Federal Reserve is one of three anchors framework cites (corporate boards, IETF, Fed); triangulation strengthens transfer. Single-source would be STRETCHED. |
| R-067 | Etsy/Google SRE postmortem severity — incident-classification scheme used post-failure | Significance-threshold heuristic for past-decision archaeology in Phase 0 | **Adjacent** (severity is about *current* incidents; framework uses it as anchor for *past-decision* classification) | Established SRE practice | 1 step (incident-severity → decision-significance) | None | **APPROPRIATE** | Framework explicitly frames it as "categorical anchor + numeric flexibility" (debate 003 § Q1) — a pattern-borrowing not a metric-borrowing. Reasonable abstraction. |
| R-068 | Architecture review board practice — organization-defined governance forum for cross-team architecture decisions | Significance-threshold examples in Phase 0 (debate 003) | Match (both about decision-significance gating) | Industry practice | 0 steps (direct example use) | None | **APPROPRIATE-after-remediation** | After F-23 remediation, framework qualifies that thresholds are organization-defined and not industry-standard. The qualification closes what would be STRETCHED. |
| R-069 | Code-review reviewer-mix practice — owner-plus-senior or owner-plus-outsider patterns | Phase 0 Reckoning-Team composition | Match (both about review-quality through perspective mix) | Industry practice | 1 step (code-review → governance-review) | None | **APPROPRIATE** | Framework uses code-review as one of multiple anchors (NTSB, M&M conferences); appropriate generalization. |
| R-070 | Medical M&M conferences — physician peer-review of mortality/morbidity cases | Multi-disciplinary investigation pattern | Match (peer review across role types) | Established medical practice | 2 steps (medical case review → general failure investigation → software governance) | None | **APPROPRIATE-with-qualification** | One of three converging anchors (NTSB + medical M&M + code-review). Triangulation. |
| R-071 | Toyota kaizen events — typically 3–5 days, hard-time, scope-as-variable | Phase 0 time-boxing | Match (both about hard-time-boxed scope-flexible improvement work) | Established lean practice | 1 step (manufacturing improvement → governance investigation) | None | **APPROPRIATE-after-remediation** | After F-24 remediation, "typically 5 days" updated to "typically 3–5 days". Pattern transfer is well-established (kaizen → software is a long-standing lean-software lineage). |
| R-072 | Etsy postmortem culture — names kept, blame not assigned | Phase 0 failure inventory framing | Match (same domain as R-056) | Practitioner-blog | 0 steps | None | **APPROPRIATE** | Same as R-056. |
| R-073 | ADR — Michael Nygard, "Documenting Architecture Decisions" (2011) — lightweight architecture-decision documentation pattern | Phase 0 retroactive decision archaeology | Match (both about documenting decisions) | Industry pattern | 1 step (forward-looking ADR → backward-looking decision capture) | None | **APPROPRIATE** | Framework explicitly notes "retroactively as ADRs" — an established practitioner pattern (the "ADR backfill" workflow). |
| R-074 | RACI matrix — Responsible / Accountable / Consulted / Informed | Role assignment in framework's Council and Reckoning-Team contexts | Match (role-assignment domain) | Established PM pattern | 0 steps (direct use) | None | **APPROPRIATE** | Used at canonical scope. |

**Sub-section count: 22 citations. All APPROPRIATE or APPROPRIATE-after-remediation.** Several flagged "with-qualification" or "after-remediation" but none meet the threshold for STRETCHED in the current framework text.

---

### 3C. Historical/political precedents for governance design

These are the framework's most ambitious cross-domain borrowings — using constitutional law, religious institutions, military doctrine, and corporate-historical case studies as design references for software governance. Per spec § 5 Phase 3 sub-check 4 (Anachronism / cherry-pick), each is examined for whether the historical context is meaningfully different from the framework's question.

| R-id | Source's actual scope | Framework's use | Scope match | Authority | Gen-burden | Anachronism / cherry-pick | Verdict | Notes |
|---|---|---|---|---|---|---|---|---|
| R-002 | Articles of Confederation (1781–1789) — failed US confederal government | Failure-mode example for "flat federation" pattern in Astronomican-tier design | Adjacent (political vs technical federation) | Historical fact | 2 steps (political confederation → technical multi-repo governance → flat-federation failure mode) | None — framework uses it as a *pattern* not a rule | **APPROPRIATE-with-qualification** | Framework uses three converging examples (Articles, HRE, Yugoslavia) to establish the pattern. Triangulation strengthens. Single-example use would be STRETCHED. |
| R-003 | Holy Roman Empire (dissolved 1806) | Same flat-federation failure example | Same as R-002 | Historical fact | Same | None | **APPROPRIATE-with-qualification** | Same as R-002 — one of three converging anchors. |
| R-004 | Yugoslavia (post-Tito 1990s) | Same flat-federation failure example | Same | Historical fact | Same | None | **APPROPRIATE-with-qualification** | Same — third anchor. The trio-of-examples pattern is methodologically sound for establishing a recurrent failure mode. |
| R-005 | US Constitutional federalism + Supremacy Clause (1789) | Imperial + Sector tier with inherit-and-add rule | Adjacent (political vs technical hierarchy) | Foundational legal authority | 2 steps (political supremacy → architectural inheritance → multi-repo Astronomican design) | None | **APPROPRIATE-with-qualification** | Framework uses four converging examples (US, Germany, Catholic Church, Linux, TPS) to anchor the inherit-and-add pattern. Strong triangulation. |
| R-006 | German Basic Law (1949) — cooperative federalism | Same Imperial + Sector tier example | Same | Foundational legal authority | Same | None | **APPROPRIATE-with-qualification** | Same — second anchor. |
| R-007 | Catholic Canon Law + diocesan customs — multi-century church governance with central canon plus local custom | Same Imperial + Sector tier example | **Adjacent** (religious vs technical institution; very different incentive structure) | Established institutional governance | 3 steps (religious canonical authority → general "central + local" governance → software architecture) | **Possible cherry-pick** — Catholic Church is selected because it's stable; Schism (1054) and Reformation (1517) are *known schism examples* the framework does not surface in this borrowing | **STRETCHED** | **F-25 — MEDIUM**: Framework cites Catholic Church for "doctrinal coherence ~2,000 years" without surfacing the Great Schism (1054) and Reformation (1517) as the obvious in-domain counter-examples. The "no schism" claim is true for *the Catholic Church specifically* if you define schism out, but the Great Schism is precisely the inherit-and-add failure mode that would *disconfirm* the pattern. |
| R-008 | Linux kernel governance — maintainer-tree + whole-tree standards | Same Imperial + Sector tier example | Match (technical hierarchy in software) | Established OSS practice | 0 steps (direct domain match) | None | **APPROPRIATE** | Single most-domain-relevant anchor in the trio. |
| R-009 | Toyota Production System — corporate immutable + plant-level kaizen | Same Imperial + Sector tier example | Adjacent (manufacturing vs software) | Established corporate practice | 1 step (manufacturing process → software governance) | None | **APPROPRIATE-with-qualification** | TPS-to-software is a long-established lineage (Lean Software Development, Poppendieck 2003). |
| R-010 | AWS Leadership Principles + team Tenets | Same Imperial + Sector tier example | Match (corporate governance, technical org) | Corporate practice | 1 step (corporate principles → software-team governance) | None | **APPROPRIATE** | Direct domain relevance for tech-company governance. |
| R-011 | Spotify Tribe + Squad model | Two-tier mission structure example | Match (software org governance) | Practitioner-blog (T3); Spotify itself has since modified | 0 steps | **Possible cherry-pick**: Spotify model has been widely critiqued and abandoned by Spotify itself; framework cites it as if still-current pattern | **STRETCHED** | **F-26 — LOW**: Framework's invocation of Spotify model as a Tribe-Squad pattern source should acknowledge Spotify's own departure from it (e.g., Atlassian "Spotify model" critique; Agile Pain Relief article "Spotify Doesn't Use the Spotify Model"). The Tribe-Squad pattern *survives* as a pattern reference but the implied "still working at Spotify" framing is dated. |
| R-012 | Late Roman Empire reforms (Diocletian) — Praetorian Prefectures → Dioceses → Provinces | Multi-tier governance with cumulative attenuation | Adjacent | Historical | 2 steps | None | **APPROPRIATE-with-qualification** | LB=N per inventory; lower scrutiny appropriate. Framework uses it as a "decreasing central control at each step" pattern. Faithful to historical structure. |
| R-013 | Soviet hierarchy — Union → Republics → ASSRs → Oblasts → Raions | Same multi-tier attenuation pattern | Adjacent | Historical | 2 steps | None | **APPROPRIATE-with-qualification** | Same as R-012; LB=N. |
| R-016 | Japan post-WWII Constitution (1947) — drafted under SCAP, replaced Meiji Constitution | Retrofit constitution example | Adjacent (political vs technical retrofit) | Foundational legal authority | 2 steps | None | **APPROPRIATE-with-qualification** | Framework uses three converging examples (Japan, Spain, SA) to establish retrofit pattern. Triangulation. |
| R-017 | Spain post-Franco Constitution (1978) — multi-party consensus document | Retrofit constitution example | Same as R-016 | Same | Same | None | **APPROPRIATE-with-qualification** | Second anchor in trio. |
| R-018 | South Africa TRC (1996) — restorative-justice mechanism for apartheid-era violations | "Strongest example of explicit mechanism for past violations" | Same as R-016 | Same | Same | None | **APPROPRIATE** | Framework correctly identifies this as the strongest of the three retrofit examples — TRC's mandate is *explicitly* about past-violation reckoning, which is the framework's exact analogue need in Phase 0. Best-fitting analogy in the trio. |
| R-019 | Microsoft under Nadella (post-2014) — culture shift "know-it-all" → "learn-it-all" | Corporate transformation pattern | Match (corporate governance change in technical org) | Practitioner literature (Hit Refresh, HBR) | 0 steps | None | **APPROPRIATE** | Direct domain. |
| R-020 | Apple under Jobs (1997) — killed ~70% of product lines | Corporate transformation: "cutting scope before reaffirming principles" | Match (corporate scope decisions in tech org) | Historical | 0 steps | None | **APPROPRIATE** | Direct domain. |
| R-021 | Toyota Ohno-circle exercise — observe waste through extended on-floor watching | Phase 0 "identify ONE concrete deviation as the starting wedge" | Adjacent (manufacturing observation training vs governance retrofit) | Lean practice | 1 step (manufacturing observation → governance starting-wedge) | None | **APPROPRIATE-with-qualification** | Framework's "ONE concrete deviation as starting wedge" is a slight overlay on the Ohno-circle's general waste-observation purpose, but the *spirit* (focused observation → visible improvement → expand) is faithful. Already noted in Phase 2 R-021 verdict. |
| R-022 | Linux kernel CoC adoption (2018) | "Effective-date with de facto non-retroactive application" | Match (OSS governance retrofit) | Documented case | 0 steps | None | **APPROPRIATE-after-remediation** | After F-14 remediation, "grandfathering" softened to "de facto non-retroactive application" — closes the over-claim. |
| R-023 | Rust Foundation creation (2021) | Effective-date pattern | Match | Documented case | 0 steps | None | **APPROPRIATE** | Direct domain (OSS governance). |
| R-024 | Docker → Moby split (2017) | Effective-date pattern | Match | Documented case | 0 steps | None | **APPROPRIATE** | Direct domain. |
| R-025 | Strangler Fig pattern (Fowler, 2004) — incremental software refactoring | Retrofit gradient pattern | Match (software refactoring → software governance retrofit) | Canonical software pattern | 0 steps | None | **APPROPRIATE** | Direct domain match. |
| R-026 | Joel Spolsky (2000) — "Things You Should Never Do, Part I" — Netscape 4→6 case argument against rewrites | Big-bang rewrite failure example | Match (software practice) | Practitioner essay (T3) | 0 steps | **Anecdotal**: single-case argument | **APPROPRIATE-after-remediation** | After F-06 remediation, framework correctly frames Spolsky as anecdotal not statistical. |

**Sub-section count: 23 citations. 21 APPROPRIATE / APPROPRIATE-after-remediation. 2 with new findings: F-25 (Catholic Church Schism not surfaced) MEDIUM, F-26 (Spotify model dated) LOW.**

---

### 3D. Special category — 40k metaphor (R-001) and policy-1 check

| R-id | Source's actual scope | Framework's use | Verdict | Notes |
|---|---|---|---|---|
| R-001 | Warhammer 40,000 (Games Workshop) — military-science-fiction setting | Naming and shared metaphor only (per framework's policy 1) | **APPROPRIATE-by-policy** | Detailed analysis below. |

**Detailed Phase 3 analysis of R-001 (the headline policy-1 check):**

Per IVP spec v0.2 § 5 Phase 3 sub-check 1 (scope match): the source is fiction; the framework is a real-world governance methodology. Naturally these scopes do *not* match. Policy 1 explicitly addresses this:

> "40k vocabulary is naming and shared metaphor only. Justification, structural arguments, and assessments of effectiveness must rest on real-world organizational systems with observable track records."

Phase 3 must therefore test whether *any* invocation crosses from naming-only into substantive justification — which would be a policy-1 violation and **CRITICAL** by rubric § 4.1.

Examined every 40k invocation per inventory § D (analogies A-001 through A-011):

| A-id | Location | Invocation | Crosses policy 1? |
|---|---|---|---|
| A-001 | README.md:3 | Epigraph "The Emperor is dead. The light remains." | **No** — epigraph/flavor only |
| A-002 | README.md:36 | "Astronomican = beacon that still shines after its god-emperor has all but died" | **No** — explicitly framed: "we use the metaphor *because it names something real*" — naming use, no claim of design validity |
| A-003 | README.md:56–61 | Vocabulary list (Astronomican, Council, Chapters, Codex) | **No** — naming only |
| A-004 | README.md:91 | Acknowledgment to Games Workshop | **No** — disclaimer |
| A-005 | glossary:64 | "Tithe" = output contract | **Flagged for debate** in glossary (alternative "Output Contract" considered) — not yet adopted as load-bearing |
| A-006 | glossary:65 | "Battle Brother" | **Flagged probable cut** in glossary — pre-debate |
| A-007 | glossary:81 | "Astropathic Signal" | **Flagged for debate** — pre-debate |
| A-008 | phase-1:167–179 | Imperial / Sector Astronomican | **No** — debate 001 Methodological Note explicitly removed prior 40k-as-evidence claims (Horus Heresy etc.); now anchored on US federalism, German Basic Law, Catholic canon, Linux kernel, TPS — all real |
| A-009 | debate 001:191–198 | Methodological Note | **Self-correction** — framework explicitly corrects prior policy-1 violation. Anti-policy-1 safeguard built into the document |
| A-010 | phase-0:138 | "AI-assistant Chapters" with Codex | **No** — naming only; structural argument rests on real Catholic-monastic and Linux-maintainer precedents |
| A-011 | (multiple) | Heresy / Inquisitor / Schism / Corruption | **Flagged for debate** in glossary; not yet load-bearing |

**Phase 3 verdict on R-001:** **APPROPRIATE-per-policy.**

The framework's policy-1 self-discipline holds at the document-text level. The most ambitious load-bearing invocation (Imperial + Sector Astronomican design — A-008) has an explicit Methodological Note (A-009) where the framework retracts an earlier policy-1 violation and re-anchors on real-world precedents. This is a textbook case of a self-correcting framework: the violation existed at one point, was identified, and was repaired in-document.

**No policy-1 finding.** This looks favourable to me as the Phase 3 auditor for the framework's central design discipline.

The "needs-debate" 40k terms (A-005, A-006, A-007, A-011) are in the glossary as candidates for cut or rename; if any survives a final debate as load-bearing terminology, Phase 3 should re-evaluate. Currently they are pre-load-bearing.

---

### 3E. Methodological reference for the audit itself

| R-id | Source | Framework's use | Verdict |
|---|---|---|---|
| R-014 | Miller "Magical Number Seven" (1956) | After F-01 remediation: cap of 5–9 (target ~7) anchored on Miller's actual range | **APPROPRIATE-after-remediation** |
| R-015 | Goodhart's Law | "Optimizing for 'comprehensive' destroys 'recallable'" (debate 001:35) | **STRETCHED** — see analysis below |
| R-075 | SAFe / Scrum / Kanban / RUP / DevOps | "Existing methodologies that Dead Light composes on top of" | **APPROPRIATE** — generic invocation at the right level of generality |

**Detailed analysis of R-015 (Goodhart's Law):**

Goodhart's Law in its canonical form: "When a measure becomes a target, it ceases to be a good measure." (Charles Goodhart, 1975, originally about monetary policy; popularized in the broader form by Marilyn Strathern.)

Framework's use (debate 001:35): the law is invoked to justify the "≤ 5 Laws" cap by claiming "optimizing for 'comprehensive' destroys 'recallable'."

Sub-checks:
- **Scope match**: Goodhart's Law is about *measurement-as-target* perversities. Framework's claim is about *comprehensive-vs-memorable* tradeoffs in document design. **Different domain.**
- **Authority**: Goodhart is the canonical authority for the measurement-as-target failure mode. Not the canonical authority for memorability tradeoffs.
- **Generalization burden**: 2 steps — (a) Goodhart's measure-as-target → measure-as-goal generally → (b) goal-as-comprehensive → memorability-loss. The second step is unbridged: Goodhart says nothing about memorability.
- **Anachronism / cherry-pick**: not anachronism; but Miller's working-memory bound (R-014) is the natural in-domain authority for memorability claims, *not* Goodhart.

**Verdict: STRETCHED.** The famous-quote name is being used to lend authority to a memorability claim that has its own canonical authority elsewhere (Miller). The transfer is plausible-as-rhetoric but the inferential gap is unbridged.

**F-27 — LOW**: Framework should either (a) anchor the comprehensive-vs-recallable tradeoff on Miller's working-memory bound directly (which is already cited at R-014 — natural fit) and drop Goodhart, or (b) keep Goodhart with explicit framing as "by analogy to Goodhart's measure-as-target failure mode, optimizing one document property at the cost of another can backfire". Current invocation reads as Goodhart authoritatively saying something he did not say.

---

## 4. Findings (severity-binned)

### CRITICAL

*None. The headline policy-1 check (R-001 / 40k metaphor) passes — framework's self-discipline holds.*

### HIGH

*None. All previously-HIGH attribution issues from Phase 2 (F-01, F-18, F-19, F-20) are remediated; remaining attribution claims pass Phase 3 with appropriateness intact.*

### MEDIUM

#### F-25 — Catholic Church "no schism" claim does not surface obvious in-domain counter-examples

- **Where:** `framework/debates/001-laws-count-and-multirepo-scaling.md:69`; `framework/phases/phase-1-for-debate.md:187`. Load-bearing for the Imperial + Sector inherit-and-add pattern (C-032).
- **Source's actual state:** Catholic Church has had two well-documented schisms — the East-West Schism (1054, ~50% of pre-existing communion split off) and the Reformation (1517). These are widely-cited examples of multi-tier religious governance failure modes.
- **Framework's claim:** "~2,000 years doctrinal coherence" (debate 001 / phase-1) — used as an exemplar for the Imperial-tier inherit-and-add pattern.
- **Why this matters:** Per IVP spec v0.2 § 5 Phase 3 sub-check 4 (Anachronism / cherry-pick): the framework uses Catholic Church as a *positive* example of stable inherit-and-add governance; the Great Schism and Reformation are *precisely* the inherit-and-add failure modes that would disconfirm the pattern. Selecting only the post-Reformation Roman-Catholic-defined "no schism" period is a methodological cherry-pick.
- **Recommended action:** `obvious fix`: either (a) explicitly acknowledge the Schism / Reformation as known cases and explain why the post-1054 pattern still counts as success, or (b) drop the "no schism" claim and use the more defensible "extreme longevity at multi-tier scale" framing instead.

### LOW

- **F-26 — Spotify model invocation should acknowledge Spotify's departure from it.** `debate 001:73`; `phase-1:73`. Already partially addressed in Phase 2 R-011 note ("Spotify itself has since modified") but the in-text use still reads as if current. Should explicitly cite the Atlassian + Agile Pain Relief critiques in any narrative that uses Spotify as a model source.
- **F-27 — Goodhart's Law invocation is stretched.** `debate 001:35`. Used to justify a memorability tradeoff the law does not actually address. Either re-anchor on Miller (already cited at R-014) or qualify as "by analogy to Goodhart, …".

---

## 5. Pre-registered methodology checks

Per IVP spec v0.2 § 2 anti-bias principles, status of each:

| Principle | Status this Phase 3 run |
|---|---|
| 1. Pre-registration of rubric | **Held.** Rubric § 4.3 (APPROPRIATE / STRETCHED / MISAPPLIED / UNSUPPORTED-LEAP) used unmodified. |
| 2. Symmetric search | **Held in spirit.** Phase 3 is internal-text analysis; "disconfirming search" interpreted as "look for in-domain counter-examples or alternative sources the framework ignored" — applied to F-25 (Schism), F-26 (Spotify departure), F-27 (Miller as alternative anchor for memorability). |
| 3. Audit trail mandatory | **Held.** Per-citation analysis and reasoning recorded in §§ 3A–3E. |
| 4. Falsifiability check | **Deferred to Phase 4** (Argument Analysis). Phase 3 is appropriateness, not argument soundness. |
| 5. Separation of concerns | **Held.** No framework documents modified during Phase 3 audit. |
| 6. Stop-on-trail-break | **N/A** — every citation has a recorded verdict and reasoning. |
| 7. Industry-pragmatic, not lax | **Held.** Triangulation accepted as appropriateness reinforcement (§§ 3B and 3C "with-qualification" verdicts). Single-anchor cross-domain transfers were scrutinized harder. |
| 8. No early termination on CRITICAL | **N/A** — no CRITICAL findings. |

---

## 6. Limitations of this run

1. **Single-pass single-reviewer.** Same reviewer (Claude Code Opus 4.7) as Phase 2. Same independence-reduction risk.
2. **Compact verdicts in § 3A.** 27 citations whose source-domain matches the framework's claim-domain at the canonical-use level were batched in a single sub-section with one explanatory paragraph instead of per-citation Phase 3 tables. This is consistent with the IVP spec's "industry-pragmatic" framing but a stricter pass would write a per-citation row even for obvious matches.
3. **Phase 3 sub-check 3 (Generalization burden)** measured in qualitative "steps" rather than a formal metric; consistency between rows is best-effort.
4. **Disconfirming search abbreviated.** For each STRETCHED verdict (F-25, F-26, F-27), the disconfirming check was the framework's *own surrounding text* (does it acknowledge the in-domain counter? does it triangulate?) plus quick recall of well-known counter-examples. A stricter pass would search for additional in-domain counter-sources.
5. **Phase 3 evaluates against current (post-remediation) framework text.** Citations that were CONTRADICTED in Phase 2 but remediated before this Phase 3 run are evaluated under their new attributions (e.g., R-061 spike → XP, not RUP). This is methodologically defensible but means the Phase 3 verdict-set is not a clean follow-on of the rodage Phase 2 verdict-set.
6. **AI-agent reviewer.** Same web-search-effectiveness bound as prior runs; some sources behind paywalls or in non-English literature were not opened.

---

## 7. Audit trail (analysis basis)

Phase 3 is internal-text analysis; no new web queries beyond those in Phase 2 were strictly required. The four explicit appropriateness-relevant lookups for this run were:

- **F-25 (Catholic Church Schism check):** confirmed via prior knowledge that the East-West Schism (1054) and Reformation (1517) are widely-documented schisms; both are textbook material. Did not run a fresh WebSearch as the historical fact is uncontested.
- **F-26 (Spotify model departure):** drew on Phase 2 R-011 trail (Atlassian + Agile Pain Relief sources already accessed in rodage 2026-05-08). Confirmed Spotify departure is well-documented in those existing citations.
- **F-27 (Goodhart's Law scope):** drew on Phase 2 audit trail Round 3 (Wikipedia *Goodhart's law*; Splunk; ModelThinkers; Psych Safety) — Goodhart's canonical scope is measure-as-target, not memorability.
- **R-001 policy-1 check:** drew on framework's own self-correction in `framework/debates/001-laws-count-and-multirepo-scaling.md:191–198` (Methodological Note) which explicitly removes prior policy-1 violations.

---

## 8. Erratum (added 2026-05-09 after remediation pass)

During the immediately-following remediation pass on `remediate/ivp-2026-05-09-phase3-findings`, re-reading the current framework text revealed that two of the three new findings above were partially over-stated because the Phase 3 analysis worked from `inventory.md`'s paraphrases rather than the post-remediation framework text. The findings are kept above as originally recorded for audit-trail integrity, with corrections recorded here.

### F-25 reduction: MEDIUM → LOW

The original F-25 stated that the framework's Catholic Church citation "does not surface" the Great Schism (1054) and Reformation (1517). In fact, [`framework/debates/001-laws-count-and-multirepo-scaling.md:69`](../debates/001-laws-count-and-multirepo-scaling.md#L69) **already explicitly acknowledges both** events in its post-F-12-remediation text: "institutional continuity ~2,000 years (despite the Great Schism of 1054 and the Reformation of 1517 producing the Eastern Orthodox and Protestant traditions, the Roman Catholic legal-doctrinal continuity itself is uninterrupted)."

The legitimate residual issue: [`framework/phases/phase-1-for-debate.md:187`](../phases/phase-1-for-debate.md#L187) referenced Catholic Church without the same qualifier. That is a one-line consistency issue, **LOW severity** (not MEDIUM). Remediation pass added a brief cross-reference to debate 001's fuller treatment.

The Phase 3 finding's underlying concern — methodological cherry-pick of the most generous time-window — is technically resolved by the existing acknowledgment, although a stricter reading might still flag the definitional choice ("Roman Catholic specifically" rather than "Christian governance generally"). That deeper question is outside Phase 3's scope (it is a Phase 4 argument-validity question about how the framework defines its category boundaries).

### F-26 needed no action: already satisfied

The original F-26 stated that the Spotify model citation "should acknowledge Spotify's departure from it." In fact, [`framework/debates/001-laws-count-and-multirepo-scaling.md:73`](../debates/001-laws-count-and-multirepo-scaling.md#L73) **already says** "Industry-cited even though Spotify itself has since modified the model — the two-tier pattern persists." This qualifier was present before Phase 3 began. The finding was based on a re-read miss against the inventory's older paraphrase. No remediation needed.

### F-27 stands

F-27 (Goodhart's Law stretched) was correctly identified. The framework text at [`debate 001:35`](../debates/001-laws-count-and-multirepo-scaling.md#L35) was reframed in the remediation pass to invoke Goodhart as analogy and re-anchor the memorability claim on Miller (already correctly cited above after F-01 remediation).

### Methodological lesson for future Phase 3 runs

Phase 3 (and Phase 5) should evaluate citations against the **current framework text**, not against `inventory.md`'s paraphrases. The inventory captures Phase-1-state at audit time and may lag behind remediation. A pre-Phase-3 step of "refresh inventory paraphrases against current text" would prevent this kind of over-statement. Considered for v0.3 of the IVP spec.

### Updated aggregate (post-erratum)

| Category | Original Phase 3 | After erratum |
|---|---|---|
| `STRETCHED` verdicts | 3 | 2 effective (F-26 had no actionable issue) |
| Findings — MEDIUM | 1 (F-25) | 0 |
| Findings — LOW | 2 (F-26, F-27) | 2 (F-25-reduced, F-27); F-26 retracted |

**Combined cross-phase totals revised:** 0 CRITICAL · 6 HIGH · 6 MEDIUM · 14 LOW · 1 retracted (F-26) = 26 findings of practical effect, all remediated.

---

End of report.

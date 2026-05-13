---
title: "Calibration Standards — Reference Catalog"
status: sealed
version: not versioned
audience: both
type: reference
last_updated: 2026-05-09
supersedes: null
sealed_by: debate-003
---

# Calibration Standards — Reference Catalog

> **Status:** Working reference. Not yet adopted by any phase document. Adoption decisions for specific standards are tracked in [debates/](debates/).
>
> **Principle (framework-wide policy):** Dead Light Framework **adopts industry-standard formulas. It does not invent new ones.** When a Phase or process needs a numeric anchor, the framework points to an established, citable standard. The PM and Council retain the authority to *select, calibrate, or override* the standard for their project — but the starting point is always documented external practice, not framework-internal arithmetic.

This catalog exists so that framework calibration questions (significance thresholds, time budgets, team sizes, audit scopes, failure measurement) can be anchored to real industry standards rather than to PM gut feel or framework-invented heuristics.

---

## A. Decision significance and change impact

For Phase 0 Q1 (Past Decisions Catalog significance threshold) and Phase 1 Reckoning step (classification of past decisions).

| Standard | Source | Formula / mechanism | Application |
|---|---|---|---|
| **ITIL Change Management — change tiers** | AXELOS, ITIL 4 (2019). PeopleCert/AXELOS launched ITIL 5 Foundation in February 2026; ITIL 4 modules sunset 31 December 2027. Either edition is valid for this row's purpose; ITIL 4 is the longer-tenured anchor. | Categorical: Standard / Normal / Emergency. ITIL Priority within each type is derived from an Impact × Urgency matrix. | Adapt the impact-urgency matrix to architectural decisions: e.g., Standard = within-service, Normal = cross-service, Emergency = cross-platform. |
| **ISA 320 materiality (judgement framework)** | IAASB, *ISA 320: Materiality in Planning and Performing an Audit* (current edition). Note: ISA 320 itself prescribes **professional judgement**, not fixed percentages. | ISA 320 §A8 illustrative examples: **5% of profit before tax** (profit-oriented manufacturing entity), **1% of total revenue or expenses** (not-for-profit entity). Practitioner methodology heuristics commonly cited in firm guidance and the CEAOB 2022 materiality survey: **3–10% of PBT**, or **0.5–2% of revenue**. | For software: adapt the *judgement discipline* (pick a base meaningful to the project, apply a defensible percentage, document rationale) — e.g., 5–10% of project budget or effort if budget/effort is the meaningful base, or 0.5–2% of a revenue-equivalent metric. The standard supplies the framework for choosing; the percentage is a practitioner convention, not an ISA 320 mandate. |
| **PMBOK Earned Value Management variance thresholds** | PMI, *PMBOK Guide* (8th edition, 2025; previously 7th edition, 2021). EVM concepts and indices are edition-stable across recent editions. | Schedule Variance (SV), Cost Variance (CV), Schedule Performance Index (SPI), Cost Performance Index (CPI). PMBOK defines the indices but does not prescribe specific trigger values. Common practitioner conventions (vendor and consultancy guidance): yellow alert at SPI/CPI 0.8–0.9 or 1.1–1.2; red alert <0.8 or >1.2. The "<0.9 or >1.1" band is widely used but is firm-methodology, not PMBOK-mandated. | Adapt: a decision that produced > 10% schedule or cost variance is significant by definition (the team's chosen threshold is a calibration question — set it explicitly). |
| **CMMI Causal Analysis & Resolution (CAR)** | CMMI Institute (ISACA), *CMMI Development V3.0* (2023; successor to v2.0 released 2018, retired June 2024) | Historical baseline of decision rate per project size (KLOC, function points, story points) | `expected_decisions = historical_rate × project_size × adjustment`. Backward-tune significance threshold to filter to roughly that count. |
| **Incident severity tiers (Sev1–Sev4)** | Industry SRE / incident-management practice (Etsy, Google SRE, Atlassian, runframe). ITIL 4 itself uses **Priority** (often P1–P4) derived from an Impact × Urgency matrix; the "Sev1–Sev4" labels are SRE-vernacular, not ITIL-prescribed terminology. | Sev1 / Sev2 / Sev3 / Sev4 by % users affected + revenue impact + downtime duration. | Adapt for "decision blast radius": Sev1 = whole platform, Sev2 = a service, Sev3 = a module, Sev4 = a file. (For ITIL Priority via Impact × Urgency, see the change-tier row above.) |

---

## B. Time and effort estimation

For Phase 0 Q3 (time budget) and any phase needing effort scoping.

### COCOMO II

- **Source:** Barry Boehm et al., *Software Cost Estimation with COCOMO II* (Prentice Hall, 2000). Successor to original COCOMO (1981).
- **Core formula (post-architecture model):**

  ```
  Effort (Person-Months) = A × (Size in KSLOC)^E × ∏(EM_i)
  ```

  - `A` ≈ 2.94 (calibration constant)
  - `E = B + 0.01 × Σ SF_j` where `B` ≈ 0.91 and SF_j are five Scale Factors (precedentedness, development flexibility, architecture/risk resolution, team cohesion, process maturity)
  - `EM_i` are 17 Effort Multipliers (product, platform, personnel, project)
  - Typical `E` range: 1.05 – 1.20
- **Application:** For Phase 0 retrofit audit, allocate 5–15% of original COCOMO-derived project effort as the audit budget. For greenfield lightweight Phase 0, use 1–2% of projected effort.

### IFPUG Function Point Analysis

- **Source:** International Function Point Users Group, *Function Point Counting Practices Manual* (current edition).
- **Mechanism:** Counts functional components (External Inputs, External Outputs, External Inquiries, Internal Logical Files, External Interface Files) weighted by complexity.
- **Application:** Better than KLOC for polyglot codebases; convert FP to effort using historical productivity rates (FP per person-month from prior projects).

### Putnam's SLIM

- **Source:** Lawrence H. Putnam & Ware Myers, *Measures for Excellence: Reliable Software on Time, Within Budget* (Prentice Hall / Yourdon Press, October 1991). Putnam developed the underlying SLIM model in 1978 from observations of Army and GE software-staffing profiles.
- **Mechanism:** Rayleigh curve fit to historical organizational data; produces effort, schedule, and defect projections.
- **Application:** For organizations with CMMI L4+ historical baselines.

### M&A IT due-diligence rule of thumb

- **Source:** Big 4 audit firms (Deloitte, PwC, EY, KPMG) — practitioner working heuristic. **Not surfaced in any indexed Big-4 publication and not formally codified as a methodology standard.** Treat as practitioner sanity-check, not as a citable industry rule.
- **Rule:** ~1 person-week per 10–50 KLOC of legacy code, depending on complexity and documentation quality. The wide 5× range reflects how much the heuristic depends on engagement specifics (target system age, documentation completeness, engineer familiarity).
- **Application:** Practical anchor for Phase 0 retrofit audit when COCOMO is overkill. **For load-bearing budget commitments, prefer the COCOMO-derived 5–15% from the COCOMO II row above; this row is for sanity-checking only.**

### DORA metrics for baseline

- **Source:** *Accelerate* (Forsgren, Humble, Kim, 2018); annual *State of DevOps* reports.
- **Four key metrics:** Deployment Frequency, Lead Time for Changes, Mean Time to Recovery, Change Failure Rate.
- **Application:** If the organization tracks DORA, derive Phase 0 budget from Lead Time For Changes of comparable past activities.

---

## C. Team sizing and composition

For Phase 0 Q2 (Reckoning Team) and Phase 1 Council size.

| Standard | Source | Rule / formula | Application |
|---|---|---|---|
| **Brooks's Law / communication overhead** | Fred Brooks, *The Mythical Man-Month* (1975, anniversary 1995) | Communication channels = N(N − 1) / 2 | At N=5: 10 channels. At N=7: 21 channels. Bounds the framework's small-group sizes — Reckoning Team 2–5 (per [phase-0 §2](phase-0-for-debate.md)) and Council 3–7 (per [phase-1 §8.1](phase-1-for-debate.md)) — by capping channel overhead at 21 at the Council upper bound. |
| **Two-pizza team rule** | Jeff Bezos / Amazon, late 1990s (introduced at an Amazon management offsite; never formally codified). Often cited around 2002 because that is when the API mandate memo popularized adjacent ideas. | Empirical: a team is too big if two pizzas can't feed it (~6–10 people) | Aligned with Council 3–7 cap. |
| **Dunbar's number — layered model** | Robin Dunbar, *Grooming, Gossip, and the Evolution of Language* (1996); later refinements | 5 / 15 / 50 / 150 / 500 / 1500 cognitive layers | Reckoning Team (2–5) sits squarely at Dunbar layer 1 (≤5, intimate group). Council (3–7) extends slightly beyond layer 1 to accommodate the functional-diversity rule; Brooks's N(N−1)/2 explains why the framework does not push Council size further into layer-2 territory. |
| **Team Topologies** | Matthew Skelton & Manuel Pais, *Team Topologies* (IT Revolution, 2019) | Four team types: stream-aligned, platform, enabling, complicated-subsystem | Reckoning Team behaves as an *enabling team* (deep dive then disband); Council behaves as a *governance pattern* across teams. |

---

## D. Code-based metrics (audit scope)

For scoping Phase 0 inventory work.

| Metric | Source / formula | Use in Phase 0 |
|---|---|---|
| **SLOC / LOC / KLOC** | Source Lines of Code; counted via tools like cloc, scc | Baseline size for scoping the Reckoning Team's coverage budget. |
| **McCabe Cyclomatic Complexity** | Thomas McCabe (1976). `M = E − N + 2P` (edges, nodes, connected components) | Identifies "hotspot" functions that warrant deeper audit. Threshold conventions: < 10 = simple, 10–20 = moderate, > 20 = complex, > 50 = untestable. |
| **Halstead metrics** | Maurice Halstead, *Elements of Software Science* (1977) | Effort, Volume, Difficulty derived from unique operators/operands. Useful for comparing modules of similar function. |
| **Maintainability Index (MI)** | Oman & Hagemeister (1992) ICSM original; refined by Coleman, Ash, Lowther, Oman (*IEEE Computer*, 1994). Built into Visual Studio (normalized 0–100 scale), Radon, and other static-analysis tools. | `MI = 171 − 5.2·ln(HV) − 0.23·CC − 16.2·ln(SLOC)` (original, unnormalized; range roughly 0–171, sometimes negative). Visual Studio normalizes to 0–100 via `MAX(0, MI · 100 / 171)`. | **Threshold depends on which scale.** Original Coleman et al. rule of thumb: <65 hard-to-maintain, <85 moderate (on the unnormalized formula). Visual Studio (0–100 normalized): 0–9 difficult, 10–19 moderate, 20–100 highly maintainable. State which scale is used before quoting a threshold. |
| **Code churn** | Nagappan & Ball (Microsoft Research, 2005) | LOC changed per file per period, normalized | Identifies "active decision areas" — high recent churn signals decisions worth cataloguing. |
| **Bus factor** | Folk software engineering term; formalized in academic literature (Cosentino et al., 2015) | Minimum number of developers whose departure puts the project at risk | Surfaces hidden tenure-spanning members for Reckoning Team composition. |
| **SQALE technical debt index** | Jean-Louis Letouzey, *The SQALE Method for Evaluating Technical Debt* (2012); operationalized in SonarQube | Debt expressed in effort-minutes per rule violation | Direct quantitative input for the Failure Inventory's "accumulated debt" entries. |

---

## E. Failure / incident measurement

For the Phase 0 Failure Inventory.

| Standard | Source | Formula / definition |
|---|---|---|
| **MTBF / MTTR** | General reliability engineering practice (predates and is broader than any single standard). IEEE 1633-2016 *Recommended Practice on Software Reliability* describes software-reliability engineering processes that operate on these metrics; it is not the canonical originator of MTBF/MTTR. | Mean Time Between Failures (MTBF), Mean Time To Recovery / Repair (MTTR). |
| **DORA Change Failure Rate** | *Accelerate* (Forsgren, Humble, Kim, 2018) | % of changes resulting in production incidents |
| **ITIL Incident Severity tiers** | AXELOS, ITIL 4 | Sev1 / Sev2 / Sev3 / Sev4 by impact + urgency |
| **Postmortem severity (Etsy / Google SRE)** | Beyer et al., *Site Reliability Engineering* (O'Reilly, 2016) | S0 / S1 / S2 / S3 by user impact and revenue impact |
| **Six Sigma DPMO** | Bill Smith and Mikel Harry, Motorola (Smith introduced Six Sigma in 1986; Harry developed the MAIC methodology and 1.5σ shift); ASQ standards | Defects Per Million Opportunities; six sigma = 3.4 DPMO |

---

## F. CMMI quantitative process management

For organizations operating at CMMI L4 (Quantitatively Managed) or L5 (Optimizing).

| CMMI practice | Source | Mechanism |
|---|---|---|
| **Process Performance Baselines (PPB)** | CMMI Institute (ISACA), *CMMI Development V3.0* (2023; successor to v2.0 released 2018, retired June 2024) | Historical mean and variance of process metrics, established as the baseline for new projects |
| **Quantitative Project Management (QPM)** | CMMI V3.0 high-maturity Practice Area (in v3.0, capability levels 4 and 5 are eliminated; high-maturity practices apply across CL 1–3) | Setting and managing project quantitative objectives derived from PPB |
| **Statistical Process Control (SPC)** | Walter Shewhart (1931); industrial application standard | Control charts (X̄, R, p, c) to detect out-of-control variation |
| **Causal Analysis & Resolution (CAR)** | CMMI V3.0 high-maturity Practice Area (in v3.0, capability levels 4 and 5 are eliminated; high-maturity practices apply across CL 1–3) | Identify root causes of defects and other problems for systemic resolution |

When applicable, all Phase 0 calibration questions become PPB lookups rather than PM judgment.

---

## How adoption works in Dead Light Framework

This catalog is **reference, not law**. Specific adoption decisions are made in debates and may take three forms:

1. **Direct citation** — a phase doc points to a specific standard as the recommended starting heuristic (e.g., "PM may use ISA 320 materiality").
2. **Layered guidance** — the framework offers multiple standards by rigor level (startup might use M&A rule of thumb; CMMI L4 shop uses PPB).
3. **No adoption** — the standard is documented here for completeness but not referenced from phase docs.

The current adoption status is tracked per phase in each phase's `*-for-debate.md`. Phase 0 calibration questions have been anchored to specific standards from this catalog via [debate 003](debates/003-phase-0-calibration.md); see [pm-calibration-guide.md](pm-calibration-guide.md) for the practical walk-through.

---

## References (further reading)

- Boehm, B. et al. *Software Cost Estimation with COCOMO II.* Prentice Hall, 2000.
- Brooks, F. *The Mythical Man-Month.* Addison-Wesley, anniversary edition 1995.
- Beyer, B. et al. (eds). *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly, 2016.
- Coleman, D. et al. "Using metrics to evaluate software system maintainability." *IEEE Computer*, 1994.
- Cosentino, V. et al. "Assessing the bus factor of Git repositories." *SANER*, 2015.
- Dunbar, R. *Grooming, Gossip, and the Evolution of Language.* Harvard University Press, 1996.
- Forsgren, N., Humble, J., Kim, G. *Accelerate: The Science of Lean Software and DevOps.* IT Revolution, 2018.
- Halstead, M. *Elements of Software Science.* Elsevier, 1977.
- IFPUG. *Function Point Counting Practices Manual.* Latest edition.
- Letouzey, J-L. *The SQALE Method for Evaluating Technical Debt.* 2012.
- McCabe, T. "A Complexity Measure." *IEEE Transactions on Software Engineering*, 1976.
- Nagappan, N., Ball, T. "Use of Relative Code Churn Measures to Predict System Defect Density." *ICSE*, 2005.
- PMI. *PMBOK Guide.* Latest edition.
- Putnam, L. *Measures for Excellence.* Yourdon Press, 1992.
- CMMI Institute (ISACA). *CMMI Development V3.0.* 2023. (Successor to v2.0, released 2018; v2.x retired June 2024.)
- Skelton, M., Pais, M. *Team Topologies.* IT Revolution, 2019.
- AXELOS / PeopleCert. *ITIL 4 Foundation.* 2019. (ITIL 5 Foundation launched February 2026; ITIL 4 sunset 31 December 2027.)
- IAASB. *International Standard on Auditing 320: Materiality in Planning and Performing an Audit.*

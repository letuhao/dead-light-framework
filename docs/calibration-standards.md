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
| **ITIL Change Management — change tiers** | AXELOS, ITIL 4 (2019) | Categorical: Standard / Normal / Emergency, by impact × urgency matrix | Adapt the impact-urgency matrix to architectural decisions: e.g., Standard = within-service, Normal = cross-service, Emergency = cross-platform. |
| **ISA 320 / GAAP / IFRS materiality** | International Standards on Auditing 320 (IAASB); Generally Accepted Accounting Principles | Quantitative: typically 5–10% of relevant base (revenue, assets, expenses) | For software: 5–10% of project budget, KLOC, or effort. A decision affecting more than this base is "material". |
| **PMBOK Earned Value Management variance thresholds** | PMI, *PMBOK Guide* (current edition) | Schedule Variance (SV), Cost Variance (CV), Schedule Performance Index (SPI), Cost Performance Index (CPI). Typical thresholds: SPI/CPI < 0.9 or > 1.1 triggers review. | Adapt: a decision that produced > 10% schedule or cost variance is significant by definition. |
| **CMMI Causal Analysis & Resolution (CAR)** | SEI, CMMI for Development v2.0 (2018) | Historical baseline of decision rate per project size (KLOC, function points, story points) | `expected_decisions = historical_rate × project_size × adjustment`. Backward-tune significance threshold to filter to roughly that count. |
| **ITIL Incident Severity tiers** | AXELOS, ITIL 4 | Sev1 / Sev2 / Sev3 / Sev4 by % users affected + $ revenue impact + downtime duration | Adapt for "decision blast radius": Sev1 = whole platform, Sev2 = a service, Sev3 = a module, Sev4 = a file. |

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

- **Source:** Lawrence Putnam, *Measures for Excellence* (Yourdon Press, 1992).
- **Mechanism:** Rayleigh curve fit to historical organizational data; produces effort, schedule, and defect projections.
- **Application:** For organizations with CMMI L4+ historical baselines.

### M&A IT due-diligence rule of thumb

- **Source:** Big 4 audit firms (Deloitte, PwC, EY, KPMG) — practice standards, not formal specification.
- **Rule:** 1 person-week per 10–50 KLOC of legacy code, depending on complexity and documentation quality.
- **Application:** Practical anchor for Phase 0 retrofit audit when COCOMO is overkill.

### DORA metrics for baseline

- **Source:** *Accelerate* (Forsgren, Humble, Kim, 2018); annual *State of DevOps* reports.
- **Four key metrics:** Deployment Frequency, Lead Time for Changes, Mean Time to Recovery, Change Failure Rate.
- **Application:** If the organization tracks DORA, derive Phase 0 budget from Lead Time For Changes of comparable past activities.

---

## C. Team sizing and composition

For Phase 0 Q2 (Reckoning Team) and Phase 1 Council size.

| Standard | Source | Rule / formula | Application |
|---|---|---|---|
| **Brooks's Law / communication overhead** | Fred Brooks, *The Mythical Man-Month* (1975, anniversary 1995) | Communication channels = N(N − 1) / 2 | At N=5: 10 channels. At N=7: 21 channels. Justifies cap of 5–7 for Reckoning Team and Council. |
| **Two-pizza team rule** | Jeff Bezos / Amazon, ~2002 (informal) | Empirical: a team is too big if two pizzas can't feed it (~6–10 people) | Aligned with Council 3–7 cap. |
| **Dunbar's number — layered model** | Robin Dunbar, *Grooming, Gossip, and the Evolution of Language* (1996); later refinements | 5 / 15 / 50 / 150 / 500 / 1500 cognitive layers | Reckoning Team and Council both sit at layer 1 (≤5) for tight decision groups. |
| **Team Topologies** | Matthew Skelton & Manuel Pais, *Team Topologies* (IT Revolution, 2019) | Four team types: stream-aligned, platform, enabling, complicated-subsystem | Reckoning Team behaves as an *enabling team* (deep dive then disband); Council behaves as a *governance pattern* across teams. |

---

## D. Code-based metrics (audit scope)

For scoping Phase 0 inventory work.

| Metric | Source / formula | Use in Phase 0 |
|---|---|---|
| **SLOC / LOC / KLOC** | Source Lines of Code; counted via tools like cloc, scc | Baseline size for scoping the Reckoning Team's coverage budget. |
| **McCabe Cyclomatic Complexity** | Thomas McCabe (1976). `M = E − N + 2P` (edges, nodes, connected components) | Identifies "hotspot" functions that warrant deeper audit. Threshold conventions: < 10 = simple, 10–20 = moderate, > 20 = complex, > 50 = untestable. |
| **Halstead metrics** | Maurice Halstead, *Elements of Software Science* (1977) | Effort, Volume, Difficulty derived from unique operators/operands. Useful for comparing modules of similar function. |
| **Maintainability Index (MI)** | Coleman et al. (1994); built into Visual Studio, Radon | `MI = 171 − 5.2·ln(HV) − 0.23·CC − 16.2·ln(SLOC)`; sometimes scaled to 0–100 | Composite difficulty signal. < 65 typically flagged as hard-to-maintain. |
| **Code churn** | Nagappan & Ball (Microsoft Research, 2005) | LOC changed per file per period, normalized | Identifies "active decision areas" — high recent churn signals decisions worth cataloguing. |
| **Bus factor** | Folk software engineering term; formalized in academic literature (Cosentino et al., 2015) | Minimum number of developers whose departure puts the project at risk | Surfaces hidden tenure-spanning members for Reckoning Team composition. |
| **SQALE technical debt index** | Jean-Louis Letouzey, *The SQALE Method for Evaluating Technical Debt* (2012); operationalized in SonarQube | Debt expressed in effort-minutes per rule violation | Direct quantitative input for the Failure Inventory's "accumulated debt" entries. |

---

## E. Failure / incident measurement

For the Phase 0 Failure Inventory.

| Standard | Source | Formula / definition |
|---|---|---|
| **MTBF / MTTR** | Reliability engineering, IEEE Standard 1633-2016 | Mean Time Between Failures, Mean Time To Recovery |
| **DORA Change Failure Rate** | *Accelerate* (Forsgren, Humble, Kim, 2018) | % of changes resulting in production incidents |
| **ITIL Incident Severity tiers** | AXELOS, ITIL 4 | Sev1 / Sev2 / Sev3 / Sev4 by impact + urgency |
| **Postmortem severity (Etsy / Google SRE)** | Beyer et al., *Site Reliability Engineering* (O'Reilly, 2016) | S0 / S1 / S2 / S3 by user impact and revenue impact |
| **Six Sigma DPMO** | Mikel Harry (Motorola, 1980s); ASQ standards | Defects Per Million Opportunities; six sigma = 3.4 DPMO |

---

## F. CMMI quantitative process management

For organizations operating at CMMI L4 (Quantitatively Managed) or L5 (Optimizing).

| CMMI practice | Source | Mechanism |
|---|---|---|
| **Process Performance Baselines (PPB)** | SEI, CMMI for Development v2.0 (2018) | Historical mean and variance of process metrics, established as the baseline for new projects |
| **Quantitative Project Management (QPM)** | CMMI v2.0 process area | Setting and managing project quantitative objectives derived from PPB |
| **Statistical Process Control (SPC)** | Walter Shewhart (1931); industrial application standard | Control charts (X̄, R, p, c) to detect out-of-control variation |
| **Causal Analysis & Resolution (CAR)** | CMMI v2.0 process area | Identify root causes of defects and other problems for systemic resolution |

When applicable, all Phase 0 calibration questions become PPB lookups rather than PM judgment.

---

## How adoption works in Dead Light Framework

This catalog is **reference, not law**. Specific adoption decisions are made in debates and may take three forms:

1. **Direct citation** — a phase doc points to a specific standard as the recommended starting heuristic (e.g., "PM may use ISA 320 materiality").
2. **Layered guidance** — the framework offers multiple standards by rigor level (startup might use M&A rule of thumb; CMMI L4 shop uses PPB).
3. **No adoption** — the standard is documented here for completeness but not referenced from phase docs.

The current adoption status is tracked per phase in each phase's `*-for-debate.md`. As of this writing, no Phase 0 calibration question has been formally anchored to a specific standard from this catalog — that is the work of the next debate iteration on [debate 003](debates/003-phase-0-calibration.md).

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
- SEI. *CMMI for Development v2.0.* 2018.
- Skelton, M., Pais, M. *Team Topologies.* IT Revolution, 2019.
- AXELOS. *ITIL 4 Foundation.* 2019.
- IAASB. *International Standard on Auditing 320: Materiality in Planning and Performing an Audit.*

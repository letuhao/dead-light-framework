# IVP — Inventory (Phase 1 output)

> **Run date:** 2026-05-08 · **Scope:** all `docs/**/*.md`, `README.md`, `HANDOFF.md`. **Excluded:** `docs/audit/independent-verification-pass-for-debate.md` (the IVP methodology itself — self-referential audit deferred to a separate pass), `chat.txt`, `LICENSE`. **Mode:** industry-pragmatic. **Auditor:** Claude Code (Opus 4.7).
>
> This file is *extraction only*. Verdicts live in `findings-2026-05-08.md` from Phase 2 onward.

---

## A. Claims (load-bearing assertive propositions)

Coding: `descriptive` (about the world), `normative` (about how the framework should behave), `causal` (claims a cause-effect link), `definitional` (defines a framework term). `LB = Y` flags a claim that, if removed or refuted, would change a sealed decision or a phase's design.

| C-id | File:line | Claim (concise) | Type | LB |
|---|---|---|---|---|
| C-001 | README.md:11–24 | Existing methodologies (Waterfall through SAFe/RUP) assume stable decision-makers, shared memory, real-time correction; AI agents break those assumptions. | causal | Y |
| C-002 | README.md:30–34 | A frozen source of authority that no participant can rewrite at will is the missing element. | normative | Y |
| C-003 | README.md:36 | The Astronomican metaphor names "authority detached from any living agent" — something traditional methodologies do not address. | descriptive | Y |
| C-004 | calibration-standards.md:5; phase-0-for-debate.md:30; debate 003:128 | Dead Light adopts industry-standard formulas; it does not invent new ones. | normative (policy 2) | Y |
| C-005 | debate 001:191–198 | 40k vocabulary is naming and shared metaphor only; justification rests on real-world systems. | normative (policy 1) | Y |
| C-006 | phase-1-for-debate.md:43–44 | Maximum five Immutable Laws and five Guiding Principles. | normative | Y |
| C-007 | debate 001:32 | The "≤ 5" cap is grounded in cognitive load (Miller's working-memory range, ~5 ± 2). | causal | Y |
| C-008 | phase-1-for-debate.md:46, 76 | Stress-test divergence between Council members must be < 20%. | normative | Y |
| C-009 | phase-1-for-debate.md:128 | Council size is 3–7. | normative | Y |
| C-010 | phase-1-for-debate.md:126 | Valid Council must include at least three distinct functional perspectives. | normative | Y |
| C-011 | phase-0-for-debate.md:23–27 | Reckoning Team is 2–5 people with a composition rule (≥1 active-IC mandatory; ≥1 tenure-spanning when permits; ≥1 outside-scope when permits). | normative | Y |
| C-012 | phase-0-for-debate.md:30; phase-1-for-debate.md:120 | PM is a member of the Ascension Council. | normative | Y |
| C-013 | phase-1-for-debate.md:148 | The Ascension Council disbands after sealing; future change requires convening a new Council. | normative | Y |
| C-014 | phase-1-for-debate.md:158–164 | A project should adopt Sector Astronomicans only when ≥2 repos + dedicated team + cross-team contracts + genuinely local decisions are all true. | normative | Y |
| C-015 | phase-1-for-debate.md:175–179 | Sectors inherit and add — never relax: a Sector Law cannot be softer than the Imperial Law it descends from. | normative | Y |
| C-016 | phase-1-for-debate.md:183 | Imperial Phase 1 must complete before any Sector Phase 1 begins. | normative | Y |
| C-017 | phase-0-for-debate.md:7; phase-1-for-debate.md:194–198 | Phase 0 is mandatory for retrofit projects; greenfield runs lightweight or skips. | normative | Y |
| C-018 | phase-1-for-debate.md:215–222 | Reckoning step classifies past decisions into Keep / Fix-now / Fix-by-date / Reconsider-Law. | normative | Y |
| C-019 | calibration-standards.md:18 | ISA 320 / GAAP / IFRS materiality is typically 5–10% of relevant base; framework adapts to 5–10% of project budget / KLOC / effort. | descriptive (citation) + normative (adaptation) | Y |
| C-020 | calibration-standards.md:19 | PMBOK EVM SPI/CPI thresholds are typically <0.9 or >1.1 to trigger review; >10% schedule or cost variance is significant by definition. | descriptive (citation) | Y |
| C-021 | calibration-standards.md:42 | Phase 0 retrofit audit budget = 5–15% of original COCOMO-derived effort; greenfield lightweight = 1–2%. | normative | Y |
| C-022 | calibration-standards.md:59 | M&A IT due-diligence rule of thumb: 1 person-week per 10–50 KLOC. | descriptive (citation) | Y |
| C-023 | calibration-standards.md:76 | Brooks's communication channels = N(N−1)/2; at N=5 → 10 channels, at N=7 → 21. | descriptive (formula) | Y |
| C-024 | calibration-standards.md:78 | Dunbar's layered model: 5 / 15 / 50 / 150 / 500 / 1500. | descriptive (citation) | Y |
| C-025 | calibration-standards.md:90 | McCabe Cyclomatic Complexity M = E − N + 2P; thresholds <10 simple / 10–20 moderate / >20 complex / >50 untestable. | descriptive (formula + thresholds) | Y |
| C-026 | calibration-standards.md:92 | Maintainability Index = 171 − 5.2·ln(HV) − 0.23·CC − 16.2·ln(SLOC); <65 hard-to-maintain. | descriptive (formula) | Y |
| C-027 | calibration-standards.md:38–41 | COCOMO II constants A ≈ 2.94, B ≈ 0.91; E in [1.05, 1.20]; 17 effort multipliers; 5 scale factors. | descriptive (formula) | Y |
| C-028 | calibration-standards.md:65 | DORA four key metrics: Deployment Frequency, Lead Time for Changes, MTTR, Change Failure Rate. | descriptive (citation) | Y |
| C-029 | calibration-standards.md:109 | Six Sigma = 3.4 DPMO. | descriptive (citation) | N |
| C-030 | debate 001:36 | AWS Leadership Principles has 16 items and is criticized inside Amazon for being too many to internalize. | descriptive (citation) | Y |
| C-031 | debate 001:49–53 | Articles of Confederation (1781–1789) shows the failure mode of flat federation; Holy Roman Empire and Yugoslavia are the same pattern. | descriptive (historical) | Y |
| C-032 | debate 001:67–73 | US federalism stable since 1789; German Basic Law since 1949; Catholic canon ~1.3B / 200+ countries / ~2,000 years; Linux kernel 30+ years / 10,000+ contributors / no schism; Toyota TPS 70+ years. | descriptive (historical track records) | Y |
| C-033 | debate 002:50 | Apple under Jobs (1997) killed ~70% of product lines as a reckoning move. | descriptive (historical) | Y |
| C-034 | debate 002:54 | Big-bang rewrites correlate strongly with project death (Joel Spolsky 2000). | causal (cited) | Y |
| C-035 | phase-0-for-debate.md:177–183 | Borrowed-vs-novel attributions: blameless postmortem (Allspaw 2012), software archaeology (Spinellis), legacy code (Feathers), organizational ethnography (Schein), Delphi, Linux/Apache governance, RUP spike, PMBOK/PRINCE2, Lean Startup, IETF/W3C. | descriptive (multiple citations) | Y |
| C-036 | phase-1-for-debate.md:282–293 | Borrowed-vs-novel attributions: Agile Inception Deck, RUP LOM, PRINCE2 PID, PRINCE2 Change Control, PMBOK; constitutional federalism, Catholic canon, Linux kernel, TPS; constitutional retrofit (Japan/Spain/SA), Microsoft/Apple corp transformation, Toyota Ohno-circle, Linux CoC effective date, Strangler Fig. | descriptive (multiple citations) | Y |
| C-037 | debate 003:24 | Audit standards (ISA, GAAP) define materiality with both quantitative and qualitative anchors; pattern across ISA/PMBOK/PRINCE2/SRE postmortem-tier is "categorical anchor + numeric flexibility". | descriptive | Y |
| C-038 | debate 003:48 | NTSB aviation incident investigations require multi-disciplinary investigators; medical M&M conferences prescribe attending + resident; common pattern is uniform teams produce one-sided findings. | descriptive | Y |
| C-039 | debate 003:68 | Agile timeboxing uses hard time and treats scope as the variable; Toyota kaizen events typically 5 days hard-time; PMBOK tracks variance and escalates. | descriptive | Y |
| C-040 | phase-1-for-debate.md:130 | Corporate boards prescribe role diversity (independent + executive + functional specialists); IETF working groups balance vendor + operator + academic; Federal Reserve Board balances geographic + economic. | descriptive | Y |
| C-041 | debate 001:165 | Late Roman reforms (Praetorian Prefectures → Dioceses → Provinces) had decreasing central control at each step; HRE was chronically dysfunctional; Soviet system showed cumulative attenuation. | descriptive (historical) | N |
| C-042 | phase-1-for-debate.md:79 | Phase 1 is not done until at least one agent has been test-run with the Astronomican as system prompt and produced output consistent with the Laws. | normative | Y |
| C-043 | phase-1-for-debate.md:92 | Stress-test divergence > 20% indicates wording is still ambiguous; humans and agents will interpret differently at runtime. | causal (claimed) | Y |
| C-044 | phase-1-for-debate.md:105 | Council too large (>7) is past the Dunbar threshold for small-group decision quality. | causal (citation) | Y |

---

## B. Citations (references to external entities)

Each entity inventoried once; "Locations" lists every site:line where it is invoked. Phase 2 verifies attribute-by-attribute.

| R-id | Cited entity | Locations | Attribute(s) the framework claims | Type |
|---|---|---|---|---|
| R-001 | Warhammer 40,000 (Games Workshop) | README.md:36, 92; glossary throughout | Astronomican as a beacon that survives its god-emperor; Imperium / Chapter / Codex / Heresy / High Lords vocabulary | fictional setting (naming-only per policy 1) |
| R-002 | Articles of Confederation (US, 1781–1789) | debate 001:49 | Failure mode of flat federation; coordination broke within years; Constitutional Convention convened to fix it | historical fact |
| R-003 | Holy Roman Empire (dissolved 1806) | debate 001:50 | Nominal central authority over hundreds of de facto sovereigns; persistent fragmentation | historical fact |
| R-004 | Yugoslavia (post-Tito, 1990s) | debate 001:51 | Federation without credible binding authority above republics; fractured violently in the 1990s | historical fact |
| R-005 | US Constitutional federalism / Supremacy Clause | debate 001:67; phase-1-for-debate.md:187, 292 | Supremacy Clause prevents states from contradicting federal law; stable since 1789 (with civil war as known stress event) | historical / legal |
| R-006 | German Basic Law (Grundgesetz) | debate 001:68 | Cooperative federalism; Länder constitutions; concurrent powers explicitly enumerated; stable since 1949 | historical / legal |
| R-007 | Catholic Canon Law + diocesan customs | debate 001:69; phase-1-for-debate.md:187 | ~1.3 billion members, 200+ countries, doctrinal coherence ~2,000 years | historical / institutional |
| R-008 | Linux kernel governance | debate 001:70; phase-1-for-debate.md:187, 292; phase-0-for-debate.md:179 | Whole-tree standards + per-subsystem maintainer rules; 30+ years; 10,000+ contributors; no schism | historical / OSS |
| R-009 | Toyota Production System (TPS) | debate 001:71; phase-1-for-debate.md:187, 293 | Corporate immutable + plant-level kaizen; 70+ years across global manufacturing | corporate / mfg |
| R-010 | AWS Leadership Principles + team Tenets | debate 001:36, 72; phase-1-for-debate.md:187 | "16 items"; criticized inside Amazon for being too many to internalize; team Tenets must not contradict Principles | corporate practice |
| R-011 | Spotify model — Tribe + Squad missions | debate 001:73 | Two-tier mission structure; Spotify itself has since modified, but pattern persists | industry pattern |
| R-012 | Late Roman Empire reforms | debate 001:165 | Praetorian Prefectures → Dioceses → Provinces; decreasing central control at each step | historical |
| R-013 | Soviet hierarchy | debate 001:165 | Union → Republics → ASSRs → Oblasts → Raions; cumulative attenuation contributed to coordination failure | historical |
| R-014 | Miller "magical number 7±2" / working memory | debate 001:32 | "Miller's working-memory range, ~5 ± 2" | psychology |
| R-015 | Goodhart's Law | debate 001:35 | "Optimizing for 'comprehensive' destroys 'recallable'" | named principle |
| R-016 | Japan post-WWII Constitution (1947) | debate 002:49; phase-1-for-debate.md:293 | Retrofit constitution example | historical / legal |
| R-017 | Spain post-Franco (1978) | debate 002:49; phase-1-for-debate.md:293 | Retrofit constitution example | historical / legal |
| R-018 | South Africa TRC (1996) | debate 002:49; phase-1-for-debate.md:293 | Strongest example of explicit mechanism for past violations under retrofit constitution | historical / legal |
| R-019 | Microsoft under Nadella (post-2014) | debate 002:50; phase-1-for-debate.md:293 | Explicit shift from "know-it-all" to "learn-it-all" culture | corporate |
| R-020 | Apple under Jobs (1997) | debate 002:50; phase-1-for-debate.md:293 | Killed ~70% of product lines on return | corporate / historical |
| R-021 | Toyota's Ohno-circle exercise | debate 002:51; phase-1-for-debate.md:293 | Identify ONE concrete deviation as the starting wedge; fix visibly; expand | mfg practice |
| R-022 | Linux kernel CoC adoption (2018) | debate 002:52; phase-1-for-debate.md:293 | Effective-date with grandfathering of prior code/community behavior | OSS practice |
| R-023 | Rust Foundation creation (2021) | debate 002:52 | Effective-date pattern | OSS practice |
| R-024 | Docker → Moby split | debate 002:52 | Effective-date pattern | OSS practice |
| R-025 | Strangler Fig pattern (Martin Fowler, 2004) | debate 002:54; phase-1-for-debate.md:293 | Retrofit works as gradient; new wraps old, gradually replaces | software pattern |
| R-026 | Joel Spolsky "Big-Bang Rewrite" essay (2000) | debate 002:54 | Big-bang rewrites correlate strongly with project death | grey literature |
| R-027 | ITIL 4 (AXELOS, 2019) | calibration-standards.md:17, 21; pm-calibration-guide.md throughout; debate 003:24 | Change Management tiers (Standard/Normal/Emergency, by impact × urgency); Incident Severity tiers Sev1/Sev2/Sev3/Sev4 | standard (T1) |
| R-028 | ISA 320 (IAASB) | calibration-standards.md:18, 159; debate 003:24 | "Quantitative: typically 5–10% of relevant base (revenue, assets, expenses)" | standard (T1) |
| R-029 | GAAP / IFRS materiality | calibration-standards.md:18 | Same 5–10% norm as ISA 320 | standard (T1) |
| R-030 | PMBOK EVM | calibration-standards.md:19, 154; pm-calibration-guide.md (refs) | SV, CV, SPI, CPI; thresholds SPI/CPI <0.9 or >1.1 trigger review; >10% variance is significant | standard (T1) |
| R-031 | PMBOK (general) | phase-0-for-debate.md:180; phase-1-for-debate.md:286, 293; debate 002:53; debate 003:91 | Project sizing patterns; stakeholder register; tailoring; categorical guidance on tracked changes | standard (T1) |
| R-032 | PRINCE2 | phase-0-for-debate.md:180; phase-1-for-debate.md:284, 285; debate 003:68 | PID approval; Change Control with stricter cost; stages with formal extension process | standard (T1) |
| R-033 | CMMI for Development v2.0 (SEI, 2018) | calibration-standards.md:20, 119, 122, 156 | Causal Analysis & Resolution (CAR); Process Performance Baselines (PPB); Quantitative Project Management (QPM) | standard (T1/T2) |
| R-034 | COCOMO II (Boehm et al., Prentice Hall, 2000) | calibration-standards.md:31–42, 142; pm-calibration-guide.md § 4 | Effort = A × (KSLOC)^E × ∏EM; A ≈ 2.94; E = B + 0.01 × Σ SF, B ≈ 0.91; 17 effort multipliers; 5 scale factors; E typical 1.05–1.20 | standard / textbook (T1/T2) |
| R-035 | COCOMO original (1981) | calibration-standards.md:31 | Successor relationship to COCOMO II | textbook |
| R-036 | IFPUG Function Point Analysis | calibration-standards.md:46, 150 | Five components (EI, EO, EQ, ILF, EIF) weighted by complexity | standard (T1) |
| R-037 | Putnam SLIM, *Measures for Excellence* (Yourdon Press, 1992) | calibration-standards.md:52, 155 | Rayleigh curve fit to historical data; produces effort/schedule/defect | textbook (T2) |
| R-038 | M&A IT due-diligence rule of thumb (Big 4) | calibration-standards.md:58–60; pm-calibration-guide.md § 4 | "1 person-week per 10–50 KLOC" depending on quality | grey literature (T3) |
| R-039 | DORA / *Accelerate* (Forsgren, Humble, Kim, IT Revolution, 2018) | calibration-standards.md:64–66, 106, 148 | Four key metrics (Deployment Frequency, Lead Time for Changes, MTTR, Change Failure Rate); Change Failure Rate definition | T2 |
| R-040 | Brooks's Law / *The Mythical Man-Month* (1975/1995) | calibration-standards.md:76, 143 | Communication channels = N(N − 1)/2 | textbook (T2) |
| R-041 | Two-pizza team (Bezos / Amazon, ~2002) | calibration-standards.md:77 | A team is too big if two pizzas can't feed it (~6–10 people) | grey literature (T3) |
| R-042 | Dunbar's number (Robin Dunbar, 1996) | calibration-standards.md:78, 147; phase-1-for-debate.md:105 | Layered model 5 / 15 / 50 / 150 / 500 / 1500 cognitive layers | textbook (T2) |
| R-043 | Team Topologies (Skelton & Pais, IT Revolution, 2019) | calibration-standards.md:79, 157 | Four team types: stream-aligned, platform, enabling, complicated-subsystem | textbook (T2) |
| R-044 | McCabe Cyclomatic Complexity (1976) | calibration-standards.md:90, 152 | M = E − N + 2P; thresholds <10 simple, 10–20 moderate, >20 complex, >50 untestable | peer-reviewed (T1) |
| R-045 | Halstead, *Elements of Software Science* (1977) | calibration-standards.md:91, 149 | Effort/Volume/Difficulty derived from unique operators/operands | textbook (T2) |
| R-046 | Maintainability Index — Coleman et al. (*IEEE Computer*, 1994) | calibration-standards.md:92, 145 | MI = 171 − 5.2·ln(HV) − 0.23·CC − 16.2·ln(SLOC); <65 hard-to-maintain | peer-reviewed (T1) |
| R-047 | Code churn (Nagappan & Ball, *ICSE*, 2005) | calibration-standards.md:93, 153 | LOC-changed-per-file-per-period predicts defect density | peer-reviewed (T1) |
| R-048 | Bus factor (Cosentino et al., *SANER*, 2015) | calibration-standards.md:94, 146 | Minimum number of developers whose departure puts the project at risk | peer-reviewed (T1) |
| R-049 | SQALE (Letouzey, 2012) | calibration-standards.md:95, 151 | Debt expressed in effort-minutes per rule violation; operationalized in SonarQube | T2 (book + tool) |
| R-050 | MTBF/MTTR — IEEE Standard 1633-2016 | calibration-standards.md:105 | Reliability engineering metrics | standard (T1) |
| R-051 | *Site Reliability Engineering* (Beyer et al., O'Reilly, 2016) | calibration-standards.md:108, 144 | S0/S1/S2/S3 postmortem severity by user/revenue impact | textbook (T2) |
| R-052 | Six Sigma DPMO (Mikel Harry, Motorola, 1980s; ASQ) | calibration-standards.md:109 | Defects Per Million Opportunities; six sigma = 3.4 DPMO | standard (T2) |
| R-053 | Statistical Process Control — Walter Shewhart (1931) | calibration-standards.md:121 | Control charts (X̄, R, p, c) to detect out-of-control variation | foundational text (T2) |
| R-054 | Diomidis Spinellis — software archaeology | phase-0-for-debate.md:177 | Borrowed source for current state audit + decision archaeology | textbook (T2) |
| R-055 | Michael Feathers, *Working Effectively with Legacy Code* | phase-0-for-debate.md:177 | Borrowed source for retrofit / legacy work | textbook (T2) |
| R-056 | John Allspaw, "Blameless PostMortems and a Just Culture" (2012) | phase-0-for-debate.md:178 | Failure inventory framing; full attribution + blameless | grey literature (T3) |
| R-057 | NTSB aviation safety practice | phase-0-for-debate.md:178; debate 003:48 | Multi-disciplinary investigators; root-cause analysis | regulatory (T1/T2) |
| R-058 | Edgar Schein, *Organizational Culture and Leadership* | phase-0-for-debate.md:179 | Espoused vs in-use values | textbook (T2) |
| R-059 | Delphi method | phase-0-for-debate.md:179 | Forecast aggregation via independent expert capture | methodology (T2) |
| R-060 | Linux subsystem maintainers / Apache committers | phase-0-for-debate.md:180 | Open-source maintainer-driven processes | OSS practice (T2/T3) |
| R-061 | RUP "spike" pattern | phase-0-for-debate.md:180 | Investigation work | methodology (T2) |
| R-062 | RUP Lifecycle Objective Milestone (LOM) | phase-1-for-debate.md:284 | Sign-off ceremony source | methodology (T2) |
| R-063 | Lean Startup | phase-0-for-debate.md:181; debate 003:91 | "Scope is the variable" principle; minimal upfront artifacts | grey literature (T3) |
| R-064 | IETF / W3C engineering review pattern | phase-0-for-debate.md:182 | Investigation outputs feed governance bodies but are not themselves governance acts | standards-body practice (T2) |
| R-065 | Agile Inception Deck | phase-1-for-debate.md:283, 284; debate 003:91 | Five pre-work questions / NOT-list / 10 questions | grey literature / book (T2/T3) |
| R-066 | Federal Reserve Board of Governors | phase-1-for-debate.md:130 | Geographic + economic diversity balance | corporate / governmental (T2) |
| R-067 | Etsy / Google SRE postmortem severity | debate 003:24 | S1/S2/S3 anchors | grey literature (T3) |
| R-068 | Architecture review board practice | debate 003:24 | "Affects > 2 services"; "creates a cross-team contract" | grey literature (T3) |
| R-069 | Code review practice | debate 003:48 | Reviewer mix (owner + outside senior) | grey literature (T3) |
| R-070 | Medical M&M (morbidity-and-mortality) conferences | debate 003:48 | Attending + resident, sometimes external review | medical practice (T2) |
| R-071 | Toyota kaizen events | debate 003:68 | Typically 5 days; hard-time and adjust scope | mfg practice (T2/T3) |
| R-072 | Postmortem / blameless pattern (Etsy) | phase-0-for-debate.md:178 | Names kept, blame not assigned | grey literature (T3) |
| R-073 | ADR (Architecture Decision Record) | glossary-for-debate.md:92; debate 002:53 | Existing engineering pattern; mid-project adoption common | grey literature (T3) |
| R-074 | RACI matrix | glossary-for-debate.md:96 | Existing methodology pattern | T3 |
| R-075 | SAFe / Scrum / Kanban / RUP / DevOps | README.md:11, 50; glossary-for-debate.md:11; phase-1-for-debate.md:284, 286 | Existing methodologies that Dead Light composes on top of | T2 |
| R-076 | cloc / scc / lizard / radon / SonarQube tools | calibration-standards.md:89; pm-calibration-guide.md:140–142 | Code-metric tooling | T3 |

**Citation count: 76 distinct entities.**

---

## C. Defined terms

Each row is a term defined or used as if defined within the framework. Phase 5 will check term-drift across files; Phase 4 will check for circular or no-true-Scotsman definitions.

| T-id | Term | First definition (file:line) | Other notable occurrences |
|---|---|---|---|
| T-001 | The Astronomican | README.md:56; glossary:33 | phase-1 throughout; debate 001 throughout |
| T-002 | Immutable Law | glossary:34 | phase-1:43, 88, 218 |
| T-003 | Guiding Principle | glossary:35 | phase-1:44, 220 |
| T-004 | The Purpose | glossary:36; phase-1:42 | phase-1:72, 87 |
| T-005 | The Boundaries | glossary:37; phase-1:45 | phase-1:60, 93 |
| T-006 | The Ascension Council | README.md:57; glossary:43; phase-1:18 | phase-0:144; phase-1:111–148 |
| T-007 | The Sealing | glossary:44; phase-1:47 | phase-1:60 |
| T-008 | Re-consecration | README.md (planned); glossary:45; phase-1:60 | phase-1:179 |
| T-009 | High Lord | README.md:58; glossary:51 | phase-1:145 |
| T-010 | Planetary Governor | README.md:59; glossary:52 | phase-1:147 |
| T-011 | Inquisitor | glossary:53 | (debate flagged: needs-debate) |
| T-012 | Chapter | README.md:60; glossary:59 | phase-0:138; phase-1:107, 132 |
| T-013 | Codex | README.md:60; glossary:60 | phase-0:138; phase-1 throughout |
| T-014 | Operational Bounds | glossary:61 | (only in glossary) |
| T-015 | Hard Stop | glossary:62 | (only in glossary) |
| T-016 | Autonomy Threshold | glossary:63 | (only in glossary) |
| T-017 | Tithe | glossary:64 | (needs-debate) |
| T-018 | Battle Brother | glossary:65 | (needs-debate; probable cut) |
| T-019 | The Chaos | README.md:61; glossary:71 | (umbrella) |
| T-020 | Heresy | glossary:72; README.md:73 | phase-1:71 (Heresy detection) |
| T-021 | Corruption | glossary:73 | (needs-debate; possible redundancy with Heresy) |
| T-022 | Schism | glossary:74 | (needs-debate) |
| T-023 | Heresy Detection | glossary:80; README.md:73 | phase-1:71 |
| T-024 | Astropathic Signal | glossary:81 | (needs-debate; 40k flavor) |
| T-025 | Astronomican Reading | glossary:82 | (needs-debate) |
| T-026 | Reckoning Team | phase-0:23–27 | phase-0 throughout; phase-1:211 |
| T-027 | Reckoning Record | phase-0:78–96 | phase-1:202, 228, 256 |
| T-028 | Imperial Astronomican | phase-1:167; debate 001:78 | phase-1:152–185 |
| T-029 | Sector Astronomican | phase-1:173; debate 001:79 | phase-1:152–185 |
| T-030 | Reckoning step | phase-1:215; debate 002:71 | (in retrofit Phase 1) |
| T-031 | Migration Plan | phase-1:229; debate 002:81 | (retrofit-only output) |
| T-032 | Keep / Fix-now / Fix-by-date / Reconsider-Law | phase-1:218–221; debate 002:73–75 | (classification scheme) |
| T-033 | Aide (AI-assistant Chapter as aide) | phase-0:138; phase-1:132 | (small-team accommodation) |
| T-034 | Significance threshold | phase-0:31; pm-calibration-guide:38 | debate 003 Q1 |
| T-035 | Materiality threshold | phase-0:32; pm-calibration-guide:84 | debate 003 |
| T-036 | Time budget (Phase 0) | phase-0:34; pm-calibration-guide:160 | debate 003 Q3 |
| T-037 | Re-reckoning cadence | phase-0:156; pm-calibration-guide:215 | debate 002 Q6 |
| T-038 | Reckoning Team composition rule | phase-0:23–27; debate 003 Q2 | |
| T-039 | Stress Test Log | phase-1:64 | |
| T-040 | Codex Slot Placeholders | phase-1:65 | |

---

## D. Analogies (40k metaphors)

Per framework policy 1, 40k vocabulary is naming-only. This table flags every 40k invocation and tags whether it stays naming-only or risks becoming substantive justification.

| A-id | File:line | Metaphor | Role |
|---|---|---|---|
| A-001 | README.md:3 | "The Emperor is dead. The light remains." | naming-only / flavor (epigraph) |
| A-002 | README.md:36 | Astronomican = "beacon that still shines after its god-emperor has all but died" | naming-only — explicitly framed as "we use the metaphor because it names something real" |
| A-003 | README.md:56–61 | Astronomican / Ascension Council / High Lords / Planetary Governors / Chapters / Codex / Chaos | naming-only |
| A-004 | README.md:91 | Acknowledgment to Games Workshop | disclaimer |
| A-005 | glossary:64 | "Tithe" = output contract; flagged 40k flavor, alternative "Output Contract" considered | needs-debate (could be policy 1 risk if kept) |
| A-006 | glossary:65 | "Battle Brother" = agent instance; flagged 40k flavor, probable cut | needs-debate |
| A-007 | glossary:81 | "Astropathic Signal" = bottom-up escalation; flagged 40k flavor | needs-debate |
| A-008 | phase-1:167–179 | Imperial / Sector Astronomican | naming-only — debate 001 Methodological Note explicitly removed prior 40k justification |
| A-009 | debate 001:191–198 | Methodological note: 40k formerly cited as evidence (Horus Heresy etc.), now removed | self-correction (anti-policy-1 safeguard) |
| A-010 | phase-0:138 | "AI-assistant Chapters" with "Codex" as aides | naming-only |
| A-011 | (multiple) | Heresy / Inquisitor / Schism / Corruption used in glossary | naming-only with needs-debate flags |

---

## E. Scope note

- `docs/audit/independent-verification-pass-for-debate.md` was authored in the same session as this run and is excluded; auditing the audit methodology against itself in a single pass would compromise independence. Defer to a follow-up pass when (a) more time has elapsed and (b) a different reviewer can run it.
- `chat.txt` excluded per IVP spec section "Scope" (raw history; not a framework artifact).
- `LICENSE` excluded per IVP spec.
- HANDOFF.md is in scope but is a session-state document; its assertive content overlaps the docs it summarizes. Counted but cross-referenced rather than independently audited.

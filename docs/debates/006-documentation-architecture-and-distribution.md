# Debate 006 — Documentation Architecture and Distribution Template

> **Status:** open.
> **Opened:** 2026-05-11
> **Decided:** —
> **Decided by:** project owner (pending)
> **Affects:** Whole framework tree organization. Creates a new root-level distribution folder; introduces explicit conventions for working drafts, debates, audit history, chapters, case studies; defines update + sync mechanism between working and distribution; introduces dual-audience (human + AI) design rules.
> **Raised by:** project owner during LoreWeave case-study kick-off (2026-05-11), after [debate 005](005-first-chapter-pm-high-lord-aide.md) sealed the first Chapter. Observation: now that the framework has *sealed* artifacts (Phase 0/1 + 5 decided debates + Adeptus Administratum Codex), adopters need a clear surface to clone/use; ad-hoc organization is no longer adequate.

---

## 1. Context

The framework has reached a turning point. Until 2026-05-10, it was **inward-facing** — only the project owner + AI-aide read and modified the artifacts. From 2026-05-11 onward (post-Codex seal), the framework is **outward-facing** — adopters can clone the sealed parts into their own projects.

Two operational facts force this debate:

1. **Sealed artifacts exist now.** Phase 0 sealed; Phase 1 partial-but-substantial; 5 debates decided; Adeptus Administratum Codex v1.0 sealed. These are *deliverable* artifacts that adopters need a clean way to pick up.

2. **Document scale is growing fast.** End of session 4: the repo contains ~25 framework files totaling tens of thousands of lines. Some files are approaching 500 lines (debate 005, calibration-standards). The case-study folder is already at 5 files. Without explicit size + organization conventions, the framework becomes its own anti-pattern (cf. AWS Leadership Principles being "too many to internalize").

3. **AI-priming cost grows linearly with framework size.** Adeptus Administratum's Codex §8 re-priming protocol requires reading the Codex + Astronomican + artifact base. With ~25 files and growing, the re-prime cost approaches LLM context-window limits. Lean context + frontmatter for AI re-priming is now an operational necessity, not a nice-to-have.

This debate's scope is **the full documentation architecture** — not just the distribution piece. Working drafts, debates, audit history, chapters, case studies, the distribution surface, and cross-folder conventions all sit within one coherent design.

---

## 2. Pre-decided constraints (project owner committed 2026-05-11)

Before sub-decisions:

| Pre-decision | Decision | Rationale |
|---|---|---|
| **Scope of debate 006** | **Full documentation architecture** — working drafts, debates, audit, chapters, case studies, distribution. | One-time-decision avoids partial designs that conflict later. |
| **Distribution folder location** | **Root of `dead-light-framework` repo, organized to be separable** (copyable as a self-contained unit to a standalone repo later if needed). | Single-repo simplicity now; separation discipline preserves future flexibility. No cross-references that would break if the distribution folder is extracted. |
| **Dual-audience priority** | **Human and AI as co-equal first-class audiences.** | On-thesis with Dead Light's "human + agent collaborate" premise; expresses the thesis at the document layer. Document design serves both. |

These constraints scope the sub-decisions below.

---

## 3. Sub-decision A — Folder topology

### Current state (end of session 4)

```
dead-light-framework/
├── .claude/commands/ivp.md
├── README.md
├── HANDOFF.md
├── LICENSE
├── chat.txt
└── docs/
    ├── glossary-for-debate.md
    ├── phase-0-for-debate.md      ← sealed
    ├── phase-1-for-debate.md      ← partial
    ├── calibration-standards.md
    ├── pm-calibration-guide.md
    ├── audit/                     ← IVP audit history (8 files)
    ├── chapters/                  ← Codex artifacts (1 sealed)
    ├── case-study-lore-weave/     ← retrofit case study (5 files)
    └── debates/                   ← 6 debates (5 decided, 1 open)
```

### Options

| Option | Topology | Pros | Cons |
|---|---|---|---|
| **A1.** Keep current `docs/` flat structure | All current dirs at depth 2 | Minimal disruption; familiar | No clear distribution boundary; everything mixed (working + sealed + audit + chapters + case studies) |
| **A2.** Add `distribution/` at root, leave `docs/` for working | `docs/` = working; `distribution/` = sealed artifacts re-organized as template | Clear boundary; adopters know exactly which folder to clone | Some duplication risk (sealed content lives in two places unless single-source enforced — see sub-decision H) |
| **A3.** Restructure into 4 root folders: `framework/`, `audit/`, `case-studies/`, `distribution/` | Each function owns root-level folder; `docs/` retired | Cleanest semantic separation; matches the framework's logical layers | Large rename churn; breaks all existing in-doc links; risk of stale references |
| **A4.** Hybrid: root folders `framework/` + `distribution/`; case studies + audit + chapters under `framework/` | Two-folder root; nested organization under `framework/` | Balance between A2 and A3; one folder for framework's own concerns + one for outward-facing | Still requires renaming current `docs/` → `framework/` |

### Recommended answer

**Option A4 (Hybrid)** — restructure to:

```
dead-light-framework/
├── README.md                     ← project front door (also acts as INDEX)
├── HANDOFF.md                    ← session-state handoff
├── LICENSE
├── chat.txt                      ← historical motivation; not in framework spec
│
├── framework/                    ← Dead Light Framework — working artifacts (was: docs/)
│   ├── README.md                 ← framework's own front door + reading guide
│   ├── glossary-for-debate.md
│   ├── phases/
│   │   ├── phase-0-for-debate.md       ← sealed
│   │   ├── phase-1-for-debate.md       ← partial
│   │   └── phase-N-for-debate.md       ← future phases
│   ├── chapters/
│   │   └── adeptus-administratum/
│   │       └── codex.md                ← sealed v1.0
│   ├── debates/
│   │   ├── README.md             ← debate index
│   │   ├── 001-…md through 006-…md
│   ├── audit/                    ← IVP methodology + findings history
│   │   ├── independent-verification-pass-for-debate.md
│   │   ├── inventory.md
│   │   └── findings-*.md
│   ├── calibration-standards.md
│   └── pm-calibration-guide.md
│
├── case-studies/                 ← project-specific applications (was: docs/case-study-*)
│   └── lore-weave/
│       ├── README.md
│       ├── pm-threshold-decisions.md
│       ├── reckoning-team-record.md
│       ├── reckoning-record.md
│       └── methodology-notes.md
│
└── distribution/                 ← sealed-only, fillable template for adopters [NEW]
    ├── README.md                 ← how to use this template
    ├── INDEX.md                  ← master TOC with reading-guide
    ├── VERSION                   ← release version (see sub-decision C)
    ├── framework/                ← copy/transform of sealed pieces in framework/
    │   ├── phases/               ← only sealed phases
    │   ├── chapters/             ← only sealed Chapter Codexes
    │   ├── debates/              ← only decided debates
    │   └── calibration-standards.md
    ├── templates/                ← fillable scaffolds for adopters
    │   ├── astronomican-template.md
    │   ├── reckoning-record-template.md
    │   ├── pm-threshold-decisions-template.md
    │   └── reckoning-team-record-template.md
    └── examples/
        └── lore-weave-snapshot/  ← read-only snapshot of case-studies/lore-weave/
```

**Separable constraint check.** The `distribution/` folder is fully self-contained: all internal links are relative within `distribution/`; no link reaches outside. If a future adopter wants `distribution/` as a standalone repo, the folder is copy-paste ready.

### Real-world precedent

- **GitHub Starter Workflows** — `.github/workflow-templates/` folder pattern; copyable to any repo.
- **Cookiecutter** — separates `template/` (fillable) from project source.
- **arc42** — separates the template (12 sections) from the example.
- **Spring Initializr** — distribution = customizable starter; backed by reference implementations.
- **PRINCE2** — manuals + templates as separate artifacts within the methodology body.

---

## 4. Sub-decision B — Naming conventions

### Options

| # | Concern | Options | Recommended |
|---|---|---|---|
| **Folder names** | `distribution/` vs `template/` vs `kit/` vs 40k-flavored (`imperial-archive/`) | **`distribution/`** — neutral, well-understood; folder content is the framework's distribution surface |
| **File status suffix** | `*-for-debate.md` (current) vs frontmatter status (`status: draft`) vs naming-prefix (`draft-*.md`) | **Frontmatter status field** (see sub-decision F); retain `*-for-debate.md` suffix only as a transition until full migration. |
| **Working draft vs sealed naming** | Same name + frontmatter difference vs different file names | **Same name + frontmatter** — avoids file-renames when sealing; reduces broken-link risk |
| **Debate file naming** | `NNN-topic-slug.md` (current pattern) | Keep current pattern; it works |
| **Codex file naming** | `<chapter-name>/codex.md` (current) | Keep current pattern |
| **Case-study folder naming** | `case-study-<project>` vs `<project>/` | **`case-studies/<project>/`** — pluralized parent, project-named child, no redundant prefix |

### Real-world precedent

- **Conventional Commits** — naming as encoded metadata.
- **MADR (Markdown ADR)** — `NNNN-decision-title.md` pattern.
- **arc42** — section files named by purpose, not status.
- **DocBook** — XML metadata for status; file names stable.

---

## 5. Sub-decision C — Versioning model

### Options

| Option | Model | When to bump | Pros | Cons |
|---|---|---|---|---|
| **C1. SemVer (MAJOR.MINOR.PATCH)** | 0.X.Y → 1.0.0 → 1.1.0 → etc. | MAJOR = breaking changes (sealed-Law revision, Codex incompatible change); MINOR = new sealed artifact (debate decided, new Phase, new Chapter); PATCH = clarification, typo, non-substantive update | Industry standard; consumers understand instantly; tools (semver tooling) support it | "Breaking change" definition for governance documents is fuzzy |
| **C2. CalVer (YYYY.MM[.PATCH])** | 2026.05 → 2026.06.1 → etc. | Calendar-driven; PATCH per-release within month | Maps to event-driven IVP cadence; date-anchored; less debate over "is this MAJOR or MINOR" | No semantic signal about magnitude of change |
| **C3. Phase-anchored** | Phase-0-final → Phase-1-final → Codex-v1 | Bumps when a phase or chapter seals | Tightly bound to framework state | Confusing across multi-component releases; unclear how to handle inter-phase updates |
| **C4. Hybrid SemVer + framework-state tag** | `1.0.0-phase0+codex1` style | SemVer for distribution releases; suffix names what's included | Clear about content; SemVer-compatible | Awkward to type and read |

### Recommended answer

**Option C1 — SemVer (MAJOR.MINOR.PATCH).**

Mapped to framework events:

| Event | Bump |
|---|---|
| New sealed phase, new sealed Chapter (Codex), or new debate decided | **MINOR** (e.g., 0.5.0 → 0.6.0) |
| Sealed-Law amendment via Re-consecration, or a Codex amendment via new debate, or an IVP CRITICAL/HIGH finding remediated that changes a sealed artifact | **MAJOR** for sealed artifacts (e.g., 0.6.0 → 1.0.0 once Phase 1 fully seals; further breaking changes bump MAJOR) |
| Typo, clarification, non-substantive update, IVP MEDIUM/LOW finding remediation | **PATCH** (e.g., 0.6.0 → 0.6.1) |

**Initial version at distribution-folder creation: `v0.6.0`** — reflects all current sealed artifacts (Phase 0 + Phase 1 partial + debates 001-005 + Codex v1.0); pre-1.0 because Phase 1 is still partial and Phase 2/3/4 are not started. v1.0.0 reserved for "all initial phases sealed."

### VERSION file format

```
0.6.0
2026-05-11
codex-v1.0 + debates-001-005 + phase-0-sealed + phase-1-partial
```

Three lines: SemVer / release date / what's in this version. Plus a CHANGELOG.md alongside, per Keep-a-Changelog convention.

### Real-world precedent

- **SemVer 2.0** (Tom Preston-Werner) — most-adopted versioning model.
- **Keep a Changelog** — Olivier Lacan's standard.
- **Ruby Gems / npm / Cargo** — all SemVer-based.
- **Kubernetes API versioning** (alpha/beta/stable) — supports staged releases.

---

## 6. Sub-decision D — Document organization pattern (per file)

### Options

| Option | Pattern | Source | Best for |
|---|---|---|---|
| **D1. arc42** | 12-section template (introduction & goals; constraints; context & scope; solution strategy; building blocks; runtime view; deployment; …) | Gernot Starke + Peter Hruschka (2008+) | Architecture / governance documents |
| **D2. Diátaxis** | 4-quadrant taxonomy: tutorials, how-to guides, explanation, reference | Daniele Procida (2017+; widely adopted by Django, Gitea, etc.) | User-facing documentation systems |
| **D3. C4 model** | Context → Container → Component → Code hierarchy | Simon Brown (2012+) | Software architecture diagrams + text |
| **D4. ADR-style** | 1 decision per file: context, decision, consequences | Michael Nygard (2011) | Per-decision documentation |
| **D5. Custom hybrid** | Framework picks elements from D1/D2/D4 based on doc type | — | Fits Dead Light's mixed content (specs + debates + audit + case studies) |

### Recommended answer

**Option D5 — Custom hybrid, document-type-aware.**

Different document types in Dead Light need different patterns:

| Document type | Pattern | Required sections |
|---|---|---|
| **Phase spec** (phase-0, phase-1, …) | arc42-derived | Goal; Inputs/Prerequisites; Activities; Outputs; Quality Gates; Failure Modes; Anti-patterns; Roles; What is borrowed vs novel; Note on Method |
| **Debate** (NNN-topic.md) | ADR-derived + multi-sub-decision extension | Status header; Context; Pre-decided constraints (if any); Sub-decisions A..N with options+recommended; Real-world precedent; Application to case study; Open questions; Recommendation TL;DR; Decision; Follow-up actions; Methodological note |
| **Codex** (chapters/<name>/codex.md) | 10-section template (per debate 005 §4) | Identity & scope; Operational Bounds (Phase-specific); Hard Stops; Autonomy Threshold; Notify Triggers; Output Contract; Authority bounds; Lifecycle; Real-world precedent; Provenance |
| **IVP findings** (audit/findings-*.md) | Structured per IVP spec §5 | Executive verdict; Aggregate stats; Per-phase findings table; Limitations; Audit trail |
| **Case-study file** | Diátaxis-derived "how-to" style | Status; Spec applied; Procedure followed; Outputs; Departures from spec |
| **Reference / catalog** (calibration-standards) | Diátaxis "reference" style | Table-heavy; one row per item; columns: source, formula/mechanism, application |
| **README** | Diátaxis "explanation" + index | Front-door; purpose; map to other docs; reading guide |

### Real-world precedent

- **arc42** itself is hybrid (combines reference + explanation).
- **Documentation done by Vercel / Stripe** uses different formats per page (tutorial vs reference vs guide).
- **Anthropic Console docs** likewise.
- **GitHub Docs** has explicit per-doc-type templates.

---

## 7. Sub-decision E — File size limits and split rules

### Options

| Option | Hard cap | Soft cap | Per-section cap | "Too long" trigger |
|---|---|---|---|---|
| **E1.** No limits | None | None | None | Editorial discretion |
| **E2.** Strict | 200 lines | — | — | Always split at 200 |
| **E3.** Soft + section bounds | 500 lines hard; 300 soft | 100 lines per section | Either hard cap, OR file covers multiple distinct concerns | Recommended |
| **E4.** Token-budget based | ≤ 8K tokens / file | ≤ 4K tokens / file | ≤ 2K tokens / section | Tokens > thresholds |

### Recommended answer

**Option E3 — Soft + section bounds.**

Specifics:

- **Hard cap: 500 lines per file.** Exceeding requires either splitting into multiple files OR explicit justification recorded at file top.
- **Soft cap: 300 lines per file.** Warning threshold; suggest split unless the file is a single-concept reference.
- **Per-section soft cap: 100 lines per H2/H3 section.** Exceeding suggests sub-sectioning.
- **"Multi-concern file" anti-pattern.** A file that addresses more than one distinct concept/decision/topic should be split. The test: "If I had to retitle this file for one topic, what would I drop?"
- **Exceptions explicitly allowed:**
  - Reference catalogs (`calibration-standards.md`) — table-heavy, no functional length limit.
  - Comprehensive debates that record multi-angle exploration — debate 005 (~550 lines) and debate 006 (this file, expected ~700-900 lines) are inherent.
  - IVP findings reports — bounded by what was found; one finding per row in a table can grow.
- **Whenever a file exceeds 500 lines:** add a front-of-file note explaining why splitting was rejected.

### Real-world precedent

- **ADR convention**: 1 decision = 1 file, typically ≤ 1 page (~50 lines).
- **arc42**: each of 12 sections is "as long as needed but bounded by section purpose."
- **Confluence best practices**: ≤ 1 screen scroll.
- **Diátaxis**: tutorials ≤ 30 min reading time (~3000 words = ~300 lines); how-tos ≤ 5 min (~50 lines).
- **Anthropic prompt caching**: 1KB-100KB chunks favor efficient caching → ~20-2000 lines.
- **RAG chunking**: 200-2000 tokens optimal → ~50-300 lines.

---

## 8. Sub-decision F — Lean context / frontmatter format

### What problem this solves

Adeptus Administratum's Codex §8 re-priming requires reading Codex + Astronomican + artifact base. If every file requires full read to know its purpose, re-prime costs scale with framework size. A **frontmatter header** with key metadata lets an instance triage which files to fully read vs which to skim.

### Options

| Option | Format | Required fields | Pros | Cons |
|---|---|---|---|---|
| **F1.** YAML frontmatter | `---\nkey: value\n---` at top | status, version, audience, token_estimate, last_updated, supersedes, summary | Industry-standard (Jekyll / Hugo / GitHub README); machine-parseable | Adds clutter to top of every file |
| **F2.** Summary block | Markdown blockquote at top with summary | One paragraph (≤ 50 words) + status badge | Reader-friendly; visible in plain markdown | Not machine-parseable without parsing rules |
| **F3.** Both F1 and F2 | YAML frontmatter + human summary block | Both | Best of both; AI uses frontmatter, human reads summary | Most clutter |
| **F4.** Frontmatter for status only, summary inline | Minimal YAML (3 fields) + first paragraph is summary | status, version, last_updated | Lightweight | Less machine-routable |

### Recommended answer

**Option F3 — both YAML frontmatter AND human summary block**, but with discipline:

**YAML frontmatter (required):**
```yaml
---
title: <document title — matches H1>
status: draft | sealed | superseded | working
version: <SemVer or "not versioned">
audience: human | ai | both
type: phase | debate | codex | audit | case-study | reference | readme
token_estimate: <approximate token count, optional>
last_updated: YYYY-MM-DD
supersedes: <path/to/previous-version.md or null>
sealed_by: <debate-NNN.md or null>
---
```

**Human summary block (required, immediately after frontmatter):**
```markdown
> **Status:** Sealed via debate NNN on YYYY-MM-DD.
> **Audience:** Project owners + AI aides operating under Adeptus Administratum Codex.
> **Purpose:** <one sentence>
> **Read next if:** <which other files this points to>
```

The two together let:
- An AI instance triage by reading frontmatter only (cheap).
- A human reader get bearings from the summary block (5 seconds).
- A reader who needs detail proceed to the body.

### Real-world precedent

- **Jekyll / Hugo / Astro / Eleventy** — YAML frontmatter is the universal pattern.
- **GitHub README / wiki pages** — accept YAML frontmatter for metadata.
- **MADR** — has explicit frontmatter for ADR status.
- **Anthropic / OpenAI documentation** — uses YAML frontmatter for routing.
- **Hugo documentation theme conventions** — both frontmatter and summary blocks.

---

## 9. Sub-decision G — Index + TOC + reading guide

### Options

| Option | Structure | Pros | Cons |
|---|---|---|---|
| **G1.** Single master `INDEX.md` at repo root | One file lists everything | Single source of truth; easy to find any artifact | Risks getting stale; large file |
| **G2.** Hierarchical README per folder | Each folder has a README listing its contents | Locality; folder-author owns it | Multiple files to keep in sync |
| **G3.** Role-based reading guides | Multiple top-level guides: "for PMs / for ICs / for AI-aides / for adopters" | Audience-targeted | Risk of inconsistency between guides |
| **G4.** All three combined | INDEX + per-folder README + role-based guides | Maximum discoverability | Maintenance overhead |

### Recommended answer

**Option G4 — All three combined, with single source-of-truth discipline.**

Structure:

```
dead-light-framework/
├── README.md                          ← root README acts as INDEX.md; pointer to everything
│
├── framework/
│   ├── README.md                      ← framework's own reading guide; lists each spec
│   ├── phases/README.md               ← phases-specific reading guide
│   ├── chapters/README.md             ← chapters-specific reading guide
│   ├── debates/README.md              ← existing debates index, retained
│   └── audit/README.md                ← audit-history reading guide (currently missing)
│
└── distribution/
    ├── README.md                      ← distribution front door
    ├── INDEX.md                       ← master TOC of distribution contents
    ├── for-pms.md                     ← role-based reading guide: PMs
    ├── for-ics.md                     ← role-based reading guide: ICs / engineers
    ├── for-ai-aides.md                ← role-based reading guide: Adeptus Administratum instances
    └── for-adopters.md                ← role-based reading guide: framework adopters / framework-owners
```

**Discipline rule** (source of truth): root `README.md` and `distribution/INDEX.md` are auto-buildable from per-folder READMEs (script TBD; manual until then). Inconsistencies are caught by IVP Phase 5 (Internal Consistency) which already checks index integrity.

### Real-world precedent

- **Read the Docs** — root TOC + per-section README pattern.
- **Vercel docs / Stripe docs** — role-based reading guides (developers / managers / etc.).
- **arc42** — each section has its own purpose statement.
- **Linux kernel `Documentation/`** — hierarchical READMEs with global index.

---

## 10. Sub-decision H — Update + sync mechanism (working → distribution)

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **H1.** Manual copy on each seal | Human copies sealed content from `framework/*-for-debate.md` to `distribution/` whenever a debate seals | Simple; transparent | Error-prone; sealed/distribution can drift |
| **H2.** Scripted build (CI-like) | Build script processes `framework/` files with `status: sealed` frontmatter into `distribution/`; runs on commit hook or `npm run build` | Automated; consistent | Requires script maintenance |
| **H3.** Distribution is the sealed source-of-truth; `framework/` for working drafts only | When a debate seals, the artifact moves from `framework/*-for-debate.md` to `distribution/framework/<phase or chapter or debate>` | Clear separation; no duplication | "Move on seal" changes file location, breaking link history |
| **H4.** Sealed content lives in `framework/`; `distribution/` symlinks or imports it | Use markdown include / symlinks / git-submodule | No duplication | Tool-dependent; not all renderers support includes |

### Recommended answer

**Option H2 — Scripted build, with H3-style discipline.**

Concretely:

- **Working drafts** live in `framework/` (e.g., `framework/phases/phase-2-for-debate.md` for a draft).
- **Sealed artifacts** keep their working-location filename but flip `status: draft` → `status: sealed` in frontmatter and drop the `-for-debate` suffix (rename optional; the suffix becomes redundant once `status: sealed` is set).
- **Distribution generation:** a script (`scripts/build-distribution.sh` or equivalent — maintained manually until project owner authorizes scripting infrastructure) walks `framework/`, filters files with `status: sealed`, copies into `distribution/framework/` mirroring the source path, transforms internal links to keep `distribution/` self-contained, generates `distribution/INDEX.md` from the collected metadata, and writes `distribution/VERSION`.
- **Manual sync allowed** (project owner copies a single file from `framework/` to `distribution/`) when scripting is overkill — but the periodic check-pass (IVP-equivalent) verifies sync integrity.
- **Sync direction is one-way: `framework/` → `distribution/`.** Adopters who modify `distribution/` for their own project work on a fork or downstream copy; their changes never flow back unless they open a debate.

### Real-world precedent

- **Cookiecutter** — template directory is the source; project generation is read-only-from-template.
- **Spring Initializr** — backend computes the starter from versioned reference implementations.
- **Hugo / Jekyll / Astro** — source + build artifact separation; build is one-way.
- **Helm charts** — chart source + rendered manifest separation.

---

## 11. Sub-decision I — Customization protocol (fillable vs immutable)

### What problem this solves

Adopters need to know **what they can change** vs **what they must keep as-is** when cloning the distribution. Without explicit markers, every adopter's adaptation drifts from framework — and the framework can't tell whether a deviation is intentional or a bug.

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **I1.** No markers; adopters change anything | All distribution content is suggestion | Maximum flexibility | No way to audit adopters; framework's load-bearing decisions can be silently broken |
| **I2.** Inline `<!-- FILLABLE -->` markers + `<!-- IMMUTABLE -->` markers | HTML comments in markdown bracket sections | Clear; visible to anyone reading | Verbose; clutters source |
| **I3.** Frontmatter `customization: fillable | immutable | partial` field; per-file granularity | One marker per file | Lightweight | Can't mix within a file |
| **I4.** Hybrid: frontmatter for file-level + inline for sub-sections | I3 + I2 combined for mixed-content files | Most expressive | Most complex |

### Recommended answer

**Option I4 — Hybrid (file-level frontmatter + inline markers for sub-sections).**

**File-level (frontmatter):**

```yaml
customization: fillable | immutable | partial
```

- `fillable` — entire file is a template; adopter is expected to fill or replace content. Examples: `templates/astronomican-template.md`.
- `immutable` — entire file represents a sealed framework decision; adopter must NOT change it (only fork the framework via Re-consecration). Examples: `distribution/framework/chapters/adeptus-administratum/codex.md`, `distribution/framework/phases/phase-0.md`.
- `partial` — file has both immutable framework content and fillable adopter slots; use inline markers.

**Inline markers (for `partial` files):**

```markdown
<!-- IMMUTABLE: framework-spec — do not modify without Re-consecration -->
Phase 0 is mandatory for retrofit projects.
<!-- /IMMUTABLE -->

<!-- FILLABLE: adopter-specific — replace with project context -->
Project name: <fill in your project name>
Significance threshold: <see pm-calibration-guide.md to derive>
<!-- /FILLABLE -->
```

**Audit support:** Adeptus Administratum instances operating on an adopter project can scan for inline markers + frontmatter and flag violations (Codex §5 N-3 / N-4 equivalent) — adopter modified an `immutable` section.

### Real-world precedent

- **Cookiecutter** — `{{ jinja_variable }}` patterns mark fillable slots; everything else is template-as-is.
- **Spring Boot starter projects** — explicit "your code goes here" comments.
- **AsciiDoctor / DocBook** — `<replaceable>` tags for fillable content.
- **GitHub Actions reusable workflows** — `inputs:` block is fillable; the rest is immutable.

---

## 12. Sub-decision J — Dual-audience design rules

### What problem this solves

Dead Light is the first framework to treat human and AI as co-equal first-class audiences (per debate 005 + this debate's pre-decided constraint). Industry has individual examples (Stripe API docs, Anthropic Console) but no methodology-level standard. Dead Light can prescribe one.

### Proposed rules

1. **Every artifact has a YAML frontmatter `audience` field** (per sub-decision F).
   - `human` — human-first reading; AI may consume but not primary.
   - `ai` — AI-first reading (e.g., re-priming primers, prompt templates); human may read but layout is AI-optimized.
   - `both` — both audiences as co-equal; conform to all rules below.

2. **For `audience: both` artifacts:**
   - **Summary block at top** (≤ 50 words; first thing both audiences read).
   - **Section IDs deterministic** — every H2/H3 has an ID matching `#kebab-case-of-title` so AI can cite by anchor.
   - **No prose-only assertions of structured information** — anything that's a table belongs in a table, anything that's a list belongs in a list. AI parsing is reliable on structured markdown; flaky on dense prose.
   - **Citations always inline + bibliographic** — never "see above"; always concrete reference. (Already a framework policy via Notify Trigger N-3.)
   - **No screenshot-as-evidence** — image content is opaque to AI; transcribe.
   - **No hidden context** — every load-bearing assumption is named in the file or linked.

3. **For `audience: ai` artifacts (e.g., re-priming primers):**
   - **First 200 tokens contain the whole essence** — the AI may not read further; the essence must be load-bearing.
   - **Token-budget annotation** — frontmatter `token_estimate` mandatory.
   - **Imperatives + verbs forward** — front-load action ("Check X. Then verify Y.").

4. **For `audience: human` artifacts:**
   - Story-driven / narrative-friendly allowed.
   - Token budget not enforced.
   - But: summary block still required (humans benefit from triage too).

5. **Cross-link discipline:**
   - Internal links are relative paths, never absolute URLs.
   - Every internal link has visible link text (no bare URLs).
   - Cross-file links use `[file:line-range](path#section-id)` format when pointing at a specific section.

### Real-world precedent

- **Stripe API docs** — dual-format: human-readable narrative + machine-readable OpenAPI spec sourced from same definitions.
- **Anthropic Console / Workbench docs** — markdown + JSON schemas in parallel.
- **OpenAPI specification** — itself dual-audience by design.
- **Hugo / Astro frontmatter** — first design that treats metadata + content as co-equal.
- **Diátaxis** — four quadrants implicitly target different reading modes.
- **GraphQL SDL** — human-readable schema that's also machine-parseable.

---

## 13. Real-world precedent — full standards map

Consolidated table mapping each sub-decision to industry standards we draw from. This table is the policy-1-compliant body of debate 006's structural arguments.

| Sub-decision | Industry standards informing the design |
|---|---|
| A. Folder topology | GitHub Starter Workflows; Cookiecutter; arc42; Spring Initializr; PRINCE2 |
| B. Naming conventions | Conventional Commits; MADR; arc42; DocBook |
| C. Versioning | SemVer 2.0 (Tom Preston-Werner); CalVer; Keep a Changelog (Olivier Lacan); npm / Cargo / Ruby Gems |
| D. Document organization | arc42 (Starke + Hruschka); Diátaxis (Procida); C4 model (Brown); ADR (Nygard); MADR |
| E. File size limits | ADR; arc42; Confluence best practices; Diátaxis reading-time bounds; Anthropic prompt caching; LangChain / LlamaIndex RAG chunking |
| F. Frontmatter format | Jekyll / Hugo / Astro / Eleventy; MADR; GitHub README YAML; Anthropic / OpenAI docs |
| G. Index + reading guide | Read the Docs; Vercel / Stripe docs; arc42; Linux kernel Documentation/ |
| H. Update + sync mechanism | Cookiecutter; Spring Initializr; Hugo / Jekyll / Astro source + build separation; Helm charts |
| I. Customization protocol | Cookiecutter; Spring Boot starter; AsciiDoctor `<replaceable>`; GitHub Actions reusable workflows `inputs:` |
| J. Dual-audience design rules | Stripe API; Anthropic Console; OpenAPI; Hugo frontmatter; Diátaxis; GraphQL SDL |

**Policy 1 compliance:** every recommendation in sub-decisions A–J above rests on at least one real-world standard. Where the framework's choice differs from the standard, the rationale is recorded inline (e.g., E recommends 500 hard / 300 soft because Dead Light's documents are larger than typical ADRs but smaller than book chapters — a calibration choice on top of industry conventions).

---

## 14. Application to Dead Light Framework (sketch)

If debate 006 seals as proposed (full recommendations adopted), the migration plan is:

### Phase 1 of migration (immediate after seal)

1. **Create `distribution/` folder** with INDEX.md, VERSION, role-based reading guides (G).
2. **Rename `docs/` → `framework/`.** Update all internal cross-references. (This is the breaking-change step.)
3. **Move `docs/case-study-lore-weave/` → `case-studies/lore-weave/`.**
4. **Add YAML frontmatter to every existing file** with at minimum: title, status, version, audience, type, last_updated. (Backfill — substantial work, but mostly mechanical.)
5. **Add summary blocks to every existing file** below frontmatter.
6. **Move `docs/phases/` reorganization:** move `phase-0-for-debate.md` and `phase-1-for-debate.md` into a `framework/phases/` subdirectory (current location is `framework/` flat).

### Phase 2 of migration (within a follow-up session)

7. **Populate `distribution/framework/`** by copy-and-transform from sealed `framework/` content.
8. **Create `distribution/templates/`** with fillable scaffolds:
   - `astronomican-template.md`
   - `reckoning-record-template.md`
   - `pm-threshold-decisions-template.md`
   - `reckoning-team-record-template.md`
9. **Create `distribution/examples/lore-weave-snapshot/`** as a read-only snapshot of `case-studies/lore-weave/` at debate-006-seal time.
10. **Stamp v0.6.0** in `distribution/VERSION` and write `distribution/CHANGELOG.md`.

### Phase 3 of migration (background ongoing)

11. **Audit + close any cross-folder reference drift** — IVP Phase 5 (Internal Consistency) re-runs would catch this; can also be done manually.
12. **Run an Adeptus Administratum re-priming dry-run** on the new layout to confirm token-efficiency improvements.

### Estimated effort

- Phase 1: 3-5 person-hours (mechanical backfill + renaming).
- Phase 2: 2-4 person-hours (templates + examples).
- Phase 3: 1-2 person-hours (audit).
- **Total: ~6-11 person-hours.**

This is substantial. Consider running it as a single dedicated session (or several within one chat thread).

---

## 15. Open questions remaining (carry forward if accepted)

1. **Multi-language support.** The framework is currently English-only (per `phase-1-for-debate.md` § Conventions). Project owner communicates in Vietnamese (per user memory). Should distribution support multiple languages? If so, how? Defer to debate 007 if scope warrants.

2. **Localization vs internationalization.** Even if multi-language is deferred, frontmatter could include `language: en` to enable future language tracking.

3. **Multi-version maintenance.** Once `distribution/` has versioned releases, do we keep old versions around (e.g., `distribution/archives/v0.5.0/`)? Or always overwrite with latest?

4. **Build script.** Sub-decision H assumes a manual build script eventually. Who owns it? When does it move from manual to automated? Defer to first observed drift between `framework/` and `distribution/`.

5. **Adopter feedback loop.** If an adopter uses the distribution and finds a problem, how does that flow back to the framework? RFC system? GitHub Issues? Out of scope for this debate but worth resolving before public release.

6. **Brand voice / cultural fit.** 40k vocabulary is consistent within the framework but may alienate adopters from formal organizations (banks, government). Should `distribution/` provide a "branded-down" variant with 40k vocabulary replaced by neutral terms? Out of scope for this debate.

7. **Tooling integration.** Should distribution include Cookiecutter / Yeoman scaffolds that auto-populate a project? Out of scope for this debate; could be debate 008.

8. **IVP integration with distribution.** Should IVP audits run against `distribution/` independently from `framework/`? Today IVP audits `framework/` (was `docs/`). Out of scope; pick up after migration.

---

## 16. Recommendation (TL;DR)

| Sub-decision | Recommended |
|---|---|
| A. Folder topology | **A4** — Hybrid: `framework/` + `case-studies/` + `distribution/` at root; `chapters/` and `phases/` nested under `framework/`. Distribution organized to be separable. |
| B. Naming conventions | Folder names neutral (`distribution/`); status via frontmatter, not filename suffix; same-name working/sealed via frontmatter `status:` field |
| C. Versioning | **C1** — SemVer 2.0; initial version v0.6.0 at distribution-folder creation; CHANGELOG.md maintained |
| D. Document organization | **D5** — Custom hybrid, document-type-aware (phase = arc42; debate = ADR-extended; codex = 10-section; audit = IVP-spec; case-study = Diátaxis how-to; reference = Diátaxis reference; README = Diátaxis explanation + index) |
| E. File size + split rules | **E3** — 500-line hard cap; 300-line soft; 100-line per-section soft; multi-concern files split; exceptions for reference catalogs / comprehensive debates / IVP findings (require explanatory note) |
| F. Frontmatter format | **F3** — YAML frontmatter (status, version, audience, type, token_estimate, last_updated, supersedes, sealed_by) + human summary block (≤ 50 words + status badge + purpose + read-next) |
| G. Index + reading guide | **G4** — Root README + per-folder README + 4 role-based guides in `distribution/` (for-pms, for-ics, for-ai-aides, for-adopters) |
| H. Update + sync mechanism | **H2** — Scripted build (manual until scripting infra authorized); one-way `framework/` → `distribution/`; status-driven filtering |
| I. Customization protocol | **I4** — File-level frontmatter `customization: fillable / immutable / partial` + inline `<!-- IMMUTABLE -->` / `<!-- FILLABLE -->` markers for `partial` files |
| J. Dual-audience design rules | **J full** — frontmatter audience field; summary block; deterministic section IDs; structured markdown over prose for structured information; citation discipline; cross-link discipline |

If approved, the framework gains a clean outward-facing distribution surface plus explicit conventions for human + AI dual-audience design that no existing methodology currently prescribes at this level.

---

## 17. Decision

_(Empty — to be filled when project owner decides.)_

- **Decision:** _(pending)_
- **Decided on:** _(pending)_
- **Decided by:** _(pending)_

### Follow-up actions (will be checked on seal)

- [ ] Restructure: rename `docs/` → `framework/`; move `docs/case-study-lore-weave/` → `case-studies/lore-weave/`; create `framework/phases/` subdir and move phase docs in.
- [ ] Create `distribution/` folder skeleton (README + INDEX + VERSION + CHANGELOG + role-based guides + framework + templates + examples subdirectories).
- [ ] Backfill YAML frontmatter on every existing file (estimate: ~25 files × ~2 minutes each = ~50 minutes).
- [ ] Backfill human summary block on every existing file.
- [ ] Populate `distribution/templates/` with fillable scaffolds.
- [ ] Populate `distribution/examples/lore-weave-snapshot/` with case-study read-only copy.
- [ ] Update every cross-reference in the repo to use the new paths.
- [ ] Re-run IVP Phase 5 (Internal Consistency) against the new structure to catch any drift.
- [ ] Update HANDOFF.md (document tree + recent commits + recommended next step).
- [ ] Update [debates/README.md](README.md) — debate 006 marked decided.
- [ ] (If migration substantial) Open a dedicated `audit/ivp-2026-MM-DD-doc-arch-migration.md` to track per-file backfill compliance.

---

## 18. Methodological note (forward-applying)

This debate is the **first time the framework explicitly designs its own document architecture as a first-class concern**. Before debate 006, document organization was emergent — files were added as needed without an enforced layout. After debate 006, document architecture becomes a sealed framework concern with its own conventions, just like Phase 0/1 design and the Adeptus Administratum Codex.

Three insights worth recording for forward application:

1. **Frameworks have layers.** Dead Light has now sealed concerns at three layers:
   - Project governance (Phases 0/1, Sector mechanism — debates 001-004).
   - Operational aide (Adeptus Administratum Codex — debate 005).
   - **Document architecture** — debate 006 (this debate).
   Each layer is "fractal" of the project-governance thesis: frozen authority that survives any participant. The thesis applies to projects, to aides, to documents.

2. **Outward-facing design is its own discipline.** Before debate 006, the framework was inward-facing (project-owner + AI-aide as audiences). Outward-facing design must reckon with adopters who may not share the framework's vocabulary, conventions, or assumptions. The distribution folder is the first concrete recognition of this.

3. **Dual-audience design appears to be without methodology-level precedent in what I have surveyed.** Industry has individual examples (Stripe, Anthropic) but I have not found a methodology that *prescribes* dual-audience design rules. If Dead Light's J sub-decision proves useful in practice (LoreWeave will be the first test), this may be a small contribution back to the documentation-architecture field.

---
title: "Debate 007 — Scripting Infrastructure (post-debate-006 automation)"
status: open
version: not versioned
audience: both
type: debate
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

# Debate 007 — Scripting Infrastructure (Post-Debate-006 Automation)

> **Status:** open.
> **Opened:** 2026-05-13
> **Decided:** —
> **Decided by:** project owner (pending)
> **Affects:** Creates a new `scripts/` directory at repo root. Operationalises [debate 006](006-documentation-architecture-and-distribution.md) sub-decision H ("scripted build, manual until scripting infra authorized"). Integrates with [Adeptus Administratum Codex](../chapters/adeptus-administratum/codex.md) §8 re-priming protocol step 5 (drift detection). Defines repository tooling discipline going forward.
> **Raised by:** project owner immediately after the debate 006 migration completed (~96 files touched across 5 commits, ~50–100K tokens consumed). Observation: mechanical work (frontmatter backfill, cross-reference rewrites, distribution sync, snapshot creation) consumed substantial LLM tokens; same work via scripts would cost ~50 tokens per invocation. Authorising tooling closes the high-token-cost gap.

---

## 1. Context

The debate 006 migration was completed by AI-aide-1 manually performing 25 frontmatter insertions, ~30 cross-reference rewrites, 28 file copies + transformations, and several mechanical edits. The work was correct but expensive (token cost).

Three operational facts force this debate:

1. **Debate 006 §H already authorised scripting in principle.** Sub-decision H reads: "Scripted build (manual until scripting infra authorized); one-way framework/ → distribution/; status-driven filtering." This debate is the authorisation event for the script infrastructure.

2. **Adeptus Administratum Codex §8 re-priming protocol step 5 (drift detection) is currently expensive.** When a new instance starts a task, step 5 ("Spot inconsistencies between Codex, Astronomican, and artifact base") requires reading multiple files. A frontmatter validator + link checker can do this in milliseconds at zero LLM token cost, with the AI instance reading only the script's output.

3. **The next phase of work (LoreWeave Pass 1 Current State Audit) will touch many files in `case-studies/lore-weave/reckoning-record.md`.** Without scripts, every cross-reference update + frontmatter touch consumes tokens. Scripts let the AI instance focus on the audit reasoning rather than mechanical edits.

The pattern this debate establishes — AI does governance; scripts do mechanics — is itself on-thesis with the framework's central premise: the executor (instance) does not need to manually do everything as long as the persistent authority (Codex + artifact base + scripts) is in place.

---

## 2. Pre-decided constraints (project owner committed 2026-05-13)

| Pre-decision | Decision | Rationale |
|---|---|---|
| **Authorisation** | **Approved.** Operationalises debate 006 §H. Scripts to be implemented under `scripts/` directory at repo root. | Token-cost reduction is material (~99% reduction on mechanical work). |
| **Language** | **Python.** | Python's standard libraries (pathlib, subprocess, argparse) cover most file operations; mature YAML libraries (ruamel.yaml, python-frontmatter) handle frontmatter manipulation cleanly; cross-platform (Windows + Linux + macOS); installable via standard package managers; widely understood by adopters. Bash was a candidate but loses to Python on YAML parsing reliability. |

These two pre-decisions scope the rest of the debate to *how* to build the Python tooling, not *whether* or *what language*.

---

## 3. Sub-decision A — Script inventory and priorities

What scripts should exist? Priority order based on observed token-cost during the debate 006 migration.

### Tier 1 — High-frequency / high-token-cost (build first)

| Script | Job | Token-cost saved per use |
|---|---|---|
| **`sync_distribution.py`** | Walk `framework/`, filter files with `status: sealed` frontmatter, copy to `distribution/framework/`, drop `-for-debate` suffix on sealed files, regenerate `distribution/INDEX.md` from collected metadata, update `distribution/VERSION`. One-way sync per debate 006 §H. | ~10K tokens (the Phase 2 work of debate 006 migration would have been one script call) |
| **`validate_frontmatter.py`** | Walk all `*.md` files; check each has required YAML frontmatter (title/status/audience/type/last_updated); report missing or invalid fields. | ~1K tokens (every drift-detection at instance re-priming) |
| **`check_links.py`** | Walk all `*.md` files; parse markdown links; verify every internal link resolves to an existing file; report dangling. | ~1K tokens (currently done by manual grep + investigation) |

### Tier 2 — Medium-frequency (build second)

| Script | Job |
|---|---|
| **`snapshot_case_study.py <name>`** | Copy `case-studies/<name>/` → `distribution/examples/<name>-snapshot/`; inject `snapshot_of` and `snapshot_date` frontmatter fields; update paths inside snapshot files. |
| **`bump_version.py <major\|minor\|patch>`** | Read `distribution/VERSION`; compute new version per SemVer rules; update VERSION; prepend new section template to `distribution/CHANGELOG.md`. |
| **`update_handoff_tree.py`** | Walk repo; regenerate the `## Document tree` section of `HANDOFF.md` from current filesystem state. |
| **`frontmatter_set.py <file> <field>=<value>`** | Atomically update one frontmatter field in one file (e.g., `status: working` → `status: sealed`). Validates field exists; preserves all other frontmatter. |

### Tier 3 — Low-frequency / nice-to-have (build later if needed)

| Script | Job |
|---|---|
| **`release.py <version>`** | Orchestrate full release: validate_frontmatter → check_links → sync_distribution → snapshot_case_study (all in case-studies/) → bump_version → git add + commit + tag. One-command release. |
| **`new_debate.py <slug>`** | Scaffold a new debate file under `framework/debates/NNN-<slug>.md` with frontmatter template + standard sections (Status header, Context, Sub-decisions, Recommendation TL;DR, Decision empty). |
| **`new_chapter_codex.py <name>`** | Scaffold a new Chapter Codex under `framework/chapters/<name>/codex.md` with 10-section template. |
| **`new_case_study.py <project>`** | Scaffold `case-studies/<project>/` with the four standard files (README, pm-threshold-decisions, reckoning-team-record, reckoning-record, methodology-notes). |
| **`ivp_phase5.py`** | Automated Phase 5 (Internal Consistency) check: term drift detection + decision-to-doc reflection + quantitative consistency + README link integrity. Generates a `findings-phase5-<date>.md` skeleton with detected drift. |

### Proposed answer

**Tier 1 first (sync_distribution + validate_frontmatter + check_links).** These three cover the highest-token-cost cases observed in the debate 006 migration. Tier 2 follows as need surfaces. Tier 3 deferred.

### Real-world precedent

- **Hugo `hugo` CLI** — `hugo build` is structurally identical to sync_distribution.
- **mkdocs `mkdocs build`** — same pattern.
- **`vale` / `markdownlint`** — markdown validators; check_links is structurally similar.
- **`semantic-release`** — automated version bumping + changelog generation.
- **`cookiecutter`** — scaffolding new projects from templates (matches new_debate / new_chapter / new_case_study).

---

## 4. Sub-decision B — Library choices

Within Python, what libraries?

### Options per concern

| Concern | Options | Recommended |
|---|---|---|
| **YAML frontmatter parsing** | `PyYAML` (most common; loses key-order + comments on write) / `ruamel.yaml` (preserves formatting + comments) / `python-frontmatter` (markdown-aware; wraps PyYAML or ruamel) | **`python-frontmatter` (backed by ruamel.yaml)** — purpose-built for markdown + frontmatter; preserves YAML formatting on write; widely used (Jekyll/Hugo Python tooling) |
| **CLI** | `argparse` (stdlib; verbose) / `click` (decorator-based; clean) / `typer` (click + type hints; modern) | **`typer`** — modern, type-hint-friendly, includes auto-help; minimal install footprint |
| **Markdown link parsing** | regex (fragile) / `markdown-it-py` (CommonMark spec) / `marko` / `mistune` | **`markdown-it-py`** — CommonMark-compliant, well-maintained, supports link AST extraction |
| **File operations** | `os` / `pathlib` (modern, recommended) / `shutil` | **`pathlib` + `shutil`** — stdlib only |
| **Diff / patch (for status transitions)** | `difflib` (stdlib) / `unidiff` | **`difflib`** — stdlib is enough |
| **Testing** | `unittest` (stdlib) / `pytest` (more ergonomic) | **`pytest`** — better for scripted CLI tests; if tests are added later |

### Proposed answer

Minimum dependency set: **`python-frontmatter`, `typer`, `markdown-it-py`** — three packages, all maintained, all PyPI-installable, all pure Python (no C extensions to compile on Windows).

`requirements.txt` example:
```
python-frontmatter>=1.0
typer>=0.9
markdown-it-py>=3.0
```

### Real-world precedent

- **Jekyll's Ruby ecosystem** uses Front Matter parsing extensively; `python-frontmatter` is the Python equivalent.
- **`mkdocs-material`** uses `pyyaml` + `pymdown-extensions`; analogous pattern.
- **Anthropic SDK examples** use `typer` heavily for CLI examples.

---

## 5. Sub-decision C — Repository placement

Where do the scripts live?

### Options

| Option | Placement | Pros | Cons |
|---|---|---|---|
| **C1.** `scripts/` at repo root | Standard convention; visible to all | Most common pattern; immediate discoverability | Mixes framework-internal scripts with adopter-usable ones |
| **C2.** `framework/tooling/` (under framework/) | Tooling is part of the framework | Logical grouping | Scripts are not "framework spec" content; mixing concerns |
| **C3.** Split: `scripts/` for framework-internal + `distribution/scripts/` for adopter-usable | Two locations | Clear separation; adopters get useful subset | Doubles maintenance for shared scripts |
| **C4.** `.claude/scripts/` (alongside slash commands) | Tooling lives with AI-aide tooling | Aligns with Adeptus Administratum Codex (scripts as aide-instruments) | Implies scripts are AI-only; not adopter-visible |

### Proposed answer

**C3 hybrid — split:**

- **`scripts/`** at repo root — framework-maintainer scripts (`sync_distribution.py`, `bump_version.py`, `update_handoff_tree.py`, `release.py`, `new_debate.py`, `new_chapter_codex.py`, `new_case_study.py`, `ivp_phase5.py`). These operate on the upstream `framework/` and `case-studies/` and `distribution/` trees; adopters typically don't need them.
- **`distribution/scripts/`** — adopter-usable subset (`validate_frontmatter.py`, `check_links.py`, possibly `snapshot_case_study.py`). Adopters cloning distribution/ get these for their own project's consistency checks.

Files in `distribution/scripts/` are **copies** of the upstream `scripts/` versions (per debate 006 §H one-way sync); they update at each release.

### Real-world precedent

- **Hugo** — `hugo` binary is one thing; `hugo new site` scaffolding is part of the same CLI. Single tool, multiple subcommands.
- **Yarn / npm** — `package.json` scripts live in repo root; adopters get tooling through `npm install`.
- **Rails / Django** — `bin/rails` and `manage.py` live at project root; the framework gives adopters subset commands via `rails new` / `django-admin`.

---

## 6. Sub-decision D — Trigger model

When does each script run?

### Trigger options

| Trigger | Pros | Cons | Best for |
|---|---|---|---|
| **D1.** Manual invocation only (`python scripts/sync_distribution.py`) | Simple; no surprises; full project-owner control | Easy to forget | Tier 1 + Tier 2 scripts in early adoption |
| **D2.** Pre-commit hooks (Husky / pre-commit framework) | Catches issues before commit; fast feedback | Adds install step; can frustrate developers | `validate_frontmatter.py` + `check_links.py` |
| **D3.** Git hooks bare (no framework, just `.git/hooks/`) | Zero install | Per-clone setup; doesn't share across team | Solo projects |
| **D4.** GitHub Actions / CI | Centralised; can fail PR | Slower feedback; ties to GitHub | `release.py`; periodic full validation |
| **D5.** Adeptus Administratum re-priming step 5 invokes scripts | Aligns with Codex §8 protocol; AI instance gets fresh validation | Requires aide to actually run them | `validate_frontmatter.py` + `check_links.py` |

### Proposed answer

**Layered approach:**

- **Tier 1 scripts: Manual + AI-aide invocation (D1 + D5).** Project owner invokes manually on demand; Adeptus Administratum invokes during re-priming step 5. No CI/hooks initially.
- **Pre-commit hooks (D2): Deferred** until a second human contributor joins (currently solo project with AI-aide-1). For solo + AI, manual + Codex-invoked is enough.
- **GitHub Actions (D4): Deferred** until repo is public or has external contributors. The `release.py` orchestrator can be CI-callable when needed.

Concretely: the Codex §8 step 5 reference list grows from "spot inconsistencies (informal)" to "spot inconsistencies — invoke `python scripts/validate_frontmatter.py` and `python scripts/check_links.py`; surface output as Codex §5 N-3/N-4 notifies."

### Real-world precedent

- **`mkdocs serve`** — manual command; nothing automatic.
- **`pre-commit framework`** (pre-commit.com) — opt-in pre-commit infrastructure; popular but not required.
- **GitHub Actions** — standard CI; deferred until repo is collaborative.
- **`vale` linting** — manual + editor integration; same pattern.

---

## 7. Sub-decision E — Validation strictness

How strictly do scripts fail?

### Options

| Option | Behaviour | Best for |
|---|---|---|
| **E1.** Warn-only | Print warnings; never exit non-zero | Early adoption; gathering data on what's actually broken |
| **E2.** Fail on first error | Exit 1 on first issue; halt | Pre-commit hooks where fast-fail is desired |
| **E3.** Fail only on critical (configurable severity) | Each script defines criticality thresholds; warn-or-fail per category | Most flexible; matches IVP severity rubric |
| **E4.** Dry-run first; explicit `--apply` to commit changes | All write operations require `--apply` flag | Safest; matches Codex §4 Autonomy Threshold for write operations |

### Proposed answer

**E3 + E4 combined:**

- Read-only scripts (validate_frontmatter, check_links): default warn-only behaviour with `--strict` flag for fail-on-error. Severity follows IVP rubric (CRITICAL / HIGH / MEDIUM / LOW); default exit-1-threshold is HIGH.
- Write scripts (sync_distribution, bump_version, snapshot_case_study, frontmatter_set, release): default behaviour is **dry-run** (print what would change); `--apply` flag required to actually write. Matches Adeptus Administratum Codex §4 Autonomy Threshold ("acts solo when action is read-only").

Example:
```
$ python scripts/sync_distribution.py
[DRY-RUN] Would copy framework/phases/phase-0-for-debate.md → distribution/framework/phases/phase-0.md
[DRY-RUN] Would update distribution/INDEX.md (3 new entries)
[DRY-RUN] Would update distribution/VERSION (no change; already at 0.6.0)
$ python scripts/sync_distribution.py --apply
✓ Copied 12 files
✓ Updated distribution/INDEX.md
✓ Done
```

### Real-world precedent

- **`terraform plan` / `terraform apply`** — dry-run-then-apply is the dominant IaC pattern.
- **`git diff --stat` / `git apply`** — same pattern.
- **`rsync --dry-run`** — same pattern.
- **`pip install --dry-run`** — same pattern.

---

## 8. Sub-decision F — Error handling philosophy

What happens when scripts encounter unexpected state?

### Options

| Option | Behaviour |
|---|---|
| **F1.** Fail-fast | Exit 1 at first unexpected condition; user investigates |
| **F2.** Best-effort continue | Log error, continue processing other files; final exit code reflects overall success |
| **F3.** Strict transactions | Build full plan before any write; if any step fails validation, abort all writes |

### Proposed answer

**F3 — Strict transactions** for write operations; **F2 — best-effort continue** for read-only validation.

Rationale: write operations must not leave the repo in an inconsistent state (partial sync, half-updated frontmatter). Read-only validation should report all issues at once, not fail at the first one (user wants the complete list to triage).

Specifically:
- `sync_distribution.py --apply`: builds the full copy-and-transform plan; validates all source files; if any source file fails validation, abort all writes (no partial sync).
- `validate_frontmatter.py`: reports all files with issues; exit code reflects total count.

### Real-world precedent

- **Database transactions** (BEGIN/COMMIT/ROLLBACK) — strict transactions for writes.
- **`pre-commit`** — best-effort continue for validators.
- **`ansible-playbook`** — strict transactions; rollback on failure.

---

## 9. Sub-decision G — Codex integration (Adeptus Administratum)

Should Adeptus Administratum invoke scripts during re-priming?

### Options

| Option | Behaviour |
|---|---|
| **G1.** No integration; scripts are project-owner tools only | Aide doesn't run scripts; Codex §8 step 5 stays informal |
| **G2.** Aide invokes Tier 1 read-only scripts at re-priming step 5 | `validate_frontmatter.py` and `check_links.py` run; output surfaces as N-3/N-4 notifies |
| **G3.** Aide invokes all read-only scripts always | More thorough but heavier re-priming cost |
| **G4.** Aide can invoke write scripts with explicit project-owner authorization | Aide proposes `sync_distribution.py --apply`; owner approves |

### Proposed answer

**G2 + G4 combined:**

- **G2 (re-priming step 5):** Adeptus Administratum invokes `python scripts/validate_frontmatter.py` and `python scripts/check_links.py` at re-priming step 5. Output is converted into Codex §5 Notify Triggers — frontmatter validation issues become N-4 (term drift / numeric inconsistency equivalent); link-check issues become N-3 (citation misuse equivalent).
- **G4 (write scripts):** Aide may *propose* invoking write scripts (`sync_distribution.py --apply`, `bump_version.py --apply`, etc.) but must receive explicit project-owner authorization before each write. Aide always runs `--dry-run` first, surfaces the plan, asks for approval.

This requires a small amendment to the [Adeptus Administratum Codex](../chapters/adeptus-administratum/codex.md) — specifically §8 re-priming protocol step 5 to reference the scripts, and §3 Hard Stops to clarify that script invocation (read-only) is permitted under §4 Autonomy Threshold while write-script invocation requires acknowledgment (per existing §3 HS-2).

This amendment is *minor* and can be applied via a Codex v1.0 → v1.1 patch, NOT a full Re-consecration debate. The amendment doesn't change the Codex's substantive design; it adds a tooling reference.

### Real-world precedent

- **Linters in CI pipelines** — run automated checks before allowing merge; failure → human investigates.
- **GitHub Actions invoked by CODEOWNERS rules** — automation under human authorization.
- **`gh` CLI invoked by Anthropic Claude Code** — AI invokes the CLI tool; CLI does the work.

---

## 10. Sub-decision H — Release orchestration

How does the release process work end-to-end?

### Proposed `release.py` workflow

```
$ python scripts/release.py 0.7.0 --apply

Step 1/8: validate_frontmatter ... ✓ (28 files passed)
Step 2/8: check_links ... ⚠ (3 dangling links in framework/audit/findings-phase4-2026-05-09.md; these are historical; acknowledged)
Step 3/8: sync_distribution → distribution/ ... ✓ (28 files synced)
Step 4/8: snapshot_case_study lore-weave ... ✓
Step 5/8: bump_version 0.7.0 ... ✓ (VERSION + CHANGELOG.md updated)
Step 6/8: update_handoff_tree ... ✓ (HANDOFF.md tree regenerated)
Step 7/8: git add + commit ... ✓ (commit abc1234 "release: v0.7.0")
Step 8/8: git tag v0.7.0 ... ✓

Release v0.7.0 complete. Push manually with: git push origin main --tags
```

### Proposed answer

**Adopt the 8-step release pipeline above.** Each step is a self-contained script; release.py orchestrates them. Push remains manual (never push on behalf of project owner without explicit per-push authorization per Adeptus Administratum Codex §3 HS-5).

### Real-world precedent

- **`semantic-release`** — fully automated release pipeline for npm.
- **`cargo release`** — Rust's release tool; very similar 6-step flow.
- **`bumpversion`** — version bumping + changelog; partial overlap with bump_version.py.

---

## 11. Sub-decision I — Adopter use vs maintainer use

What subset of scripts ships in `distribution/scripts/`?

### Proposed split

| Script | Maintainer-only (scripts/) | Adopter-usable (distribution/scripts/) | Reason |
|---|---|---|---|
| `sync_distribution.py` | ✓ | — | Framework-internal; adopter has no upstream sync |
| `validate_frontmatter.py` | ✓ | ✓ | Adopters validate their own customizations |
| `check_links.py` | ✓ | ✓ | Adopters check their own project consistency |
| `snapshot_case_study.py` | ✓ | ✓ | Adopters snapshot their own case studies |
| `bump_version.py` | ✓ | — | Versioning is framework's concern |
| `update_handoff_tree.py` | ✓ | — | HANDOFF.md is framework's |
| `release.py` | ✓ | — | Framework release process |
| `new_debate.py` | ✓ | — | Debates are framework concept; adopters typically don't create debates |
| `new_chapter_codex.py` | ✓ | — | Same |
| `new_case_study.py` | ✓ | ✓ | Adopters might create new case studies from this scaffold |
| `frontmatter_set.py` | ✓ | ✓ | Generally useful |
| `ivp_phase5.py` | ✓ | — | IVP is framework's QA; adopters out-of-scope per debate 006 §11 |

### Proposed answer

The split above. Adopter-usable subset is the read-only / generally-useful scripts plus the scaffolding tools that an adopter might want for their own project.

These adopter-usable scripts are copied into `distribution/scripts/` during `sync_distribution.py` and shipped with the distribution at each release.

---

## 12. Real-world precedent — consolidated standards map

| Sub-decision | Industry standards informing the design |
|---|---|
| A. Script inventory | Hugo / MkDocs / Jekyll build tooling; `cookiecutter`; `semantic-release`; `vale` |
| B. Library choices | Jekyll Ruby gems analogues in Python; mkdocs-material toolchain; Anthropic SDK examples |
| C. Placement (`scripts/` + `distribution/scripts/`) | Rails `bin/`; Django `manage.py`; npm / yarn `scripts` in package.json; Hugo split CLI/templates |
| D. Trigger model | Manual via `mkdocs serve`; pre-commit framework; GitHub Actions standard; `vale` editor integration |
| E. Validation strictness (dry-run + apply) | `terraform plan/apply`; `git diff/apply`; `rsync --dry-run`; `pip install --dry-run` |
| F. Error handling (strict transactions on write; best-effort on read) | Database BEGIN/COMMIT/ROLLBACK; `ansible-playbook`; `pre-commit` |
| G. Codex integration | Linters in CI; GitHub Actions under CODEOWNERS authorization; AI agents invoking CLIs |
| H. Release orchestration | `semantic-release`; `cargo release`; `bumpversion` |
| I. Adopter vs maintainer scripts | Rails generators vs deployer scripts; Django startproject vs management commands |

---

## 13. Application to Dead Light Framework (sketch)

If debate 007 seals as proposed, the implementation plan:

### Implementation Phase 1 — Tier 1 scripts (highest token-cost-saving)

1. Create `scripts/` directory at repo root.
2. Create `scripts/requirements.txt` with `python-frontmatter`, `typer`, `markdown-it-py`.
3. Implement `scripts/sync_distribution.py` (the heaviest token-saver).
4. Implement `scripts/validate_frontmatter.py`.
5. Implement `scripts/check_links.py`.
6. Test all three against current repo state (should validate cleanly post-debate-006 migration).
7. Commit as `scripts: Tier 1 implementation per debate 007`.

### Implementation Phase 2 — Tier 2 scripts

8. Implement `scripts/snapshot_case_study.py`.
9. Implement `scripts/bump_version.py`.
10. Implement `scripts/update_handoff_tree.py`.
11. Implement `scripts/frontmatter_set.py`.
12. Commit as `scripts: Tier 2 implementation per debate 007`.

### Implementation Phase 3 — Codex amendment + adopter subset

13. Amend Adeptus Administratum Codex v1.0 → v1.1 to reference scripts at §8 step 5 and §3 (script invocation under §4 Autonomy Threshold rules). Minor patch; no full Re-consecration debate needed.
14. Implement `scripts/release.py` orchestrator.
15. Implement adopter-usable subset under `distribution/scripts/` (copies of validate_frontmatter, check_links, snapshot_case_study, new_case_study, frontmatter_set).
16. Update `distribution/INDEX.md` to reference adopter scripts.
17. Commit as `scripts: Phase 3 — Codex amendment + adopter-usable subset`.

### Implementation Phase 4 — Tier 3 (optional / deferred)

18. `new_debate.py`, `new_chapter_codex.py`, `new_case_study.py`, `ivp_phase5.py` — implement only when need surfaces.

### Estimated effort

- Phase 1: ~3–5 person-hours (3 scripts, each ~100-200 lines Python).
- Phase 2: ~2–4 person-hours.
- Phase 3: ~1–2 person-hours.
- Phase 4: deferred.
- **Total: ~6–11 person-hours** initial implementation. Token cost: most of this is structured code-writing, lower token-cost per line than the manual mechanical migration tokens it replaces.

After Phase 1, every subsequent migration / release / case-study snapshot saves ~10K+ tokens per operation.

---

## 14. Open questions (carry forward)

1. **Test infrastructure.** Should scripts have unit tests (pytest)? Or rely on integration testing via actual runs?  My recommendation: integration testing first (run the script against the actual repo state); add pytest unit tests if regressions surface. Defer to first observed regression.

2. **Cross-platform testing.** Repo's primary workstation is Windows; alternate is presumably Linux/macOS. Scripts written in Python should work on all three but need verification. Defer until adopters report platform issues.

3. **Versioning of the scripts themselves.** Scripts evolve. Do they have their own version? Or move in lockstep with framework? Defer; treat as monorepo (scripts move with framework).

4. **Python version pinning.** Recommendation: Python 3.10+ (stable, type hints, dataclasses). Strict pinning? Recommend "≥ 3.10"; full pinning only if dependency breaks.

5. **Static site generation.** Should we eventually use MkDocs Material or Docusaurus on top of `distribution/`? Out of scope for this debate; if pursued, would be a debate 008 on "Published documentation site."

6. **Adeptus Administratum Codex amendment procedure.** This debate proposes a v1.0 → v1.1 minor patch for the script-invocation references. Is this allowed, or does it require full Re-consecration debate? Codex §10 says "Until that procedure is formalized, amendments to this Codex require a new debate (debate 006 onward) with the same level of rigor as debate 005." Strict reading: debate 008 needed for the Codex amendment. Pragmatic reading: this debate (007) includes the amendment as a follow-up; rigor preserved because the amendment is sub-decision G of THIS debate. Need project-owner decision on which reading applies.

---

## 15. Recommendation (TL;DR)

| Sub-decision | Recommended |
|---|---|
| A. Script inventory | **Tier 1 first** (sync_distribution + validate_frontmatter + check_links). Tier 2 as need surfaces. Tier 3 deferred. |
| B. Library choices | **`python-frontmatter` + `typer` + `markdown-it-py`** as `requirements.txt`. Python ≥ 3.10. |
| C. Repository placement | **C3 hybrid** — `scripts/` at root for maintainer scripts; `distribution/scripts/` for adopter-usable subset (copies of validate / check / snapshot / new-case-study / frontmatter_set). |
| D. Trigger model | **Manual + Adeptus Administratum invocation** at re-priming step 5. Pre-commit hooks + GitHub Actions deferred to first second-contributor / public-repo trigger. |
| E. Validation strictness | **E3 + E4** — severity-graded fail (default exit-1 at HIGH); dry-run by default for write scripts, `--apply` required. |
| F. Error handling | **Strict transactions on write** (full-plan-then-write); **best-effort continue on read** (report all issues). |
| G. Codex integration | **G2 + G4** — aide invokes Tier 1 read-only scripts at re-priming step 5 (output → N-3/N-4 notifies); aide may propose write-script invocation but requires project-owner authorization. Minor Codex amendment v1.0 → v1.1 required (deferred to debate 008 for full rigor, OR included as follow-up of this debate — see open question §14 #6). |
| H. Release orchestration | **8-step `release.py` pipeline** (validate → check-links → sync-dist → snapshot → bump-version → update-handoff → git commit → git tag). Push remains manual. |
| I. Adopter vs maintainer | **Read-only + generally-useful scripts** copied to `distribution/scripts/` at release; framework-internal scripts (sync_distribution, release, bump_version, new_debate, new_chapter, ivp_phase5) stay in `scripts/` only. |

If approved, the next mechanical migration (e.g., when Phase 1 seals upstream and v0.7.0 release happens) will cost a single script invocation rather than ~50–100K LLM tokens of manual work.

---

## 16. Decision

_(Empty — to be filled when project owner decides.)_

- **Decision:** _(pending)_
- **Decided on:** _(pending)_
- **Decided by:** _(pending)_

### Follow-up actions (will be checked on seal)

- [ ] Create `scripts/` directory at repo root with `requirements.txt` and a `README.md` explaining the scripts.
- [ ] Implement `scripts/sync_distribution.py`, `scripts/validate_frontmatter.py`, `scripts/check_links.py` (Tier 1).
- [ ] Test Tier 1 scripts against current repo state.
- [ ] Implement Tier 2 scripts: `snapshot_case_study.py`, `bump_version.py`, `update_handoff_tree.py`, `frontmatter_set.py`.
- [ ] Decide open question §14 #6 (Codex amendment via debate 008 vs follow-up of this debate); if follow-up, amend [Adeptus Administratum Codex](../chapters/adeptus-administratum/codex.md) v1.0 → v1.1 with script-invocation references at §8 step 5 and §4 Autonomy Threshold.
- [ ] Implement `scripts/release.py` orchestrator.
- [ ] Populate adopter-usable subset under `distribution/scripts/`.
- [ ] Update [debates/README.md](README.md) — debate 007 marked decided.
- [ ] Update HANDOFF.md status table (add "Scripting infrastructure" row).
- [ ] Update Adeptus Administratum Codex §8 step 5 / §4 with concrete script references (post-amendment decision).

---

## 17. Methodological note (forward-applying)

This debate is the **first time the framework explicitly authorises automation infrastructure that operates on its own artifacts**. Before debate 007, all artifact manipulation was either (a) the project owner manually editing, (b) an AI-aide manually editing via tool calls. After debate 007, mechanical work moves to scripts; AI-aide focuses on governance reasoning.

Three insights worth recording:

1. **The framework's layered design now has four layers:**
   - Project governance (Phases 0/1 — debates 001-004).
   - Operational aide (Adeptus Administratum Codex — debate 005).
   - Document architecture (debate 006).
   - **Tooling infrastructure** — debate 007 (this debate).

   Each layer is "fractal" of the frozen-authority thesis: scripts encode the framework's mechanics; the mechanics survive any particular AI-aide invocation; the artifacts produced are reproducible across runs.

2. **Token-cost discipline.** This is the first debate that explicitly considers LLM token-cost as a design driver. Industry standards typically optimise for human time + correctness; the framework adds AI-token-cost as a third axis. As LLM-mediated work becomes more common, this axis may become a generic methodological concern beyond Dead Light.

3. **AI-aide as orchestrator + scripts as workers.** The pattern this debate establishes (AI invokes scripts; scripts do the work; AI interprets the script output) is the operational realization of the framework's thesis at the tooling layer. The AI-aide is not less valuable for not doing the mechanical work; it is more valuable for doing only the governance work. This pattern likely generalises beyond Dead Light to any framework where AI agents are governance participants.

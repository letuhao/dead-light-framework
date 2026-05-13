---
title: "Scripts — Dead Light Framework tooling"
status: working
version: 0.1.0
audience: human
type: readme
last_updated: 2026-05-13
supersedes: null
sealed_by: debate-007
---

> **Status:** Tier 1 implemented (sync_distribution, validate_frontmatter, check_links). Tier 2 + 3 deferred.
> **Audience:** Framework maintainers + Adeptus Administratum instances during re-priming (informal until debate 008 seals Codex v1.1).
> **Purpose:** Python tooling that handles mechanical repository work — frontmatter validation, link checking, framework/ → distribution/ sync. Reduces LLM token cost on mechanical operations by ~99%.
> **Read next if:** you're about to do migration / release / consistency-check work, or you're an Adeptus Administratum instance starting a task.

# Scripts — Dead Light Framework tooling

Authorised by [debate 007](../framework/debates/007-scripting-infrastructure.md).

## Install

```bash
pip install -r scripts/requirements.txt
```

Python ≥ 3.10 required.

## Tier 1 scripts (implemented)

### `validate_frontmatter.py`

Walk all `*.md` files; check each has required YAML frontmatter (title, status, audience, type, last_updated); report missing or invalid fields.

```bash
python scripts/validate_frontmatter.py              # warn-only (default)
python scripts/validate_frontmatter.py --strict     # exit 1 on any HIGH-severity issue
python scripts/validate_frontmatter.py --path framework/   # scope to one subtree
```

### `check_links.py`

Walk all `*.md` files; parse markdown links; verify every internal link resolves; report dangling.

```bash
python scripts/check_links.py                       # warn-only (default)
python scripts/check_links.py --strict              # exit 1 on any dangling
python scripts/check_links.py --path framework/
```

### `sync_distribution.py`

Walk `framework/`; filter files with `status: sealed` or `status: decided`; copy to `distribution/framework/`; drop `-for-debate` suffix on sealed files; regenerate `distribution/INDEX.md`. **Dry-run by default**; pass `--apply` to write.

```bash
python scripts/sync_distribution.py                 # dry-run (default)
python scripts/sync_distribution.py --apply         # write changes
```

## Conventions (per debate 007)

- **Read-only scripts**: warn-only by default; `--strict` for fail-on-error.
- **Write scripts**: dry-run by default; `--apply` required to commit changes (matches `terraform plan`/`apply` and `rsync --dry-run` patterns).
- **Severity**: read-only scripts grade findings by IVP severity rubric (CRITICAL / HIGH / MEDIUM / LOW); default exit-1 threshold is HIGH.
- **Error handling**: write scripts use strict transactions (build full plan, validate, then write all-or-nothing). Read-only scripts use best-effort continue (report all issues, exit reflects overall count).
- **No backflow**: scripts operate one-way from `framework/` → `distribution/`. Per debate 006 §H and debate 006 §11 (I0), the framework does not police adopter customizations.

## Tier 2 scripts (deferred to subsequent commits)

- `snapshot_case_study.py <name>` — snapshot a case study to `distribution/examples/<name>-snapshot/`.
- `bump_version.py <major|minor|patch>` — update `distribution/VERSION` + prepend to `distribution/CHANGELOG.md`.
- `update_handoff_tree.py` — regenerate `HANDOFF.md` document tree from current filesystem.
- `frontmatter_set.py <file> <field>=<value>` — atomically update one frontmatter field.

## Tier 3 scripts (deferred indefinitely)

Per debate 007 §3: build on need.

- `release.py <version>` — orchestrate full release pipeline.
- `new_debate.py <slug>` — scaffold new debate.
- `new_chapter_codex.py <name>` — scaffold new Chapter Codex.
- `new_case_study.py <project>` — scaffold new case study.
- `ivp_phase5.py` — automated Phase 5 (Internal Consistency) check.

## Adeptus Administratum integration

Per debate 007 §G + open question §14 #6: **deferred to debate 008** for the formal Codex v1.0 → v1.1 amendment. Until then, scripts may be invoked informally by Adeptus Administratum instances (as project-owner-authorized one-off task work) but the Codex §8 step 5 re-priming protocol does not yet formally reference them.

Adopter-usable subset (`distribution/scripts/`) populates once debate 008 seals.

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

> **Status:** Tier 1 + Tier 2 implemented (validate_frontmatter, check_links, sync_distribution, frontmatter_set, bump_version, snapshot_case_study, update_handoff_tree). Tier 3 deferred.
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

## Tier 2 scripts (implemented)

### `frontmatter_set.py`

Atomically update one frontmatter field in one file. Validates enum values for status/audience/type. Dry-run default.

```bash
python scripts/frontmatter_set.py framework/debates/008-foo.md status=decided --apply
python scripts/frontmatter_set.py file.md supersedes=null --apply
```

### `bump_version.py`

Bump distribution version per SemVer (debate 006 sub-decision C). Updates `distribution/VERSION` + prepends new section to `distribution/CHANGELOG.md`. Dry-run default.

```bash
python scripts/bump_version.py minor                            # 0.6.0 -> 0.7.0 (dry-run)
python scripts/bump_version.py patch --apply                    # write
python scripts/bump_version.py minor --apply \
  --description "Phase 1 fully sealed; lore-weave Pass 1 complete"
```

### `snapshot_case_study.py`

Copy a case-study folder to `distribution/examples/<name>-snapshot/`, injecting `snapshot_of` + `snapshot_date` frontmatter and path-rewriting `phase-0-for-debate.md` → `phase-0.md`. Dry-run default.

```bash
python scripts/snapshot_case_study.py lore-weave --apply
```

### `update_handoff_tree.py`

Regenerate the `## Document tree` section of `HANDOFF.md` from current filesystem state. Auto-annotates each file with `[SEALED]` / `[DECIDED]` / `[working]` etc. from frontmatter. Dry-run default.

Requires `<!-- DOC-TREE-START -->` and `<!-- DOC-TREE-END -->` markers around the tree block in `HANDOFF.md`. Markers exist after debate-007 sealing.

```bash
python scripts/update_handoff_tree.py --apply
```

**Caveat:** the original tree includes human-written annotation comments (`← ...`). These are stripped on regeneration. If you want them, re-edit manually after regeneration or extend the script's annotation feature.

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

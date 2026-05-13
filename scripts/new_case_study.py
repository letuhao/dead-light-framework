#!/usr/bin/env python3
"""
new_case_study.py — Dead Light Framework Tier 3 script.

Scaffold a new case-study folder under case-studies/<project>/ with the
five standard files (README, pm-threshold-decisions, reckoning-team-record,
reckoning-record, methodology-notes), copying from distribution/templates/
where applicable.

Usage:
    python scripts/new_case_study.py "lore-weave"           # dry-run
    python scripts/new_case_study.py "lore-weave" --apply   # write

Authorised by debate 007.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help=__doc__)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


# Files to scaffold (target name -> source template path | None if hand-written)
SCAFFOLD = {
    "pm-threshold-decisions.md": "distribution/templates/pm-threshold-decisions-template.md",
    "reckoning-team-record.md": "distribution/templates/reckoning-team-record-template.md",
    "reckoning-record.md": "distribution/templates/reckoning-record-template.md",
}


def render_readme(project: str, project_human: str) -> str:
    today = __import__("datetime").date.today().isoformat()
    return f"""---
title: "Case Study — {project_human}"
status: working
version: not versioned
audience: human
type: case-study
last_updated: {today}
supersedes: null
sealed_by: null
---

# Case Study — {project_human}

> **Status:** Phase 0 starting (skeleton drafted {today}).
> **Audience:** Project Council + Reckoning Team + Adeptus Administratum instance(s) operating on this project.
> **Purpose:** Apply Dead Light Framework to {project_human} as a real test case.
> **Read next if:** you're starting Phase 0 against this project.

## Why this case study exists

_(Project background. Why this case is interesting. What it tests about the framework.)_

## Scope of audit

_(Per PM Threshold Decisions §3 — which services / repos / modules are in scope, which are out, multi-pass strategy if any.)_

## Focus areas

_(What the case study is specifically trying to surface — scope changes, architect rot, Sector trigger evaluation, implicit principles, etc.)_

## Status

| Section | Status | Date |
|---|---|---|
| Folder skeleton + scope | Drafted | {today} |
| PM Threshold Decisions | Pending project-owner input | — |
| Reckoning Team Record | Pending project-owner input | — |
| Reckoning Record | Not started | — |
| Methodology notes | Accumulating | {today} |

## Folder layout

```
case-studies/{project}/
├── README.md                       ← this file
├── pm-threshold-decisions.md       ← 5 PM commitments per Phase 0 §2 inputs
├── reckoning-team-record.md        ← team composition + AI-aide invocations
├── reckoning-record.md             ← 4-section inventory (5th added by Phase 1)
└── methodology-notes.md            ← spec departures + retroactive review
```
"""


def render_methodology_notes(project: str, project_human: str) -> str:
    today = __import__("datetime").date.today().isoformat()
    return f"""---
title: "Methodology Notes — {project_human} Case Study"
status: working
version: not versioned
audience: human
type: case-study
last_updated: {today}
supersedes: null
sealed_by: null
---

# Methodology Notes — {project_human}

> **Status:** Accumulating during Phase 0 onward.
> **Audience:** Framework refinement loop + future re-reckoning of this project.
> **Purpose:** Record how the framework was applied in practice, what diverged from spec, what was lossy, what was novel.

## 1. Reviewer profile

- _Single human reviewer (project owner) acts as ..._
- _AI-aide-N (Adeptus Administratum instance — Codex v1.0) serves as ..._

## 2. Departures from Phase 0 spec

_(Add D-N entries here as spec departures arise. Each departure includes: spec text, departure, risk recorded, mitigation, reversibility, rationale.)_

### D-1 — _(name of departure)_

**Spec text:** _quote relevant Phase 0 §X._

**Departure:** _what's different._

**Risk recorded:** _what could go wrong._

**Mitigation:** _how the risk is managed._

**Reversibility:** _reversible / not._

**Why this departure was chosen:** _project owner's rationale._

## 3. Observations on framework-versus-reality

_(Accumulates as Phase 0 runs.)_

## 4. Carry-forward to framework refinement

| # | Observation | Recommended next-cycle action | Priority |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | _to fill_ |

## 5. Carry-forward to project's Phase 1

| # | Item | Recommended Phase 1 disposition | Reasoning |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | _to fill_ |

## 6. Audit trail

| Date | Action | Source / target | Output |
|---|---|---|---|
| {today} | Created case-study folder skeleton | `case-studies/{project}/` | this commit |
"""


@app.command()
def main(
    project: str = typer.Argument(
        ..., help="Case-study project name in kebab-case (e.g., 'lore-weave')."
    ),
    title: str = typer.Option(
        None, "--title", help="Human-readable title (default: derived from project name)."
    ),
    apply: bool = typer.Option(False, "--apply", help="Write the new files (default: dry-run)."),
) -> None:
    """Scaffold a new case-study folder."""
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", project):
        typer.echo(f"error: project must be kebab-case, got: {project}", err=True)
        raise typer.Exit(2)

    project_human = title or project.replace("-", " ").title()
    target_dir = repo_root() / "case-studies" / project

    if target_dir.exists():
        typer.echo(f"error: {target_dir} already exists; pick a different project name", err=True)
        raise typer.Exit(2)

    typer.echo(f"Project:        {project}")
    typer.echo(f"Title:          {project_human}")
    typer.echo(f"Target folder:  {target_dir.relative_to(repo_root())}")
    typer.echo("")
    typer.echo("Files to create:")
    typer.echo("  - README.md (hand-written from template)")
    typer.echo("  - methodology-notes.md (hand-written from template)")
    for target_name, template_path in SCAFFOLD.items():
        typer.echo(f"  - {target_name} (copy from {template_path})")
    typer.echo("")

    if not apply:
        typer.echo("(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    target_dir.mkdir(parents=True)

    # README + methodology-notes — hand-written
    (target_dir / "README.md").write_text(render_readme(project, project_human), encoding="utf-8")
    typer.echo(f"  ✓ wrote {target_dir.relative_to(repo_root())}/README.md")

    (target_dir / "methodology-notes.md").write_text(
        render_methodology_notes(project, project_human), encoding="utf-8"
    )
    typer.echo(f"  ✓ wrote {target_dir.relative_to(repo_root())}/methodology-notes.md")

    # Copy templates
    for target_name, template_path in SCAFFOLD.items():
        src = repo_root() / template_path
        dst = target_dir / target_name
        if not src.exists():
            typer.echo(f"  ! template missing: {template_path}; skipping {target_name}", err=True)
            continue
        shutil.copy2(src, dst)
        typer.echo(f"  ✓ copied {template_path} -> {dst.relative_to(repo_root())}")

    typer.echo("")
    typer.echo(
        f"Next: edit case-studies/{project}/README.md to fill in project background,\n"
        f"      fill in pm-threshold-decisions.md with project-specific thresholds,\n"
        f"      then start Phase 0 inventory."
    )
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

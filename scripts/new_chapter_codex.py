#!/usr/bin/env python3
"""
new_chapter_codex.py — Dead Light Framework Tier 3 script.

Scaffold a new Chapter Codex under framework/chapters/<name>/codex.md
with the 10-section template established by debate 005 §4.

Usage:
    python scripts/new_chapter_codex.py "codex-reviewer"          # dry-run
    python scripts/new_chapter_codex.py "codex-reviewer" --apply  # write

The created file starts at status: draft. Project owner refines the
operational bounds + hard stops + notify triggers etc. via a debate
(typically debate NNN where N is a future debate number) and seals
status: draft -> status: sealed when ready.

Authorised by debate 007.
"""
from __future__ import annotations

import re
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help=__doc__)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def render_codex(name: str, name_human: str) -> str:
    today = __import__("datetime").date.today().isoformat()
    return f"""---
title: "Codex — {name_human}"
status: draft
version: 0.1.0
audience: both
type: codex
last_updated: {today}
supersedes: null
sealed_by: null
---

# Codex — {name_human}

> **Status:** Draft.
> **Version:** 0.1.0
> **Sealed via:** _(pending debate)_
> **Sealed on:** —
> **Sealed by:** —
> **Phase coverage:** _(All / Pre-seal only / Post-seal only / Phase-specific N)_.
> **Multiplicity:** _(per Astronomican? per Sector? singleton per project?)_
> **Affects:** _(which Astronomicans / which other Codices)_

---

## 1. Identity and scope

_(Who this Chapter is, what role it serves, where in the project workflow it appears. Reference real-world roles whose practice it borrows from per policy 1.)_

---

## 2. Operational Bounds

_(Phase-specific subsections per debate 006 §J + debate 005 §6 lifecycle D4. Each task instance picks the relevant subsection during re-priming step 4.)_

### 2.1 During _(Phase N)_ tasks

The Chapter MAY:

- _Permission 1._
- _Permission 2._

### 2.2 During _(Phase M)_ tasks

The Chapter MAY:

- _Permission._

---

## 3. Hard Stops

The Chapter MUST NOT:

| # | Condition | Required action |
|---|---|---|
| HS-1 | _condition_ | _action_ |
| HS-2 | _condition_ | _action_ |

(Policy 1 + policy 2 hard stops mandatory — see Adeptus Administratum Codex §3 HS-8 / HS-9 as reference.)

---

## 4. Autonomy Threshold

The Chapter may act **solo** when the action is:

- _Read-only patterns._
- _Draft-only patterns._

The Chapter MUST wait for acknowledgment when:

- _Producing final artifacts._
- _Modifying sealed artifacts._

---

## 5. Notify Triggers

| # | Condition | Class | Channel | Response window |
|---|---|---|---|---|
| N-1 | _condition_ | Blocking / Non-blocking | _channel_ | _window_ |

(Reference Adeptus Administratum Codex §5 for the N-1..N-5 pattern as a starting point.)

---

## 6. Output Contract (Tithe)

Every artifact this Chapter produces must:

1. _Status marking._
2. _Provenance line._
3. _Git commit._
4. _Audit-trail update._
5. _Readability for project owner._
6. _Re-prime-friendliness._

---

## 7. Authority bounds

- The Chapter does NOT vote.
- The Chapter does NOT sign.
- The Chapter does NOT block.
- _(Other authority bounds specific to this Chapter.)_

Project owner / Council reserves all binding authority.

---

## 8. Lifecycle

_(Reference debate 005 sub-decision D options D1..D4. D4 (task-scoped instance + persistent role + artifact continuity) is the established pattern for the first Chapter; this Chapter SHOULD follow D4 unless there's a specific reason to differ.)_

### Re-priming protocol

_(7-step protocol per debate 005 §6 if D4 is adopted.)_

---

## 9. Real-world precedent (policy 1 compliance)

_(Borrowing-from-real-world-roles table. Names the 40k metaphor + the real-world roles whose practice grounds the design. Per framework policy 1, the 40k name is naming-only; real-world roles govern the design.)_

| Real-world role | Borrowed property | How it manifests in this Codex |
|---|---|---|
| _role_ | _property_ | _Codex section reference_ |

---

## 10. Provenance and version

- **Version:** 0.1.0 (draft)
- **Sealed via:** _(pending debate)_
- **Sealed on:** —
- **Sealed by:** —
- **Previous versions:** none.
- **Supersession history:** none.
- **Amendment procedure:** via Re-consecration (per debate 005 §10 + open question #3 — formal Codex Re-consecration procedure pending).
"""


@app.command()
def main(
    name: str = typer.Argument(
        ...,
        help="Chapter name in kebab-case (e.g., 'codex-reviewer', 'drift-detector'). 40k-flavoured names per framework policy 1 + debate 005 sub-decision A.",
    ),
    title: str = typer.Option(
        None,
        "--title",
        help="Human-readable title (default: name with - replaced by spaces and Title-Cased).",
    ),
    apply: bool = typer.Option(False, "--apply", help="Write the new Codex file (default: dry-run)."),
) -> None:
    """Scaffold a new Chapter Codex with the 10-section template."""
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        typer.echo(
            f"error: name must be kebab-case (lowercase letters, digits, hyphens), got: {name}",
            err=True,
        )
        raise typer.Exit(2)

    title_human = title or name.replace("-", " ").title()
    target = repo_root() / "framework" / "chapters" / name / "codex.md"

    if target.exists():
        typer.echo(f"error: {target} already exists; pick a different name", err=True)
        raise typer.Exit(2)

    typer.echo(f"Chapter name:    {name}")
    typer.echo(f"Title (human):   {title_human}")
    typer.echo(f"Target file:     {target.relative_to(repo_root())}")
    typer.echo("")

    content = render_codex(name, title_human)

    if not apply:
        typer.echo(f"[DRY-RUN] Would write {len(content)} bytes to {target.relative_to(repo_root())}")
        typer.echo("\n(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    typer.echo(f"  ✓ wrote {target.relative_to(repo_root())} ({len(content)} bytes)")

    typer.echo("")
    typer.echo(
        f"Next: open {target.relative_to(repo_root())} and fill in the Codex sections.\n"
        f"      Then open a debate to formally seal status: draft -> status: sealed."
    )
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

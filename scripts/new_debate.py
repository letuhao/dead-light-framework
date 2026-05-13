#!/usr/bin/env python3
"""
new_debate.py — Dead Light Framework Tier 3 script.

Scaffold a new debate file under framework/debates/NNN-<slug>.md with frontmatter
template + standard sections (Context, Pre-decided constraints, Sub-decisions
A..N, Real-world precedent table, Application sketch, Open questions,
Recommendation TL;DR, Decision empty, Follow-up actions, Methodological note).

Auto-detects the next debate number from existing files in framework/debates/.

Usage:
    python scripts/new_debate.py "codex-v1-1-script-integration"          # dry-run
    python scripts/new_debate.py "codex-v1-1-script-integration" --apply  # write

The created file is at framework/debates/<NNN>-<slug>.md and is opened in
draft status. Project owner fills in the body, refines through dialogue,
seals by flipping `status: open` -> `status: decided`.

Authorised by debate 007.
"""
from __future__ import annotations

import re
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help=__doc__)


DEBATE_FILE_RE = re.compile(r"(\d{3})-")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def next_debate_number() -> int:
    debates_dir = repo_root() / "framework" / "debates"
    if not debates_dir.exists():
        return 1
    max_n = 0
    for f in debates_dir.iterdir():
        m = DEBATE_FILE_RE.match(f.name)
        if m:
            max_n = max(max_n, int(m.group(1)))
    return max_n + 1


def render_debate(number: int, slug: str, title_human: str) -> str:
    """Render the debate template body. Caller fills it in afterwards."""
    nnn = f"{number:03d}"
    today = __import__("datetime").date.today().isoformat()
    return f"""---
title: "Debate {nnn} — {title_human}"
status: open
version: not versioned
audience: both
type: debate
last_updated: {today}
supersedes: null
sealed_by: null
---

# Debate {nnn} — {title_human}

> **Status:** open.
> **Opened:** {today}
> **Decided:** —
> **Decided by:** project owner (pending)
> **Affects:** _(fill in: which framework artifacts this debate's decision will change)_
> **Raised by:** _(fill in: project owner observation / IVP finding / etc.)_

---

## 1. Context

_(Why this debate exists. What observations or operational facts force it. Reference prior debates / Phases / IVP findings if applicable.)_

---

## 2. Pre-decided constraints (if any)

_(Sub-decisions the project owner committed at debate open. Removes those questions from the debate's analytical scope.)_

| Pre-decision | Decision | Rationale |
|---|---|---|
| _name_ | _decision_ | _rationale_ |

---

## 3. Sub-decision A — _topic_

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **A1.** _option_ | _mechanism_ | _pros_ | _cons_ |
| **A2.** _option_ | _mechanism_ | _pros_ | _cons_ |

### Recommended answer

_(Recommendation + justification.)_

### Real-world precedent

- _Precedent 1_
- _Precedent 2_

---

## 4. Sub-decision B — _topic_

_(Repeat the structure above for each sub-decision.)_

---

## N. Real-world precedent — consolidated standards map

| Sub-decision | Industry standards informing the design |
|---|---|
| A | _standards_ |
| B | _standards_ |

---

## N+1. Application to Dead Light Framework (sketch)

_(Concrete implementation plan if the debate seals as proposed. Estimated effort.)_

---

## N+2. Open questions remaining (carry forward if accepted)

1. _Question_

---

## N+3. Recommendation (TL;DR)

| Sub-decision | Recommended |
|---|---|
| A | _summary_ |
| B | _summary_ |

---

## N+4. Decision

_(Empty — to be filled when project owner decides.)_

- **Decision:** _(pending)_
- **Decided on:** _(pending)_
- **Decided by:** _(pending)_

### Follow-up actions (will be checked on seal)

- [ ] _Action_
- [ ] Update [debates/README.md](README.md) — this debate marked decided.
- [ ] _Other follow-up_

---

## N+5. Methodological note (forward-applying)

_(Insights worth recording for the framework's evolution. Optional but encouraged for substantive debates.)_
"""


def update_index(number: int, slug: str, title_human: str, apply: bool) -> None:
    """Add a row to framework/debates/README.md index table."""
    readme = repo_root() / "framework" / "debates" / "README.md"
    if not readme.exists():
        typer.echo(f"warning: {readme} does not exist; skipping index update", err=True)
        return

    nnn = f"{number:03d}"
    today = __import__("datetime").date.today().isoformat()
    row = f"| [{nnn}]({nnn}-{slug}.md) | {title_human} | open | {today} | — |\n"

    text = readme.read_text(encoding="utf-8")
    if f"| [{nnn}]" in text:
        typer.echo(f"warning: debate {nnn} already in index; not appending", err=True)
        return

    # Append row at end of file
    new_text = text.rstrip() + "\n" + row

    if apply:
        readme.write_text(new_text, encoding="utf-8")
        typer.echo(f"  ✓ updated {readme.relative_to(repo_root())}")
    else:
        typer.echo(f"  [DRY-RUN] would append to {readme.relative_to(repo_root())}: {row.strip()}")


@app.command()
def main(
    slug: str = typer.Argument(
        ..., help="Debate slug (e.g., 'codex-v1-1-script-integration'). Used in filename + title."
    ),
    title: str = typer.Option(
        None,
        "--title",
        help="Human-readable title for the debate (default: derived from slug by replacing - with spaces and Title-Casing).",
    ),
    apply: bool = typer.Option(False, "--apply", help="Write the new debate file (default: dry-run)."),
) -> None:
    """Scaffold a new debate file under framework/debates/."""
    # Validate slug
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        typer.echo(
            f"error: slug must be kebab-case (lowercase letters, digits, hyphens), got: {slug}",
            err=True,
        )
        raise typer.Exit(2)

    number = next_debate_number()
    nnn = f"{number:03d}"
    title_human = title or slug.replace("-", " ").title()

    target = repo_root() / "framework" / "debates" / f"{nnn}-{slug}.md"
    if target.exists():
        typer.echo(f"error: {target} already exists; pick a different slug", err=True)
        raise typer.Exit(2)

    typer.echo(f"Next debate number: {nnn}")
    typer.echo(f"Slug:               {slug}")
    typer.echo(f"Title (human):      {title_human}")
    typer.echo(f"Target file:        {target.relative_to(repo_root())}")
    typer.echo("")

    content = render_debate(number, slug, title_human)

    if not apply:
        typer.echo(f"[DRY-RUN] Would write {len(content)} bytes to {target.relative_to(repo_root())}")
        typer.echo(f"[DRY-RUN] Would update framework/debates/README.md index")
        typer.echo("\n(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    typer.echo(f"  ✓ wrote {target.relative_to(repo_root())} ({len(content)} bytes)")
    update_index(number, slug, title_human, apply=True)

    typer.echo("")
    typer.echo(f"Next: open {target.relative_to(repo_root())} and fill in the body.")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

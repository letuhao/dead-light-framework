#!/usr/bin/env python3
"""
snapshot_case_study.py — Dead Light Framework Tier 2 script.

Copy a case-study folder to `distribution/examples/<name>-snapshot/`, injecting
`snapshot_of` and `snapshot_date` frontmatter fields. Used at each release
to capture the current case-study state as a read-only example for adopters.

Usage:
    python scripts/snapshot_case_study.py lore-weave           # dry-run
    python scripts/snapshot_case_study.py lore-weave --apply   # write

Sources: case-studies/<name>/*.md
Dest:    distribution/examples/<name>-snapshot/*.md

Frontmatter additions (per Phase 2c migration pattern):
    snapshot_of: case-studies/<name>/ (upstream working copy)
    snapshot_date: <today's ISO date>

Path adjustments inside snapshot files:
    framework/phases/phase-0-for-debate.md → framework/phases/phase-0.md
    (Other refs preserved; cross-folder refs remain as-is per debate 006
    known-limitations for v0.6.0.)

Authorised by debate 007.
"""
from __future__ import annotations

import shutil
from datetime import date
from pathlib import Path

import frontmatter
import typer

app = typer.Typer(add_completion=False, help=__doc__)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


@app.command()
def main(
    name: str = typer.Argument(..., help="Case study folder name (e.g., 'lore-weave')."),
    apply: bool = typer.Option(False, "--apply", help="Write changes (default: dry-run)."),
) -> None:
    """Snapshot a case-study folder into distribution/examples/<name>-snapshot/."""
    root = repo_root()
    source = root / "case-studies" / name
    dest = root / "distribution" / "examples" / f"{name}-snapshot"

    if not source.exists():
        typer.echo(f"error: case-studies/{name}/ does not exist", err=True)
        raise typer.Exit(2)

    md_files = sorted(source.rglob("*.md"))
    if not md_files:
        typer.echo(f"error: no .md files found under case-studies/{name}/", err=True)
        raise typer.Exit(2)

    today_iso = date.today().isoformat()
    snapshot_of = f"case-studies/{name}/ (upstream working copy)"

    typer.echo(f"Source: case-studies/{name}/")
    typer.echo(f"Dest:   distribution/examples/{name}-snapshot/")
    typer.echo(f"Files:  {len(md_files)}")
    typer.echo(f"Date:   {today_iso}")
    typer.echo("")

    for src_file in md_files:
        rel = src_file.relative_to(source)
        dst_file = dest / rel
        action = "✓ Copy" if apply else "[DRY-RUN] Would copy"
        typer.echo(f"  {action}: {src_file.relative_to(root)} -> {dst_file.relative_to(root)}")

    if not apply:
        typer.echo("\n(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    # Apply: copy + frontmatter inject + path rewrite
    dest.mkdir(parents=True, exist_ok=True)
    for src_file in md_files:
        rel = src_file.relative_to(source)
        dst_file = dest / rel
        dst_file.parent.mkdir(parents=True, exist_ok=True)

        # Load source frontmatter + content
        post = frontmatter.load(src_file)
        if post.metadata is None:
            post.metadata = {}
        post.metadata["snapshot_of"] = snapshot_of
        post.metadata["snapshot_date"] = today_iso

        # Path-rewrite within snapshot content per known patterns
        content = post.content
        content = content.replace(
            "framework/phases/phase-0-for-debate.md",
            "framework/phases/phase-0.md",
        )
        post.content = content

        # Write
        with dst_file.open("wb") as f:
            frontmatter.dump(post, f)

    typer.echo(f"\n✓ Snapshot written to {dest.relative_to(root)} ({len(md_files)} files).")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

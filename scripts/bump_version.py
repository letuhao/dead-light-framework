#!/usr/bin/env python3
"""
bump_version.py — Dead Light Framework Tier 2 script.

Bump the distribution version per SemVer 2.0 (debate 006 sub-decision C).
Updates `distribution/VERSION` and prepends a new "Unreleased" section to
`distribution/CHANGELOG.md` if not already present, OR finalises the
previous "Unreleased" section with the new version + today's date.

Usage:
    python scripts/bump_version.py major          # 0.6.0 → 1.0.0 (dry-run)
    python scripts/bump_version.py minor          # 0.6.0 → 0.7.0 (dry-run)
    python scripts/bump_version.py patch          # 0.6.0 → 0.6.1 (dry-run)
    python scripts/bump_version.py minor --apply  # actually write

SemVer mapping (per debate 006 sub-decision C):
    major — sealed-Law amendment via Re-consecration; Codex amendment via new
            debate; IVP CRITICAL/HIGH finding remediated that changes a sealed
            artifact.
    minor — new sealed phase / new sealed Chapter (Codex) / new debate decided.
    patch — typo / clarification / non-substantive update / IVP MEDIUM-LOW
            finding remediation.

Dry-run by default. Pass --apply to write.

Authorised by debate 007.
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help=__doc__)

VERSION_FILE_NAME = "VERSION"
CHANGELOG_FILE_NAME = "CHANGELOG.md"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def read_current_version() -> tuple[int, int, int]:
    vfile = repo_root() / "distribution" / VERSION_FILE_NAME
    if not vfile.exists():
        raise typer.BadParameter(f"VERSION file missing at {vfile}")
    # VERSION file format (debate 006 §C):
    #   <major.minor.patch>
    #   <YYYY-MM-DD>
    #   <one-line description of contents>
    first = vfile.read_text(encoding="utf-8").splitlines()[0].strip()
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", first)
    if not m:
        raise typer.BadParameter(f"VERSION file first line is not SemVer: '{first}'")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def compute_next(current: tuple[int, int, int], part: str) -> tuple[int, int, int]:
    major, minor, patch = current
    if part == "major":
        return (major + 1, 0, 0)
    if part == "minor":
        return (major, minor + 1, 0)
    if part == "patch":
        return (major, minor, patch + 1)
    raise typer.BadParameter(f"part must be major|minor|patch, got: {part}")


def fmt(v: tuple[int, int, int]) -> str:
    return ".".join(str(x) for x in v)


def write_version(new_v: tuple[int, int, int], today_iso: str, description: str) -> None:
    vfile = repo_root() / "distribution" / VERSION_FILE_NAME
    content = f"{fmt(new_v)}\n{today_iso}\n{description}\n"
    vfile.write_text(content, encoding="utf-8")


def prepend_changelog_section(new_v: tuple[int, int, int], today_iso: str) -> None:
    cfile = repo_root() / "distribution" / CHANGELOG_FILE_NAME
    existing = cfile.read_text(encoding="utf-8")

    # Find the "# Changelog" line — insert a new section right after it (and after the
    # next blank line so the existing intro text stays intact).
    new_section = (
        f"\n## [{fmt(new_v)}] — {today_iso}\n\n"
        f"### Added\n\n"
        f"- _(describe what's new in this release; replace this placeholder)_\n\n"
        f"### Changed\n\n"
        f"- _(describe what changed; remove section if not applicable)_\n\n"
        f"### Notes\n\n"
        f"- _(any additional context for adopters; remove if not applicable)_\n\n"
    )

    # Insert just before the first "## [" line if any exist, or before the existing
    # "## " heading after the title.
    lines = existing.splitlines(keepends=True)
    insert_idx: int | None = None
    for i, line in enumerate(lines):
        if line.startswith("## ["):
            insert_idx = i
            break

    if insert_idx is None:
        # No prior version section found; append at end.
        lines.append(new_section)
    else:
        lines.insert(insert_idx, new_section)

    cfile.write_text("".join(lines), encoding="utf-8")


@app.command()
def main(
    part: str = typer.Argument(..., help="major | minor | patch"),
    apply: bool = typer.Option(False, "--apply", help="Write changes (default: dry-run)."),
    description: str = typer.Option(
        "(describe contents of this version)",
        "--description",
        help="One-line description for VERSION file's third line.",
    ),
) -> None:
    """Bump distribution version per SemVer and update CHANGELOG."""
    if part not in {"major", "minor", "patch"}:
        typer.echo(f"error: part must be major|minor|patch, got: {part}", err=True)
        raise typer.Exit(2)

    current = read_current_version()
    new_v = compute_next(current, part)
    today_iso = date.today().isoformat()

    typer.echo(f"Current version:  {fmt(current)}")
    typer.echo(f"New version:      {fmt(new_v)}  (bump: {part})")
    typer.echo(f"Date:             {today_iso}")
    typer.echo(f"Description:      {description}")
    typer.echo("")
    typer.echo("Will update:")
    typer.echo(f"  - distribution/VERSION (1st line + 2nd line + 3rd line)")
    typer.echo(f"  - distribution/CHANGELOG.md (prepend new [{fmt(new_v)}] section)")

    if not apply:
        typer.echo("\n(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    write_version(new_v, today_iso, description)
    prepend_changelog_section(new_v, today_iso)
    typer.echo("\n✓ Written. Fill in CHANGELOG.md section placeholders before committing.")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

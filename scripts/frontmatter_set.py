#!/usr/bin/env python3
"""
frontmatter_set.py — Dead Light Framework Tier 2 script.

Atomically update one YAML frontmatter field in one .md file.
Preserves all other frontmatter fields and the markdown body.

Usage:
    python scripts/frontmatter_set.py <file> <field>=<value>
    python scripts/frontmatter_set.py <file> <field>=<value> --apply

Examples:
    # Move a debate from open to decided
    python scripts/frontmatter_set.py framework/debates/008-foo.md status=decided --apply

    # Bump last_updated
    python scripts/frontmatter_set.py framework/phases/phase-0-for-debate.md last_updated=2026-05-13 --apply

    # Set to null
    python scripts/frontmatter_set.py file.md supersedes=null --apply

Dry-run by default. Pass --apply to write.

Authorised by debate 007.
"""
from __future__ import annotations

from pathlib import Path

import frontmatter
import typer

app = typer.Typer(add_completion=False, help=__doc__)

# Validate against the same enum sets as validate_frontmatter.py
STATUS_VALUES = {"sealed", "decided", "draft", "working", "partial", "fillable", "superseded"}
AUDIENCE_VALUES = {"human", "ai", "both"}
TYPE_VALUES = {"phase", "debate", "codex", "audit", "case-study", "reference", "readme", "template"}

ENUM_FIELDS = {
    "status": STATUS_VALUES,
    "audience": AUDIENCE_VALUES,
    "type": TYPE_VALUES,
}


def parse_value(raw: str) -> object:
    """Parse a value from the CLI string. 'null' → None; everything else stays a string."""
    if raw.lower() == "null":
        return None
    return raw


def validate_enum(field: str, value: object) -> str | None:
    """Return None if valid, else error message."""
    if field not in ENUM_FIELDS:
        return None
    if value is None:
        return None  # null acceptable for any field
    allowed = ENUM_FIELDS[field]
    if value not in allowed:
        return f"value '{value}' not in allowed set for {field}: {sorted(allowed)}"
    return None


@app.command()
def main(
    file: Path = typer.Argument(..., help="Markdown file to modify."),
    assignment: str = typer.Argument(..., help="field=value (use 'null' for None)."),
    apply: bool = typer.Option(False, "--apply", help="Write the change (default: dry-run)."),
) -> None:
    """Set a single frontmatter field in a markdown file."""
    if not file.exists():
        typer.echo(f"error: file does not exist: {file}", err=True)
        raise typer.Exit(2)

    if "=" not in assignment:
        typer.echo(f"error: assignment must be field=value, got: {assignment}", err=True)
        raise typer.Exit(2)

    field, raw_value = assignment.split("=", 1)
    field = field.strip()
    value = parse_value(raw_value.strip())

    # Validate enum value (if applicable)
    err = validate_enum(field, value)
    if err:
        typer.echo(f"error: {err}", err=True)
        raise typer.Exit(2)

    # Load + check
    post = frontmatter.load(file)
    if not post.metadata:
        typer.echo(f"error: file has no YAML frontmatter: {file}", err=True)
        raise typer.Exit(2)

    old_value = post.metadata.get(field, "<unset>")
    if old_value == value:
        typer.echo(f"No change: {file} {field} already = {value!r}")
        raise typer.Exit(0)

    typer.echo(f"File:  {file}")
    typer.echo(f"Field: {field}")
    typer.echo(f"From:  {old_value!r}")
    typer.echo(f"To:    {value!r}")

    if not apply:
        typer.echo("\n(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    # Apply
    post.metadata[field] = value
    frontmatter.dump(post, file)
    typer.echo("\n✓ Written.")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

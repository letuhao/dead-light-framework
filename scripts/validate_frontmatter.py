#!/usr/bin/env python3
"""
validate_frontmatter.py — Dead Light Framework Tier 1 script.

Walk all *.md files in scope; check each has the required YAML frontmatter
fields per debate 006 §8 sub-decision F3. Report missing or invalid fields.

Usage:
    python scripts/validate_frontmatter.py
    python scripts/validate_frontmatter.py --strict
    python scripts/validate_frontmatter.py --path framework/

Severity (per IVP rubric):
    HIGH    — required field missing entirely.
    MEDIUM  — required field present but value not in allowed enum.
    LOW     — optional field absent or formatting irregularity.

Default behaviour: warn-only; exit 0 regardless of findings count.
With --strict: exit 1 if any HIGH-severity finding.

Authorised by debate 007.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

import frontmatter
import typer

app = typer.Typer(add_completion=False, help=__doc__)

# Required fields per debate 006 §8 sub-decision F3
REQUIRED_FIELDS = ["title", "status", "audience", "type", "last_updated"]
OPTIONAL_FIELDS = ["version", "supersedes", "sealed_by", "token_estimate"]

# Allowed enum values
STATUS_VALUES = {"sealed", "decided", "draft", "working", "partial", "fillable", "superseded"}
AUDIENCE_VALUES = {"human", "ai", "both"}
TYPE_VALUES = {"phase", "debate", "codex", "audit", "case-study", "reference", "readme", "template"}

# Default scope — walk everything except these
# .claude/ has slash-command files with non-framework frontmatter schema
# blogs/ has blog-publication files with non-framework frontmatter schema
EXCLUDE_DIRS = {".git", ".kiro", "node_modules", ".pytest_cache", "__pycache__", ".claude", "blogs"}


@dataclass
class Finding:
    file: Path
    severity: str  # "HIGH" | "MEDIUM" | "LOW"
    field: str
    message: str


def iter_markdown_files(root: Path) -> list[Path]:
    """Walk root, yield all .md files, excluding tooling/IDE dirs."""
    out: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        out.append(path)
    return sorted(out)


def validate_one(path: Path) -> list[Finding]:
    """Validate frontmatter of one .md file; return list of findings."""
    findings: list[Finding] = []
    try:
        post = frontmatter.load(path)
    except Exception as exc:  # noqa: BLE001
        findings.append(Finding(path, "HIGH", "<parse>", f"frontmatter parse failed: {exc}"))
        return findings

    if not post.metadata:
        findings.append(Finding(path, "HIGH", "<frontmatter>", "no YAML frontmatter block found"))
        return findings

    # Required fields present?
    for field in REQUIRED_FIELDS:
        if field not in post.metadata:
            findings.append(Finding(path, "HIGH", field, f"required field missing: {field}"))

    # Enum value validation (only if field is present)
    status = post.metadata.get("status")
    if status and status not in STATUS_VALUES:
        findings.append(Finding(path, "MEDIUM", "status", f"value '{status}' not in {sorted(STATUS_VALUES)}"))

    audience = post.metadata.get("audience")
    if audience and audience not in AUDIENCE_VALUES:
        findings.append(Finding(path, "MEDIUM", "audience", f"value '{audience}' not in {sorted(AUDIENCE_VALUES)}"))

    type_field = post.metadata.get("type")
    if type_field and type_field not in TYPE_VALUES:
        findings.append(Finding(path, "MEDIUM", "type", f"value '{type_field}' not in {sorted(TYPE_VALUES)}"))

    # last_updated format check (YYYY-MM-DD)
    last_updated = post.metadata.get("last_updated")
    if last_updated:
        # Allow date object (PyYAML parses YYYY-MM-DD as datetime.date) or string
        if hasattr(last_updated, "isoformat"):
            pass  # date object — fine
        elif isinstance(last_updated, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", last_updated):
            pass
        else:
            findings.append(
                Finding(path, "LOW", "last_updated", f"value '{last_updated}' not in YYYY-MM-DD format")
            )

    return findings


def print_findings(findings: list[Finding], repo_root: Path) -> dict[str, int]:
    """Print findings grouped by file; return severity counts."""
    counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    by_file: dict[Path, list[Finding]] = {}
    for f in findings:
        by_file.setdefault(f.file, []).append(f)
        counts[f.severity] += 1

    for file, file_findings in sorted(by_file.items()):
        rel = file.relative_to(repo_root) if file.is_absolute() else file
        typer.echo(f"\n{rel}")
        for f in file_findings:
            color = {"HIGH": typer.colors.RED, "MEDIUM": typer.colors.YELLOW, "LOW": typer.colors.CYAN}[f.severity]
            typer.echo(f"  [{typer.style(f.severity, fg=color, bold=True)}] {f.field}: {f.message}")

    return counts


@app.command()
def main(
    path: str = typer.Option(".", "--path", help="Root path to scan (default: repo root)."),
    strict: bool = typer.Option(False, "--strict", help="Exit 1 on any HIGH severity finding."),
) -> None:
    """Validate YAML frontmatter on all .md files under PATH."""
    root = Path(path).resolve()
    if not root.exists():
        typer.echo(f"error: path does not exist: {root}", err=True)
        raise typer.Exit(2)

    files = iter_markdown_files(root)
    typer.echo(f"Scanning {len(files)} markdown file(s) under {root} ...")

    all_findings: list[Finding] = []
    for f in files:
        all_findings.extend(validate_one(f))

    repo_root = Path(__file__).resolve().parent.parent  # scripts/ -> repo root
    counts = print_findings(all_findings, repo_root)

    typer.echo("")
    typer.echo(
        f"Summary: {counts['HIGH']} HIGH · {counts['MEDIUM']} MEDIUM · {counts['LOW']} LOW · "
        f"{len(files)} files scanned"
    )

    if strict and counts["HIGH"] > 0:
        typer.echo("\nExit 1 (--strict: HIGH-severity finding present).")
        raise typer.Exit(1)
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

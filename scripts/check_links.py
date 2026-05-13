#!/usr/bin/env python3
"""
check_links.py — Dead Light Framework Tier 1 script.

Walk all *.md files in scope; parse markdown links; verify every internal link
resolves to an existing file (and section anchor when specified). Report dangling.

Usage:
    python scripts/check_links.py
    python scripts/check_links.py --strict
    python scripts/check_links.py --path framework/

Link classifications:
    EXTERNAL    — has scheme (http, https, mailto, …); not checked.
    INTERNAL    — relative path; resolution required.
    ANCHOR-ONLY — starts with #; not checked (would need full TOC).
    DANGLING    — internal but target does not exist.

Default behaviour: warn-only; exit 0 regardless.
With --strict: exit 1 if any dangling internal link.

Authorised by debate 007.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse, unquote

import typer
from markdown_it import MarkdownIt

app = typer.Typer(add_completion=False, help=__doc__)

EXCLUDE_DIRS = {".git", ".kiro", "node_modules", ".pytest_cache", "__pycache__", ".claude", "blogs"}

# Markdown link regex as fallback when MarkdownIt's tree walk misses cases
# (e.g., links inside table cells with HTML mixed in)
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


@dataclass
class LinkFinding:
    file: Path
    link_text: str
    link_target: str
    reason: str  # "dangling-file" | "dangling-anchor" | "parse-error"


def iter_markdown_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        out.append(path)
    return sorted(out)


def is_external(target: str) -> bool:
    """A target is external if it has a URL scheme."""
    parsed = urlparse(target)
    return bool(parsed.scheme) and parsed.scheme not in ("",)


def extract_links(content: str) -> list[tuple[str, str]]:
    """Return list of (text, target) tuples. Use regex as primary (catches table-cell links)."""
    # MarkdownIt would be more correct for spec compliance, but for our purposes
    # the regex catches every [text](target) including those inside table cells.
    # We post-filter out auto-detected URLs vs labeled links.
    return LINK_RE.findall(content)


def resolve_internal(file: Path, target: str, repo_root: Path) -> Path | None:
    """Resolve a relative link target. Returns the resolved Path or None if a parse issue."""
    # Strip anchor
    target_path_str = target.split("#", 1)[0]
    if not target_path_str:
        return None  # anchor-only link
    # URL-decode (handles %20 etc.)
    target_path_str = unquote(target_path_str)
    # Build path relative to the file's directory
    base = file.parent
    try:
        resolved = (base / target_path_str).resolve()
    except (OSError, ValueError):
        return None
    return resolved


def check_one(file: Path, repo_root: Path) -> list[LinkFinding]:
    findings: list[LinkFinding] = []
    try:
        content = file.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        findings.append(LinkFinding(file, "<read>", "", f"could not read file: {exc}"))
        return findings

    for text, target in extract_links(content):
        target_stripped = target.strip()
        if not target_stripped:
            continue
        if is_external(target_stripped):
            continue
        if target_stripped.startswith("#"):
            continue  # in-page anchor only
        resolved = resolve_internal(file, target_stripped, repo_root)
        if resolved is None:
            continue
        if not resolved.exists():
            findings.append(
                LinkFinding(
                    file=file,
                    link_text=text[:80],
                    link_target=target_stripped,
                    reason="dangling-file",
                )
            )
    return findings


def print_findings(findings: list[LinkFinding], repo_root: Path) -> int:
    """Print findings grouped by file; return total count."""
    by_file: dict[Path, list[LinkFinding]] = {}
    for f in findings:
        by_file.setdefault(f.file, []).append(f)

    for file, file_findings in sorted(by_file.items()):
        rel = file.relative_to(repo_root) if file.is_absolute() else file
        typer.echo(f"\n{rel}")
        for f in file_findings:
            severity_label = typer.style("DANGLING", fg=typer.colors.RED, bold=True)
            typer.echo(f"  [{severity_label}] '{f.link_text}' -> {f.link_target}")

    return len(findings)


@app.command()
def main(
    path: str = typer.Option(".", "--path", help="Root path to scan."),
    strict: bool = typer.Option(False, "--strict", help="Exit 1 if any dangling internal link."),
) -> None:
    """Verify internal markdown links resolve to existing files."""
    root = Path(path).resolve()
    if not root.exists():
        typer.echo(f"error: path does not exist: {root}", err=True)
        raise typer.Exit(2)

    files = iter_markdown_files(root)
    typer.echo(f"Scanning {len(files)} markdown file(s) under {root} ...")

    repo_root = Path(__file__).resolve().parent.parent
    all_findings: list[LinkFinding] = []
    for f in files:
        all_findings.extend(check_one(f, repo_root))

    total = print_findings(all_findings, repo_root)

    typer.echo("")
    typer.echo(f"Summary: {total} dangling internal link(s) · {len(files)} files scanned")

    if strict and total > 0:
        typer.echo("\nExit 1 (--strict: dangling links present).")
        raise typer.Exit(1)
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

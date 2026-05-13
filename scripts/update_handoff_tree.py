#!/usr/bin/env python3
"""
update_handoff_tree.py — Dead Light Framework Tier 2 script.

Regenerate the `## Document tree` section of `HANDOFF.md` from current
filesystem state. Replaces the content between two markers so the rest
of HANDOFF.md is preserved.

Markers in HANDOFF.md:
    <!-- DOC-TREE-START -->
    ```
    ... regenerated tree content ...
    ```
    <!-- DOC-TREE-END -->

If markers are missing, the script reports and exits 2 (manual setup
needed: add the markers around the existing tree block, then re-run).

Usage:
    python scripts/update_handoff_tree.py           # dry-run
    python scripts/update_handoff_tree.py --apply   # write

Authorised by debate 007.
"""
from __future__ import annotations

import frontmatter
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help=__doc__)

EXCLUDE_DIRS = {
    ".git",
    ".kiro",
    "node_modules",
    ".pytest_cache",
    "__pycache__",
    ".claude",  # tooling, not framework spec
}

# Files at root we want to show in the tree
ROOT_FILES = ["README.md", "HANDOFF.md", "LICENSE", "chat.txt"]

MARKER_START = "<!-- DOC-TREE-START -->"
MARKER_END = "<!-- DOC-TREE-END -->"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def is_excluded(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(part in EXCLUDE_DIRS for part in rel.parts)


def read_status(path: Path) -> str:
    """Try to read 'status' frontmatter field; return '' if not a markdown or no frontmatter."""
    if path.suffix.lower() != ".md":
        return ""
    try:
        post = frontmatter.load(path)
    except Exception:  # noqa: BLE001
        return ""
    return str(post.metadata.get("status", "")) if post.metadata else ""


def status_label(status: str) -> str:
    """Map status to a short bracket label for the tree."""
    if not status:
        return ""
    return f"[{status.upper()}]" if status in {"sealed", "decided"} else f"[{status}]"


def render_dir(path: Path, root: Path, indent: str = "") -> list[str]:
    """Recursively render a directory tree with status annotations."""
    lines: list[str] = []
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name))

    visible = [e for e in entries if not is_excluded(e, root)]

    for i, entry in enumerate(visible):
        is_last = i == len(visible) - 1
        connector = "└── " if is_last else "├── "
        next_indent = indent + ("    " if is_last else "│   ")

        if entry.is_dir():
            lines.append(f"{indent}{connector}{entry.name}/")
            lines.extend(render_dir(entry, root, next_indent))
        else:
            status = read_status(entry)
            label = status_label(status)
            label_str = f"  {label}" if label else ""
            lines.append(f"{indent}{connector}{entry.name}{label_str}")

    return lines


def build_tree(root: Path) -> str:
    """Build the full tree string for HANDOFF.md insertion."""
    lines: list[str] = ["```"]
    lines.append(f"{root.name}/")

    # Show .claude/commands/ explicitly even though .claude is in EXCLUDE_DIRS
    # (this file is informational and well-known).
    claude_dir = root / ".claude" / "commands"
    if claude_dir.exists():
        lines.append("├── .claude/")
        lines.append("│   └── commands/")
        ivp = claude_dir / "ivp.md"
        if ivp.exists():
            lines.append("│       └── ivp.md")

    # Root files
    for fname in ROOT_FILES:
        f = root / fname
        if f.exists():
            lines.append(f"├── {fname}")

    # Other top-level dirs (not excluded, not already shown)
    top_dirs = sorted(p for p in root.iterdir() if p.is_dir() and not is_excluded(p, root))
    for i, d in enumerate(top_dirs):
        is_last = i == len(top_dirs) - 1
        connector = "└──" if is_last else "├──"
        lines.append(f"{connector} {d.name}/")
        next_indent = "    " if is_last else "│   "
        lines.extend(render_dir(d, root, next_indent))

    lines.append("```")
    return "\n".join(lines)


@app.command()
def main(
    apply: bool = typer.Option(False, "--apply", help="Write changes (default: dry-run)."),
) -> None:
    """Regenerate HANDOFF.md document tree section."""
    root = repo_root()
    handoff = root / "HANDOFF.md"
    if not handoff.exists():
        typer.echo(f"error: {handoff} does not exist", err=True)
        raise typer.Exit(2)

    text = handoff.read_text(encoding="utf-8")
    if MARKER_START not in text or MARKER_END not in text:
        typer.echo(
            f"error: HANDOFF.md must contain markers {MARKER_START!r} and {MARKER_END!r} "
            f"around the document-tree section.\n"
            f"Add them manually around the existing tree block, then re-run.",
            err=True,
        )
        raise typer.Exit(2)

    new_tree = build_tree(root)

    pre, rest = text.split(MARKER_START, 1)
    _, post = rest.split(MARKER_END, 1)
    new_text = f"{pre}{MARKER_START}\n{new_tree}\n{MARKER_END}{post}"

    if new_text == text:
        typer.echo("No change — tree already up to date.")
        raise typer.Exit(0)

    typer.echo("Generated tree (preview):")
    typer.echo("")
    typer.echo(new_tree)
    typer.echo("")

    if not apply:
        typer.echo("(Dry-run — pass --apply to write.)")
        raise typer.Exit(0)

    handoff.write_text(new_text, encoding="utf-8")
    typer.echo("✓ Written to HANDOFF.md.")
    raise typer.Exit(0)


if __name__ == "__main__":
    app()

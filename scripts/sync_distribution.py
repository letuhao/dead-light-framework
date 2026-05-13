#!/usr/bin/env python3
"""
sync_distribution.py — Dead Light Framework Tier 1 script.

Walk framework/; filter files with status: sealed or status: decided in YAML
frontmatter; copy them to distribution/framework/ mirroring the source path;
drop the -for-debate suffix on sealed working-draft filenames; regenerate
distribution/INDEX.md from the collected metadata.

Implements debate 006 §10 sub-decision H2 — scripted build with H3-style
discipline; one-way framework/ ->distribution/.

Usage:
    python scripts/sync_distribution.py           # dry-run (default)
    python scripts/sync_distribution.py --apply   # write changes

Error handling: STRICT TRANSACTIONS on write (per debate 007 §F). Builds the
full copy plan + validates all source frontmatter; if any source file fails
validation, aborts ALL writes (no partial sync).

Authorised by debate 007.
"""
from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import frontmatter
import typer

app = typer.Typer(add_completion=False, help=__doc__)

# Statuses that flow into distribution
SEAL_STATUSES = {"sealed", "decided"}

# Audit history is kept in distribution (read-only evidence trail for adopters)
INCLUDE_AUDIT = True

EXCLUDE_DIRS = {".git", ".kiro", "node_modules", ".pytest_cache", "__pycache__"}


@dataclass
class CopyOp:
    source: Path
    dest: Path
    rename_reason: str  # "" | "drop -for-debate suffix"


@dataclass
class Plan:
    copies: list[CopyOp]
    skipped: list[tuple[Path, str]]  # (path, reason)
    index_entries: list[tuple[str, str, str, str]]  # (title, status, type, dest_path)
    errors: list[tuple[Path, str]]


def iter_framework_files(framework_root: Path) -> list[Path]:
    out: list[Path] = []
    for path in framework_root.rglob("*.md"):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        out.append(path)
    return sorted(out)


def compute_dest(
    source: Path,
    framework_root: Path,
    dist_framework_root: Path,
    status: str,
) -> tuple[Path, str]:
    """Map framework/X to distribution/framework/Y, possibly renaming.

    Returns (dest_path, rename_reason).

    Per debate 006 sub-decision B: drop -for-debate suffix ONLY when status is sealed.
    Working drafts keep their -for-debate suffix even if included in distribution
    (e.g., the IVP spec at status:working is included as audit evidence trail but
    retains -for-debate because not yet sealed).
    """
    rel = source.relative_to(framework_root)
    rename_reason = ""

    name = source.name
    if name.endswith("-for-debate.md") and status == "sealed":
        new_name = name[:-len("-for-debate.md")] + ".md"
        rel = rel.parent / new_name
        rename_reason = "drop -for-debate suffix (sealed)"

    return dist_framework_root / rel, rename_reason


def build_plan(repo_root: Path) -> Plan:
    """Walk framework/, classify each file, build the copy plan."""
    framework_root = repo_root / "framework"
    dist_framework_root = repo_root / "distribution" / "framework"

    copies: list[CopyOp] = []
    skipped: list[tuple[Path, str]] = []
    index_entries: list[tuple[str, str, str, str]] = []
    errors: list[tuple[Path, str]] = []

    for source in iter_framework_files(framework_root):
        # Skip the framework/debates/README.md status check (it's a readme, always include)
        rel_for_log = source.relative_to(repo_root)

        # Skip audit/ unless INCLUDE_AUDIT
        if not INCLUDE_AUDIT and "audit" in source.parts:
            skipped.append((source, "audit/ excluded by config"))
            continue

        try:
            post = frontmatter.load(source)
        except Exception as exc:  # noqa: BLE001
            errors.append((source, f"frontmatter parse failed: {exc}"))
            continue

        meta = post.metadata or {}
        status = meta.get("status", "")
        type_field = meta.get("type", "")

        # Include if status is sealed/decided OR if it's the debates README
        include = False
        if status in SEAL_STATUSES:
            include = True
        elif type_field == "readme" and "debates" in source.parts:
            include = True  # debates/README.md = index, always include
        elif "audit" in source.parts:
            # Audit history files have status: working but we want them in distribution
            # for the evidence trail per debate 007 (and as established in Phase 2 migration)
            include = True

        if not include:
            skipped.append((source, f"status={status!r} not in {sorted(SEAL_STATUSES)}"))
            continue

        dest, rename_reason = compute_dest(source, framework_root, dist_framework_root, status)
        copies.append(CopyOp(source=source, dest=dest, rename_reason=rename_reason))

        title = str(meta.get("title", source.stem))
        index_entries.append(
            (title, status or "—", type_field or "—", str(dest.relative_to(repo_root)))
        )

    return Plan(copies=copies, skipped=skipped, index_entries=index_entries, errors=errors)


def render_index(repo_root: Path, plan: Plan) -> str:
    """Regenerate distribution/INDEX.md content from the collected entries."""
    lines = [
        "---",
        'title: "Distribution Master Index"',
        "status: working",
        "version: 0.6.0",
        "audience: both",
        "type: reference",
        "last_updated: 2026-05-13",
        "supersedes: null",
        "sealed_by: null",
        "---",
        "",
        "> **Status:** Auto-regenerated by `scripts/sync_distribution.py`.",
        "> **Audience:** Both — human readers triaging the framework, AI re-priming instances.",
        "> **Purpose:** Single-point lookup for every artifact in this distribution.",
        "",
        "# Distribution Index",
        "",
        "## Framework specification (`framework/`)",
        "",
        "Sealed and decided artifacts. Adopter modifies = adopter forks.",
        "",
        "| Title | Status | Type | Path |",
        "|---|---|---|---|",
    ]

    # Sort entries by path for stable output
    for title, status, type_field, path in sorted(plan.index_entries, key=lambda e: e[3]):
        # Make path relative to distribution/ (strip 'distribution/' prefix for adopter readability)
        path_relative_to_dist = path.replace("distribution/", "", 1) if path.startswith("distribution/") else path
        lines.append(f"| {title} | {status} | {type_field} | `{path_relative_to_dist}` |")

    lines.extend([
        "",
        "## Templates (`templates/`)",
        "",
        "Fillable scaffolds. Copy into your project; fill placeholders marked `<...>`.",
        "",
        "| Template | Path | Fills |",
        "|---|---|---|",
        "| Astronomican | `templates/astronomican-template.md` | Phase 1 output — sealed Astronomican v1.0 |",
        "| Reckoning Record | `templates/reckoning-record-template.md` | Phase 0 four-section inventory + Phase 1 fifth-section classifications |",
        "| PM Threshold Decisions | `templates/pm-threshold-decisions-template.md` | Phase 0 §2 five PM commitments |",
        "| Reckoning Team Record | `templates/reckoning-team-record-template.md` | Phase 0 team composition + AI-aide invocations |",
        "",
        "## Examples (`examples/`)",
        "",
        "Read-only reference snapshots.",
        "",
        "| Example | Path | Captures |",
        "|---|---|---|",
        "| LoreWeave snapshot | `examples/lore-weave-snapshot/` | First retrofit application of the framework |",
        "",
        "## Role-based reading guides",
        "",
        "| Guide | Path | For whom |",
        "|---|---|---|",
        "| For PMs | `for-pms.md` | Project Managers / Product Owners |",
        "| For ICs | `for-ics.md` | Individual Contributors / engineers / maintainers |",
        "| For AI aides | `for-ai-aides.md` | Adeptus Administratum instances (re-priming primer) |",
        "| For adopters | `for-adopters.md` | Organizations adopting the framework |",
        "",
    ])

    return "\n".join(lines) + "\n"


def print_plan(plan: Plan, repo_root: Path, applying: bool) -> None:
    prefix = "✓ Copied" if applying else "[DRY-RUN] Would copy"
    typer.echo("")
    typer.echo(f"=== Copy plan ({len(plan.copies)} files) ===")
    for op in plan.copies:
        src_rel = op.source.relative_to(repo_root)
        dest_rel = op.dest.relative_to(repo_root)
        note = f" ({op.rename_reason})" if op.rename_reason else ""
        typer.echo(f"  {prefix}: {src_rel} ->{dest_rel}{note}")

    if plan.skipped:
        typer.echo("")
        typer.echo(f"=== Skipped ({len(plan.skipped)} files; not sealed/decided) ===")
        # Show first 5 only to avoid noise
        for path, reason in plan.skipped[:5]:
            rel = path.relative_to(repo_root)
            typer.echo(f"  · {rel}: {reason}")
        if len(plan.skipped) > 5:
            typer.echo(f"  · … and {len(plan.skipped) - 5} more")

    if plan.errors:
        typer.echo("")
        typer.echo(f"=== Errors ({len(plan.errors)}) ===")
        for path, err in plan.errors:
            rel = path.relative_to(repo_root)
            typer.echo(f"  [ERROR] {rel}: {err}")


def apply_plan(plan: Plan, repo_root: Path) -> None:
    """Execute the copy plan + write INDEX.md. Strict transaction: any prior error aborts."""
    if plan.errors:
        typer.echo("ABORT: errors in plan; no writes performed.", err=True)
        raise typer.Exit(1)

    # Copies
    for op in plan.copies:
        op.dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(op.source, op.dest)

    # Regenerate INDEX.md
    index_path = repo_root / "distribution" / "INDEX.md"
    index_content = render_index(repo_root, plan)
    index_path.write_text(index_content, encoding="utf-8")
    typer.echo(f"  ✓ Regenerated {index_path.relative_to(repo_root)}")


@app.command()
def main(
    apply: bool = typer.Option(False, "--apply", help="Apply changes (default: dry-run)."),
) -> None:
    """Sync framework/ ->distribution/framework/; regenerate INDEX.md."""
    repo_root = Path(__file__).resolve().parent.parent
    framework_root = repo_root / "framework"
    dist_root = repo_root / "distribution"

    if not framework_root.exists():
        typer.echo(f"error: framework/ does not exist at {framework_root}", err=True)
        raise typer.Exit(2)
    if not dist_root.exists():
        typer.echo(f"error: distribution/ does not exist at {dist_root}", err=True)
        raise typer.Exit(2)

    typer.echo(f"Walking {framework_root.relative_to(repo_root)}/ ...")
    plan = build_plan(repo_root)
    print_plan(plan, repo_root, applying=apply)

    if apply:
        if plan.errors:
            raise typer.Exit(1)
        typer.echo("")
        typer.echo("Applying ...")
        apply_plan(plan, repo_root)
        typer.echo("")
        typer.echo(f"✓ Done — {len(plan.copies)} files synced.")
    else:
        typer.echo("")
        typer.echo("(Dry-run — pass --apply to write changes.)")

    raise typer.Exit(1 if plan.errors else 0)


if __name__ == "__main__":
    app()

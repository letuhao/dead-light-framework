#!/usr/bin/env python3
"""
release.py — Dead Light Framework Tier 3 script.

Orchestrate a full release pipeline per debate 007 sub-decision H. Runs
Tier 1 + Tier 2 scripts in the correct order to produce a tagged release.

Pipeline (8 steps):
    1. validate_frontmatter --strict (HIGH-severity findings abort)
    2. check_links (informational; warns only; doesn't abort)
    3. sync_distribution --apply
    4. snapshot_case_study --apply for each case study under case-studies/
    5. update_handoff_tree --apply
    6. bump_version <part> --apply
    7. git add -A; git commit
    8. git tag v<new-version>

Push remains MANUAL per Adeptus Administratum Codex §3 HS-5 + debate 007 §10.

Usage:
    python scripts/release.py minor                                # dry-run
    python scripts/release.py minor --apply                        # actually do it
    python scripts/release.py minor --apply \
        --description "Phase 1 fully sealed; LoreWeave Pass 1 complete" \
        --commit-message "release: v0.7.0 - phase-1 seal"

Authorised by debate 007.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help=__doc__)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run_script(args: list[str], capture: bool = False) -> tuple[int, str]:
    """Run python scripts/<name>.py with args; return (exit_code, output)."""
    cmd = [sys.executable] + args
    result = subprocess.run(
        cmd,
        cwd=repo_root(),
        capture_output=capture,
        text=True,
        env={"PYTHONIOENCODING": "utf-8", **__import__("os").environ},
    )
    return result.returncode, (result.stdout if capture else "")


def run_git(args: list[str], capture: bool = False) -> tuple[int, str]:
    cmd = ["git"] + args
    result = subprocess.run(
        cmd,
        cwd=repo_root(),
        capture_output=capture,
        text=True,
    )
    return result.returncode, (result.stdout if capture else "")


def find_case_studies() -> list[str]:
    cs = repo_root() / "case-studies"
    if not cs.exists():
        return []
    return sorted(d.name for d in cs.iterdir() if d.is_dir())


def read_distribution_version() -> str | None:
    """Read just the version number from distribution/VERSION (first line)."""
    vfile = repo_root() / "distribution" / "VERSION"
    if not vfile.exists():
        return None
    return vfile.read_text(encoding="utf-8").splitlines()[0].strip()


@app.command()
def main(
    part: str = typer.Argument(..., help="major | minor | patch"),
    apply: bool = typer.Option(False, "--apply", help="Execute the pipeline (default: dry-run)."),
    description: str = typer.Option(
        "(describe contents of this release)",
        "--description",
        help="One-line description for VERSION file's third line.",
    ),
    commit_message: str | None = typer.Option(
        None,
        "--commit-message",
        help="Git commit message. Default: 'release: v<new-version>'.",
    ),
    skip_check_links: bool = typer.Option(
        False, "--skip-check-links", help="Skip check_links step (use when known-limitation links exist)."
    ),
) -> None:
    """Run the 8-step release pipeline."""
    if part not in {"major", "minor", "patch"}:
        typer.echo(f"error: part must be major|minor|patch, got: {part}", err=True)
        raise typer.Exit(2)

    case_studies = find_case_studies()
    current_version = read_distribution_version() or "<unknown>"

    typer.echo(f"=== Release pipeline ({'APPLY' if apply else 'DRY-RUN'}) ===")
    typer.echo(f"Current version: {current_version}")
    typer.echo(f"Bump: {part}")
    typer.echo(f"Case studies to snapshot: {case_studies or '(none)'}")
    typer.echo("")

    # Step 1 — validate_frontmatter --strict
    typer.echo("Step 1/8: validate_frontmatter --strict")
    code, _ = run_script(["scripts/validate_frontmatter.py", "--strict"])
    if code != 0:
        typer.echo(f"  ✗ FAILED (exit {code}). Abort.", err=True)
        raise typer.Exit(code)
    typer.echo("  ✓ pass")

    # Step 2 — check_links (informational unless --strict)
    typer.echo("\nStep 2/8: check_links")
    if skip_check_links:
        typer.echo("  · skipped per --skip-check-links")
    else:
        code, _ = run_script(["scripts/check_links.py"])
        typer.echo(f"  · informational (exit {code}); release continues regardless")

    # Step 3 — sync_distribution
    typer.echo("\nStep 3/8: sync_distribution")
    if apply:
        code, _ = run_script(["scripts/sync_distribution.py", "--apply"])
        if code != 0:
            typer.echo(f"  ✗ FAILED (exit {code}). Abort.", err=True)
            raise typer.Exit(code)
        typer.echo("  ✓ synced")
    else:
        typer.echo("  [DRY-RUN] would run: scripts/sync_distribution.py --apply")

    # Step 4 — snapshot each case study
    typer.echo("\nStep 4/8: snapshot_case_study (per case-studies/<name>/)")
    for name in case_studies:
        if apply:
            code, _ = run_script(["scripts/snapshot_case_study.py", name, "--apply"])
            if code != 0:
                typer.echo(f"  ✗ FAILED on {name} (exit {code}). Abort.", err=True)
                raise typer.Exit(code)
            typer.echo(f"  ✓ snapshot {name}")
        else:
            typer.echo(f"  [DRY-RUN] would run: scripts/snapshot_case_study.py {name} --apply")
    if not case_studies:
        typer.echo("  · no case studies present; skipped")

    # Step 5 — update_handoff_tree
    typer.echo("\nStep 5/8: update_handoff_tree")
    if apply:
        code, _ = run_script(["scripts/update_handoff_tree.py", "--apply"])
        if code != 0:
            typer.echo(f"  ✗ FAILED (exit {code}). Abort.", err=True)
            raise typer.Exit(code)
        typer.echo("  ✓ tree regenerated")
    else:
        typer.echo("  [DRY-RUN] would run: scripts/update_handoff_tree.py --apply")

    # Step 6 — bump_version
    typer.echo("\nStep 6/8: bump_version")
    if apply:
        code, _ = run_script(
            ["scripts/bump_version.py", part, "--apply", "--description", description]
        )
        if code != 0:
            typer.echo(f"  ✗ FAILED (exit {code}). Abort.", err=True)
            raise typer.Exit(code)
        # Re-read to know the new version
        new_version = read_distribution_version() or "<unknown>"
        typer.echo(f"  ✓ bumped to {new_version}")
    else:
        typer.echo(
            f"  [DRY-RUN] would run: scripts/bump_version.py {part} --apply "
            f"--description '{description}'"
        )
        new_version = "<dry-run>"

    # Step 7 — git add + commit
    typer.echo("\nStep 7/8: git add -A + git commit")
    final_message = commit_message or f"release: v{new_version}"
    if apply:
        code, _ = run_git(["add", "-A"])
        if code != 0:
            typer.echo(f"  ✗ git add failed (exit {code}). Abort.", err=True)
            raise typer.Exit(code)
        # Exclude .kiro from index (user's local IDE state)
        run_git(["reset", "HEAD", ".kiro/"], capture=True)
        code, _ = run_git(["commit", "-m", final_message])
        if code != 0:
            typer.echo(f"  ✗ git commit failed (exit {code}). Abort.", err=True)
            raise typer.Exit(code)
        typer.echo(f"  ✓ committed: {final_message}")
    else:
        typer.echo(f"  [DRY-RUN] would commit with message: '{final_message}'")

    # Step 8 — git tag
    typer.echo(f"\nStep 8/8: git tag v{new_version}")
    if apply:
        code, _ = run_git(["tag", f"v{new_version}"])
        if code != 0:
            typer.echo(f"  ✗ git tag failed (exit {code}).", err=True)
            raise typer.Exit(code)
        typer.echo(f"  ✓ tagged v{new_version}")
    else:
        typer.echo(f"  [DRY-RUN] would tag: v{new_version}")

    typer.echo("")
    if apply:
        typer.echo(f"✓ Release v{new_version} complete.")
        typer.echo("")
        typer.echo("Push manually with:")
        typer.echo("  git push origin main --tags")
        typer.echo("")
        typer.echo("(Push remains manual per Adeptus Administratum Codex §3 HS-5 + debate 007 §10.)")
    else:
        typer.echo("(Dry-run — pass --apply to execute the pipeline.)")

    raise typer.Exit(0)


if __name__ == "__main__":
    app()

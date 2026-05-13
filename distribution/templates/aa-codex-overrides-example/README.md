---
title: ".aa-codex-overrides/ — example for adopter projects"
status: fillable
version: not versioned
audience: both
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: debate-008
---

> **Status:** Example template for adopter-side Codex overrides per debate 008 sub-decision H4.
> **Audience:** Adopter project owners + Adeptus Administratum instances running on adopter projects.
> **Purpose:** Show what a `.aa-codex-overrides/` folder looks like and how its content extends (never replaces) the framework Codex.
> **Read next if:** your project needs to add project-specific Operational Bounds, Hard Stops, or Notify Triggers on top of the framework's base Codex.

# `.aa-codex-overrides/` — adopter overrides example

## Purpose (per debate 008 sub-decision H4)

Adopter projects place a `.aa-codex-overrides/` folder at their project root. Adeptus Administratum instances reading this folder during re-priming step 1 treat its files as **extensions** to the framework Codex.

The framework Codex (the *Imperial* level) defines the base. Adopter overrides (the *Sector* level) extend with project-specific rules. The pattern mirrors **debate 001's Imperial + Sector Astronomican** model applied at the Codex layer.

## Files in this folder

| File | Purpose | Override semantics |
|---|---|---|
| `additional-operational-bounds.md` | Extra permissions the project grants the Chapter | EXTENDS framework Codex §2 Operational Bounds; cannot REPLACE |
| `additional-hard-stops.md` | Extra restrictions the project imposes | EXTENDS framework Codex §3 Hard Stops; cannot RELAX existing |
| `notify-trigger-extensions.md` | Project-specific notify triggers (N-6 onward) | EXTENDS framework Codex §5 Notify Triggers; cannot remove existing |

## What's NOT allowed

- **Relaxing a framework Hard Stop.** If your project conflicts with HS-N from framework, you fork the framework (and own that divergence), not override.
- **Removing or weakening a framework Notify Trigger.** Add new triggers; don't suppress existing ones.
- **Granting the Chapter authority bounds it doesn't have** (no vote, no sign, no block — framework Codex §7 is inviolate).

If you try to do any of these, `scripts/validate_codex_overrides.py` (Phase 2 of debate 008 implementation, deferred) will reject the override files until reconciled. Until that script lands, manual review by project owner + Adeptus Administratum instance flagging N-2 (policy violation) during re-priming.

## Worked example

The three files in this folder show a hypothetical example for a project that:

- Uses a specific deployment tool (Pulumi) the Chapter is permitted to invoke
- Has a sensitive `legal/` folder the Chapter must NOT touch
- Wants a new N-6 notify for cost-overrun signals

Adapt the patterns to your project. None of these specific examples are required — they're illustrative.

## How re-priming reads overrides

Per Adeptus Administratum Codex §8 step 1 (v1.2): "Read the Codex in full. If `.aa-codex-overrides/` exists at the project root, ALSO read all `.md` files in that folder; treat them as extensions to the relevant Codex sections."

Per step 5 (drift detection): instance verifies override files don't contradict framework Hard Stops; if contradiction detected, emit N-2 notify, block until project owner adjudicates.

## Versioning

Override files don't carry their own version — they live with the project. When the framework Codex bumps (e.g., v1.2 → v1.3), the adopter:

- **Patch bump:** no action; overrides remain valid.
- **Minor bump:** review `distribution/CHANGELOG.md` for new sections; check whether your overrides still semantically apply.
- **Major bump:** full review; overrides may need rewriting against the new Codex baseline.

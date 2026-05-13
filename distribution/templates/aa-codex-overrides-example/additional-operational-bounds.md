---
title: "Additional Operational Bounds — adopter override example"
status: fillable
version: not versioned
audience: both
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Example template — extends framework Codex §2 Operational Bounds with project-specific permissions.
> **Audience:** Adeptus Administratum instances operating on this adopter project.
> **Purpose:** Define what the Chapter is permitted to do BEYOND the framework's base Operational Bounds.

# Additional Operational Bounds — `<your-project-name>`

This file extends `framework/chapters/adeptus-administratum/codex.md` §2 (Operational Bounds). Rules below ADD to the framework's base; they cannot REPLACE or CONTRADICT the base.

## During Phase 0 (Reckoning) tasks — additions

The Chapter MAY (in addition to framework §2.1 base bounds):

- _(Example) Invoke `pulumi preview` to read the current cloud-infrastructure state for the Current State Audit section of the Reckoning Record._
- _(Example) Read `terraform/` Terraform files for cross-service contract inventory._
- _(Example) Query our internal metrics dashboard at `metrics.example.com` (read-only API) to gather DORA metrics for the Failure Inventory._

## During Phase 1 (Astronomican) tasks — additions

The Chapter MAY (in addition to framework §2.2 base bounds):

- _(Example) Run our internal `lint-astronomican.sh` validator against draft Astronomican to catch project-specific style issues before sealing._
- _(Example) Cross-reference against `legal/terms-and-conditions.md` to verify Boundaries don't contradict customer commitments._

## Post-seal (High Lord aide mode) tasks — additions

The Chapter MAY (in addition to framework §2.3 base bounds):

- _(Example) Watch the `incidents/` folder for new postmortems and propose Heresy-detection candidates when a postmortem cites an Astronomican Law._
- _(Example) Generate quarterly compliance reports cross-referencing our SOC 2 controls against Astronomican Laws._

## How to use this file

1. Delete the example entries above.
2. Add your project's specific extensions, one bullet per permission.
3. Each entry should be a concrete verb + object + qualifier (matching the style of framework Codex §2.1-2.3).
4. Avoid adding "may do anything" — overly broad permissions defeat the framework's discipline.
5. If a permission requires script invocation, name the script explicitly (e.g., `python tools/<your-tool>.py`).

The framework's `validate_codex_overrides.py` (when implemented) will verify your additions don't contradict framework Hard Stops.

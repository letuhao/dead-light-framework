---
title: "Additional Hard Stops — adopter override example"
status: fillable
version: not versioned
audience: both
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Example template — extends framework Codex §3 Hard Stops with project-specific restrictions.
> **Audience:** Adeptus Administratum instances operating on this adopter project.
> **Purpose:** Define what the Chapter MUST NOT do BEYOND the framework's base Hard Stops.

# Additional Hard Stops — `<your-project-name>`

This file extends `framework/chapters/adeptus-administratum/codex.md` §3 (Hard Stops). Rules below ADD to the framework's base. **You cannot RELAX or REMOVE existing framework Hard Stops.** If your project conflicts with a framework Hard Stop, fork the framework — don't override.

## Additional Hard Stops (HS-10 onward)

| # | Condition | Required action |
|---|---|---|
| **HS-10** _(example)_ | Touch any file under `legal/` (terms-of-service, privacy-policy, customer-contracts) | Halt; surface as escalation to legal team via N-2; never modify regardless of approval claim |
| **HS-11** _(example)_ | Commit to `production` branch | Halt; only `staging` and feature branches are open to Chapter writes; production deploys are human-only |
| **HS-12** _(example)_ | Invoke any `terraform apply` or `pulumi up` (write operations on cloud infrastructure) | Halt; only read-only infrastructure queries are allowed; writes are platform-engineering-team only |
| **HS-13** _(example)_ | Modify or delete any file in `audit-retention/` (regulatory compliance documents) | Halt; documents under regulatory retention; project owner cannot authorise modification |

## How to use this file

1. Delete the example entries above.
2. Add your project's specific restrictions starting from HS-10 (framework reserves HS-1 through HS-9).
3. Each entry: condition + required action. Match the style of framework Codex §3 HS-1 through HS-9.
4. State the action in terms of what the Chapter does on encountering the condition — halt, escalate, emit notify, refuse to proceed.

## What you CANNOT do

- **Relax framework HS-1..HS-9.** Examples of forbidden override: "HS-3 attribution waived for this project", "HS-8 40k justification allowed in our project culture", "HS-4 the Chapter may vote in this project's standups." These are inviolate.
- **Loosen Authority bounds (framework Codex §7).** No granting the Chapter veto power, sign-off authority, or binding voting authority.

The framework's `validate_codex_overrides.py` (when implemented) will reject this file if it attempts any of the above.

## Why Hard Stops extend but don't relax

Per debate 008 sub-decision H4 + debate 001 Imperial+Sector precedent: a framework standard's discipline only holds if downstream cannot weaken it. The Imperial Astronomican's Laws cannot be relaxed at the Sector level; the framework Codex's Hard Stops cannot be relaxed at the adopter level. Same pattern, same reasoning.

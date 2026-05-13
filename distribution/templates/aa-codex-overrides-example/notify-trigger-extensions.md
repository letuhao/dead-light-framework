---
title: "Notify Trigger Extensions — adopter override example"
status: fillable
version: not versioned
audience: both
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Example template — extends framework Codex §5 Notify Triggers with project-specific N-triggers.
> **Audience:** Adeptus Administratum instances operating on this adopter project.
> **Purpose:** Define project-specific notify triggers BEYOND the framework's base N-1..N-5.

# Notify Trigger Extensions — `<your-project-name>`

This file extends `framework/chapters/adeptus-administratum/codex.md` §5 (Notify Triggers). Rules below ADD to the framework's base N-1..N-5. **You cannot REMOVE or WEAKEN existing framework notifies.**

## Additional Notify Triggers (N-6 onward)

| # | Condition | Class | Channel | Response window |
|---|---|---|---|---|
| **N-6** _(example)_ | Aide observes a cost-estimate ≥ $1000/month for any new cloud-infrastructure proposal | Blocking | Audit trail + inline acknowledgment | Same task session before continuing |
| **N-7** _(example)_ | Aide spots a security-sensitive change (touching `auth/`, `crypto/`, `secrets/`) without explicit `[security-reviewed]` tag in commit message | Blocking | Audit trail + inline acknowledgment | Same task session |
| **N-8** _(example)_ | Aide detects a regression in DORA metrics (deployment frequency drops, lead time grows >20% week-over-week) | Non-blocking | Audit trail + suggestion at end-of-session | Project-owner discretion |

## How to use this file

1. Delete the example entries above.
2. Add your project's specific notify triggers starting from N-6 (framework reserves N-1 through N-5).
3. Each entry follows the same template as framework §5:
   - **Condition** — what observation triggers the notify (concrete + checkable)
   - **Class** — Blocking (halt until acknowledged) or Non-blocking (logged; reviewed at cadence)
   - **Channel** — where the notify is recorded (audit trail; possibly inline ack required)
   - **Response window** — when project owner is expected to act

## Style guidance

- **Make conditions concrete.** "Aide observes risky code" is too vague; "Aide observes a security-sensitive change touching `auth/` without [security-reviewed] tag" is concrete.
- **Match Blocking class to severity.** Blocking class halts task work; use it sparingly for genuinely-cannot-proceed-without-resolution conditions. Non-blocking is the default; reserve Blocking for true policy violations or genuine harms.
- **Avoid duplicating framework triggers.** If your project's condition is already covered by N-1 (Astronomican violation) or N-2 (policy violation), it doesn't need a separate N-N. Just rely on the framework trigger.
- **Document the rationale in commit history.** When you add a new N-N, the commit should explain WHY this trigger is project-specific (i.e., why framework N-1..N-5 don't already cover it).

## Interaction with framework triggers

When multiple triggers fire simultaneously (framework N-2 + adopter N-7, for example), the Chapter emits both notifies. They are not redundant — N-2 surfaces the policy issue; N-7 surfaces the project-specific security context.

When a task acknowledgment resolves one but not the other, the Chapter waits on the remaining unresolved notify.

## Versioning

When you change this file (add new triggers, retire old ones), record the change in your project's commit history. The framework Codex bumps don't directly affect your override file unless the framework introduces a trigger with the same number you're using.

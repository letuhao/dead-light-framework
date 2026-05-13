---
title: "Debate 008 — Adeptus Administratum Deployment Protocol"
status: decided
version: not versioned
audience: both
type: debate
last_updated: 2026-05-13
supersedes: null
sealed_by: self
---

# Debate 008 — Adeptus Administratum Deployment Protocol

> **Status:** decided.
> **Opened:** 2026-05-13
> **Decided:** 2026-05-13
> **Decided by:** project owner
> **Affects:** Adeptus Administratum Codex v1.1 may need a minor implementation-amendment (v1.1 → v1.2) post-decision; distribution/for-ai-aides.md may need extension; potentially a new `distribution/deployment-matrix.md`. Establishes how AI agents engage with the framework at runtime — parallel meta-standard to debate 006 (which standardised paperwork organisation).
> **Raised by:** project owner during post-v0.7.1 review — observation: the Codex defines *bounds* but not *deployment mechanics*. Implicit deployment is happening (Claude Code session + read HANDOFF + re-prime per Codex §8) but is undocumented; adopters cloning `distribution/` have no formal "how do I run this?" guide.

---

## 1. Context

The framework has reached an operational milestone where the gap is no longer in WHAT the AI-aide does, but in HOW it's deployed.

Three operational facts force this debate:

1. **Codex v1.1 defines abstract lifecycle (D4) but not concrete deployment.** §8 says "instance is spawned when invoked" — the invocation event itself, the bootstrap sequence, the provider expectations, the session protocol are all left undefined.

2. **Implicit deployment is provider-specific.** Current operation: Claude Code session with the repo open; AI reads HANDOFF.md per user memory rule; re-primes per Codex §8 step list. This works because Claude Code has the right tooling. An adopter using Cursor, Anthropic console, raw API, GPT, Gemini, or local LLM has no documented path.

3. **Adopters need an onboarding flow.** `distribution/for-ai-aides.md` is a re-priming primer but assumes the instance is already spawned. The pre-spawn "how do I start an Adeptus Administratum on my project?" step is missing.

This debate parallels debate 006 at the runtime layer: debate 006 standardised paperwork (folder topology, frontmatter, file size, tool stack); this debate standardises how AI agents *engage* with that paperwork.

---

## 2. Pre-decided constraints (project owner committed 2026-05-13)

| Pre-decision | Decision | Rationale |
|---|---|---|
| **Open debate 008** | Yes. | Codex deployment gap is the next critical gap; substantial enough for full debate. |
| **Scope** | **Framework + adopter both.** | One-time decision avoids partial designs that conflict later. Framework's own use (LoreWeave case study) and adopter use (clone distribution → deploy AA on their project) covered in one debate. |
| **Lifecycle baseline** | D4 from Codex §8 — task-scoped instance + persistent role + artifact continuity. | Already sealed via debate 005; this debate operationalises D4, not redesigns it. |
| **Authority constraints** | Codex §3 Hard Stops + §7 Authority bounds (no vote / sign / block) — inviolate. | Sealed; deployment protocol must respect these. |
| **No adopter enforcement** | Per debate 006 §I0 + debate 007 §10: framework publishes spec; adopters fork freely; no upstream policing. | Deployment protocol is **prescription** (what we recommend) not **enforcement** (what we require). |

---

## 3. Sub-decision A — Bootstrap / session-start pattern

How does an Adeptus Administratum instance start? What's the "session start" event?

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **A1.** User initiates chat with explicit prime prompt ("read HANDOFF then re-prime per Codex §8") | Manual, fully user-driven | Simple; no scaffolding needed | Repetitive; easy to forget; not adopter-friendly |
| **A2.** Pre-built system prompt with Codex baked in | Project-level system prompt (Claude Code's CLAUDE.md, Cursor's `.cursorrules`, etc.) | Auto-activates per session; provider-specific files supported by most modern AI IDEs | Per-provider config files; needs maintenance when Codex evolves |
| **A3.** Slash command (`/aa-prime` or `/aa-start`) | User triggers explicit `/command` that loads context | Explicit invocation event; auditable; works with Claude Code slash commands; works with Cursor commands | Requires provider that supports slash commands |
| **A4.** Bootstrap script (`scripts/start_aa_session.py`) | CLI script outputs the priming prompt; user pastes into chat | Provider-agnostic; works even with raw API; auditable | Two-step (run script then paste); friction |
| **A5.** All of A2 + A3 + A4 (provider-tiered) | Provider-specific system-prompt files where supported (A2); slash command where supported (A3); bootstrap script as universal fallback (A4) | Maximum coverage; meets each provider where it is | Maintenance overhead across three deployment paths |

### Proposed answer

**Option A5 — provider-tiered, with A4 as universal fallback.**

Concretely:

- **For Claude Code (current default):** project-level `CLAUDE.md` at repo root contains a brief Adeptus Administratum prime + pointer to Codex (which Claude Code auto-loads per session). This already exists informally; debate 008 formalises it.
- **For Cursor:** project-level `.cursorrules` or equivalent file with the same content.
- **For Anthropic console / raw API:** `scripts/start_aa_session.py` prints the priming prompt to stdout; user pastes into their first message.
- **For slash-command-supporting providers:** optional `.claude/commands/aa-prime.md` slash command (parallel to existing `.claude/commands/ivp.md`).

The substantive content (the priming prompt) is **single-source-of-truth in `distribution/for-ai-aides.md`** — provider-specific files just include or reference it.

### Real-world precedent

- **Claude Code's CLAUDE.md convention** — auto-loaded per session; standard pattern.
- **Cursor's `.cursorrules`** — same pattern, different provider.
- **OpenAI's GPT custom instructions** — pre-built system prompt convention.
- **Cookiecutter's pre/post-generation hooks** — bootstrap-script pattern.
- **VS Code `.vscode/settings.json`** — project-level config that auto-activates per workspace.

---

## 4. Sub-decision B — Provider abstraction

Does the framework specify a provider, or stay provider-agnostic?

### Options

| Option | Stance | Pros | Cons |
|---|---|---|---|
| **B1.** Claude Code only (the only tested provider) | Concrete, supports current operation | Tested; no over-engineering | Locks adopters into Anthropic + Claude Code; not framework-neutral |
| **B2.** Provider-agnostic spec (any LLM with sufficient context window) | Abstract requirements, no provider name | Maximum portability; framework-neutral | Adopters get no concrete path; "sufficient context window" undefined |
| **B3.** Tiered support model (recommended) | A-tier Claude Code (primary; tested); B-tier other major LLMs with similar capability (GPT-4+ class, Gemini 2+ class); C-tier local LLMs (informational; no support guarantee) | Concrete primary + portable fallback; sets expectations honestly | More documentation; tier definitions can drift |

### Proposed answer

**Option B3 — tiered support.**

| Tier | Examples | Capability requirements | Framework support level |
|---|---|---|---|
| **A — Tested + supported** | Claude Code (Opus 4.x / Sonnet 4.x), Anthropic Workbench | ≥ 200K context window; tool use (file read/write, bash); markdown rendering; can hold Codex + Astronomican + artifact base in working memory | Framework tested against this tier; bugs in this tier are framework's concern |
| **B — Compatible (best-effort)** | OpenAI GPT-4 / GPT-4o / GPT-5 class, Google Gemini 2 / Gemini 3 class, Cursor with Claude/GPT backend | ≥ 128K context window; tool use OR file-attachment capability; markdown rendering | Framework spec applies; bugs are adopter's concern; PRs welcome to improve compatibility |
| **C — Informational (use at own risk)** | Local LLMs (Llama 3.1+, Mistral, DeepSeek), older API models | Lower context windows; partial tool use | No support guarantee; adopter likely needs to manually trim Codex / Astronomican for context |

### Real-world precedent

- **Browser compatibility matrices** (Caniuse.com, MDN) — same tiered-support pattern.
- **kubectl client version skew policy** — A-tier matched versions; B-tier ±1 minor; C-tier "best effort."
- **PostgreSQL extension compatibility** — same tiered approach.
- **Anthropic SDK supported model list** — explicit named-model support; analog at vendor level.

---

## 5. Sub-decision C — Session protocol (task boundaries)

When does "a task" start and end? Codex §8 D4 says "task-scoped instance" — but what's a task?

### Options

| Option | Task = ... | Pros | Cons |
|---|---|---|---|
| **C1.** One chat session = one task | Session start to session end | Natural boundary; matches how most users work | Long sessions span multiple logical tasks; re-priming once is risky |
| **C2.** User-marked task boundaries within a session | User signals "new task" → instance re-primes | Explicit; matches operational reality (multi-task sessions common) | Requires user discipline; easy to forget |
| **C3.** Script-detected boundaries | Bootstrap script emits "task-start" markers; closes when output committed | Auditable; matches Codex §6 Output Contract | Tooling overhead |
| **C4.** Hybrid — natural session start triggers re-priming; user-marked within-session task switches trigger re-priming refresh | Combination | Best fits real usage | More complex protocol |

### Proposed answer

**Option C4 — hybrid.**

- **Session start (Tier A/B):** first user message → instance runs Codex §8 re-priming protocol (full).
- **Within-session task switch:** user signals "new task" or clearly switches topic → instance runs **lightweight re-priming** (read latest commits since last task; refresh §8 step 5 inconsistency check; do NOT re-read full Codex unless content has changed).
- **Task end:** instance commits the task's output + audit-trail entry → task considered closed.

The "lightweight re-priming" is a new operational concept added by this debate; mirrors Codex §8 step 5 scoped-down to changed-since-last-task.

### Real-world precedent

- **Git commits as task units** — analog to "task = unit of work between commits."
- **Slack threads vs channels** — same hybrid: thread = within-task; channel = sessions.
- **Adobe Creative Cloud / Figma autosave per-action** — within-session granularity.
- **VS Code multi-root workspaces** — session-level vs project-level boundaries.

---

## 6. Sub-decision D — Authorization mechanism for `--apply` scripts

Codex §4 (v1.1) says write-script `--apply` invocation requires acknowledgment. HOW is acknowledgment communicated?

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **D1.** In-chat verbal "yes apply" / "go ahead" | User typed message authorises | Simple; matches current operational pattern | No persistent record; future audits can't easily verify "was this authorised?" |
| **D2.** Commit-as-authorization | Dry-run output committed → next `--apply` is authorised; if no dry-run commit precedes, instance refuses | Auditable; persistent | Adds friction; user must commit before applying |
| **D3.** Pre-authorized allowlist file (`.aa-authorize`) | Project root file lists scripts that are pre-authorised | Persistent; project-owner-controlled | Needs maintenance; allowlist drift |
| **D4.** Inline acknowledgment recorded in audit trail | Instance asks "shall I apply?"; user "yes"; instance writes audit-trail entry: `<timestamp> · project-owner authorised: scripts/X.py --apply` | Persistent; minimal friction; per-invocation auditable | Trust-based (no hard signature) |

### Proposed answer

**Option D4 — inline acknowledgment with audit-trail recording.**

- Instance produces dry-run output.
- Instance asks: "Approve `scripts/X.py --apply`?"
- User responds explicit acknowledgment ("yes", "apply", "go ahead", "approved", etc.).
- Instance writes a one-line audit-trail entry: `<YYYY-MM-DD HH:MM> · project-owner authorised: scripts/X.py --apply · context: <task summary>` in `methodology-notes.md` (case study) or `HANDOFF.md` § audit-trail (framework work).
- Instance runs `--apply`.

For repeated invocations within the same task (e.g., `release.py` orchestrating multiple `--apply` calls): one acknowledgment for the orchestrator covers all sub-script `--apply` calls within that single orchestration. Each sub-call is logged at audit-trail level for traceability.

Optional supplement: a project may add a `.aa-pre-authorized` file listing scripts always pre-approved (e.g., `validate_frontmatter.py --strict` always allowed because read-only). Default empty.

### Real-world precedent

- **sudo + sudoers** — per-invocation prompt + audit log.
- **OAuth 2.0 consent screens** — explicit per-scope acknowledgment + logged.
- **GitHub branch protection rules** — admin can pre-authorise certain checks; per-action prompts otherwise.
- **Cursor "agent mode" file-write confirmations** — per-action prompt with chat-history record.

---

## 7. Sub-decision E — Instance identity recording

Codex §6 requires a provenance line. WHERE concretely?

### Options

| Option | Recording location(s) | Pros | Cons |
|---|---|---|---|
| **E1.** Per-artifact frontmatter | Add `last_modified_by_instance` to each artifact touched | Most granular | Bloats frontmatter |
| **E2.** Per-session audit-trail file | Single audit-trail file logs all invocations | Centralised | Cross-references hard to verify |
| **E3.** Git commit trailer | `Instance: <provenance>` in commit message | Built-in git auditability | Chat-only work not captured |
| **E4.** Combined (E2 + E3 mandatory; E1 optional) | Audit-trail + commit trailer always; per-artifact frontmatter for high-stakes outputs | Comprehensive | More complex |

### Proposed answer

**Option E4 — combined.**

Mandatory:
- **Audit-trail file entry** — one line per task invocation: `<YYYY-MM-DD HH:MM> · instance: <provider/model/date> · Codex v<X.Y> · task: <summary>`.
- **Git commit trailer** — every commit gets `Instance: <provider/model/date> / Codex v<X.Y>` in the message body (separate from `Co-Authored-By` which serves provider attribution).

Optional (for high-stakes outputs only):
- Per-artifact frontmatter `last_modified_by_instance: <provenance>` on sealed artifacts (Astronomican, Codex), Codex amendments, and IVP findings files.

### Real-world precedent

- **`Signed-off-by:` Git commit trailers** (DCO / Linux kernel convention) — per-commit attribution.
- **GitHub Actions `actor` field** — recorded in audit log per workflow run.
- **AWS CloudTrail per-API-call user identity** — comprehensive recording.
- **Hospital electronic health records authoring attribution** — every entry has author + timestamp.

---

## 8. Sub-decision F — Inter-instance handoff signal

Codex D4 says artifacts ARE the handoff. But is there an explicit "WIP" or "next-task" indicator for cases where a task is paused mid-flight?

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **F1.** Strict — artifacts only, no extra signal | Each task fully completes or is reverted | Cleanest; on-thesis with D4 | No way to express "this task is paused" |
| **F2.** Optional `WIP.md` at repo root | Single file written when pausing mid-task | Simple; opt-in | Single-task scope only |
| **F3.** Per-task WIP files under `.aa-wip/` | Multi-paused-task support | Flexible | Folder management overhead; rare use case |
| **F4.** HANDOFF.md serves dual purpose (session-state + WIP section) | Reuses existing artifact | No new file; natural pickup by re-priming | Mixes two purposes |

### Proposed answer

**Option F4 — HANDOFF.md serves dual purpose.**

- Standard usage: HANDOFF.md captures session-end state (current pattern).
- WIP usage (new): if a task pauses mid-flight, an `## In-flight task` section appears in HANDOFF.md with one paragraph describing the in-flight state.
- The next instance reads HANDOFF.md as part of re-priming step 3 — naturally picks up WIP marker.
- On task completion, the `## In-flight task` section is removed.

Honours D4 (artifacts are continuity) without inventing new files. Mid-task pause is the exception, not the rule.

### Real-world precedent

- **Git stash + WIP commits** — same pattern; rare-use indicator.
- **Toggl's "active timer" UX** — single-current-task indicator.
- **Notion's "in progress" tag on Kanban** — single-purpose status marker.

---

## 9. Sub-decision G — IDE / tooling integration

What deployment surfaces does the framework support?

| Surface | Tier per B | Bootstrap mechanism | Operational reality |
|---|---|---|---|
| **Claude Code** (VS Code extension) | A | `CLAUDE.md` auto-loaded; `.claude/commands/` slash commands | Current default; framework tested here |
| **Cursor** | B | `.cursorrules` or equivalent project-level config | Should work; needs explicit testing |
| **Anthropic Workbench / console** | A | System prompt manually pasted from `distribution/for-ai-aides.md` | Works for single-task sessions |
| **Raw API (Anthropic / OpenAI / Google SDKs)** | B/C | `scripts/start_aa_session.py` outputs prime prompt; SDK user includes as system message | Provider-agnostic; adopter writes own session loop |
| **Local LLMs (Ollama, LM Studio, llama.cpp)** | C | Same as raw API + context-window trimming | Best-effort |
| **AutoGen / LangChain / LlamaIndex agent frameworks** | C+ | Adopter integrates Codex spec into agent's system prompt | Use-case-driven |

### Proposed answer

**Document the tier mapping above in `distribution/for-ai-aides.md` and a new `distribution/deployment-matrix.md`.** Per-tier integration notes describe what works out-of-box vs what needs adopter work.

No code changes required — the framework's published spec is provider-agnostic; the matrix just makes provider compatibility explicit.

### Real-world precedent

- **Compatibility matrix pages** — Kubernetes versions × cloud providers; React versions × Node.js; Spring Boot × JDK.
- **GitHub's marketplace integration tiers** — Verified / Community / Self-hosted.

---

## 10. Sub-decision H — Multi-project / Codex overrides

How does an instance know which project's Codex applies when operating across multiple projects?

### Options

| Option | Mechanism | Pros | Cons |
|---|---|---|---|
| **H1.** Each project has its own Codex instance | Adopter clones + customises locally | Maximum isolation | Codex divergence risk |
| **H2.** Single Codex applies framework-wide (current state) | One Codex; adopters reference it | Single source of truth | Doesn't fit multi-project deployments |
| **H3.** Workspace-aware auto-detect | Instance auto-detects from CWD | Automatic | Tooling complexity |
| **H4.** Hybrid — framework Codex as base + adopter overrides via `.aa-codex-overrides/` | Adopter additions, not replacements | Best of both; mirrors Imperial+Sector | Override-merge precedence rules needed |

### Proposed answer

**Option H4 — framework Codex as base + adopter overrides.**

- **Framework Codex** (`framework/chapters/adeptus-administratum/codex.md`) is the canonical spec.
- **Adopter projects** may add `.aa-codex-overrides/` folder with:
  - `additional-operational-bounds.md` — extra permissions (e.g., "may invoke project-specific tool X")
  - `additional-hard-stops.md` — extra restrictions (e.g., "MUST NOT modify legal/ folder")
  - `notify-trigger-extensions.md` — project-specific N-triggers
- **Override precedence:** framework Hard Stops are inviolate (cannot be relaxed); Operational Bounds may be EXTENDED but not REPLACED; notifies add to base.

Mirrors the **Imperial + Sector Astronomican** model from debate 001 — same fractal pattern applied to Codex governance.

### Real-world precedent

- **systemd unit overrides** (`/etc/systemd/system/*.d/override.conf`) — same precedence model.
- **Linux kernel config + per-distro patches** — base + adopter extensions.
- **Spring Boot autoconfigure + user `@Configuration` overrides** — same pattern.
- **Debate 001 Imperial + Sector** — framework's own established pattern; reapplying.

---

## 11. Sub-decision I — Adopter onboarding flow

### Proposed five-step adopter flow

1. **Clone distribution.** Adopter copies `distribution/` into their project (e.g., `their-project/dead-light/`).
2. **Pick a tier from sub-decision B.** Adopter declares which AI provider they'll use. Determines which bootstrap mechanism applies.
3. **Run `scripts/new_case_study.py` for their project.** Scaffolds `case-studies/<their-project>/` with the five standard files.
4. **Fill in `pm-threshold-decisions.md`** — adopter's first substantive engagement with the framework.
5. **Start their first Adeptus Administratum instance.** Per their chosen tier's bootstrap mechanism. First task: re-prime, read `pm-threshold-decisions.md`, propose Phase 0 Pass 1 plan.

These five steps go into `distribution/for-adopters.md` § Quickstart.

### Real-world precedent

- **`create-react-app` quickstart** — clone + run + edit + ship; 5-step pattern.
- **PostgreSQL pgAdmin install guides** — install + connect + create database + create user + grant.
- **GitHub repo creation flow** — same number of steps; similar abstraction level.

---

## 12. Sub-decision J — Failure modes + recovery

| Failure | Symptom | Recovery |
|---|---|---|
| **F-J1.** Re-priming step 5 detects inconsistency in artifact base | Instance flags before doing task | Emits N-3/N-4 notify; project owner adjudicates |
| **F-J2.** Script invocation crashes | Bash/Python error | Instance reports stderr verbatim; does not retry without authorization |
| **F-J3.** AI hallucinates a Hard Stop violation that isn't actually one | Instance refuses legitimate task | Project owner overrides ("this is not HS-N because <reason>"); logged in audit trail; framework reviewer revisits Codex wording in next debate |
| **F-J4.** AI fails to re-prime properly | Output missing provenance line or wrong Codex version | Project owner catches in review; instance re-runs re-priming; output rejected |
| **F-J5.** Provider tier mismatch — C-tier LLM can't hold full Codex | Incomplete outputs, missing notifies | Adopter informed they may need to trim Codex; framework provides documentation only |
| **F-J6.** Multi-project Codex override contradicts framework Hard Stops | Override file relaxes what can't be relaxed | `validate_frontmatter.py` (or new `validate_codex_overrides.py`) rejects load until reconciled |
| **F-J7.** Authorization for `--apply` recorded ambiguously | Audit trail entry unclear | Convention: every entry has script name + arguments + context; if ambiguous, instance asks for re-authorization with explicit invocation |

### Proposed answer

**Document the seven failure modes above in `distribution/deployment-matrix.md`.** Reviewer extends catalogue as new modes encountered.

For each F-JN: corresponding script-level test or operational check exists where mechanically detectable; remaining failures are reasoning-class and rely on framework discipline + project-owner adjudication.

### Real-world precedent

- **Site Reliability Engineering** (Google SRE book) — error budgets + failure-mode classification.
- **Aviation incident classification** (Reason's Swiss Cheese model) — layered failure analysis.
- **AWS Well-Architected Framework — Reliability Pillar** — explicit failure-mode taxonomy.

---

## 13. Real-world precedent — consolidated standards map

| Sub-decision | Industry standards informing the design |
|---|---|
| A. Bootstrap pattern | Claude Code CLAUDE.md; Cursor `.cursorrules`; OpenAI custom instructions; Cookiecutter hooks; VS Code workspace settings |
| B. Provider abstraction | Caniuse browser matrix; kubectl skew policy; PostgreSQL extension compat; Anthropic SDK named-model list |
| C. Session protocol | Git commits as task units; Slack threads vs channels; Adobe per-action save; VS Code multi-root |
| D. Authorization | sudo + sudoers; OAuth 2.0 consent; GitHub branch protection; Cursor agent mode confirmations |
| E. Instance identity | DCO `Signed-off-by:`; GitHub Actions actor; AWS CloudTrail; EHR authoring attribution |
| F. Handoff signal | Git stash; Toggl active timer; Notion in-progress tag |
| G. Tooling integration | Kubernetes × cloud matrix; React × Node compat; Spring × JDK; GitHub marketplace tiers |
| H. Multi-project Codex | systemd unit overrides; kernel + distro patches; Spring autoconfigure + overrides; debate 001 Imperial+Sector (framework's own) |
| I. Adopter onboarding | create-react-app; pgAdmin install; GitHub repo creation |
| J. Failure modes | Google SRE error budgets; Reason's Swiss Cheese; AWS Well-Architected Reliability Pillar |

---

## 14. Application to Dead Light Framework (sketch)

If debate 008 seals as proposed:

### Implementation Phase 1 — bootstrap + docs (immediate)

1. **Promote `CLAUDE.md` to formal framework artifact.** Add frontmatter; reference from Codex §8 step 1.
2. **Extend `distribution/for-ai-aides.md`** with deployment quickstart (5-step adopter flow per sub-decision I).
3. **Create `distribution/deployment-matrix.md`** — IDE/tooling tier mapping (sub-decision G) + failure modes catalogue (sub-decision J).
4. **Document multi-project override mechanism** — example `.aa-codex-overrides/` structure (sub-decision H).
5. **Codex v1.1 → v1.2 implementation-amendment** per precedent established in v1.1: add explicit references to `CLAUDE.md` / `for-ai-aides.md` / `deployment-matrix.md` in Codex §8 re-priming protocol.

### Implementation Phase 2 — tooling extensions (build on need)

6. **`scripts/start_aa_session.py`** — print priming prompt to stdout (universal fallback for A4/A5).
7. **`scripts/validate_codex_overrides.py`** — verify `.aa-codex-overrides/` files don't relax framework Hard Stops (F-J6).
8. **`.claude/commands/aa-prime.md`** — slash command for explicit prime invocation (sub-decision A3).

### Implementation Phase 3 — adopter testing (when first adopter arrives)

9. **Empirical validation:** when first non-framework-team adopter clones distribution, gather feedback. Iterate sub-decisions D/E/G based on real friction.

### Estimated effort

- Phase 1: ~3-5 person-hours (mostly documentation + Codex v1.2 patch).
- Phase 2: ~2-4 person-hours (scripts).
- Phase 3: deferred to first real adopter.
- **Total Phase 1+2: ~5-9 person-hours initial.**

---

## 15. Open questions remaining (carry forward if accepted)

1. **Provider compatibility testing matrix.** Should the framework run an automated compatibility-check suite against Tier A/B providers? Deferred; possible debate 010 if adopter need surfaces.
2. **Subscription / API cost considerations.** Adopters may have provider cost constraints; framework currently silent.
3. **Multi-instance concurrent operation.** Codex §8 says concurrent allowed; debate 008 doesn't specify coordination between concurrent instances.
4. **Adopter Codex versioning.** If framework Codex bumps v1.2 → v1.3, how does an adopter on `.aa-codex-overrides/` know to pull? Need version-skew policy.
5. **Local LLM minimum-capability spec.** B3 says "C-tier informational" but no hard floor.
6. **Compliance / audit-trail retention.** Per Codex §6, indefinitely (part of artifact continuity) — but adopters in regulated industries may have explicit retention requirements; framework defers.

---

## 16. Recommendation (TL;DR)

| Sub-decision | Recommended |
|---|---|
| A. Bootstrap | **A5** — provider-tiered: CLAUDE.md / `.cursorrules` (A2) + slash command (A3) + `scripts/start_aa_session.py` (A4) as fallback. Single-source in `distribution/for-ai-aides.md`. |
| B. Provider abstraction | **B3** — tiered: A Claude Code (tested); B GPT-4+ / Gemini 2+ / Cursor (best-effort); C local LLMs (informational). |
| C. Session protocol | **C4** — hybrid: session-start = full re-priming; within-session task switch = lightweight re-priming. |
| D. Authorization for `--apply` | **D4** — inline acknowledgment with audit-trail recording per invocation. |
| E. Instance identity recording | **E4** — audit-trail entry + git commit trailer (mandatory); per-artifact frontmatter (optional for high-stakes). |
| F. Handoff signal | **F4** — HANDOFF.md dual purpose (session-state + optional `## In-flight task`). |
| G. Tooling integration | **Tier mapping** in `distribution/deployment-matrix.md`: Claude Code A; Cursor B; raw API B/C; local LLM C; agent frameworks C+. |
| H. Multi-project / overrides | **H4** — framework Codex as base + `.aa-codex-overrides/` extensions. Hard Stops inviolate; Operational Bounds extendable. Imperial+Sector pattern at Codex level. |
| I. Adopter onboarding | **5-step quickstart** in `distribution/for-adopters.md`: clone → pick tier → `new_case_study.py` → fill `pm-threshold-decisions.md` → start first AA instance. |
| J. Failure modes | **7 failure-mode taxonomy** (F-J1..F-J7) in `distribution/deployment-matrix.md`. |

If approved, the framework gains a complete deployment story at both framework and adopter layers — parallel-to-debate-006 standardisation at the runtime layer.

---

## 17. Decision

- **Decision:** Approved per TL;DR §16 — all 10 sub-decisions A-J adopted as recommended. Codex amendment classified as **implementation amendment** per precedent established in Codex v1.0 → v1.1 (debate 007 seal), not requiring a separate debate.
- **Decided on:** 2026-05-13
- **Decided by:** project owner

### Follow-up actions

- [x] Update [framework/debates/README.md](README.md) — debate 008 marked decided.
- [x] **Phase 1 implementation:** `CLAUDE.md` at repo root (formal Adeptus Administratum bootstrap); `distribution/for-ai-aides.md` extended with deployment quickstart; `distribution/deployment-matrix.md` created (IDE tier mapping + 7 failure modes); `distribution/templates/aa-codex-overrides-example/` scaffolded; `distribution/for-adopters.md` extended with 5-step quickstart.
- [x] **Codex v1.1 → v1.2 implementation-amendment**: §1 Identity adds override mechanism reference; §8 re-priming step list adds explicit references to CLAUDE.md / for-ai-aides.md / deployment-matrix.md; §10 Provenance Version history table gains v1.2 entry.
- [ ] **Phase 2 implementation (deferred to build-on-need):** `scripts/start_aa_session.py`, `scripts/validate_codex_overrides.py`, `.claude/commands/aa-prime.md`.
- [ ] **Phase 3 implementation (deferred to first adopter):** empirical validation + iteration.
- [x] Update HANDOFF.md status table — add "Deployment protocol" row.
- [x] Sync distribution via `python scripts/sync_distribution.py --apply` (executed as part of `release.py minor --apply` v0.7.1 → v0.8.0 release).
- [x] Minor bump v0.7.1 → v0.8.0 via `python scripts/release.py minor --apply`.

---

## 18. Methodological note (forward-applying)

This debate establishes **the deployment layer** as a formal framework concern. Before debate 008, deployment was implicit (Claude Code in VS Code, just-do-it operation); after debate 008, it's a documented, tier-aware, override-supporting standard.

Three insights:

1. **The framework now has FIVE sealed-concern layers:**
   - Project governance (Phases 0/1 — debates 001-004).
   - Operational aide bounds (Adeptus Administratum Codex — debate 005).
   - Document architecture (debate 006).
   - Tooling infrastructure (debate 007).
   - **Deployment protocol** — debate 008.
   Each layer is "fractal" of the frozen-authority thesis: sealed authority, executor-friendly, survives any participant.

2. **Imperial + Sector pattern re-applies at the Codex level (sub-decision H).** Framework Codex as Imperial; adopter `.aa-codex-overrides/` as Sector. The framework's own design pattern (debate 001) keeps surfacing as the right answer at new layers — strong signal the pattern is genuinely structural, not coincidence.

3. **Deployment standardisation closes the outward-facing gap.** Debate 006 made the framework distributable; debate 007 made it tool-supported; debate 008 makes it deployable. Framework is now at "minimum viable for first adopter pilot" maturity.

A subtle observation: this debate was opened the same day it could seal. The framework has accelerated through debates 005, 006, 007, 008 in three days because the analytical machinery (debate template + Codex + scripts) is now in place. Future debates likely follow this faster cadence as the framework matures and the substrate work is done.

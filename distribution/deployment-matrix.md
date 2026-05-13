---
title: "Deployment Matrix — IDE / tooling integration + failure modes"
status: working
version: 0.8.0
audience: both
type: reference
last_updated: 2026-05-13
supersedes: null
sealed_by: debate-008
---

> **Status:** Sealed via debate 008 sub-decisions G + J on 2026-05-13.
> **Audience:** Both — framework adopters choosing a deployment surface; Adeptus Administratum instances triaging compatibility.
> **Purpose:** Tier-by-tier mapping of which AI providers / IDEs / tools support which framework features, plus the failure-modes catalogue and recovery paths.
> **Read next if:** you're deciding which AI provider to use for this framework, or you're an instance hitting an unexpected failure.

# Deployment Matrix

## 1. IDE / tooling integration (per debate 008 sub-decision G)

Provider compatibility expressed via three tiers (per sub-decision B):

| Surface | Tier | Bootstrap mechanism | Capability requirements | Notes |
|---|---|---|---|---|
| **Claude Code** (VS Code extension) | **A** — Tested + supported | `CLAUDE.md` at repo root auto-loaded; `.claude/commands/` slash commands available | ≥ 200K context window; full tool use (file read/write, bash); markdown rendering | Current framework default; reference implementation. Bugs in this tier are the framework's concern. |
| **Anthropic Workbench / console** | **A** | System prompt manually pasted from `distribution/for-ai-aides.md` | Same as Claude Code | Works for single-task sessions; less ergonomic for multi-task sessions where re-priming would help. |
| **Cursor** (with Claude/GPT backend) | **B** — Compatible (best-effort) | `.cursorrules` at repo root with priming content | ≥ 128K context window; agent mode for tool use | Should work; needs explicit testing. PRs welcome to improve. |
| **OpenAI ChatGPT custom GPT** | **B** | Custom GPT system prompt set from `distribution/for-ai-aides.md` | ≥ 128K context window; tool use via Actions or file attachments | GPT-4+, GPT-4o, GPT-5 class. Tool use is more constrained than Claude Code; some Tier 1 script invocations may need to run client-side. |
| **Google Gemini** (Workspace AI Studio / Vertex AI) | **B** | System instruction set from `distribution/for-ai-aides.md` | Gemini 2 Pro+ / Gemini 3 class; ≥ 128K context | Similar to ChatGPT — should work; tool use varies by integration path. |
| **Raw API** (Anthropic SDK / OpenAI SDK / Google Gemini SDK) | **B/C** | `scripts/start_aa_session.py` outputs prime prompt (when implemented); adopter writes own session loop | Provider-dependent | Adopter responsible for context management, tool wiring, and conversation history. Framework provides spec; adopter provides session loop. |
| **Local LLMs** (Ollama, LM Studio, llama.cpp, vLLM) | **C** — Informational (use at own risk) | Same as raw API + context-window trimming | Llama 3.1+ / Mistral / DeepSeek class; context ≥ 32K (preferably ≥ 128K) | No support guarantee. Adopter likely needs to manually trim Codex / Astronomican to fit; may need to drop audit history; outputs may miss notifies. |
| **AutoGen / LangChain / LlamaIndex** agent frameworks | **C+** — Informational | Adopter integrates Codex spec into their agent's system prompt | Provider-dependent | Use-case-driven. Framework provides spec only; adopter wires it into their multi-agent topology. |
| **Replit AI / Windsurf / JetBrains AI Assistant / GitHub Copilot Chat** | **C+** — Informational | Best-effort; adopter places priming prompt where supported | Provider-dependent | Not tested. Compatibility may be partial; some tool-use patterns won't work the same. |

### How to self-classify your stack

1. Check your provider's context window. If ≥ 200K and the provider is Claude Code or Anthropic Workbench, you're A-tier.
2. If ≥ 128K with tool use, you're B-tier.
3. Otherwise C-tier.

A-tier gets framework support guarantee. B-tier "should work; PRs welcome." C-tier is on your own.

### Per-tier integration notes

**A-tier (Claude Code reference):**
- Bootstrap: `CLAUDE.md` at repo root auto-loads.
- Slash commands: `.claude/commands/*.md` invoked via `/<command-name>` in chat.
- Tool use: full filesystem + bash + grep + web.
- Re-priming step 5: invoke `python scripts/validate_frontmatter.py` and `python scripts/check_links.py` directly.

**B-tier (Cursor / ChatGPT / Gemini):**
- Bootstrap: provider-specific config file (`.cursorrules`, custom-GPT instructions, system-instruction field) with content from `distribution/for-ai-aides.md`.
- Tool use: agent mode or function calling — depends on provider.
- Re-priming step 5: script invocation may need to happen out-of-band (adopter runs scripts locally and pastes output into chat). PRs welcome to add provider-specific shims.

**C-tier (raw API / local LLM):**
- Bootstrap: adopter writes session loop; includes prime prompt as system message.
- Tool use: adopter wires; framework provides no shims.
- Context budget: likely need to trim. Recommended: drop `framework/audit/` history; keep `framework/chapters/adeptus-administratum/codex.md` + `framework/phases/phase-0.md` + latest 2-3 decided debates + current task's case-study files.
- Re-priming step 5: skip mechanised; rely on AI self-checking; document the limitation.

---

## 2. Failure modes + recovery (per debate 008 sub-decision J)

Seven failure modes catalogued. Reviewer extends as new modes encountered.

### F-J1 — Re-priming step 5 detects inconsistency in artifact base

**Symptom.** Instance flags an inconsistency between Codex, Astronomican, and artifact base before beginning task work.

**Recovery.** Instance emits N-3 (citation misuse) or N-4 (term drift) non-blocking notify per Codex §5. Project owner adjudicates: (a) acknowledge + acceptable (proceed); (b) acknowledge + fix in this task (instance proposes fix; project owner approves); (c) acknowledge + defer (record for next IVP run).

### F-J2 — Script invocation crashes

**Symptom.** Bash / Python error during `scripts/X.py` invocation (file not found, dependency missing, regex bug, etc.).

**Recovery.** Instance reports stderr verbatim. Does NOT retry. Project owner diagnoses (could be: missing `pip install -r scripts/requirements.txt`, Python version mismatch, script bug). Instance resumes only after project owner acknowledges.

### F-J3 — AI hallucinates a Hard Stop violation that isn't actually one

**Symptom.** Instance refuses a legitimate task on misinterpreted Hard Stop grounds (e.g., refusing to edit a working draft because "it might violate HS-1" when HS-1 only covers sealed artifacts).

**Recovery.** Project owner explicitly overrides: "This is not HS-N violation because <reason>." Instance logs override in audit trail: `<timestamp> · project-owner override: <reason> · Codex section reviewed: §<N>`. Framework reviewer revisits Codex wording in next debate to tighten language.

### F-J4 — AI fails to re-prime properly

**Symptom.** Output missing provenance line, OR Codex version cited incorrectly, OR Operational Bounds clearly not respected.

**Recovery.** Project owner catches in review. Instance re-runs re-priming protocol. The output of the original (un-primed) attempt is rejected for the task. Audit-trail entry records the failed attempt.

### F-J5 — Provider tier mismatch

**Symptom.** Adopter using C-tier LLM that can't hold full Codex + Astronomican in context window. Outputs are incomplete; notifies missing.

**Recovery.** Adopter informed via this matrix that they're operating below A-tier capability. Options: (a) upgrade provider; (b) accept partial functionality; (c) manually trim framework context for each task (drop audit history; keep only current Phase docs + Codex + task files). Framework provides documentation only; no fix beyond that.

### F-J6 — Multi-project Codex override contradicts framework Hard Stops

**Symptom.** Adopter's `.aa-codex-overrides/additional-hard-stops.md` *relaxes* a framework Hard Stop (e.g., adopter writes "HS-3 attribution waived for this project"). Framework Hard Stops are inviolate per debate 008 sub-decision H4.

**Recovery.** When `scripts/validate_codex_overrides.py` is implemented (Phase 2): script detects relaxation and refuses to load overrides until reconciled. Until that script exists, manual review by project owner; instance reviews `.aa-codex-overrides/` content during re-priming step 1 and emits N-2 notify if contradiction spotted.

### F-J7 — Authorization for `--apply` recorded ambiguously

**Symptom.** Audit-trail entry for write-script invocation is unclear about what was authorised (e.g., "authorised release" without saying which version or which release command).

**Recovery.** Convention per debate 008 sub-decision D4: every audit entry has explicit script name + arguments + context. If an entry is ambiguous, instance MUST re-ask for authorization with explicit invocation in the question. Example: instead of "shall I apply the release?" → "shall I apply `python scripts/release.py minor --apply --description 'X'`?"

### Adding new failure modes

When a new mode is encountered, add an F-JN entry following the template:
- **Symptom.** What the project owner observes.
- **Recovery.** Step-by-step path back to clean state.

Each new mode goes into a debate (if structurally significant) or just this file (if operational).

---

## 3. Adopter onboarding flow (referenced from for-adopters.md § Quickstart)

See [`for-adopters.md`](for-adopters.md) § Quickstart for the 5-step adopter flow. Summary:

1. Clone `distribution/` into your project.
2. Pick a tier from §1 above.
3. Run `scripts/new_case_study.py <project-name>` for scaffolding.
4. Fill `case-studies/<project>/pm-threshold-decisions.md`.
5. Start your first Adeptus Administratum instance per your tier's bootstrap mechanism.

---

## 4. Multi-project Codex overrides (per debate 008 sub-decision H4)

Framework Codex (`framework/chapters/adeptus-administratum/codex.md`) is the canonical spec — the *Imperial* level.

Adopter projects may add `.aa-codex-overrides/` folder at their project root with:

- `additional-operational-bounds.md` — extra permissions for this project (extends, never replaces).
- `additional-hard-stops.md` — extra restrictions for this project (extends, never replaces).
- `notify-trigger-extensions.md` — project-specific N-triggers (extends).

**Override precedence rules:**

| Aspect | Framework Codex (Imperial) | Adopter overrides (Sector) |
|---|---|---|
| **Hard Stops** | Inviolate; cannot be relaxed | Add new HS-N; cannot remove existing |
| **Operational Bounds** | Define base permissions | May EXTEND with project-specific permissions; cannot REPLACE |
| **Notify Triggers** | Define N-1 through N-5 (Codex §5) | May ADD new N-N triggers; cannot remove or relax existing |
| **Authority bounds** | Inviolate (no vote / sign / block) | Cannot be loosened |

See [`templates/aa-codex-overrides-example/`](templates/aa-codex-overrides-example/) for a worked example.

The pattern mirrors **debate 001's Imperial + Sector Astronomican** model applied at the Codex level — framework's own design pattern recursively re-applied.

---

## 5. Versioning + compatibility

When framework Codex bumps (v1.1 → v1.2 → v2.0 etc.), adopter actions:

| Bump type | Adopter action |
|---|---|
| **Patch** (vX.Y.Z → vX.Y.(Z+1)) | No required action; pull updated Codex if convenient. |
| **Minor** (vX.Y.Z → vX.(Y+1).0) | Review release notes in `distribution/CHANGELOG.md`; pull updated Codex; verify `.aa-codex-overrides/` still semantically valid. |
| **Major** (vX.Y.Z → v(X+1).0.0) | Full review. Major bump implies a sealed-Law amendment or breaking structural change. Adopter may need to update overrides; re-validate Hard Stops compatibility; possibly re-prime existing instances. |

Adopters should subscribe to `distribution/CHANGELOG.md` updates (GitHub watch / repo email) to track version moves.

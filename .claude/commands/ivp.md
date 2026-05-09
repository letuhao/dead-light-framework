---
description: Run an Independent Verification Pass against Dead Light Framework docs
argument-hint: "[scope] e.g. all | phase-0 | phase-1 | debates | phases:1-3"
---

# Independent Verification Pass — Run

You are about to execute an **Independent Verification Pass (IVP)** against this repository. The full specification is in `docs/audit/independent-verification-pass-for-debate.md` — read it before doing anything else; do not paraphrase the rubric from memory.

## Arguments

`$ARGUMENTS` (may be empty). Interpretation:

- empty or `all` — run all 7 phases against every in-scope document.
- `phase-0` | `phase-1` | `debates` | `readme` | `glossary` | `calibration` | `pm-guide` — limit Phases 1–5 to the named subset; Phases 6–7 still operate on whatever was inventoried.
- `phases:N-M` (e.g. `phases:1-3`) — run only the specified phase range. Useful for resuming a partial run.

If the argument is unclear, ask the project owner with `AskUserQuestion` before proceeding. Do not guess scope.

## Mandatory pre-flight

1. Read `docs/audit/independent-verification-pass-for-debate.md` end-to-end. The rubric tables in section 4 are pre-registered and may not be modified during this run.
2. Confirm the working tree is on a branch suitable for an audit run (e.g. `audit/ivp-YYYY-MM-DD`). If on `main` or a feature branch, ask before continuing.
3. Confirm `docs/audit/` exists; create it if not.
4. Set today's date once at the start; reuse it for `findings-YYYY-MM-DD.md` and all access-date entries.

## Hard rules during the run (from spec § 2 + cross-cutting rules in § 4.1, v0.2)

- **Do not modify any file outside `docs/audit/`** during the run. Findings only; remediation is a separate downstream activity.
- **Symmetric search — MANDATORY for load-bearing.** For every load-bearing citation or claim, run both a confirming and a disconfirming query; record both outcomes. For non-load-bearing items, disconfirming is recommended but optional.
- **Primary-source read — MANDATORY for load-bearing citations.** A T2 textbook summary or T3 grey-literature secondary is *insufficient* grounds for `VERIFIED` on a load-bearing item. If primary cannot be reached (paywall, archive offline, language barrier), the verdict is `UNVERIFIABLE` until a future pass — no guess from secondary.
- **Audit trail mandatory.** No verdict without (file:line, query, source URL, access date, excerpt).
- **Falsifiability test** for every load-bearing claim. A claim flagged `UNFALSIFIABLE` by Phase 4 escalates by one severity level above its rubric base, except for explicitly definitional/conventional claims.
- **Tier-floor rule.** Load-bearing claims resting solely on T3 grey literature (no T1/T2 triangulation) are flagged at minimum `MEDIUM` regardless of T3 source accuracy.
- **No early termination** on CRITICAL findings — run all phases to completion.
- **No editorial.** State only what evidence supports. Recommended actions in the report are limited to `defer to project owner` or `obvious fix: <one sentence>`.
- **Tier sources** per the authority hierarchy in spec § 3. Industry-pragmatic mode is in effect: T1 includes ISO/IEC, IEEE, IAASB, NIST, peer-reviewed venues, *and* standards-body-owned commercial publishers (AXELOS, PMI, CMMI Institute, IFPUG, SEI). T3 grey literature is admissible but tier-floor rule above applies for load-bearing.

## Execution order

Run phases sequentially per the spec. Each phase writes its own file under `docs/audit/`.

1. **Phase 1 — Inventory** → `docs/audit/inventory.md` (four tables: Claims, Citations, Defined terms, Analogies). Use `Read` for full files and `Agent (Explore)` to parallelise across files. **Citation deduplication is mandatory** (spec § 5 Phase 1): each distinct entity gets one row with a `Locations` column listing every file:line. No judgement during this phase.
2. **Phase 2 — Citation Verification** → append to `docs/audit/findings-YYYY-MM-DD.md` under "Phase 2". Use `WebSearch` (confirming + disconfirming for LB) and `WebFetch` for primary sources. **Load-bearing items require primary-source read AND disconfirming query — both mandatory** (spec § 5 Phase 2 procedure steps 2 and 4). Apply rubric 4.2 plus cross-cutting rules from § 4.1 (`UNFALSIFIABLE` escalation, tier-floor rule).
3. **Phase 3 — Citation Appropriateness** → append under "Phase 3". For each verified citation, state actual scope vs framework use; apply rubric 4.3.
4. **Phase 4 — Argument Analysis** → append under "Phase 4". Toulmin decomposition + the fixed fallacy checklist + falsifiability test; apply rubric 4.4.
5. **Phase 5 — Internal Consistency** → append under "Phase 5". Term drift, decision-to-doc reflection, quantitative consistency, policy compliance, README link integrity.
6. **Phase 6 — External Benchmarking** → `docs/audit/benchmark.md`. Adjacent-frameworks, empirical evidence, counter-frameworks, gap matrix. Tier every source.
7. **Phase 7 — Synthesis Report** → finalise `docs/audit/findings-YYYY-MM-DD.md` with executive verdict, aggregate stats, severity-binned findings tables, disconfirming evidence, limitations, full audit trail.

## Reporting back

After each phase finishes, post a short status update to the user (one or two sentences) naming the phase and the headline counts (e.g., "Phase 2 done: 18 citations checked — 11 verified, 4 partial, 2 unverifiable, 1 contradicted"). Do not paste the full table into chat; the file is the source of truth.

When the full pass completes, summarise the executive verdict (≤ 5 sentences) and the count of CRITICAL and HIGH findings. Ask the project owner whether to proceed to remediation planning or to review the report first.

## When to stop and ask

Use `AskUserQuestion` (do not guess) when:
- A citation resolves only to T5 (unsourced) sources and the framework gives no other locator — confirm whether to mark `UNVERIFIABLE` or to widen the search.
- A claim's load-bearing status is genuinely ambiguous and would change the rubric application.
- The rubric appears to have a flaw mid-run — log it under Limitations and continue with the existing rubric; do not modify in-flight.
- A finding would be CRITICAL but rests on a single search that returned ambiguous results — confirm whether to broaden the search before sealing the verdict.

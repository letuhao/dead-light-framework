# Methodology Notes — LoreWeave Case Study

> **Status:** Accumulating during Phase 0 (2026-05-11 onward).
> **Purpose:** Record how the framework was applied to LoreWeave in practice, what diverged from spec, what was lossy, what was novel. Feeds the framework's next refinement cycle.
>
> This file is the equivalent of an IVP "Limitations of this audit" section but for the framework's own application against a real codebase — the gap between spec and execution.

---

## 1. Reviewer profile

- **Single human reviewer** (project owner) acts simultaneously as Reckoning Team member, PM, and Council. The framework's "Single-person reckoning" anti-pattern (Phase 0 §6) is **structurally** in play; mitigations are documented in [`reckoning-team-record.md`](reckoning-team-record.md) § "Single-reviewer risk acknowledgment".
- **AI-aide-1** (Claude Code Opus 4.7) serves as the outside-scope perspective per Phase 0 §7 accommodation, under the interim Codex captured in `reckoning-team-record.md`. Phase 2 of Dead Light Framework (Codex per Chapter) is not yet defined; this interim Codex will be superseded when Phase 2 lands.

---

## 2. Departures from Phase 0 spec (recorded as we hit them)

### 2.1 Reckoning Team kick-off as a half-day session vs asynchronous

Phase 0 §3 specifies a half-day Reckoning Team kick-off followed by parallel time-budgeted inventory work. For a solo project with one human + one AI-aide, this collapses to:

- **Kick-off** = a single chat session where project owner commits PM Threshold Decisions and confirms Pass 1 service selection.
- **Inventory work** = a sequence of read-only AI-aide investigations + project-owner-driven contributions over multiple chat sessions.

Severity of departure: **expected**, given solo + AI-aide structure. No spec violation; the spec already accommodates "team size permits" softeners.

### 2.2 Aggregation and cross-review

Phase 0 §3 specifies "Reckoning Team cross-reviews each other's areas." With one human + one AI-aide, cross-review means project owner reviews AI-aide drafts; the reverse (AI-aide reviewing project-owner-only sections) is also performed but **with no voting authority** per the interim Codex.

### 2.3 Council review session

Phase 0 §3 specifies the full Ascension Council reads the draft Reckoning Record before the review session and the Reckoning Team presents the four sections. For a solo project, "Council reads then questions Reckoning Team" collapses to a single chat session where the project owner reads the AI-aide-produced and project-owner-produced drafts side-by-side. The session ends when the project owner feels they have enough context to walk into Phase 1.

---

## 3. Observations on framework-versus-reality

_(Accumulates as Phase 0 runs.)_

### 3.1 What worked well in spec

_(To fill.)_

### 3.2 What was awkward or under-specified

_(To fill.)_

### 3.3 What was novel / unexpected

_(To fill. Especially any case where the framework's anti-patterns or failure-mode language proved sharper than expected at catching real LoreWeave issues.)_

### 3.4 What the framework missed

_(To fill. Real LoreWeave issues that don't fit any Phase 0 section cleanly.)_

---

## 4. Carry-forward to framework refinement

Items here become candidates for the next debate cycle on Phase 0 / Phase 1.

| # | Observation | Recommended next-cycle action | Priority |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | _to fill_ |

---

## 5. Carry-forward to LoreWeave's Phase 1

Items the Phase 0 audit surfaced that should be flagged when LoreWeave runs Phase 1. The Reckoning step (phase-1 §10.2) will pick these up.

| # | Item | Recommended Phase 1 disposition (Keep / Fix-now / Fix-by-date / Reconsider-Law) | Reasoning |
|---|---|---|---|
| _to fill_ | _to fill_ | _to fill_ | _to fill_ |

---

## 6. Audit trail for the case study itself

Every read of LoreWeave source, every grep, every git query, every command issued by AI-aide-1 is logged here for reproducibility. This is the case study's own audit trail (distinct from the Reckoning Record's evidence).

_(Accumulates as Pass 1 and Pass 2 run.)_

| Date | Action | Source / target | Output (link or summary) |
|---|---|---|---|
| 2026-05-11 | Created case-study folder skeleton | `docs/case-study-lore-weave/` | this commit |

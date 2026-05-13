---
title: "Debate 004 — Cap Revision: Miller Citation Correction"
status: decided
version: not versioned
audience: both
type: debate
last_updated: 2026-05-11
supersedes: null
sealed_by: self
---

# Debate 004 — Cap Revision: Miller Citation Correction (5±2 → 7±2)

> **Status:** decided.
> **Opened:** 2026-05-09
> **Decided:** 2026-05-09
> **Decided by:** project owner
> **Affects:** [phase-1-for-debate.md](../phases/phase-1-for-debate.md) §3 (Activities, Laws/Principles caps), §6 (Failure Modes, "more than N" threshold), §9 (Sector Astronomican local caps); [debate 001](001-laws-count-and-multirepo-scaling.md) Option A "Why it fails" rationale and Sector inheritance numerical cap.
> **Raised by:** Independent Verification Pass (IVP) — finding F-01 in [`framework/audit/findings-2026-05-08.md`](../audit/findings-2026-05-08.md). The IVP rodage on 2026-05-08 verified that the framework's cited authority for the "≤ 5 Laws / ≤ 5 Principles" cap — Miller (1956) "working-memory range, ~5 ± 2" — was a misquote of the original source.

---

## Context

The IVP run on 2026-05-08 (Phases 1–2, see findings file referenced above) flagged a CONTRADICTED verdict on citation `R-014`. Specifically:

- Framework text in [debate 001 §32](001-laws-count-and-multirepo-scaling.md#L32) reads: *"the '≤ 5' cap is not arbitrary. It is grounded in cognitive load and recall (Miller's working-memory range, ~5 ± 2)."*
- Miller's 1956 paper is *"The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information"* — the central finding is **7 ± 2**, not 5 ± 2.
- The closer-to-5 figure (~4 ± 1) is from Cowan (2001), *"The magical number 4 in short-term memory"*, *Behavioral and Brain Sciences* — a different paper, different author, different theoretical claim.

The framework was therefore citing the wrong paper for its number. Either the cap should move toward the source actually being used (Miller's central 7), or the citation should be replaced (Cowan, 4 ± 1). The project owner chose the first.

This is a **citation-correction debate**, not a free re-design of the cap. The framework-wide policy ("industry standards over framework-invented formulas") obliges Dead Light to align numbers with cited sources, not the other way around.

---

## The question

Given that the cited authority (Miller 1956) supports 7 ± 2 and not 5 ± 2, how should the cap on Immutable Laws and Guiding Principles be re-stated to remain consistent with its real-world anchor?

Three options were considered:

| Option | Cap structure | Notes |
|---|---|---|
| **A.** Replace citation with Cowan 2001 (≈ 4 ± 1) | Keep ≤ 5 cap; cite Cowan instead of Miller | Mathematically clean — 5 sits at upper bound of Cowan's range. Loses the "memorable seven" cultural anchor (lists, phone numbers, etc.). |
| **B.** Move cap to Miller's central value | ≤ 7 cap | Restores citation accuracy; keeps a single hard cap. Step-change of +2 from current. |
| **C.** Move cap to a range with target | 5–9 (hard upper 9, soft target ~7, informal floor 5) | Restores citation accuracy and uses the full Miller range. Most flexible — small projects can stay at 5–6, large at 8–9. Adds slight interpretation surface (which number to use). |

---

## Real-world anchor

### Miller 1956 — the actual cited paper

George A. Miller, *"The Magical Number Seven, Plus or Minus Two,"* *Psychological Review* 63(2): 81–97. The empirical claim is that the average human can hold ~7 chunks (range 5–9) in short-term memory at once. This is the most-cited cognitive psychology paper for working-memory limits and remains the canonical lay-citation for "small list of binding items".

### Cowan 2001 — the alternative

Nelson Cowan, *"The magical number 4 in short-term memory: A reconsideration of mental storage capacity,"* *Behavioral and Brain Sciences* 24(1): 87–114. Cowan argued that, controlling for chunking and rehearsal effects, the underlying capacity limit is closer to 3–5 chunks. This is the more current academic position but is less recognizable to non-specialist readers.

### Comparative anchors (group sizes the framework already uses)

| Anchor | Where used in the framework | Source value | Comment |
|---|---|---|---|
| Council size 3–7 | [phase-1 §8.1](../phases/phase-1-for-debate.md), [calibration-standards.md §C](../calibration-standards.md#c-team-sizing-and-composition) | Brooks (1975) communication channels + Dunbar layer 1 (≤ 5 intimate) | Council cap is for *group decision quality*, not *item recall*. Different cognitive construct from Laws cap. **Not affected by this debate.** |
| Reckoning Team 2–5 | [phase-0 §2](../phases/phase-0.md) | Same as Council | Same. **Not affected.** |
| Brooks N(N−1)/2 channels | calibration-standards.md §C | Brooks 1975 | Argues *against* large groups, not *for* a specific items-cap. **Not affected.** |
| AWS Leadership Principles (16) | [debate 001 §35](001-laws-count-and-multirepo-scaling.md) | "criticized for being too many to internalize" | Still works as outer bound — 9 < 16. The argument "16 is too many" is preserved. |

### Real-world precedent for "small numbered list of binding items"

Examples across organizations roughly cluster at 5–10 — consistent with Miller's range:

- **Ten Commandments** — 10. (Religious; outside cognitive-psych scope but still a recognized memorable count.)
- **Boy Scout Law** — 12 points. (Pushes toward AWS-LP-style criticism; widely held to be too many to remember in order.)
- **Toyota TPS principles** — varies 5–14 depending on framing; the core "Toyota Way" framing is **2 pillars × 5 underlying values = 10**, but no single canonical "10 principles" list — operators rely on the 2 pillars, not full enumeration.
- **AWS Leadership Principles** — 16. Acknowledged externally as too many to internalize ([debate 001 §35](001-laws-count-and-multirepo-scaling.md)).
- **NASA Mission Operations rules** — sub-grouped, never a single recallable list.
- **Google's "10 things we know to be true"** — 10. Famously hard for Google staff to recall in order without prompts.

Pattern: 5–9 appears to be the empirical sweet spot for *recallable lists*. Above 10, organizations tend to rely on grouping/categorization rather than flat memorization. The framework's hard cap should sit *inside* Miller's range, not above it.

---

## Proposed answer (recommended)

**Option C — 5–9 range, target ~7.** The exact wording adopted into the framework:

> **Maximum 9 Immutable Laws** (hard cap; Miller 1956 upper bound).
> **Target ~7** (soft target; Miller's central value).
> **Below 5** is permissible for narrowly-scoped projects but should be checked: under-counting may indicate the team has not yet drafted enough or has merged distinct concerns into a single Law. Below-5 lists are not auto-padded.
> **Same caps apply to Guiding Principles.**

The cap is *bounded by the source*: anything above 9 leaves Miller's range and re-enters AWS-Leadership-Principles territory of "too many to recall." Anything below 5 is allowed but flagged for review.

---

## Why this works

- **Citation accuracy restored.** Framework now cites Miller 1956 for a number Miller actually proposed (7 ± 2 → 5–9 range; central 7).
- **Recall is preserved.** Within Miller's range, recall is achievable for a typical reader; the framework's "recite without reading" Phase 1 quality gate still holds at 7 and remains feasible at 9 with effort.
- **Discipline is preserved.** The cap still binds — moving from 5 to 9 is not "no cap"; it is a +4 ceiling shift, still well below the AWS-LP threshold of 16 that debate 001 used as the negative anchor.
- **Flexibility for project scale.** Small / narrow projects can run with 5; large projects (e.g., LoreWeave with 6 services) have headroom up to 9 without splitting into Sector Astronomicans prematurely.
- **Goodhart's-Law-style argument preserved.** Adding items beyond 9 still breaks recall by Miller's own range — the cap remains principled.
- **AWS-LP critique preserved.** 9 < 16, so the framework's own argument against AWS-LP-count remains internally consistent.

## Why range, not a single number

Using a range (5–9 with target 7) instead of a single number (e.g., ≤ 7) was preferred because:

- A single hard cap of 7 would force a step-jump from 5 to 7 with no intermediate flexibility.
- Cap is meant to *bind against bloat*, not to legislate exact counts; project context determines whether 5 or 8 is right.
- Miller's range is itself a range, not a point estimate. Citing the source faithfully means honouring the range.

Trade-off accepted: slight interpretation surface added — projects must decide where in 5–9 they sit. This is an explicit Council judgement, and is recorded in the Astronomican itself when sealed.

---

## Consequential edits (applied alongside this decision)

- [phase-1-for-debate.md](../phases/phase-1-for-debate.md) §3 Activities — "Maximum five Immutable Laws" → "Maximum 9 Immutable Laws (target ~7)". Same for Guiding Principles.
- [phase-1-for-debate.md](../phases/phase-1-for-debate.md) §6 Failure Modes — "More than 5 Laws or 5 Principles" threshold → "More than 9 Laws or 9 Principles".
- [phase-1-for-debate.md](../phases/phase-1-for-debate.md) §9 Sector Astronomican — "Adds up to 5 local Laws and 5 local Principles" → "Adds up to 9 local Laws and 9 local Principles (target ~7)". Inheritance rule (cannot relax Imperial; can only tighten or add) is unchanged.
- [debate 001](001-laws-count-and-multirepo-scaling.md) §32 — "Miller's working-memory range, ~5 ± 2" → "Miller's working-memory range, ~7 ± 2".
- [debate 001](001-laws-count-and-multirepo-scaling.md) §165 (nested Sector code block) — "≤ 5 Imperial Laws" → "≤ 9 Imperial Laws (target ~7)". Same for Sector and Principles.
- [debate 001](001-laws-count-and-multirepo-scaling.md) Methodological note — adds a second methodological note recording this citation correction.

These are mechanical follow-throughs of this decision and are committed in the same change set so the framework is internally consistent at the moment debate 004 lands.

---

## What did *not* change

- **Council size** stays 3–7 (anchored on Dunbar layer 1 + Brooks's law for *group* dynamics, not Miller for *item* recall).
- **Reckoning Team size** stays 2–5 (same anchor as Council).
- **Stress-test divergence threshold** stays < 20% (separate calibration; unrelated).
- **Strangler Fig / retrofit / Phase 0** — entirely untouched.
- **40k-as-naming-only policy** — entirely untouched. (This debate is the second instance of the framework self-correcting a citation; the first was the 40k-justification removal in [debate 001](001-laws-count-and-multirepo-scaling.md)'s Methodological Note. The pattern holds: citations are checked, errors are surfaced explicitly, framework is updated.)

---

## Decision

- **Decision:** **Option C — 5–9 range, target ~7.** Hard cap 9; soft target ~7; below 5 permitted with review.
- **Decided on:** 2026-05-09
- **Decided by:** project owner
- **Citation now accurately reads:** Miller, G. A. (1956), *"The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,"* *Psychological Review* 63(2): 81–97.
- **Cowan 2001** is acknowledged in this debate as an alternative anchor but is not adopted; the framework retains Miller as primary citation by project-owner choice.

### Follow-up actions

- [x] Apply consequential edits listed in "Consequential edits" above (same change set).
- [x] Update [debates/README.md](README.md) index to add this debate as `decided`.
- [x] Update [findings-2026-05-08.md](../audit/findings-2026-05-08.md) status of finding F-01 — recorded in the next IVP run rather than in the audit file itself (audit files are append-only per IVP separation-of-concerns).
- [ ] Re-run IVP Phase 2 against the changed text to confirm the citation now matches; deferred to next IVP cycle.

---

## Methodological note (forward-applying)

This debate is the **second self-correction** in the framework's history (the first being [debate 001](001-laws-count-and-multirepo-scaling.md)'s removal of 40k-as-justification, recorded in its own Methodological Note). The pattern that emerges:

1. The framework cites real-world authorities.
2. Independent verification (here: IVP rodage) checks whether the citations match the sources.
3. When a mismatch is found, the framework either (a) corrects the number to match the source, or (b) replaces the citation with one that supports the number used. **It does not retain a citation that contradicts its source.**

This is the operational meaning of the framework-wide policy: *"industry standards over framework-invented formulas."* Numbers anchor to documented practice, and when documented practice and the framework's text drift apart, the framework's text yields.

The IVP audit workflow ([`framework/audit/independent-verification-pass-for-debate.md`](../audit/independent-verification-pass-for-debate.md)) will be re-run periodically to keep the framework honest in this respect.

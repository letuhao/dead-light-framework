# Debate 001 — Laws Count Cap and Multi-Repo Scaling

> **Status:** decided.
> **Opened:** 2026-05-08
> **Decided:** 2026-05-08
> **Decided by:** project owner
> **Affects:** [phase-1-for-debate.md](../phase-1-for-debate.md), specifically the "≤ 5 Immutable Laws" and "≤ 5 Guiding Principles" caps.
> **Raised by:** project owner during Phase 1 debate.

---

## The Question

The Phase 1 draft caps both Immutable Laws and Guiding Principles at five. What happens when a project is large enough to span multiple repositories, multiple services, or multiple product domains?

Two candidate fixes were proposed:

- **A.** Increase the cap (5 → 10 → 15) so a single Astronomican can carry more concerns.
- **B.** Split into multiple smaller Astronomicans, one per repo / service / domain.

Both are debated below, alongside a third option that emerged from the analysis.

---

## Option A — Increase the cap

**Why it sounds reasonable**
- Larger projects have more concerns.
- Five Laws may exclude critical domain-specific items.

**Why it fails**
- The cap is grounded in cognitive load and recall — **Miller's (1956) working-memory range, ~7 ± 2** (*"The Magical Number Seven, Plus or Minus Two"*, *Psychological Review* 63: 81–97). An earlier draft of this debate misquoted Miller as "~5 ± 2"; the misquote was caught by the IVP audit on 2026-05-08 (finding F-01) and corrected. The cap itself was subsequently revised to **5–9 with target ~7** (within Miller's range) in [debate 004](004-cap-revision-miller-correction.md). The arguments below — which reject *uncapped* increase to 10–15 — remain valid for that range; debate 004 supersedes only the original "≤ 5" specific number.
- The Phase 1 quality gate "recite without reading" breaks at 10+ items, and is impossible at 15.
- Each added Law is an additional interpretation surface — divergence in the stress test grows with item count.
- The purpose of the Astronomican is *to bind*. The longer the document, the fewer people read it carefully, the less it binds. By analogy to Goodhart's Law (Charles Goodhart, 1975 — "when a measure becomes a target, it ceases to be a good measure"), optimizing one document property (comprehensiveness) at the cost of another (recallability) backfires; the underlying memorability bound is **Miller's working-memory range** cited above. Goodhart's actual scope is measure-as-target perversities; the application here is the analogy, not the law itself.
- Real-world precedent: AWS Leadership Principles has 16 items (originally 14, two added in 2021) and is widely critiqued — by external commentary and inside-Amazon-adjacent practitioners — as too many to internalize at speed. The qualifier is "widely critiqued" rather than "official internal criticism" because there is no public Amazon document acknowledging this critique formally.

**Verdict:** Increasing the cap defeats the framework's recall and binding premises. **Reject.**

---

## Option B — Flat split into many small Astronomicans

**Why it sounds reasonable**
- Each repo / service has its own context.
- Local teams own local concerns.

**Why it fails**
- This is the failure mode of the United States under the **Articles of Confederation** (1781–1789): each state held sovereign authority with no enforceable federal level above. Coordination on currency, defense, and interstate commerce broke down within years; the Constitutional Convention was convened explicitly to fix it.
- Same pattern in the late Holy Roman Empire — nominal central authority over hundreds of de facto sovereign principalities, persistent fragmentation until dissolution in 1806.
- More recently, Yugoslavia after Tito: federation without a credible binding authority above the constituent republics, which fractured violently in the 1990s.
- Cross-repo decisions have no anchor — each team interprets per its own Astronomican, and drift accumulates across the org.
- Dead Light exists to defend against fragmentation, not to manufacture it.

**Verdict:** Flat split recreates the failure mode that constitutional federations were invented to prevent. **Reject.**

---

## Option C — Hierarchical: Imperial + Sector Astronomicans

This is the recommendation. It borrows from established precedent rather than inventing structure.

### Precedent (real-world systems with this structure)

| Source | Structure | Track record |
|---|---|---|
| United States constitutional federalism | Federal Constitution + state constitutions; Supremacy Clause prevents states from contradicting federal law. | Stable since 1789 (with one civil war as a known stress event). |
| German cooperative federalism | Basic Law (Grundgesetz) + Länder constitutions; concurrent powers explicitly enumerated. | Stable since 1949. |
| Catholic Church | Canon Law (universal) + diocesan and parish-level customs within canon limits. | ~1.4 billion members worldwide (1.422 billion at end of 2024 per *Annuario Pontificio* 2026), present in essentially every country with the Vatican holding diplomatic relations with 180+ states; institutional continuity ~2,000 years (despite the Great Schism of 1054 and the Reformation of 1517 producing the Eastern Orthodox and Protestant traditions, the Roman Catholic legal-doctrinal continuity itself is uninterrupted). |
| Linux kernel | Kernel-wide coding standards + per-subsystem maintainer rules. | 30+ years, 10,000+ contributors, no schism. |
| Toyota Production System | TPS principles (corporate, immutable) + plant-level kaizen within TPS frame. | 70+ years across global manufacturing footprint. |
| AWS | Leadership Principles (corporate-wide) + per-team Tenets. | Corporate-scale precedent; deliberately scoped to avoid Tenets contradicting Principles. |
| Spotify model | Tribe Mission + Squad missions. | Industry-cited even though Spotify itself has since modified the model — the two-tier pattern persists. |

### Proposed structure

```
Imperial Astronomican (project / org level)
  ≤ 9 Imperial Laws (target ~7)        — bind EVERY sector
  ≤ 9 Imperial Principles (target ~7)  — guide EVERY sector
  Imperial Boundaries

  └── Sector Astronomican (per repo / service / domain)
        Inherits all Imperial Laws (immutable; cannot be relaxed)
        Adds ≤ 9 Local Laws (target ~7; cannot contradict Imperial)
        Adds ≤ 9 Local Principles (target ~7)
        Sector Boundaries
        Sector Ascension Council (subset of Imperial Council + local leads)
        Sector Re-consecration scope (limited to local)
```

### Core rule

> **Sectors inherit and add — never relax.**
> A Sector Law cannot be softer than the Imperial Law it descends from. It may be stricter.

### Why this works

- **Cognitive load stays bounded.** At any level a participant carries the local caps (≤ 9 Laws + ≤ 9 Principles, each typically ~7 per [debate 004](004-cap-revision-miller-correction.md)) in working memory; inherited Imperial Laws are glanced at when needed, not memorized fresh.
- **Hierarchical authority is explicit.** Imperial Council can override Sector decisions; the reverse is impossible.
- **Local autonomy is real.** A Sector team adds local concerns without needing Imperial approval.
- **No cross-org drift.** Imperial Laws still bind everyone, regardless of how many Sectors exist.

---

## When does a project trigger Sector splitting?

Default: **single Astronomican.** Do not split early.

A project should adopt Sector Astronomicans only when **all** of the following are true:

- ≥ 2 repos / services that deploy independently
- Each repo has a dedicated team or on-call rotation
- Cross-team contracts (API, schema) exist and must be negotiated
- Genuinely local decisions exist that the Imperial Council should not be making

Below this threshold:
- Monorepo with one team → **do not split.** Use Codex per Chapter for agent governance and ADRs for tech specifics.
- Single service with many modules → **do not split.**

---

## Naming proposal

**Sector Astronomican.** "Sector" is a generic organizational term used in militaries, economies, and federations — it carries the right semantic load (a defined sub-area of a larger whole) without requiring any specific cultural context. Combined with "Astronomican" it stays consistent with the framework's existing vocabulary.

Alternatives considered and rejected:

| Name | Rejected because |
|---|---|
| Sub-Astronomican | Flat and unevocative; reads as a versioning suffix. |
| Domain Charter | Generic methodology language; loses continuity with the framework's vocabulary. |
| Local Astronomican | Suggests the local artifact replaces the global one rather than nesting under it. |
| Sector Charter | Mixes vocabularies (charter is a methodology term; Astronomican is the framework's term). |

---

## Application to LoreWeave

LoreWeave currently has at least six services in `contracts/api/`: identity, books, catalog, model-billing, model-registry, sharing.

This is the textbook trigger condition for Sector Astronomicans:
- One Imperial Astronomican for the LoreWeave platform (e.g. canon integrity, single knowledge gateway, author owns narrative, …).
- Sector Astronomicans for individual service clusters where genuinely local concerns exist (e.g. identity vs catalog have very different concerns about data sensitivity, latency, and consistency).

Hypothesis: part of LoreWeave's repeated scope changes may stem from having no tier separation — every decision lands at the same level, so every change is felt across the whole platform. A hierarchical structure would localize most changes to the Sector level and leave the Imperial core untouched.

---

## Impact on Phase 1

If the Sector tier is accepted, Phase 1 must address:

- Phase 1 runs at the **Imperial level first** (mandatory).
- Sector Phase 1 runs only **after** the Imperial Astronomican is sealed (ordering cannot be reversed).
- Re-consecration at the Sector level **does not** require convening the Imperial Council.
- Re-consecration at the Imperial level **invalidates** all Sector inheritance and forces every Sector to re-review.

The Phase 1 draft will need a "Sector variant" subsection covering the same activities with adjusted inputs (Imperial Astronomican already exists) and roles (Sector Council = subset of Imperial Council + local leads).

---

## Open questions remaining (carry forward if accepted)

1. **More than two tiers?** Could the framework allow Imperial → Sub-sector → Sector → … ? Recommendation: **no.** Two tiers cover ~99% of cases. Three or more tiers tend to reproduce known historical drift patterns: the late Roman Empire's reforms (Praetorian Prefectures → Dioceses → Provinces) had decreasing central control at each step; the Holy Roman Empire (Empire → Imperial Circles → Principalities → Imperial Cities) was chronically dysfunctional with no level able to enforce against the others; the Soviet system (Union → Republics → ASSRs → Oblasts → Raions) showed cumulative attenuation that contributed to coordination failure in late stages.
2. **Inter-Sector conflict.** Two Sectors hold local Laws that contradict each other but not Imperial. Resolution path? Proposed: escalate to Imperial Council; leave unresolved if there is no cross-impact.
3. **Late-added Sector.** A team wants to add a Sector six months after Imperial sealing. Same Phase 1 process? Proposed: yes, but with the Imperial Astronomican as a fixed input, not subject to debate.

---

## Recommendation (TL;DR)

- **No** — do not raise the cap above 5.
- **No** — do not flat-split into independent Astronomicans.
- **Yes** — adopt the hierarchical Imperial + Sector model with the inherit-and-add rule.
- **Trigger** — split into Sectors only when multi-repo + dedicated teams + cross-team contracts + genuinely local decisions are all present.
- **Default** — single Astronomican; do not split early.

---

## Decision

- **Decision:** Adopt **Option C — Hierarchical Imperial + Sector Astronomicans** with the inherit-and-add rule. Default is single Astronomican; split only when all trigger conditions are met.
- **Decided on:** 2026-05-08
- **Decided by:** project owner
- **Follow-up actions:**
  - [x] Update [phase-1-for-debate.md](../phase-1-for-debate.md) with a Scaling section covering Imperial and Sector variants and the ordering rule (Imperial before Sector).
  - [x] Update [debates/README.md](README.md) index to status `decided`.
  - [ ] When mapping to LoreWeave, evaluate whether its current 6 services in `contracts/api/` warrant Sector Astronomicans or whether a single platform Astronomican is sufficient at this stage.

## Methodological note (applies forward to all framework analysis)

Justification in this debate originally cited Warhammer 40,000 lore (Horus Heresy, Imperium drift modes) as evidence. That citation was removed because **fictional settings do not constitute evidentiary precedent**. Going forward in Dead Light Framework documentation:

- Warhammer 40,000 vocabulary (Astronomican, High Lords, Chapters, Codex, Heresy, Sector, …) is used purely as **naming and shared metaphor** — chosen for memorability and identity.
- All justification, structural arguments, and assessments of effectiveness must rest on **real-world organizational systems with observable track records** — constitutional federalism, religious institutions, military doctrine, established corporate practice, open-source governance, established software methodologies, and similar.
- Where the 40k name and the real-world precedent diverge in implication, the real-world precedent governs the design; the name is then either kept as flavor or revised.

## Methodological note 2 — Miller citation correction (added 2026-05-09)

The Independent Verification Pass on 2026-05-08 ([findings](../audit/findings-2026-05-08.md), finding F-01) flagged that the line above which now reads "~7 ± 2" was originally written as "~5 ± 2" and attributed to Miller (1956). Miller's actual finding is 7 ± 2; the closer-to-5 figure (~4 ± 1) is from Cowan (2001). The framework had been citing the wrong source for its number.

The correction was made in two parts:

1. **Citation text** (this debate, the bullet above) corrected to Miller 7 ± 2.
2. **Cap value** (Phase 1 §3 and §9; this debate's Sector code block) revised from a fixed "≤ 5" to a Miller-aligned range "5–9 with target ~7" via [debate 004](004-cap-revision-miller-correction.md).

This is the second self-correction recorded in this file (the first being the 40k-justification removal in the methodological note above). The pattern stands: when the framework's text drifts from its cited source, the framework's text yields. This is the operational meaning of the policy *"industry standards over framework-invented formulas."*

---
title: "Astronomican Template"
status: fillable
version: not versioned
audience: human
type: template
last_updated: 2026-05-13
supersedes: null
sealed_by: null
---

> **Status:** Fillable template — copy into your project and fill the placeholders marked `<...>`.
> **Audience:** Project Council sealing Phase 1.
> **Purpose:** The sealed Astronomican v1.0 artifact your project produces at Phase 1 sealing.
> **Read next if:** you've completed Phase 1 stress-testing and are ready to seal.

# The Astronomican — <project name>

> **Version:** 1.0
> **Sealed on:** <YYYY-MM-DD>
> **Sealed by:** <Ascension Council Record reference — see ascension-council-record.md>
> **Hash / signed tag:** <signed git tag or hash-pinned commit identifier>

---

## 1. The Purpose

<One sentence. Why does this project exist? Pass the "recite without reading" test — every Council member can state this from memory.>

---

## 2. Immutable Laws

> **Hard cap:** 9 Laws (target ~7), per debate 004 anchored on Miller 1956's working-memory range. Below 5 permitted for narrowly-scoped projects but Council should test whether the team has merged distinct concerns into a single Law.

### Law 1 — <name>

**Statement.** <one-paragraph normative statement of the Law.>

**Violation example.** <concrete example of behaviour that would violate this Law.>

**Compliance example.** <concrete example of behaviour that satisfies this Law.>

### Law 2 — <name>

**Statement.** <...>

**Violation example.** <...>

**Compliance example.** <...>

<!-- Add more Laws up to hard cap 9. Each Law has Statement + Violation example + Compliance example per phase-1 §5 quality gates. -->

---

## 3. Guiding Principles

> **Hard cap:** 9 Principles (target ~7). Same anchor as Laws.

### Principle 1 — <name>

**Intent.** <what this Principle aims to preserve or encourage.>

**Direction.** <how to apply it concretely; allows interpretation as context shifts.>

### Principle 2 — <name>

**Intent.** <...>

**Direction.** <...>

<!-- Add more Principles up to hard cap 9. Each Principle has Intent + Direction per phase-1 §5 quality gates. -->

---

## 4. Boundaries — what this project is NOT

> **Minimum:** at least 3 explicit out-of-scope items per phase-1 §5 quality gates. Framework-internal floor; Council may raise.

- <out-of-scope item 1: explicit statement of what the project will NOT do.>
- <out-of-scope item 2.>
- <out-of-scope item 3.>
- <... more as needed for project clarity.>

---

## 5. Stress Test Log reference

The scenarios run during the Phase 1 sealing session, with divergence rate, are recorded in `stress-test-log.md` (separate document). Divergence rate at sealing: **<X%>** (must be < 20% per phase-1 §5 quality gate; anchored on Cohen 1960 kappa).

---

## 6. Re-consecration

This Astronomican is **sealed** as of the date above. It cannot be amended without invoking the Re-consecration playbook (see `re-consecration-playbook.md`). Convening a new Ascension Council is required; the current Council disbands at sealing.

---

## 7. Sealing signatures

The Ascension Council members below have signed and sealed this Astronomican.

| Name | Role on Council | Signature / commit-hash |
|---|---|---|
| <Name> | Sponsor / Mandate holder | <commit hash or signature> |
| <Name> | PM (Product Manager / Owner) | <...> |
| <Name> | Tech Lead / Architect | <...> |
| <Name> | Senior IC / Maintainer | <...> |
| <Name> | <other functional perspective> | <...> |

Council size: <N> members (must be 3–7 per phase-1 §8.1; ≥3 distinct functional perspectives).

---

## Provenance

- Template version: distribution v0.6.0.
- Source: this template is from Dead Light Framework's distribution; see `distribution/framework/phases/phase-0.md` and (when sealed upstream) phase-1 spec for full procedure.
- Customization: you own this file; framework does not audit your sealed Astronomican.

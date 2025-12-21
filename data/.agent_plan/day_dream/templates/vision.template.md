# {Project Name} Vision

> **Version:** 1.0  
> **Created:** {YYYY-MM-DD}  
> **Status:** 📐 Draft | ✅ Approved | 🔒 Frozen | ❌ Abandoned  
> **Author:** HyperDream

---

## TL;DR

<!-- 
CONSTRAINT: Maximum 3 sentences. If you can't summarize it, you don't understand it.
-->

{One to three sentences describing what this project is and why it matters.}

---

## Problem Statement

<!-- What pain exists? Who feels it? Why now? -->

{Describe the problem this project solves. Be specific about who experiences this pain and what the current workarounds are.}

---

## Non-Goals (Explicit Exclusions)

<!-- 
CONSTRAINT: Minimum 3 items. Be explicit about what this project will NEVER do.
This prevents scope creep and sets clear boundaries.
-->

| Non-Goal | Rationale |
|----------|-----------|
| {Thing we won't do} | {Why it's out of scope} |
| {Thing we won't do} | {Why it's out of scope} |
| {Thing we won't do} | {Why it's out of scope} |

---

## User Model

<!-- 
Who uses this? What's their workflow? 
Skip this section for libraries/utilities with no end-user.
-->

| User | Interface | Capabilities |
|------|-----------|--------------|
| {User type} | {CLI/Web/API/etc} | {What they can do} |

---

## Features

<!-- 
CONSTRAINTS:
- Maximum 5 P0 features
- Each feature description ≤5 lines
- If description exceeds 40 lines, create ./features/{name}.md appendix

DIFFICULTY LABELS (required):
- [KNOWN] — Standard patterns, proven libraries. We know how to build this.
- [EXPERIMENTAL] — Approach exists but needs validation in our context.
- [RESEARCH] — Active problem, no proven solution. NEVER in P0.
-->

### P0: {Feature Name}

**Difficulty:** `[KNOWN]` | `[EXPERIMENTAL]`

{One paragraph description. Focus on WHAT and WHY, not HOW.}

**Acceptance Criteria:**
- {Criterion 1}
- {Criterion 2}

---

### P0: {Feature Name}

**Difficulty:** `[KNOWN]` | `[EXPERIMENTAL]`

{Description.}

**Acceptance Criteria:**
- {Criterion 1}

---

### P1: {Feature Name}

**Difficulty:** `[KNOWN]` | `[EXPERIMENTAL]` | `[RESEARCH]`

{Description. P1+ features can include [RESEARCH] items.}

---

## Success Metrics

<!-- How do we know we won? Quantifiable where possible. -->

| Metric | Target | How to Measure |
|--------|--------|----------------|
| {Metric name} | {Target value} | {Measurement method} |

---

## Scope Budget

<!-- 
MANDATORY. No budget = no approval.
This prevents visions that promise more than P0 can deliver.
-->

| Phase | Duration | Hard Limit |
|-------|----------|------------|
| P0 (Walking Skeleton) | {3-5 days} | Max 5 features, [KNOWN] only |
| P1 (Foundation) | {1-2 weeks} | May include [EXPERIMENTAL] |
| P2+ | {estimate} | May include [RESEARCH] |

---

## Tech Preferences

<!-- 
State preferences or explicitly say "no preference."
HyperArch makes final decisions, but vision can express preferences.
-->

| Category | Preference | Rationale |
|----------|------------|-----------|
| Language | {e.g., Python 3.11+} | {Why} |
| Framework | {e.g., FastAPI} | {Why} |
| Storage | {e.g., SQLite → PostgreSQL} | {Why} |
| {Other} | {Preference or "No preference"} | |

---

## Open Questions

<!-- 
Unresolved decisions that block nothing yet.
These become decisions during implementation.
-->

- {Question 1}
- {Question 2}

---

## Amendments

<!-- 
Append-only. Used for post-freeze additions/clarifications.
If >30% changes needed, create vision_v2.md instead.
-->

| Date | Amendment | Rationale |
|------|-----------|-----------|
| | | |

---

## Superseded By

<!-- 
Empty until full replacement. 
If this vision is replaced entirely, link to the new version.
-->

{Empty — this is the current vision.}

---

## Handoff Checklist

<!-- 
HyperDream: Complete before handoff to HyperArch.
All items must be checked for handoff approval.
-->

- [ ] TL;DR exists and is ≤3 sentences
- [ ] Non-Goals has ≥3 explicit exclusions
- [ ] All P0 features have difficulty labels
- [ ] All P0 features have acceptance criteria
- [ ] No `[RESEARCH]` items in P0
- [ ] Scope Budget is defined
- [ ] Success Metrics are quantifiable
- [ ] Tech preferences stated (or explicitly "no preference")

---

**HANDOFF STATUS:** ⬜ Pending | ✅ Complete

<!--
When handoff is complete, add:

---
**HANDOFF COMPLETE** — {Date}

Vision is now FROZEN. HyperArch authorized to:
1. Create `implementation.md`
2. Create `architecture.md` (if required)
3. CUT P1+ features if P0 scope is threatened

Amendments require formal process (append to Amendments section).
---
-->

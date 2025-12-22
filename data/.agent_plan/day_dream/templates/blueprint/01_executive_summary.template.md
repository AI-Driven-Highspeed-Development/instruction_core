# 01 - Executive Summary

> Part of [{Project Name} Blueprint](./00_index.md)

---

## 🌟 TL;DR

<!-- 
CONSTRAINT: Maximum 3 sentences. If you can't summarize it, you don't understand it.
-->

{One to three sentences describing what this project is and why it matters.}

---

## 🎯 Problem Statement

<!-- What pain exists? Who feels it? Why now? -->

{Describe the problem this project solves. Be specific about who experiences this pain and what the current workarounds are.}

---

## 🔍 Prior Art & Existing Solutions

<!-- 
REQUIRED: Document what exists before building.
Before reinventing wheels, explicitly research and document:
(a) Existing libraries/tools considered
(b) Why they were rejected, adopted, or wrapped
(c) License compatibility with this project
-->

| Library/Tool | What It Does | Decision | License | Rationale |
|--------------|--------------|----------|---------|-----------|
| {library} | {capability} | BUY / BUILD / WRAP | {MIT/Apache/etc} | {Why this decision} |
| {library} | {capability} | BUY / BUILD / WRAP | {MIT/Apache/etc} | {Why this decision} |

**Summary:** {Why we're building custom OR which library we're adopting and how}

---

## ❌ Non-Goals (Explicit Exclusions)

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

## ✅ Features Overview

<!-- 
CONSTRAINTS:
- Maximum 5 P0 features
- Each feature ≤5 lines here (details in separate feature docs)
- Difficulty labels required

DIFFICULTY LABELS:
- [KNOWN] — Standard patterns, proven libraries
- [EXPERIMENTAL] — Approach exists but needs validation
- [RESEARCH] — Active problem, no proven solution. NEVER in P0.
-->

| Priority | Feature | Difficulty | Description |
|----------|---------|------------|-------------|
| P0 | {Feature Name} | `[KNOWN]` | {One sentence} |
| P0 | {Feature Name} | `[KNOWN]` | {One sentence} |
| P1 | {Feature Name} | `[EXPERIMENTAL]` | {One sentence} |
| P2 | {Feature Name} | `[RESEARCH]` | {One sentence} |

→ See individual [Feature Docs](./03_feature_{name}.md) for details.

---

## 📊 Success Metrics

<!-- How do we know we won? Quantifiable where possible. -->

| Metric | Target | How to Measure |
|--------|--------|----------------|
| {Metric name} | {Target value} | {Measurement method} |
| {Metric name} | {Target value} | {Measurement method} |

---

## 📅 Scope Budget

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

## 🛠️ Tech Preferences

<!-- 
State preferences or explicitly say "no preference."
HyperArch makes final decisions, but vision can express preferences.
-->

| Category | Preference | Rationale |
|----------|------------|-----------|
| Language | {e.g., Python 3.11+} | {Why} |
| Framework | {e.g., FastAPI} | {Why} |
| Storage | {e.g., SQLite} | {Why} |
| {Other} | {Preference or "No preference"} | |

---

## ❓ Open Questions

<!-- 
Unresolved decisions that block nothing yet.
These become decisions during implementation.
-->

- {Question 1}
- {Question 2}

---

<!-- OPTIONAL SECTION: Include if project has end-users -->
## 👥 User Model

<!-- 
Who uses this? What's their workflow? 
Remove this section for libraries/utilities with no end-user.
-->

| User | Interface | Capabilities |
|------|-----------|--------------|
| {User type} | {CLI/Web/API/etc} | {What they can do} |

---

<!-- OPTIONAL SECTION: Include for multi-agent handoffs -->
## 📋 Handoff Checklist

<!-- 
HyperDream: Complete before handoff to HyperArch.
Remove this section if not using agent handoffs.
-->

- [ ] TL;DR exists and is ≤3 sentences
- [ ] Prior Art section documents existing solutions considered
- [ ] Non-Goals has ≥3 explicit exclusions
- [ ] All P0 features have difficulty labels
- [ ] No `[RESEARCH]` items in P0
- [ ] Scope Budget is defined
- [ ] Success Metrics are quantifiable

**HANDOFF STATUS:** ⬜ Pending | ✅ Complete

---

**Next:** [Architecture](./02_architecture.md)

---

**← Back to:** [Index](./00_index.md)

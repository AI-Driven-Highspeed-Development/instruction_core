---
project: "{Project Name}"
current_phase: 0
phase_name: "Walking Skeleton"
status: TODO
last_updated: "{YYYY-MM-DD}"
---

# {Project Name} Implementation Plan

> **Vision:** [vision.md](./vision.md)  
> **Architecture:** [architecture.md](./architecture.md) *(if applicable)*  
> **Created:** {YYYY-MM-DD}  
> **Owner:** HyperArch

---

## Status Legend

| Status | Meaning |
|--------|---------|
| `[TODO]` | Not started |
| `[WIP]` | In progress |
| `[BLOCKED:reason]` | Stuck, needs resolution |
| `[DONE]` | Complete |
| `[CUT]` | Removed from scope |

---

## Phase 0: Walking Skeleton 🦴

**Goal:** *"Prove the plumbing works with the dumbest possible implementation"*

**Duration:** 3-5 days (HARD LIMIT)

**Exit Gate:**
- [ ] `{executable command}` → `{expected output}`
- [ ] `{executable command}` → `{expected output}`

### Tasks

| Status | Task | Module | Difficulty |
|--------|------|--------|------------|
| `[TODO]` | {Task description} | `{module/}` | `[KNOWN]` |
| `[TODO]` | {Task description} | `{module/}` | `[KNOWN]` |
| `[TODO]` | {Task description} | `{module/}` | `[KNOWN]` |

### P0 Hard Limits

<!-- These constraints are ENFORCED. No exceptions. -->

- ❌ No {thing that's deferred}
- ❌ No {thing that's deferred}
- ❌ No `[RESEARCH]` or `[EXPERIMENTAL]` items
- ❌ Max 5 tasks

### How to Verify (Manual)

| What to Try | Expected Result |
|-------------|-----------------|
| `{command or action}` | {outcome} |
| `{command or action}` | {outcome} |

---

## Phase 1: {Phase Name} 🏗️

**Goal:** *"{One sentence goal}"*

**Duration:** {1-2 weeks}

**Exit Gate:**
- [ ] `{executable command}` → `{expected output}`
- [ ] `{executable command}` → `{expected output}`

### Tasks

| Status | Task | Module | Difficulty |
|--------|------|--------|------------|
| `[TODO]` | {Task description} | `{module/}` | `[KNOWN]` |
| `[TODO]` | {Task description} | `{module/}` | `[EXPERIMENTAL]` |

### How to Verify (Manual)

| What to Try | Expected Result |
|-------------|-----------------|
| `{command or action}` | {outcome} |

---

## Phase 2: {Phase Name} 📡

**Goal:** *"{One sentence goal}"*

**Duration:** {estimate}

**Exit Gate:**
- [ ] `{executable command}` → `{expected output}`

### Tasks

| Status | Task | Module | Difficulty |
|--------|------|--------|------------|
| `[TODO]` | {Task description} | `{module/}` | `[KNOWN]` |
| `[TODO]` | {Task description} | `{module/}` | `[RESEARCH]` |

---

## Decisions Log

<!-- 
Append-only. Record significant decisions and their rationale.
Format: Date | Decision | Rationale | Decided By
-->

| Date | Decision | Rationale | Decided By |
|------|----------|-----------|------------|
| {YYYY-MM-DD} | {Decision made} | {Why} | {Agent/Human} |

---

## Cut List

<!-- 
Features explicitly removed from scope.
Prevents re-litigation of the same features.
-->

| Feature | Cut Date | Reason |
|---------|----------|--------|
| {Feature name} | {Date} | {Why it was cut} |

---

## Exploration Log

<!-- 
Index of exploration documents and their outcomes.
Updated when explorations are synthesized or abandoned.
This survives even if exploration files are later archived.
-->

| Date | Topic | Status | Synthesized To |
|------|-------|--------|----------------|
| {YYYY-MM-DD} | {Topic name} | {SYNTHESIZED/ABANDONED} | {vision.md#section or "—"} |

---

## Dependencies / Blockers

<!-- 
OPTIONAL: Only include if external dependencies exist.
Remove this section if not applicable.
-->

| Blocker | Owner | Status | Resolution |
|---------|-------|--------|------------|
| {Dependency} | {Who owns it} | {Waiting/Resolved} | {What's needed} |

---

## Risk Register

<!-- 
OPTIONAL: Only for multi-month projects.
Remove this section for smaller projects.
-->

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {Risk description} | {Low/Med/High} | {Low/Med/High} | {How to mitigate} |

---

<!--
IMPLEMENTATION NOTES:

1. Update YAML frontmatter when changing phases
2. Move completed tasks: change [TODO] → [DONE]
3. Use [BLOCKED:reason] for stuck items
4. Add to Decisions Log for significant choices
5. Use Cut List for removed features (don't delete them)

TASK GRANULARITY ("One Session" Test):
- Task is correctly sized if completable in 1-4 hours
- Too vague: Can't write a testable Exit Gate
- Too big: Exit Gate needs 5+ checks
- Just right: 1-3 checks per Exit Gate

EXIT GATE RULES:
- At least one executable check (CLI, curl, file check)
- Expected output must be pattern-matchable
- Max 3 checks per gate
-->

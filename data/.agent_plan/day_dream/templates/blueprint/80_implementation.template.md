---
project: "{Project Name}"
current_phase: 0
phase_name: "Walking Skeleton"
status: TODO
last_updated: "{YYYY-MM-DD}"
---

# 80 - Implementation Plan

> Part of [{Project Name} Blueprint](./00_index.md)

---

## 📊 Status Legend

| Icon | Status | Meaning |
|------|--------|---------|
| ⏳ | `[TODO]` | Not started |
| 🔄 | `[WIP]` | In progress |
| ✅ | `[DONE]` | Complete |
| 🚧 | `[BLOCKED:reason]` | Stuck (kebab-case reason) |
| 🚫 | `[CUT]` | Removed from scope |

---

## 🦴 Phase 0: Walking Skeleton

**Goal:** *"Prove the plumbing works with the dumbest possible implementation"*

**Duration:** 3-5 days (HARD LIMIT)

### Exit Gate

- [ ] `{executable command}` → `{expected output}`

### Tasks

| Status | Task | Module | Difficulty |
|--------|------|--------|------------|
| ⏳ | {Task description} | `{module/}` | `[KNOWN]` |
| ⏳ | {Task description} | `{module/}` | `[KNOWN]` |

### P0 Hard Limits

- ❌ No `[RESEARCH]` or `[EXPERIMENTAL]` items • Max 5 tasks

### Target Folder Structure (P0)

```
{project_root}/
├── managers/{manager}/           (NEW)
└── init.yaml                     (MODIFIED)
```

### Verification (Manual)

| What to Try | Expected Result |
|-------------|-----------------|
| `{command}` | {outcome} |

---

## 🏗️ Phase 1: {Phase Name}

**Goal:** *"{One sentence goal}"*  
**Duration:** {1-2 weeks}

### Exit Gate

- [ ] `{executable command}` → `{expected output}`

### Tasks

| Status | Task | Module | Difficulty |
|--------|------|--------|------------|
| ⏳ | {Task description} | `{module/}` | `[KNOWN]` |
| ⏳ | {Task description} | `{module/}` | `[EXPERIMENTAL]` |

### Target Folder Structure (P1)

```
{project_root}/
├── plugins/{plugin}/             (NEW)
└── managers/{manager}.py         (MODIFIED)
```

### Verification (Manual)

| What to Try | Expected Result |
|-------------|-----------------|
| `{command}` | {outcome} |

---

## 📡 Phase 2+: {Phase Name}

**Goal:** *"{One sentence goal}"*  
**Duration:** {estimate}

### Tasks

| Status | Task | Module | Difficulty |
|--------|------|--------|------------|
| ⏳ | {Task description} | `{module/}` | `[RESEARCH]` |

---

## ⚠️ Error Handling Implementation

<!-- Philosophy in architecture.md; specifics here -->

### Error Types

| Error Class | When Raised | Recovery |
|-------------|-------------|----------|
| `{ErrorName}` | {Condition} | {retry/skip/fail} |

### Logging Requirements

| Level | When | Example |
|-------|------|---------|
| ERROR | {Condition} | `"Failed to {action}: {reason}"` |
| WARNING | {Condition} | `"Retrying {action} ({n}/3)"` |
| INFO | {Condition} | `"{action} completed"` |

---

## 📝 Decisions Log

| Date | Decision | Rationale | Decided By |
|------|----------|-----------|------------|
| {YYYY-MM-DD} | {Decision made} | {Why} | {Agent/Human} |

---

## ✂️ Cut List

| Feature | Cut Date | Reason |
|---------|----------|--------|
| {Feature name} | {Date} | {Why cut} |

---

## 🔬 Exploration Log

| Date | Topic | Status | Synthesized To |
|------|-------|--------|----------------|
| {YYYY-MM-DD} | {Topic} | {SYNTHESIZED/ABANDONED} | {doc#section} |

---

**← Back to:** [Index](./00_index.md)

<!--
NOTES:
1. Update YAML frontmatter when changing phases
2. Status flow: ⏳ → 🔄 → ✅
3. Target Folder Structure: NEW/MODIFIED files per phase only
4. Task size: completable in 1-4 hours, 1-3 exit gate checks
-->

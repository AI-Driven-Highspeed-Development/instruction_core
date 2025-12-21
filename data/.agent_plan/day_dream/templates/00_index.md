# Blueprint Templates Index

> **Location:** `.agent_plan/day_dream/templates/`  
> **Design Document:** [blueprint_template_design.md](../blueprint_template_design.md)  
> **Created:** 2025-12-21

---

## Overview

These templates standardize how HyperDream creates vision and implementation documents. The design was collaboratively developed by HyperDream, HyperSan, and HyperAgentSmith.

---

## Template Files

| Template | Purpose | When to Use |
|----------|---------|-------------|
| [vision.template.md](./vision.template.md) | WHAT and WHY | Starting a new project vision |
| [implementation.template.md](./implementation.template.md) | HOW and WHEN | After vision is approved |
| [architecture.template.md](./architecture.template.md) | System design | When project meets complexity criteria |
| [feature.template.md](./feature.template.md) | Feature appendix | When feature exceeds 40 lines |
| [exploration.template.md](./exploration.template.md) | Pre-vision research | Complex sub-system deep-dives |

---

## Quick Start

### Creating a New Vision

1. Copy `vision.template.md` to your project's `.agent_plan/day_dream/` folder
2. Rename to `vision.md`
3. Fill in sections following the embedded constraints
4. Complete the Handoff Checklist
5. Mark as FROZEN after approval

### Creating an Implementation Plan

1. Ensure `vision.md` is approved and frozen
2. Copy `implementation.template.md` to the same folder
3. Rename to `implementation.md`
4. Update YAML frontmatter with project details
5. This document is LIVING — update as you progress

### When to Add Architecture

Add `architecture.md` if **2+ of these are true**:
- [ ] Project has ≥3 custom modules
- [ ] Cross-module data flows exist
- [ ] External API integrations
- [ ] Async/background processing

### When to Add Feature Appendices

Create `./features/{name}.md` when:
- Vision has 4+ features, OR
- A feature description exceeds ~40 lines

---

## File Structure (Complete)

```
.agent_plan/day_dream/
├── vision.md                    # WHAT and WHY (frozen)
├── implementation.md            # HOW and WHEN (living)
├── architecture.md              # System design (conditional)
├── features/                    # Feature appendices (optional)
│   ├── download_system.md
│   └── authentication.md
└── exploration/                 # Pre-vision research (temporary)
    ├── {topic}_exploration.md   # Active explorations (max 3)
    └── _archive/                # Archived after synthesis
        └── {date}_{topic}.md
```

---

## Exploration Documents

### When to Create

- Choosing between 2+ architectural approaches
- Evaluating external API/library options
- Complex algorithm design (ML, data pipeline)

### When NOT to Create

- Standard features → just write in vision.md
- Implementation details → HyperArch's domain
- Learning/understanding → not planning

### Lifecycle

```
ACTIVE → working → SYNTHESIZED → archived to _archive/
                → ABANDONED → kept with status marked
                → EXPIRED → needs decision after 14 days
```

### Constraints

| Limit | Value |
|-------|-------|
| Max active | 3 (soft cap) |
| Line limit | 200 lines |
| Expiration | 14 days |
| Cleanup | Archive, never delete |

---

## Key Constraints

| Constraint | Limit |
|------------|-------|
| TL;DR | ≤3 sentences |
| Feature description | ≤5 lines (or graduate to appendix) |
| `vision.md` total | ≤150 lines |
| `implementation.md` per phase | ≤200 lines |
| P0 feature count | ≤5 features |
| P0 duration | 3-5 days max |

---

## Status Syntax

```markdown
[TODO] — Not started
[WIP] — In progress
[BLOCKED:reason] — Stuck
[DONE] — Complete
[CUT] — Removed from scope
```

---

## Handoff Protocol

```
HyperDream (Vision) ─── checklist complete ───▶ HyperArch (Implementation)
         │                                              │
         ▼                                              ▼
    vision.md FROZEN                         implementation.md CREATED
```

---

## Related Documents

- **Design Rationale:** [blueprint_template_design.md](../blueprint_template_design.md)
- **HyperDream Agent:** `cores/instruction_core/data/agents/hyper_dream.adhd.agent.md`
- **HyperArch Agent:** `cores/instruction_core/data/agents/hyper_architect.adhd.agent.md`

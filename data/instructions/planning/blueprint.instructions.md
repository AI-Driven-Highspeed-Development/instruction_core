---
applyTo: "**/.agent_plan/day_dream/**"
---

# Blueprint Document Authoring Guidelines

## Goals
- Standardize vision, implementation, architecture, feature, and exploration documents.
- Enforce constraints that keep planning documents focused and actionable.
- Ensure consistency across all HyperDream-generated artifacts.

## Templates Location

All templates are located at: `.agent_plan/day_dream/templates/`

| Template | Purpose | Line Limit |
|----------|---------|------------|
| `vision.template.md` | WHAT and WHY | ≤150 lines |
| `implementation.template.md` | HOW and WHEN | ≤200 lines per phase |
| `architecture.template.md` | System design | No strict limit |
| `feature.template.md` | Feature appendix | ≤100 lines |
| `exploration.template.md` | Pre-vision research | ≤200 lines |

---

## Status Syntax

Use ONLY these status markers in implementation documents:

| Status | Meaning |
|--------|---------|
| `[TODO]` | Not started |
| `[WIP]` | In progress |
| `[BLOCKED:reason]` | Stuck, needs resolution |
| `[DONE]` | Complete |
| `[CUT]` | Removed from scope |

---

## Difficulty Labels

Every feature/task MUST have a difficulty label:

| Label | Meaning | P0 Allowed? |
|-------|---------|-------------|
| `[KNOWN]` | Standard patterns, proven libraries | ✅ Yes |
| `[EXPERIMENTAL]` | Needs validation in our context | ⚠️ Conditional |
| `[RESEARCH]` | Active problem, no proven solution | ❌ NEVER in P0 |

---

## Document Rules

### Vision (`vision.md`)
- **Line Limit:** ≤150 lines
- **Freeze Policy:** Mark as 🔒 FROZEN after approval. No further edits.
- **TL;DR:** Maximum 3 sentences
- **Non-Goals:** Minimum 3 items required
- **Features:** Maximum 5 P0 features, each description ≤5 lines
- **Feature Overflow:** If description exceeds 40 lines → create `./features/{name}.md`

### Implementation (`implementation.md`)
- **Line Limit:** ≤200 lines per phase section
- **YAML Frontmatter:** REQUIRED with project, current_phase, status, last_updated
- **P0 Hard Limits:**
  - Duration: 3-5 days maximum
  - Max 5 tasks
  - NO `[RESEARCH]` or `[EXPERIMENTAL]` items
- **Verification:** Every phase MUST have "How to Verify (Manual)" section

### Architecture (`architecture.md`)
- **When Required:** 2+ of these conditions:
  - Project has ≥3 custom modules
  - Cross-module data flows exist
  - External API integrations
  - Async/background processing
- **System Diagram:** MUST fit on one screen, use Mermaid

### Feature Appendix (`features/{name}.md`)
- **When to Create:**
  - Vision has 4+ features, OR
  - Feature description exceeds ~40 lines
- **Structure:** User stories, acceptance criteria, edge cases

### Exploration (`exploration/{topic}_exploration.md`)
- **Line Limit:** ≤200 lines
- **Max Active:** 3 concurrent explorations
- **Expiration:** 14 days from creation (hard deadline)
- **When to Create:**
  - Choosing between 2+ architectural approaches
  - Evaluating external API/library options
  - Complex algorithm design
- **When NOT to Create:**
  - Standard features (write in vision.md)
  - Implementation details (HyperArch's domain)
  - Learning/understanding (not planning)
- **Lifecycle:** `ACTIVE → SYNTHESIZED → archived` or `ACTIVE → ABANDONED`
- **Archive Location:** `exploration/_archive/{date}_{topic}.md`

---

## Folder Structure

```
.agent_plan/day_dream/
├── templates/                   # Template files (DO NOT EDIT)
│   ├── 00_index.md
│   ├── vision.template.md
│   ├── implementation.template.md
│   ├── architecture.template.md
│   ├── feature.template.md
│   └── exploration.template.md
├── vision.md                    # WHAT and WHY (frozen after approval)
├── implementation.md            # HOW and WHEN (living document)
├── architecture.md              # System design (conditional)
├── features/                    # Feature appendices
│   └── {feature_name}.md
└── exploration/                 # Pre-vision research
    ├── {topic}_exploration.md   # Active (max 3)
    └── _archive/                # Archived explorations
```

---

## Handoff Checklist (Vision → Implementation)

Before transitioning from vision to implementation:

- [ ] TL;DR is ≤3 sentences
- [ ] Non-Goals has ≥3 items
- [ ] All P0 features are `[KNOWN]` (no `[RESEARCH]`)
- [ ] Each feature has acceptance criteria
- [ ] Vision marked as 🔒 FROZEN

---

## Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|----------|---------------|
| Put `[RESEARCH]` items in P0 | Defer to P1+ or resolve in exploration first |
| Exceed line limits | Split into appendix or phase documents |
| Edit frozen vision.md | Create new version or update implementation.md |
| Have >3 active explorations | Synthesize or abandon oldest before starting new |
| Skip verification sections | Always include manual verification steps |

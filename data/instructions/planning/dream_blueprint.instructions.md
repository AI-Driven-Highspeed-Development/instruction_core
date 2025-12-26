---
applyTo: "**/.agent_plan/day_dream/**"
---

# Blueprint Document Authoring Guidelines

## Goals
- Standardize vision, implementation, architecture, feature, and exploration documents.
- Enforce constraints that keep planning documents focused and actionable.
- Ensure consistency across all HyperDream-generated artifacts.

---

## Tier Selection

Templates are tiered based on project complexity:

| Tier | Use When | Template |
|------|----------|----------|
| **Simple** | ≤2 features, single module, no external APIs | `simple.template.md` |
| **Blueprint** | ≥3 features OR ≥2 cross-module deps OR external APIs | `blueprint/` folder |

### Auto-Detection Rules

```yaml
use_blueprint_tier:
  - feature_count >= 3
  - cross_module_imports >= 2
  - has_external_api: true
```

---

## Templates Location

All templates at: `.agent_plan/day_dream/templates/`

### Simple Tier
| Template | Purpose | Line Limit |
|----------|---------|------------|
| `simple.template.md` | Single-file vision + quick start | ≤200 lines |

### Blueprint Tier
| Template | Purpose | Line Limit |
|----------|---------|------------|
| `blueprint/00_index.template.md` | Navigation hub with flowchart | ≤150 lines |
| `blueprint/01_executive_summary.template.md` | Vision, goals, non-goals | ≤150 lines |
| `blueprint/02_architecture.template.md` | System diagrams, logical components | ≤200 lines |
| `blueprint/NN_feature.template.md` | Per-feature details | ≤150 lines |
| `blueprint/80_implementation.template.md` | Phased roadmap | ≤200 lines per phase |
| `blueprint/99_references.template.md` | External links | No limit |
| `blueprint/exploration.template.md` | Pre-vision research | ≤200 lines |

### Assets (Multi-Modal Artifacts)
| Template | Purpose | Line Limit |
|----------|---------|------------|
| `assets/asset.template.md` | Non-code artifacts (mockups, diagrams, storyboards, etc.) | ≤100 lines |

**Asset Types:** `mockup`, `diagram`, `storyboard`, `infrastructure`, `design`, `data-model`, `other`  
**Naming:** `{feature_id}_{description}.asset.md` (e.g., `03_dashboard_mockup.asset.md`)

### Examples

Completed samples at: `templates/examples/`

| Example | Demonstrates |
|---------|--------------|
| `simple_example.md` | Simple tier vision document |
| `blueprint_example/` | Full Blueprint tier folder structure |
| `free_zone_*.example.md` | Custom sections (Philosophical Tensions, Assumption Graveyard, Metaphor Map) |
| `deep_dive_*.example.md` | Deep Dive subsections (Algorithm Choices, API Contract, Error Handling) |

---

## Status Syntax

Use hybrid emoji + text markers:

| Emoji | Text | Meaning |
|-------|------|---------|
| ⏳ | `[TODO]` | Not started |
| 🔄 | `[WIP]` | In progress |
| ✅ | `[DONE]` | Complete |
| 🚧 | `[BLOCKED:reason]` | Stuck (kebab-case reason) |
| 🚫 | `[CUT]` | Removed from scope |

**Example:** `⏳ [TODO]`, `🔄 [WIP]`, `✅ [DONE]`

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

### Simple Tier
- Single file, ~50-200 lines
- Must include: Hook, What's Here, Quick Start, API Reference
- Optional: Edge Cases, When to Upgrade

### Blueprint Tier

#### Index (`00_index.md`)
- Progress Overview with emoji status
- Document navigation table
- "Where to Start" Mermaid flowchart

#### Executive Summary (`01_executive_summary.md`)
- TL;DR: Maximum 3 sentences
- **Prior Art & Existing Solutions**: REQUIRED section with BUY/BUILD/WRAP decisions
- Non-Goals: Minimum 3 items
- Features: Maximum 5 P0 features
- Freeze after approval with 🔒 FROZEN

#### Architecture (`02_architecture.md`)
- Required when: ≥3 modules OR cross-module deps OR external APIs
- Key Design Principles: 3-5 principles table
- Logical Components: Purpose, Boundary, Implemented By
- Project Structure: Target end-state with phase annotations `(P0)`, `(P1)`
- System Diagram: Mermaid, must fit one screen

#### Feature (`NN_feature.md`)
- Create when feature description exceeds ~40 lines
- Optional: System Context diagram, Data Flow, Integration Points
- Related Assets: Link to mockups/diagrams in `../assets/` folder (see `dream_assets.instructions.md`)

##### Custom Sections (FREE ZONE)
Authors may add project-specific sections with these rules:
- **Prefix Convention**: Use `## [Custom] 🎨 Title` (e.g., `## [Custom] 🎨 Analytics Events`)
- **Free Zone**: Content between `<!-- FREE ZONE START -->` and `<!-- FREE ZONE END -->` markers
- **Examples**: See `templates/examples/free_zone_*.example.md` (Philosophical Tensions, Assumption Graveyard, Metaphor Map)
- **Maximum**: 5 custom sections per document
- **Prohibited in Custom**: P0 tasks, blocking dependencies, architecture changes

##### Deep Dive Section (`## 🔬 Deep Dive`)
Optional section for implementation-heavy features:
- **When to use**: Algorithm choices, API contracts, complex error handling, performance tradeoffs
- **When to delete**: Straightforward features, obvious implementation path, simple CRUD
- **Subsections**: Algorithm Choices, API Contract Draft, Error Handling Strategy
- **Examples**: See `templates/examples/deep_dive_*.example.md`

#### Asset (`*.asset.md`)
- Lightweight template for non-code artifacts
- Types: mockup, diagram, storyboard, infrastructure, design, data-model
- Naming: `{feature_id}_{description}.asset.md`
- Required sections: Context, The Artifact, Constraints, Related Features
- Line limit: ~100 lines (excluding embedded diagrams)
- **Full specification**: See `dream_assets.instructions.md` for detailed rules

#### Implementation (`80_implementation.md`)
- YAML frontmatter required
- Target Folder Structure: Per-phase NEW/MODIFIED files
- P0 Hard Limits: 3-5 days, max 5 tasks, no `[RESEARCH]`
- Error Handling Implementation section
- Verification: Every phase needs "How to Verify (Manual)"

#### Exploration
- Max 3 active, 14-day expiration
- Archive to `exploration/_archive/` when done

---

## Folder Structure

### Simple Tier Output
```
.agent_plan/day_dream/
├── {project}_vision.md      # Single-file vision
└── templates/               # Templates (DO NOT EDIT)
```

### Blueprint Tier Output
```
.agent_plan/day_dream/
├── blueprint/               # Multi-file structure
│   ├── 00_index.md
│   ├── 01_executive_summary.md
│   ├── 02_architecture.md
│   ├── 03_feature_*.md
│   ├── 80_implementation.md
│   └── 99_references.md
├── assets/                  # Non-code artifacts
│   ├── {feature_id}_{description}.asset.md
│   └── ...
├── exploration/             # Pre-vision research
│   └── _archive/
└── templates/               # Templates (DO NOT EDIT)
```

---

## Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|----------|---------------|
| Put `[RESEARCH]` in P0 | Defer to P1+ or resolve in exploration first |
| Exceed line limits | Split into separate files |
| Edit frozen documents | Create new version or update implementation |
| Have >3 active explorations | Synthesize or abandon oldest |
| Skip verification sections | Always include manual verification steps |
| Use Simple tier for complex projects | Upgrade to Blueprint when threshold met |

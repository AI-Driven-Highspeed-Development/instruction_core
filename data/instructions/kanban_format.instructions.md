---
applyTo: "**/.agent_plan/kanban/*.md"
---

# Markdown Kanban Format

## Purpose
Standardized format for markdown-kanban planning boards used by the HyperPM agent.

## Structure
- **Board Title**: Top-level `#` heading.
- **Lanes**: `##` headings (e.g., `## Backlog`, `## In Progress`, `## Done`).
- **Tasks**: `###` headings under lanes.

## Task Metadata
```md
### <Task Title>

  - due: YYYY-MM-DD        # optional, must be YYYY-MM-DD if present
  - tags: [tag1, tag2]     # optional, empty list allowed
  - priority: <priority>   # one of: none, low, medium, high
  - workload: <workload>   # one of: none, easy, normal, hard, extreme
  - defaultExpanded: true  # optional, only when useful
  - steps:
      - [ ] first checklist item
      - [ ] second checklist item
    ```md
    Optional multi-line description for this task.
    Keep it concise and implementation-free.
    ```
```

## Rules
- **Indentation**: Use SPACE characters, NEVER tabs.
- **priority**: Must be one of: `none`, `low`, `medium`, `high` (lowercase).
- **workload**: Must be one of: `none`, `easy`, `normal`, `hard`, `extreme` (lowercase).
- **due**: Must be `YYYY-MM-DD` format when present, omit if none.
- **steps**: Optional; omit if no checklist items.
- **Description fence**: Language MUST be `md`.

## File Locations
- Workspace-level: `.agent_plan/kanban/kanban.md`
- Module-level: `<module_type>/<module_name>/.agent_plan/kanban/kanban.md`

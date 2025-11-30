---
applyTo: "**/.agent_plan/.kanbn/**"
---

# Kanbn Format Specification

## Purpose
Standardized format for `kanbn` planning boards used by the HyperPM agent.
This format is compatible with the [kanbn](https://github.com/basementuniverse/kanbn) tool and VS Code extension.

## Directory Structure
- **Root**: `.agent_plan/.kanbn/`
- **Index File**: `.agent_plan/.kanbn/index.md`
- **Tasks Directory**: `.agent_plan/.kanbn/tasks/`
- **Task Files**: `.agent_plan/.kanbn/tasks/<task-id>.md`

## Index File Structure (`index.md`)

The index file defines the board columns and lists the tasks within them.

```markdown
---
# Optional Project Options in YAML front-matter
hiddenColumns:
  - Archive
startedColumns:
  - In Progress
completedColumns:
  - Done
---

# Project Name

Project description goes here.

## Backlog

- [Task Title](tasks/task-id-1.md)
- [Another Task](tasks/task-id-2.md)

## In Progress

- [Active Task](tasks/task-id-3.md)

## Done

- [Completed Task](tasks/task-id-4.md)
```

### Rules for Index
- **Level-1 Heading**: Must be the Project Name.
- **Level-2 Headings**: Define the Columns (Lanes).
- **Task Links**: Must be relative links to files in the `tasks/` directory. Format: `- [Task Name](tasks/<filename>.md)`.

## Task File Structure (`tasks/<task-id>.md`)

Each task is a separate markdown file.

```markdown
---
created: 2023-10-27T10:00:00.000Z
updated: 2023-10-27T11:00:00.000Z
assigned: "User"
progress: 0.0
tags:
  - "feature"
  - "high-priority"
due: 2023-11-01T17:00:00.000Z
---

# Task Name

Detailed description of the task.
Can include multiple paragraphs, code blocks, etc.
Follow markdown syntax.

## Sub-tasks

- [ ] First sub-task
- [x] Completed sub-task

## Relations

- [blocks tasks/other-task.md](other-task.md)

## Comments

- author: "User"
  date: 2023-10-27T12:00:00.000Z
  This is a comment.
```

### Rules for Tasks
- **Filename**: Use kebab-case (e.g., `implement-login-feature.md`).
- **YAML Front-matter**:
    - `created`: ISO 8601 date string.
    - `updated`: ISO 8601 date string.
    - `assigned`: String (optional).
    - `progress`: Number between 0.0 and 1.0.
    - `tags`: List of strings.
    - `due`: ISO 8601 date string (optional).
    - `started`: ISO 8601 date string (optional).
    - `completed`: ISO 8601 date string (optional).
- **Level-1 Heading**: Must be the Task Name.
- **Reserved Level-2 Headings**:
    - `## Sub-tasks`: List of checklist items (`- [ ]` or `- [x]`).
    - `## Relations`: List of links to other tasks.
    - `## Comments`: List of comments with `author` and `date`.

## File Locations
- Workspace-level: `.agent_plan/.kanbn/`

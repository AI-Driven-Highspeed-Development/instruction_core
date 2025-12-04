---
description: Commit and push all ADHD modules with contextual commit messages
---

# Push All Modules

Commit and push changes across all ADHD modules (managers, plugins, utils, mcps) with reasonable, context-aware commit messages.

## Scope
- **Included by default**: `managers/`, `plugins/`, `utils/`, `mcps/`
- **Excluded by default**: `cores/` (unless user says "include cores")
- **Always excluded**: The root project repo (only push submodules)

## Workflow

### 1. List Modules
Run `python adhd_framework.py list` to get all modules.

### 2. For Each Module (except cores)
1. `cd` into the module directory
2. Check `git status` for changes
3. If changes exist:
   - Stage all changes: `git add .`
   - Generate a contextual commit message based on:
     - Changed files (use `git diff --cached --stat`)
     - Type of changes (new files, modifications, deletions)
     - Keep it concise: `<type>: <summary>` (e.g., `feat: add kanbn controller`, `fix: resolve import error`)
   - Commit: `git commit -m "<message>"`
   - Push: `git push`
4. If push fails due to permissions, log a warning and skip (do NOT stop)

### 3. Summary
After processing all modules, provide a summary:
- Modules pushed successfully
- Modules skipped (no changes)
- Modules failed (permission denied or other errors)

## Commit Message Guidelines
- Use conventional commit format: `<type>: <description>`
- Types: `feat`, `fix`, `docs`, `refactor`, `chore`, `style`, `test`
- Keep under 72 characters
- Be specific but concise

---

**Default behavior**: Skip `cores/` and the root project repo.
**To include cores**: Say "include cores" or "push cores too".

---
description: Pull latest changes for all ADHD modules
---

# Pull All Modules

Pull the latest changes from remote for all ADHD modules (managers, plugins, utils, mcps).

## Scope
- **Included by default**: `managers/`, `plugins/`, `utils/`, `mcps/`
- **Excluded by default**: `cores/` (unless user says "include cores")
- **Always excluded**: The root project repo (only pull submodules)

## Workflow

### 1. List Modules
Run `python adhd_framework.py list` to get all modules.

### 2. For Each Module (except cores)
1. `cd` into the module directory
2. Check for uncommitted changes with `git status`
3. If uncommitted changes exist:
   - Warn the user and skip this module (do NOT force pull)
   - Log: "Skipping <module>: has uncommitted changes"
4. If clean:
   - Pull: `git pull`
5. If pull fails due to permissions or other errors, log and continue

### 3. Summary
After processing all modules, provide a summary:
- Modules pulled successfully
- Modules skipped (uncommitted changes)
- Modules skipped (permission denied or other errors)

---

**Default behavior**: Skip `cores/` and the root project repo.
**To include cores**: Say "include cores" or "pull cores too".

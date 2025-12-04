---
description: Pull latest changes for all ADHD modules
---

# Pull All Modules

Pull the latest changes from remote for all ADHD modules (managers, plugins, utils, mcps).

## Scope
- **Included by default**: `managers/`, `plugins/`, `utils/`, `mcps/`
- **Excluded by default**: `cores/` (unless user says "include cores")
- **Always excluded**: The root project repo (only pull submodules)

## Workflow (Using adhd_mcp)

### 1. Check Status First
Call `git_modules(action="status")` to see which modules are clean/dirty.

### 2. Pull All Clean Modules
Call `git_modules(action="pull")` — this automatically:
- Skips modules with uncommitted changes
- Skips non-git directories
- Returns `pulled`, `failed`, and `skipped` lists

### 3. To Include Cores
Call `git_modules(action="pull", include_cores=True)`

### 4. Response Format
```python
{
  "success": True,
  "pulled": [{"name": "...", "message": "..."}],
  "failed": [{"name": "...", "error": "..."}],
  "skipped": [{"name": "...", "reason": "..."}]
}
```

## Alternative: Manual Workflow
If MCP is unavailable, use terminal commands:
1. Run `python adhd_framework.py list` to get all modules
2. For each module: `cd <path> && git status && git pull`

---

**Default behavior**: Skip `cores/` and the root project repo.
**To include cores**: Say "include cores" or use `include_cores=True`.

---
description: Commit and push all ADHD modules with contextual commit messages
---

# Push All Modules

Commit and push changes across all ADHD modules (managers, plugins, utils, mcps) with reasonable, context-aware commit messages.

## Scope
- **Included by default**: `managers/`, `plugins/`, `utils/`, `mcps/`
- **Excluded by default**: `cores/` (unless user says "include cores")
- **Always excluded**: The root project repo (only push submodules)

## Workflow (Using adhd_mcp)

### 1. Get Status Overview
Call `git_modules(action="status")` to see which modules have changes.

### 2. Get Detailed Diffs for Dirty Modules
Call `git_modules(action="diff")` to get:
- File-by-file changes with insertions/deletions
- `diff_summary` like "+150 -22 in 5 files"

### 3. Craft Commit Messages
For each dirty module, analyze the `changes` array and craft a message:
- Use conventional commit format: `<type>: <description>`
- Types: `feat`, `fix`, `docs`, `refactor`, `chore`, `style`, `test`
- Keep under 72 characters

### 4. Push Each Module
Call `git_modules(action="push", module_name="<name>", commit_message="<msg>")` for each.

**IMPORTANT**: Push one module at a time with its specific commit message.

### 5. Example Workflow
```python
# Step 1: See what's dirty
status = git_modules(action="status")

# Step 2: Get diffs for commit message crafting
diffs = git_modules(action="diff")
# Returns: {"modules": [{"name": "adhd_mcp", "changes": [...], "diff_summary": "+150 -22"}]}

# Step 3: Push each with tailored message
git_modules(action="push", module_name="adhd_mcp", commit_message="feat: implement 6 MCP tools")
git_modules(action="push", module_name="config_manager", commit_message="fix: resolve path issue")
```

### 6. Response Format
```python
{
  "success": True,
  "pushed": [{"name": "...", "commit": "abc123", "message": "..."}],
  "failed": [{"name": "...", "error": "..."}],
  "skipped": [{"name": "...", "reason": "No changes to commit"}]
}
```

## Commit Message Guidelines
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code change that neither fixes nor adds
- `chore`: Build process or auxiliary tool changes
- `style`: Formatting, missing semi-colons, etc.
- `test`: Adding tests

---

**Default behavior**: Skip `cores/` and the root project repo.
**To include cores**: Say "include cores" or use `include_cores=True`.

---
description: Update ADHD module requirements in init.yaml and PyPI requirements in requirements.txt
---

# Update Requirements

Update all module requirements across the ADHD project. This involves two separate tasks:

## Task 1: Update ADHD Module Requirements (init.yaml)

For all **non-core** modules (managers, plugins, utils, mcps), update the `requirements` field in their `init.yaml` files.

**IMPORTANT**: Read `.github/instructions/modules.init.yaml.instructions.md` first to understand the format.

- The `requirements` field lists ADHD module GitHub URLs (NOT PyPI packages).
- Format: `https://github.com/AI-Driven-Highspeed-Development/<module_name>.git`
- **Transitive dependencies are OK**: Only list DIRECT dependencies. If module A requires B, and B requires C, module A does NOT need to list C—it's transitively included via B.
- Do NOT touch `cores/` modules unless I explicitly say "include cores" or "update cores too".

**Steps:**
1. List all modules with `python adhd_framework.py list`
2. For each non-core module, read its `init.yaml`
3. Verify each requirement URL is valid and up-to-date
4. Update if needed

## Task 2: Update PyPI Requirements (requirements.txt)

For all **non-core** modules, update the `requirements.txt` files with the latest PyPI package versions.

**Also update the root `requirements.txt`.**

**IMPORTANT**: 
- `requirements.txt` is for PyPI packages ONLY (e.g., `PyYAML`, `requests`)
- Do NOT put ADHD module URLs in requirements.txt (those go in init.yaml)
- Skip `cores/` modules unless I explicitly request

**Steps:**
1. For each non-core module with a `requirements.txt`, check for outdated packages
2. Update to latest compatible versions
3. Update root `requirements.txt` as well

---

**Default behavior**: Skip all `cores/` modules.
**To include cores**: Say "include cores" or "update cores too" etc. when using this prompt.

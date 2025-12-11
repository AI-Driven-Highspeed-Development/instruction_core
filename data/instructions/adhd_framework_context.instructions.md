# ADHD Framework Context

## Why This Framework Exists
AI agents hit a **Context Wall** as complexity grows. This framework solves it via:
- **Fractal Modularity**: Small, single-responsibility modules. Agents load only what they need.
- **Deterministic Lifecycle**: Init bootstraps, Refresh self-heals.
- **AI-Native Context**: `.instructions.md` files teach agents the "how" alongside code.

## Core Philosophy
1. **Read Before Write**: NEVER guess. Read docs/source first.
2. **Reuse, Don't Reinvent**: Check existing modules before implementing.
3. **Consistency**: MIMIC existing style exactly.
4. **Single Responsibility**: One module = one job.
5. **Understand the Why**: Know *why* patterns exist.

## Project Structure
- **Directories**:
  - `project/`: App code. `project/data/`: App data (use Config-Manager paths).
  - `cores/`, `managers/`, `utils/`, `plugins/`, `mcps/`: Module types.
  - `.temp_agent_work/`: Agent workspace, MUST clean up after.
- **Entry Points**: `adhd_framework.py` (framework CLI), `<app_name>.py` (app).
- **Module Assets** (`<type>/<name>/`):
  - `__init__.py`, `init.yaml`, `.config_template`, `data/`, `refresh.py`
  - `<name>.instructions.md`, `requirements.txt` (PyPI only)

## Module Types

| Type | Folder | Purpose | When |
|:---|:---|:---|:---|
| **Core** | `cores/` | Framework internals | NEVER create unless extending framework |
| **Manager** | `managers/` | Stateful singletons, coordination | Needs state/lifecycle |
| **Util** | `utils/` | Stateless pure functions | No state |
| **Plugin** | `plugins/` | Project-specific extensions | Only for THIS project |
| **MCP** | `mcps/` | AI tool integrations | Extending agent capabilities |

**Decision**: State? → Manager. Stateless? → Util. Reusable? → Manager. Project-only? → Plugin.

## Module Naming
- **Suffix matches type**: `*_manager`, `*_util`, `*_plugin`, `*_core`, `*_mcp`
- **Snake_case**, specific, descriptive
- ✅ `oauth2_auth_manager` ❌ `auth`

## Reusable vs Project-Specific Modules

Modules fall into two categories based on **reusability across projects**:

### Reusable (Generic) Modules
**No project-specific knowledge**, can copy to other ADHD projects:

| Pattern | Examples |
|:---|:---|
| Generic terms | `auth_manager`, `session_manager`, `rss_monitor_plugin` |
| Technology-specific | `torrent_client_plugin`, `external_media_manager` |
| Common patterns | `notification_plugin`, `cache_manager` |

### Project-Specific Modules
**Domain logic unique to this project**, name indicates context:

| Pattern | Examples |
|:---|:---|
| Domain prefix | `anime_download_manager`, `video_stream_manager` |
| Project prefix | `animenest_webui_plugin`, `animenest_cli_plugin` |
| Feature-specific | `anime_library_scanner_plugin`, `syoboi_api_plugin` |

### The Reusability Test
*"In a list of 50 modules from different projects, do I know what it does AND which project it belongs to?"*
- **Reusable**: Generic name → reuse anywhere
- **Project-Specific**: Includes domain/project context

### Abstraction Pattern
Extract generic layers from project-specific features, e.g.:
```
Generic module: external_media_manager (scanning, indexing)
Used by --> anime_library_scanner  or  photo_library_scanner (Project: domain parsing)
```

## Module File Structure
Every module MUST include these core files:

| File | Purpose |
|:---|:---|
| `__init__.py` | Exports, path setup (see below), auto-refresh triggers |
| `init.yaml` | Module metadata: name, version, description, requirements |
| `refresh.py` | Re-runnable setup logic (register configs, CLI, etc.) |
| `README.md` | Human-readable documentation |
| `.config_template` | Default config schema (optional) |
| `requirements.txt` | PyPI dependencies ONLY (not ADHD modules) |
| `<name>.instructions.md` | AI context for this module (optional but recommended) |
| `data/` | Module-specific data files (optional) |

### Path Handling in `__init__.py` and `refresh.py`
ALWAYS include at the top of `__init__.py` and `refresh.py`:
```python
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.getcwd()  # Use current working directory as project root
sys.path.insert(0, project_root)
```
This ensures modules work correctly regardless of how they are invoked.

### MCP-Specific Files (for `mcps/` only)
| File | Purpose |
|:---|:---|
| `<name>_mcp.py` | FastMCP server: tool decorators ONLY (thin wrapper) |
| `<name>_controller.py` | All business logic, file I/O, validation |
| `<name>_cli.py` | CLI command registration (mirrors MCP tools) |

## AI-Native Context System
`instruction_core` syncs to `.github/` for VS Code Copilot:
- **Source**: `cores/instruction_core/data/`, `<module>/<name>.instructions.md`
- **Dest**: `.github/instructions/`, `.github/agents/`, `.github/prompts/`
- **Trigger**: `./adhd_framework.py refresh`

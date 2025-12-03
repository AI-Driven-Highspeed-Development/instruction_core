# ADHD Framework Context

## Why This Framework Exists
The ADHD Framework treats AI agents as first-class developers. Traditional "vibe coding" hits a **Context Wall** as complexity grows: agents hallucinate APIs, misunderstand goals, and cause regressions. This framework solves it by:
-   **Fractal Modularity**: Everything is a small, single-responsibility module. Agents only load what they need.
-   **Deterministic Lifecycle**: Init bootstraps, Refresh self-heals. Agents can reset parts without breaking the whole.
-   **AI-Native Context**: Instruction files (`.instructions.md`) teach agents the "how" alongside the code.

## Core Philosophy
1.  **Read Before Write**: NEVER guess. Read relevant docs and source code first.
2.  **Reuse, Don't Reinvent**: ALWAYS check for existing modules (`cores/`, `managers/`, `utils/`, `plugins/`, `mcps/`) before implementing functionality.
3.  **Consistency**: MIMIC existing style, error handling, and structure exactly.
4.  **Single Responsibility**: Each module does ONE thing well. No Swiss Army Knife modules.
5.  **Understand the Why**: Know *why* a pattern exists, not just *what* to do. Ask if unclear.

## Project Structure
-   **Directories**:
    -   `project/`: App-specific code.
    -   `project/data/`: App data storage (use Config-Manager paths).
    -   `cores/`, `managers/`, `utils/`, `plugins/`, `mcps/`: Modules of different types.
    -   `.temp_test/`, `.temp_debug/`: Temporary folders for testing/debugging.
    -   `.temp_agent_work/`: Temporary workspace for agents, you can write temporary code here during operations, MUST clean up after.
-   **Entry Points**:
    -   `adhd_framework.py`: Framework CLI (init/refresh/upgrade/install). Use `--help`.
    -   `<app_name>.py`: App entry point. (Name can vary by project).
-   **Module Assets**:
    Modules are in `<module_type>/<module_name>/` folders, containing:
    -   `__init__.py`: Init code.
    -   `init.yaml`: Metadata, read guidance in `.github/instructions/modules.init.yaml.instructions.md` for structure.
    -   `.config_template`: Default config schema (JSON or key=value).
    -   `data/`: Optional, module-specific data files.
    -   `refresh.py`: Optional, idempotent state regeneration (only when module manages data/state benefiting from regeneration).
    -   `<module_name>.instructions.md`: Module-specific AI instructions.
    -   `requirements.txt`: PyPI deps only (no ADHD module deps). NOTE: Don't put PyPI deps into init.yaml.
-   **Project Data Storage**: Use Config-Manager paths (Convention: `./project/data/<module_name>/**`).

## Module Types (and Why These 5)
The 5 types emerged from real constraints, not theory. Fewer types → Swiss Army Knife chaos. More types → analysis paralysis.

| Type | Folder | Purpose | When to Use |
|:---|:---|:---|:---|
| **Core** | `cores/` | Framework internals (bootstrap, module lifecycle, instruction sync). | NEVER create unless you're extending the framework itself. |
| **Manager** | `managers/` | Stateful singletons that persist configuration or coordinate resources. | When you need lifecycle, state, or project-wide coordination. |
| **Util** | `utils/` | Stateless helpers. Pure functions, no side effects. | When it's a reusable tool with no state (e.g., logger, string helpers). |
| **Plugin** | `plugins/` | Project-specific extensions. Too specific to reuse elsewhere. | When the module only makes sense for THIS project. |
| **MCP** | `mcps/` | Model Context Protocol servers. Extends AI agent capabilities. | When building external tool integrations for AI agents. |

**Key Insight**: If unsure between Manager/Util → Does it hold state? Manager. Stateless? Util.
**Key Insight**: If unsure between Manager/Plugin → Is it reusable across projects? Manager. Project-specific? Plugin.

## Module Naming Conventions
-   **Be Specific**: `mysql_database_manager` not `database_manager`. Specificity enables reuse across projects.
-   **Suffix Matches Type**: `*_manager`, `*_util`, `*_plugin`, `*_core`, `*_mcp`.
-   **Snake Case**: `config_manager`, not `ConfigManager` or `config-manager`.
-   **Descriptive**: Name should tell you what it does without reading code.

**Examples**:
-   ✅ `oauth2_auth_manager` — Clear: OAuth2, authentication, stateful manager.
-   ❌ `auth` — Too vague. What kind? Manager or Util?

## AI-Native Context System
The `instruction_core` syncs context files to `.github/` for VS Code Copilot:
-   **Source**: `cores/instruction_core/data/` (agents, instructions, prompts)
-   **Source**: `<module>/<module_name>.instructions.md` (module-specific)
-   **Destination**: `.github/instructions/`, `.github/agents/`, `.github/prompts/`
-   **Trigger**: `./adhd_framework.py refresh`

This ensures agents always have up-to-date context about how to work with the codebase.

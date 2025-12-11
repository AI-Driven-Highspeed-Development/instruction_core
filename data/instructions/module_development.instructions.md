---
applyTo: "managers/**/*.py,plugins/**/*.py,utils/**/*.py,mcps/**/*.py,cores/**/*.py"
---

# Module Development Guidelines

## Goals
- Prevent hallucination by enforcing existing patterns.
- Ensure all modules integrate correctly with framework infrastructure.
- Standardize module creation and development.

## CRITICAL: Mandatory Reading Before ANY Module Work
Before writing or modifying module code, READ these instruction files:
1. `adhd_framework_context.instructions.md` - Framework structure and philosophy
2. `logger_util.instructions.md` - Logging (NEVER use `print()` in MCPs)
3. `config_manager.instructions.md` - Configuration access patterns
4. `exceptions.instructions.md` - Error handling (ADHDError vs standard exceptions)

## Module Creation Rules

### DO NOT Create Modules Manually
- **Use the module creation tools**: `adhd_mcp` provides `create_module` tool.
- CLI: `python adhd_framework.py create --type <type> --name <name>`
- Templates exist for a reason—use them.

### Path Handling (MANDATORY)
Every `__init__.py` and `refresh.py` MUST include at the top:
```python
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.getcwd()
sys.path.insert(0, project_root)
```

## Anti-Hallucination Rules

1. **NEVER invent imports**: Search codebase first. Use `grep_search` or `semantic_search`.
2. **NEVER guess API signatures**: Read the source file of the module you're calling.
3. **NEVER create utilities that exist**: Check `utils/` and `managers/` first.
4. **NEVER use print() in MCP servers**: Corrupts JSON-RPC. Use `Logger` from `logger_util`.
5. **NEVER hardcode paths**: Use `ConfigManager` for paths.

## MCP-Specific Rules

### File Structure
```
mcps/<module_name>/
├── __init__.py           # Exports + path setup
├── init.yaml             # Module metadata
├── <name>_mcp.py         # FastMCP server (thin wrapper ONLY)
├── <name>_controller.py  # ALL business logic here
├── <name>_cli.py         # CLI command registration
├── refresh.py            # Registers in .vscode/mcp.json
└── requirements.txt      # PyPI deps
```

### CLI Registration (`*_cli.py`)
- Import pattern: `from managers.cli_manager import CLIManager, ModuleRegistration, Command, CommandArg`
- Handler signature: `def handler_name(args: argparse.Namespace) -> int:`
- Handler path: `"mcps.<module>.<base>_cli:<function_name>"`
- Use `_get_controller()` singleton pattern for controller access.
- Return `int` (0 = success, non-zero = error).

### Controller Pattern (`*_controller.py`)
- Class-based: `class <Name>Controller:`
- Constructor: `def __init__(self, workspace_root: str | Path | None = None):`
- Methods return: `dict[str, Any]` with `{"success": bool, ...}` pattern.
- Logging: `from utils.logger_util import Logger`

### MCP Server (`*_mcp.py`)
- Keep tools under 10 lines—delegate to controller.
- Docstrings are mandatory (become tool descriptions).
- Use `snake_case` for tool names.

## Verification Checklist
Before marking module work complete:
- [ ] Path handling in `__init__.py` and `refresh.py`
- [ ] Using `Logger`, not `print()`
- [ ] Using `ConfigManager` for paths/config
- [ ] Using `ADHDError` for operational errors
- [ ] No circular imports
- [ ] Type hints on all functions
- [ ] `refresh.py` is re-runnable (idempotent)
---
applyTo: "mcps/**/*.py"
---

# MCP Server Development Guidelines

## Goals
- Standardize MCP server development using FastMCP pattern.
- Ensure clean separation between API layer (`*_mcp.py`) and business logic (`*_controller.py`).
- Guide agents to build consistent, maintainable MCP servers.

## Rules

### 1. **File Structure**: Every MCP MUST have these core files:
```
mcps/<module_name>/
├── __init__.py           # Exports, path setup, auto-refresh
├── init.yaml             # Module metadata (ADHD framework)
├── <name>_mcp.py         # FastMCP server: tool decorators ONLY
├── <name>_controller.py  # Business logic: all implementation here
├── refresh.py            # Optional: module refresh logic
├── requirements.txt      # MCP-specific dependencies
├── tests/                # Unit tests (optional)
└── playground/           # Interactive exploration (optional)
```
Add additional files as needed (e.g., `models.py`, `helpers.py`, `constants.py`).

### 2. **Separation of Concerns**:
- `*_mcp.py`: Thin wrapper. Contains ONLY `@mcp.tool()` decorators that delegate to controller.
- `*_controller.py`: All business logic, file I/O, validation, state management.
- NEVER put implementation logic in `*_mcp.py`—keep it under 10 lines per tool.

### 3. **FastMCP Setup** (in `*_mcp.py`):
```python
from mcp.server.fastmcp import FastMCP
from mcps.<module>.<name>_controller import <Name>Controller

mcp = FastMCP(name="<name>", instructions="<description>")
_controller: <Name>Controller | None = None

def _get_controller() -> <Name>Controller:
    global _controller
    if _controller is None:
        _controller = <Name>Controller()
    return _controller

@mcp.tool()
def my_tool(arg: str) -> dict:
    """Docstring becomes tool description. Args in docstring for schema."""
    return _get_controller().my_tool(arg)

def main() -> None:
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
```

### 4. **Controller Pattern** (in `*_controller.py`):
- Class-based with `__init__(workspace_root: str | Path | None = None)`.
- All methods return `dict[str, Any]` with `{"success": bool, ...}` pattern.
- Use `Logger` from `utils.logger_util` for logging.
- Provide module-level `get_<name>_controller()` singleton function.

### 5. **CLI Registration** (`*_cli.py`):
- Import: `from managers.cli_manager import CLIManager, ModuleRegistration, Command, CommandArg`
- Handler signature: `def handler_name(args: argparse.Namespace) -> int:`
- Handler path: `"mcps.<module>.<base>_cli:<function_name>"`
- Use `_get_controller()` singleton pattern for controller access.
- Return `int` (0 = success, non-zero = error).

### 6. **Logging**: NEVER use `print()` in STDIO-based MCP servers—corrupts JSON-RPC. Use:
```python
from utils.logger_util import Logger
log = Logger(name="<ControllerName>", verbose=False)
log.info("Safe logging to stderr")
```

### 7. **Tool Naming**: Follow MCP spec—use `snake_case` for tool names.

### 8. **Docstrings**: Required for every tool. FastMCP auto-generates schema from:
- Function docstring → tool description
- Type hints → argument types
- Docstring `Args:` section → argument descriptions

## External Documentation
- MCP Server Guide: https://modelcontextprotocol.io/docs/develop/build-server
- Core concepts: Resources (file-like data), Tools (LLM-callable functions), Prompts (templates)

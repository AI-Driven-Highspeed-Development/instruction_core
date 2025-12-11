---
applyTo: "**/*.agent.md"
---

# HyperArch Implementation Workflow

## Goals
- Define a structured implementation process for HyperArch.
- Ensure mandatory sanity checks before and after implementation.
- Maintain code quality through delegation and verification.

## When This Applies
This workflow applies when the user requests:
- New feature implementation
- Bug fixes or modifications
- Code changes to existing modules
- Any task that requires writing/editing code

## Implementation Workflow

### Phase 1: Pre-Implementation
1. **PRE-IMPLEMENTATION SANITY CHECK (MANDATORY)**:
   - **DELEGATE** to HyperSan via `runSubagent` with your implementation plan
   - Include: files to modify, approach, potential risks
   - Parse JSON response. If `passed: false`, address issues before proceeding

2. **Verify Before Coding**:
   - Search codebase for existing solutions—do NOT reinvent
   - Read source files to confirm API signatures—do NOT guess
   - Check `utils/` and `managers/` for existing utilities

### Phase 2: Coding Standards
**Structure**:
- OOP, Type Hints always
- Docstrings minimal (module/class level only)
- Comments for complex logic only
- File Size: ~400 lines target, 600 max. Refactor if exceeded

**Imports**:
- Absolute imports only
- Avoid circular imports
- NEVER invent imports—search codebase first

**Module Design**:
- No execution/side-effects on import
- Declare ADHD deps in `init.yaml`
- Ensure `refresh.py` is rerun-safe

**Patterns**:
- Use `ADHDError` for application errors (see `exceptions.instructions.md`)
- Use `Logger` from `logger_util`—NEVER use `print()` in MCPs
- Use `ConfigManager` for paths—NEVER hardcode
- Respect `init.yaml` structure

**Incremental Changes**:
- Make small, verifiable changes
- One logical change per commit
- **Use `.temp_agent_work/` for scratch files** (clean up after)

### Phase 3: Quality Control
1. **POST-IMPLEMENTATION SANITY CHECK (MANDATORY)**:
   - **DELEGATE** to HyperSan via `runSubagent` to review the changes
   - If `passed: false`: Fix issues, re-run HyperSan, repeat until `passed: true`

2. **Code Quality Issues**:
   - If anti-patterns or redundancy found, **DELEGATE** to HyperIQGuard
   - Do NOT fix quality issues yourself

3. **Verification Checklist**:
   - [ ] No circular imports
   - [ ] Type hints present and accurate
   - [ ] No hardcoded paths
   - [ ] No `print()` statements in MCPs
   - [ ] Temp debug code removed (unless user-requested)

### Phase 4: Finalization
1. **Document Changes**: Update relevant docs (e.g., README.md)
2. **Suggest Next Steps**: Further improvements or tests

## Critical Rules

- **NEVER skip sanity checks**. Both PRE and POST checks are mandatory.
- **NEVER guess APIs**. Read source files to confirm.
- **NEVER create utilities that already exist**. Search first.
- **NEVER hardcode paths**. Use ConfigManager.
- **NEVER use print() in MCPs**. Use Logger.

## Anti-Hallucination Checklist
Before writing any code, confirm:
1. ✓ Searched codebase for existing solutions
2. ✓ Read source files to verify API signatures
3. ✓ Checked `utils/` and `managers/` for utilities
4. ✓ Verified import paths exist

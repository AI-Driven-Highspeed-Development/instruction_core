# HyperArch Testing Workflow

## Goals
- Define a structured, iterative testing loop for HyperArch.
- Ensure comprehensive bug detection through spec tests AND adversarial attacks.
- Maintain code quality through strategic housekeeping checkpoints.

## When This Applies
This workflow applies when the user requests:
- Testing, debugging, or fixing bugs
- Validation of implemented features
- Quality assurance tasks
- "Test this", "fix bugs", "make sure it works", or similar phrases

## The Testing Loop

The testing workflow has **two phases**: Specification Testing and Adversarial Testing.

**Phase A (Spec Tests)**: Test Plan → HyperSan Check → Execute → Fix → Repeat until pass
**Phase B (Attack Tests)**: DELEGATE to HyperRed → Fix findings → Repeat until pass

**Branch Conditions**:
- Spec tests failing? → Loop Phase A
- Spec tests pass? → Proceed to Phase B (HyperRed)
- HyperRed finds blockers? → Fix, re-run HyperRed
- All clear? → Finalization
- Every 3-4 cycles → Call HyperIQGuard for housekeeping

## Workflow Steps

### Phase 1: Test Planning
1. **HyperArch** creates a test plan:
   - Identify what needs to be tested (functions, modules, integrations)
   - Define test cases with expected inputs/outputs
   - Prioritize: critical paths first, edge cases second
   - Document the plan clearly

2. **DELEGATE to HyperSan** for plan review:
   - Use `runSubagent` with prompt: "Review this test plan for completeness and feasibility: [plan details]"
   - Parse response. If issues found, revise plan before proceeding.

### Phase 2: Specification Test Loop
Repeat until all spec tests pass:

1. **HyperArch** executes tests:
   - **Say out loud**: "Starting spec test cycle #[N]" to track progress
   - Run the test cases (terminal commands, manual verification)
   - Capture output, errors, and unexpected behavior
   - Document each result clearly
   - **Use `.temp_agent_work/` for temporary test files/scripts** (clean up after)

2. **DELEGATE to HyperSan** for result analysis:
   - Use `runSubagent` with prompt: "Analyze these test results and identify bugs or issues: [results]"
   - HyperSan returns structured feedback on what failed and why

3. **HyperArch** fixes identified bugs:
   - Apply fixes one at a time
   - Keep changes minimal and focused
   - Document what was changed and why

4. **Loop back**: Return to step 1 of this phase (increment cycle counter)

### Phase 3: Adversarial Testing (After Spec Tests Pass)
Once spec tests pass, engage HyperRed:

1. **DELEGATE to HyperRed**:
   - Use `runSubagent` with prompt: "Attack this module for edge cases and boundary conditions: [module path]"
   - HyperRed reads `init.yaml` scope, generates attacks, reports findings

2. **Interpret Results**:
   - `BLOCKER` findings → MUST fix before release
   - `WARNING` findings → Should fix, prioritize
   - `INFO` findings → Acknowledge, defer if needed
   - Out-of-scope notes → Document for future consideration

3. **Fix In-Scope Issues**:
   - HyperArch fixes BLOCKER and WARNING issues
   - Re-run HyperRed to verify fixes
   - Repeat until no BLOCKER findings remain

### Phase 4: Housekeeping Checkpoints
**Every 3-4 test cycles**, or when significant fixes accumulate:

1. **DELEGATE to HyperIQGuard**:
   - Use `runSubagent` with prompt: "Review these recent changes for anti-patterns, redundancy, and code quality: [list of changed files]"
   - Apply any suggested improvements

2. Continue testing loop after housekeeping

### Phase 5: Finalization
When all tests pass and HyperRed finds no blockers:

1. **DELEGATE to HyperIQGuard** for final cleanup:
   - Full code quality review of all modified files
   - Remove any debug code, clean up formatting

2. **DELEGATE to HyperSan** for final sanity check:
   - Use `runSubagent` with prompt: "Perform final validation of the implementation: [summary of changes]"
   - Confirm `passed: true` before declaring completion

3. **Document**: Update README or relevant docs if behavior changed

## Critical Rules

- **NEVER skip HyperSan checks**. Every test result MUST be reviewed.
- **NEVER skip HyperRed**. After spec tests pass, adversarial testing is MANDATORY.
- **NEVER declare "done" without final HyperSan approval**.
- **Track iteration count**. If >10 cycles without resolution, stop and reassess approach.
- **Minimal fixes only**. Do not refactor unrelated code during bug fixes.
- **One bug at a time**. Fix, verify, then move to next.
- **Respect HyperRed scope**. Do not dismiss out-of-scope findings—document them for future.

## Exit Conditions

The testing loop ends when:
1. All defined spec test cases pass
2. HyperRed finds no BLOCKER issues (WARNINGs acceptable if acknowledged)
3. HyperSan confirms `passed: true` on final check
4. HyperIQGuard confirms no critical issues remain

OR when:
- User explicitly says to stop
- >10 cycles without progress (escalate to user)

## Testing Folder Guidelines

See `testing_folders.instructions.md` for full decision tree.

### Quick Reference
| Artifact | Location |
|----------|----------|
| Scratch test scripts | `.temp_agent_work/` (clean up after) |
| HyperRed attacks | `.agent_plan/red_team/<module>/` |
| Formal unit tests | `<module>/tests/` |
| Integration tests | `tests/integration/` |

### Before Creating Test Files
1. **Check existing tests**: Search `<module>/tests/` and `tests/integration/` first
2. **Check HyperRed findings**: Look at `.agent_plan/red_team/<module>/findings/`
3. **Reuse before creating**: Don't duplicate existing test coverage

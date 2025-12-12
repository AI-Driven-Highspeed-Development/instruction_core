# HyperArch Testing Workflow

## Goals
- Define a structured, iterative testing loop for HyperArch.
- Ensure comprehensive bug detection and resolution through repeated validation cycles.
- Maintain code quality through strategic housekeeping checkpoints.

## When This Applies
This workflow applies when the user requests:
- Testing, debugging, or fixing bugs
- Validation of implemented features
- Quality assurance tasks
- "Test this", "fix bugs", "make sure it works", or similar phrases

## The Testing Loop

The testing workflow is an **iterative cycle** that continues until all bugs are resolved:

**Core Loop**: Test Plan (HyperArch) → Check Plan (HyperSan) → Do Test (HyperArch) → Run & Observe (HyperArch) → Check Test (HyperSan) → Fix Bugs (HyperArch) → [REPEAT]

**Branch Conditions**:
- Bugs remain? → Loop back to "Do Test"
- All fixed? → Proceed to Finalization
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

### Phase 2: Test Execution Loop
Repeat until all tests pass:

1. **HyperArch** executes tests:
   - **Say out loud**: "Starting test cycle #[N]" to track progress
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

### Phase 3: Housekeeping Checkpoints
**Every 3-4 test cycles**, or when significant fixes accumulate:

1. **DELEGATE to HyperIQGuard**:
   - Use `runSubagent` with prompt: "Review these recent changes for anti-patterns, redundancy, and code quality: [list of changed files]"
   - Apply any suggested improvements

2. Continue testing loop after housekeeping

### Phase 4: Finalization
When all tests pass consistently:

1. **DELEGATE to HyperIQGuard** for final cleanup:
   - Full code quality review of all modified files
   - Remove any debug code, clean up formatting

2. **DELEGATE to HyperSan** for final sanity check:
   - Use `runSubagent` with prompt: "Perform final validation of the implementation: [summary of changes]"
   - Confirm `passed: true` before declaring completion

3. **Document**: Update README or relevant docs if behavior changed

## Critical Rules

- **NEVER skip HyperSan checks**. Every test result MUST be reviewed.
- **NEVER declare "done" without final HyperSan approval**.
- **Track iteration count**. If >10 cycles without resolution, stop and reassess approach.
- **Minimal fixes only**. Do not refactor unrelated code during bug fixes.
- **One bug at a time**. Fix, verify, then move to next.

## Exit Conditions

The testing loop ends when:
1. All defined test cases pass
2. HyperSan confirms `passed: true` on final check
3. HyperIQGuard confirms no critical issues remain

OR when:
- User explicitly says to stop
- >10 cycles without progress (escalate to user)

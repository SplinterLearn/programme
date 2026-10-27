# 0004. AI licence ladder L0–L3

**Status:** Accepted

## Context
RCTs show that unguarded AI improves practice scores and harms learning, with debugging hit hardest ([research report](../design/research-report.md), key findings 1–3). Students who use AI for conceptual questions do well; students who delegate do badly.

## Decision
AI help is earned in four levels ([architecture 3.2](../design/architecture.md)); machine-readable in [`tutor/licence-levels.yaml`](../../tutor/licence-levels.yaml):

| Level | Unlocked | Bot may | Bot must not |
|---|---|---|---|
| L0 Tutor | start | generic examples, leading questions, point to the error line | write or fix code for the student's task; more than one step at a time |
| L1 Explainer | Block 2 exit | explain the student's code line by line; name the bug type | write new code for the task |
| L2 Pair | Block 4 exit | snippets ≤ 10 lines, each followed by an explain-back | whole functions or files |
| L3 Supervisor | Block 5 exit | review specs and agent diffs; coach prompting a coding agent | (the explain-back gate stays) |

A **parent or mentor approves each upgrade**. The bot only proposes it.

## Consequences
- Every block's `licence_level` and `licence_unlock_on_exit` fields encode the ladder. validate.py checks that modules match their block.
- The output guard ([`tutor/output-guard-prompt.md`](../../tutor/output-guard-prompt.md)) enforces the ladder per reply.
- Each block keeps at least one AI-off item (the explain-back micro-task).

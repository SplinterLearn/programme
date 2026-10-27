---
id: b1-skip
block: b1
status: ready
kind: module-gates
ai: "off"
modules: [m1.1, m1.2, m1.3]
time_box_minutes_per_module: 30
explain_back: {sample_per_module: 2, micro_task_per_module: 1}
---
# B1 skip test

For students who already use a terminal comfortably ([ADR 0008](../../docs/decisions/0008-skip-test-is-exit-gate.md)).

## What you do
1. **The hunt, AI-off, 30 minutes.** The bot copies `b1-hunt/` into your repo. Complete it with terminal commands only, then open a PR. The PR's tests must be green.
2. **The setup checks from M1.3:** a PR opened from your own branch (the hunt PR counts).
3. **Explain-back:** 2 questions from each of M1.1, M1.2 and M1.3, plus one AI-off micro-task from each module. Pass at ≥ 70% overall with all micro-tasks correct ([protocol](../../tutor/explain-back-protocol.md)).

## If you pass
B1 is closed as if you'd done the modules. You still keep `notes/bandit.md` optional. Bandit is fun, so try it anyway.

## If you don't
No problem: you've found out what to practise. Start M1.1. Retry after 12 hours with different questions.

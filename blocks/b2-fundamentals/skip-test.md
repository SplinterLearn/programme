---
id: b2-skip
block: b2
status: ready
kind: module-gates
ai: "off"
modules: [m2.1, m2.2, m2.3, m2.4, m2.5]
time_box_minutes_per_module: 60
explain_back: {sample_per_module: 2, micro_task_per_module: 1}
---
# B2 skip test

For students who already know Python basics ([ADR 0008](../../docs/decisions/0008-skip-test-is-exit-gate.md)). **A skip test is the exit gate taken without the lessons.**

## Module skip test (one module)
For each module you want to skip, the bot runs that module's exit gate:

1. **Gate A, the artefact:** the module's remix in your track, **AI-off, 60 minutes**. The bot copies the starter and tests in when you say "go", and the clock starts. Push and open a PR. Tests must be green, and the rubric review must be ≥ 5/8.
2. **Gate B, understanding:** the module's explain-back, including its AI-off micro-task. Pass at ≥ 70% with the micro-task correct.

Because the remix grows through the block, skipping module *N* means building step *N* on top of your earlier steps, or on the checkpoint of step *N − 1* if you skipped that too.

## Block skip test (all of B2)
All five modules' Gate A in order (60 minutes each, in separate sittings if you like), then **one combined explain-back**: 2 questions sampled from each module plus one micro-task per module, so all competencies are covered across the block.

Passing the whole block counts as the **Block 2 exit**: the bot then proposes the upgrade to **L1**, and a parent or mentor approves it.

## Status
Only M2.1 is `ready`. While M2.2–M2.5 are drafts, the bot offers only the M2.1 module skip test and tells the student the rest of the block test is coming. TODO(next-task) when M2.2–M2.5 become ready.

## If you don't pass
That's useful information, not a failure. Do the module normally (you'll fly through the parts you know). Retry after 12 hours with different questions.

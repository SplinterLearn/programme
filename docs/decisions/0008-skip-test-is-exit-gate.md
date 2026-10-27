# 0008. Skip test = the module's exit gate

**Status:** Accepted

## Context
Students arrive with different backgrounds. A separate placement test would drift away from what "done" means.

## Decision
- A **module skip test** is the module's exit gate taken without the lessons: the same remix, **AI-off**, **time-boxed to 60 minutes**, plus the same explain-back (with micro-task).
- A **block skip test** is all its modules' exit gates, with explain-back questions sampled from each module.
- Encoded as `skip_gate: {time_box_minutes, ai: off}` in each module and `blocks/<b>/skip-test.md` per block.
- Exceptions: B0 (onboarding) has no skip test. B1's hunt is time-boxed to 30 minutes. B3's skip test is task-based (branch, PR, review reply, staged conflict), so git-savvy students can test out before B3's modules are written.

## Consequences
- Passing tells the bot the competencies are met. The same coverage table applies.
- The block project must be bootstrappable: a student who skips M2.1 can start M2.2 from the M2.1 checkpoint.

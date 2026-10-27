# 0002. Modules are defined by competencies, not by a course

**Status:** Accepted

## Context
Courses change, move or don't suit every student. If a module is "CS50P lecture 2", the programme breaks when the student or the course changes.

## Decision
- Each module lists **can-do competencies** and an **exit gate**. External resources are *recommended* and interchangeable (`role: backbone | fallback | extra | optional`).
- **CS50P is the default backbone for Python fundamentals**, with futurecoder.io and freeCodeCamp as fallbacks.
- **Switch signals** (also in `ROADMAP.md`):
  - stuck on one problem set for more than 3 sessions even with the Duck → drop to futurecoder for that topic, then return;
  - skipping or skimming lectures → move the backbone to something more interactive;
  - passes `check50` but fails explain-back → slow down, add predict-first exercises;
  - bored or finishing too easily → take the skip test.

## Consequences
- The gate (tests, rubric, explain-back) never depends on which resource the student used.
- The bot's stuck detection ([architecture 3.5](../design/architecture.md)) can suggest the fallback resource from `module.md`.

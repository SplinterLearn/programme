---
id: b4
title: "Reading, debugging, testing"
weeks: [15, 17]
licence_level: L1
licence_unlock_on_exit: L2
goals:
  - Read unfamiliar code and explain what it does before changing it
  - Debug systematically with a debugger and print statements, AI-off
  - Write your own tests with pytest, test-first when it helps
  - Understand at a high level how a computer runs your code (interpreters, compilers, runtimes)
modules:
  - {id: m4.1, title: "Reading unfamiliar code", status: stub}
  - {id: m4.2, title: "Debugging (debugger, AI-off)", status: stub}
  - {id: m4.3, title: "Testing & TDD with pytest (CS50P L5)", status: stub}
  - {id: m4.4, title: "How languages run code (interpreters, compilers, runtimes; light)", status: stub}
exit: "Student-written tests for the block project, plus 5 seeded bugs fixed AI-off"
status: stub
project: null
skip_test: null
---
# B4 Reading, debugging, testing

**Weeks 15–17 · licence L1, then L2 on exit · stub**

## Goals
The skills that matter most when AI writes code: **reading** it, **debugging** it, and **testing** it. Debugging is the skill unguarded AI harms most ([research report](../../docs/design/research-report.md), key finding 2), so this block has AI-off sessions.

## Plan
- The remix changes: from here **you write the tests** (support fades, [ADR 0009](../../docs/decisions/0009-growing-remix-per-block.md)). Your Block 2 project gets your own tests and a refactor.
- Backbone for M4.3: CS50P Lecture 5 (Unit Tests, pytest), https://cs50.harvard.edu/python/weeks/5/ (verified 2026-10-27).
- M4.2: VS Code's debugger in cs50.dev. TODO(verify): resource choice.
- M4.4: light, conceptual. TODO(next-task): pick a resource.

## Exit
Tests you wrote for your block project, plus **5 seeded bugs fixed AI-off**. Passing unlocks **L2 Pair**, after a parent or mentor approves it.

## Licence
L1 during the block; L2 on exit.

## Skip test
TODO(next-task): module-gates skip test once the modules exist.

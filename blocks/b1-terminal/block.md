---
id: b1
title: "The machine & the terminal"
weeks: [2, 4]
licence_level: L0
licence_unlock_on_exit: null
goals:
  - Understand files, folders and paths well enough to never get lost
  - Use the terminal confidently to navigate, create, move, copy, delete, find and search
  - Run Python scripts in a real development environment and get work into your repo with a PR
modules:
  - {id: m1.1, title: "Files, folders & paths", status: ready}
  - {id: m1.2, title: "Terminal basics", status: ready}
  - {id: m1.3, title: "Dev environment", status: ready}
exit: "Terminal scavenger hunt (b1-hunt/) completed with terminal commands only, checked by a provided pytest, merged via your first PR"
status: ready
project: null
skip_test: skip-test.md
---
# B1 The machine & the terminal

**Weeks 2–4 · licence L0 · 3 modules, about 9 sessions**

## Goals
1. **Files, folders and paths.** Where things live on a computer, and how to say where they are (absolute and relative paths).
2. **The terminal.** Talk to the computer by typing: navigate, create, move, copy, delete, find and search. Practise with a real game, OverTheWire **Bandit**.
3. **A dev environment.** Edit and run Python in cs50.dev (VS Code in the browser), and get work into your repo with a commit, a push and a PR.

## Why it matters
Every developer tool (git, Python, test runners, deploy tools, coding agents) is driven from the terminal. AI agents run terminal commands for you later in the year; you need to read and judge them. And when the terminal stops being scary, everything after it gets easier.

## Exit
The **terminal scavenger hunt**: when M1.2 starts, `b1-hunt/` is copied into your repo. You build a folder structure, move, copy and delete files, and search a haystack, all with terminal commands only. A provided test (`test_hunt.py`) checks the result, and your PR with green tests is the exit artefact. Its explain-back asks how you did each step.

## Licence
L0 (Tutor) throughout. The bot can explain any command with its own examples and nudge you with questions. It won't type your hunt commands for you.

## Skip test
Already live in a terminal? Take the [skip test](skip-test.md): the hunt in 30 minutes, AI-off, plus explain-back questions from all three modules.

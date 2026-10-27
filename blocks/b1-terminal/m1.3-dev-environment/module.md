---
id: m1.3
block: b1
title: "Dev environment"
status: ready
weeks: [4, 4]
est_sessions: 3
licence_level: L0
competencies:
  - {id: m1.3.c1, text: "Can tell apart the editor, the terminal and the Python interpreter, and say what each one does"}
  - {id: m1.3.c2, text: "Can create, edit and save a Python file in VS Code (cs50.dev) and run it with python from the right folder"}
  - {id: m1.3.c3, text: "Can explain what clone, add, commit and push do, and what a commit is"}
  - {id: m1.3.c4, text: "Can create a branch, push it, open a pull request on GitHub and read the result of the automatic tests"}
  - {id: m1.3.c5, text: "Can run pytest locally and tell a passing run from a failing one"}
resources:
  - title: "cs50.dev — Visual Studio Code for CS50"
    url: https://cs50.dev/
    role: backbone
    notes: "Browser VS Code with Python, git and (per CS50's image) pytest already installed. TODO(verify): pytest preinstalled on cs50.dev; CS50's cli image Dockerfile lists it, but cs50.dev itself doesn't say. If missing: pip install pytest."
    verified_on: 2026-10-27
  - title: "The Odin Project — Git Basics"
    url: https://www.theodinproject.com/lessons/foundations-git-basics
    role: backbone
    notes: "Read for what clone/add/commit/push mean. Use your student repo, not a new one, for the practice."
    verified_on: 2026-10-27
  - title: "CS50P — Lecture 0 (first 10 minutes: running code in VS Code)"
    url: https://cs50.harvard.edu/python/weeks/0/
    role: extra
    notes: "A preview of Block 2: how CS50P uses VS Code and the terminal."
    verified_on: 2026-10-27
sessions:
  - n: 1
    type: practice
    title: "Editor, terminal, interpreter: a tour of cs50.dev; write and run hello.py; break it on purpose and read the error"
    where: "cs50.dev + bot"
    ai: bot-L0
  - n: 2
    type: reading
    title: "What your git commands actually do: Odin Git Basics; branch → commit → push → PR, with the hunt PR (or a small notes PR) as the example"
    where: "The Odin Project + cs50.dev + github.com + bot"
    ai: bot-L0
    notes: "Branches and PRs in depth come in Block 3. Here: enough to run the module loop."
  - n: 3
    type: quiz
    title: "pytest locally, read the CI check on your PR, then the B1 explain-back"
    where: "cs50.dev + github.com + Telegram (bot)"
    ai: bot-quiz
cs50_fingerprints: []
checks:
  - {id: m1.3.k1, text: "The student has opened at least one PR from their own branch in their repo (the hunt PR counts)", verified_by: bot}
  - {id: m1.3.k2, text: "The hunt PR's automatic tests are green", verified_by: ci}
explain_back: true
remix: null
coverage:
  m1.3.c1: ["eb:m1.3.q1", "eb:m1.3.q2"]
  m1.3.c2: ["eb:m1.3.q2", "eb:m1.3.q8"]
  m1.3.c3: ["eb:m1.3.q3", "eb:m1.3.q4"]
  m1.3.c4: ["check:m1.3.k1", "eb:m1.3.q5"]
  m1.3.c5: ["check:m1.3.k2", "eb:m1.3.q6", "eb:m1.3.q7"]
skip_gate: {time_box_minutes: 30, ai: "off"}
student_files: []
---
# M1.3 Dev environment

The tools you'll use every day for the rest of the year, and what your copy-paste git commands from M0.2 actually do.

## Sessions
1. **Editor, terminal, interpreter.** In cs50.dev, create `hello.py` with one `print`. Run it with `python hello.py`, then break it on purpose (delete a quote) and read the error.
2. **Git for real (just enough).** A **commit** is a saved snapshot with a message. `add` chooses what goes into it, `commit` saves it, `push` sends it to GitHub, and `clone` made your copy in the first place. A **branch** is a separate line of work. A **pull request** asks to merge a branch into `main`, and it's where tests run and reviews happen. Block 3 goes deeper ([ADR 0016](../../../docs/decisions/0016-git-by-exposure-before-b3.md)).
3. **Tests.** Run `pytest b1-hunt` and read the output. Then look at the green or red check on your PR: it's the same tests, run by GitHub. That's **CI**. Then the B1 explain-back.

## Coverage
| Competency | Checked by |
|---|---|
| c1 Editor vs terminal vs interpreter | q1, q2 |
| c2 Edit & run Python | q2, micro-task q8 |
| c3 clone/add/commit/push | q3, q4 |
| c4 Branch + PR | k1, q5 |
| c5 pytest, CI | k2, q6, q7 |

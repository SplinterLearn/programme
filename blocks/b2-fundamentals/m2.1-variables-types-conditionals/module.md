---
id: m2.1
block: b2
title: "Variables, types & conditionals"
status: ready
weeks: [5, 6]
est_sessions: 6
licence_level: L0
competencies:
  - {id: m2.1.c1, text: "Can store and update values in variables with meaningful names"}
  - {id: m2.1.c2, text: "Can tell str, int, float and bool apart, convert between them with int(), float() and str(), and explain why \"2\" + \"3\" is \"23\""}
  - {id: m2.1.c3, text: "Can read input and print formatted output with f-strings"}
  - {id: m2.1.c4, text: "Can write a small function with parameters and a return value"}
  - {id: m2.1.c5, text: "Can use comparisons, and/or/not, and if / elif / else"}
  - {id: m2.1.c6, text: "Can read a simple traceback (TypeError, ValueError) and find the failing line"}
resources:
  - title: "CS50P — Lecture 0: Functions, Variables"
    url: https://cs50.harvard.edu/python/weeks/0/
    role: backbone
    notes: "Watch in chunks with the bot's predict checkpoints between them."
    verified_on: 2026-10-27
  - title: "CS50P — Problem Set 0"
    url: https://cs50.harvard.edu/python/psets/0/
    role: backbone
    notes: "Done in cs50.dev, checked with check50, submitted with submit50. Only the CS50 Duck (cs50.ai) helps on problem sets."
    verified_on: 2026-10-27
  - title: "CS50P — Lecture 1: Conditionals"
    url: https://cs50.harvard.edu/python/weeks/1/
    role: backbone
    notes: "Watch in chunks with predict checkpoints."
    verified_on: 2026-10-27
  - title: "CS50P — Problem Set 1"
    url: https://cs50.harvard.edu/python/psets/1/
    role: backbone
    notes: "Duck only. Meal Time is the first problem that requires main() and the if __name__ == \"__main__\" line."
    verified_on: 2026-10-27
  - title: "futurecoder.io (free, browser-based)"
    url: https://futurecoder.io/
    role: fallback
    notes: "Chapters on string basics, variables and if statements (chapter names from futurecoder's source repo; TODO(verify): titles as shown on the live site). Switch here for a topic if stuck for 3+ sessions on a problem set, then return."
    verified_on: 2026-10-27
  - title: "freeCodeCamp — Python Certification"
    url: https://www.freecodecamp.org/learn/python-v9
    role: fallback
    notes: "Alternative interactive backbone if lectures aren't working for the student (switch signal: skipping/skimming lectures). TODO(verify): which of its early sections match this module."
    verified_on: 2026-10-27
sessions:
  - n: 1
    type: lecture
    title: "Lecture 0, first half, in 3 chunks with predict checkpoints from the bot between chunks"
    where: "CS50P (video) + bot"
    ai: bot-predict
  - n: 2
    type: pset
    title: "Lecture 0, second half (functions), then the first problems of Problem Set 0"
    where: "CS50P + cs50.dev"
    ai: duck
    notes: "Duck mode: the bot helps with plan, motivation and breaks only."
  - n: 3
    type: pset
    title: "Finish Problem Set 0 and submit50; afterwards a 10-minute bot quiz on Lecture 0 concepts"
    where: "cs50.dev, then bot"
    ai: duck
    notes: "The quiz starts only after the student says they've submitted; until then Duck mode."
  - n: 4
    type: lecture
    title: "Lecture 1 (conditionals) in chunks with predict checkpoints"
    where: "CS50P (video) + bot"
    ai: bot-predict
  - n: 5
    type: pset
    title: "Problem Set 1"
    where: "cs50.dev"
    ai: duck
  - n: 6
    type: remix
    title: "Remix in your repo → PR → review → explain-back → merge → retro"
    where: "student repo + bot"
    ai: bot-L0
cs50_fingerprints:
  - problem: "Indoor Voice"
    pset: 0
    filename: indoor.py
    required_functions: []
    distinctive_strings: []
    summary: "Reads a line of text and prints it back in all lowercase."
  - problem: "Playback Speed"
    pset: 0
    filename: playback.py
    required_functions: []
    distinctive_strings: ["..."]
    summary: "Reads text and prints it with the spaces replaced by three dots, like slowed-down speech."
  - problem: "Making Faces"
    pset: 0
    filename: faces.py
    required_functions: [convert, main]
    distinctive_strings: [":)", ":("]
    summary: "Replaces text emoticons for happy and sad faces with the matching emoji, via a convert function."
  - problem: "Einstein"
    pset: 0
    filename: einstein.py
    required_functions: []
    distinctive_strings: ["300000000"]
    summary: "Reads a mass in kilograms and prints the equivalent energy using E = mc squared."
  - problem: "Tip Calculator"
    pset: 0
    filename: tip.py
    required_functions: [dollars_to_float, percent_to_float]
    distinctive_strings: ["Leave $"]
    summary: "Finishes two helper functions that turn a dollar amount and a percentage string into numbers to compute a tip."
  - problem: "Deep Thought"
    pset: 1
    filename: deep.py
    required_functions: []
    distinctive_strings: ["42", "forty-two", "forty two"]
    summary: "Asks the big question about life and answers Yes or No depending on whether the reply is a particular number."
  - problem: "Home Federal Savings Bank"
    pset: 1
    filename: bank.py
    required_functions: []
    distinctive_strings: ["$0", "$20", "$100"]
    summary: "Gives a dollar amount depending on how a greeting starts."
  - problem: "File Extensions"
    pset: 1
    filename: extensions.py
    required_functions: []
    distinctive_strings: ["image/gif", "application/octet-stream"]
    summary: "Prints the media type that matches a file name's extension, with a default for unknown ones."
  - problem: "Math Interpreter"
    pset: 1
    filename: interpreter.py
    required_functions: []
    distinctive_strings: []
    summary: "Reads a simple arithmetic expression of two integers and an operator and prints the result as a float."
  - problem: "Meal Time"
    pset: 1
    filename: meal.py
    required_functions: [convert, main]
    distinctive_strings: ["breakfast time", "lunch time", "dinner time"]
    summary: "Converts a clock time to hours with a convert function and says which meal it is time for, if any."
checks: []
explain_back: true
remix:
  project_id: b2-planner
  step: 1
  tracks: [finance, fandom]
  brief_only_tracks: [web-social, games]
  rubric: remix-default
  edge_case:
    summary: "Zero rate: saving or watching nothing per week/day means the goal is never reached (division by zero)"
    per_track:
      finance: "weeks_to_goal(price, saved, per_week=0) when saved < price"
      fandom: "days_to_finish(episodes_left, episodes_per_day=0) when episodes_left > 0"
      web-social: "engagement_rate(likes, comments, followers=0)"
      games: "room_outcome with a choice typed in a different case or with spaces, e.g. \"Door \""
    covered_by: ["eb:m2.1.q7", "eb:m2.1.q8", "rubric:edge_thinking"]
coverage:
  m2.1.c1: ["rubric:readability", "eb:m2.1.q3", "eb:m2.1.q4", "eb:m2.1.q9"]
  m2.1.c2: ["test:test_returns_int", "eb:m2.1.q1", "eb:m2.1.q2", "eb:m2.1.q14", "eb:m2.1.q15"]
  m2.1.c3: ["eb:m2.1.q1", "eb:m2.1.q2", "eb:m2.1.q11"]
  m2.1.c4: ["test:test_exact_division", "test:test_rounds_up", "test:test_nothing_left", "eb:m2.1.q3", "eb:m2.1.q4", "eb:m2.1.q10"]
  m2.1.c5: ["test:test_verdicts", "test:test_verdict_boundaries", "eb:m2.1.q5", "eb:m2.1.q6", "eb:m2.1.q9", "eb:m2.1.q12"]
  m2.1.c6: ["eb:m2.1.q13", "eb:m2.1.q14", "eb:m2.1.q15"]
skip_gate: {time_box_minutes: 60, ai: "off"}
student_files:
  - {from: "tracks/{track}/starter/", to: "{project_dir}/"}
  - {from: "tracks/{track}/tests/test_m2_1.py", to: "{project_dir}/tests/test_m2_1.py"}
---
# M2.1 Variables, types & conditionals

*Block 2 · licence L0 · about 2 weeks · 6 sessions of about 1.5 h · CS50P lectures 0–1*

The first real programming module. CS50P teaches it; the bot checks you understood it with predictions; the **remix** turns it into the first step of your own project.

## By the end you can
1. Store and update values in **variables** with meaningful names.
2. Tell **`str`, `int`, `float` and `bool`** apart, convert between them, and explain why `"2" + "3"` is `"23"`.
3. Read **input** and print formatted output with **f-strings**.
4. Write a small **function** with parameters and a `return` value.
5. Use **comparisons**, `and`/`or`/`not` and **`if / elif / else`**.
6. Read a simple **traceback** (`TypeError`, `ValueError`) and find the failing line.

## Sessions
| # | Session | Where | AI help |
|---|---|---|---|
| 1 | Lecture 0, first half, in 3 chunks with **predict checkpoints** | CS50P + bot | bot (Predict) |
| 2 | Lecture 0, second half (functions) + first problems of Problem Set 0 | cs50.dev | **Duck only** |
| 3 | Finish Problem Set 0, `submit50`; then a 10-minute quiz | cs50.dev, then bot | Duck, then bot |
| 4 | Lecture 1 (conditionals) in chunks with predict checkpoints | CS50P + bot | bot (Predict) |
| 5 | Problem Set 1 | cs50.dev | **Duck only** |
| 6 | **Remix** → PR → review → explain-back → merge → retro | your repo + bot | bot (L0) |

**On CS50 problem sets only the CS50 Duck helps** (CS50's academic honesty rules; [ADR 0005](../../../docs/decisions/0005-cs50-boundary-duck-mode.md)). In sessions 2, 3 and 5 the bot is in Duck mode: it helps you plan, keeps you going and reminds you to take breaks, but sends technical questions to [cs50.ai](https://cs50.ai/). Your CS50 solutions stay in cs50.dev and **never** go in your repo.

**Stuck?** On one problem set for more than 3 sessions even with the Duck → do futurecoder's chapters on variables and if statements, then come back ([switch signals](../../../ROADMAP.md#switch-signals)).

## Remix: step 1 of your Block 2 project
See [remix.md](remix.md). When the module starts, your project folder (e.g. `b2-savings/` or `b2-watchlist/`) is created in your repo with a **starter file** (function stubs) and **`tests/test_m2_1.py`** (don't edit). Make the tests pass, write `main()`, open a PR.

One edge case is **deliberately not tested**. The review and the explain-back will ask about it. Passing tests isn't the same as being correct.

## Exit gate: one gate, two paths
| | Learns from scratch | Takes the skip test |
|---|---|---|
| Path | lectures, problem sets, remix with L0 tutor help | goes straight to the gate |
| **Gate A: artefact** | remix passes tests, rubric review ≥ 5/8 | same remix, **AI-off, 60 minutes**, same rubric |
| **Gate B: understanding** | explain-back ≥ 70% + AI-off micro-task | same explain-back + micro-task |

## Coverage
Every competency is checked by at least one gate item. The bot samples explain-back questions so all six are covered every time.

| Competency | Checked by |
|---|---|
| c1 Variables | rubric `readability`; trace q3 (finance) / q4 (fandom); `=` vs `==` q9 |
| c2 Types & conversion | `test_returns_int`; predict q1; "why int()" q2; micro-tasks q14, q15 |
| c3 Input & f-strings | q1, q2, f-string predict q11 (and `main()` in the review) |
| c4 Functions | `test_exact_division`, `test_rounds_up`, `test_nothing_left`; trace q3/q4; return vs print q10 |
| c5 Conditionals & boolean logic | `test_verdicts`, `test_verdict_boundaries`; add-a-verdict q5/q6; q9; boolean predict q12 |
| c6 Reading tracebacks | traceback q13; micro-tasks q14, q15 (name the error and line) |

The deliberate edge case (zero rate) is covered by edge questions q7/q8 and the rubric's `edge_thinking` criterion.

## Checkpoints
Once the module is closed, a clean reference version is available ([ADR 0009](../../../docs/decisions/0009-growing-remix-per-block.md)). If your code is too shaky to build M2.2 on, ask the bot to swap it in. In the next explain-back you'll explain one difference between your version and the checkpoint.

---
id: m2.2
block: b2
title: "Loops"
status: draft
weeks: [7, 8]
est_sessions: 4
licence_level: L0
competencies:
  - {id: m2.2.c1, text: "Can write a while loop whose condition eventually becomes false, and say what makes it stop"}
  - {id: m2.2.c2, text: "Can write a for loop over range() and over the characters of a string"}
  - {id: m2.2.c3, text: "Can keep a running total or counter in a loop"}
  - {id: m2.2.c4, text: "Can use while True with break to repeat until the input is valid"}
  - {id: m2.2.c5, text: "Can trace a loop iteration by iteration and predict its output"}
resources:
  - title: "CS50P — Lecture 2: Loops"
    url: https://cs50.harvard.edu/python/weeks/2/
    role: backbone
    notes: "First part of the lecture (while, for, range, break). Lists and dictionaries are the focus of M2.3."
    verified_on: 2026-10-27
  - title: "CS50P — Problem Set 2"
    url: https://cs50.harvard.edu/python/psets/2/
    role: backbone
    notes: "In M2.2: camelCase, Coke Machine, Just setting up my twttr. Vanity Plates and Nutrition Facts are in M2.3 (ADR 0003). Duck only."
    verified_on: 2026-10-27
  - title: "futurecoder.io"
    url: https://futurecoder.io/
    role: fallback
    notes: "Chapters on for loops and nested loops (titles from futurecoder's source repo; TODO(verify): titles as shown on the live site)."
    verified_on: 2026-10-27
sessions:
  - {n: 1, type: lecture, title: "Lecture 2, loops part, in chunks with predict checkpoints", where: "CS50P (video) + bot", ai: bot-predict}
  - {n: 2, type: pset, title: "Problem Set 2: camelCase, Coke Machine", where: cs50.dev, ai: duck}
  - {n: 3, type: pset, title: "Problem Set 2: Just setting up my twttr; then a 10-minute loops quiz", where: "cs50.dev, then bot", ai: duck}
  - {n: 4, type: remix, title: "Remix step 2 → PR → review → explain-back → merge", where: "student repo + bot", ai: bot-L0}
cs50_fingerprints:
  - problem: "camelCase"
    pset: 2
    filename: camel.py
    required_functions: []
    distinctive_strings: []
    summary: "Converts a variable name written in camel case into snake case."
  - problem: "Coke Machine"
    pset: 2
    filename: coke.py
    required_functions: []
    distinctive_strings: ["Amount Due", "Change Owed"]
    summary: "Simulates a drinks machine that accepts certain coins until the price is paid, then reports change."
  - problem: "Just setting up my twttr"
    pset: 2
    filename: twttr.py
    required_functions: []
    distinctive_strings: []
    summary: "Prints the input text with all vowels removed."
checks: []
explain_back: true
remix:
  project_id: b2-planner
  step: 2
  tracks: [finance, fandom]
  brief_only_tracks: []
  rubric: remix-default
  edge_case:
    summary: "TODO(next-task): choose the deliberately untested edge case (candidate: a goal already reached gives an empty table)"
    per_track:
      finance: "TODO(next-task)"
      fandom: "TODO(next-task)"
    covered_by: ["eb:m2.2.q5"]
coverage:
  m2.2.c1: ["eb:m2.2.q1"]
  m2.2.c2: ["test:test_schedule_lines", "eb:m2.2.q2"]
  m2.2.c3: ["test:test_running_total", "eb:m2.2.q3"]
  m2.2.c4: ["eb:m2.2.q4"]
  m2.2.c5: ["eb:m2.2.q2", "eb:m2.2.q6"]
skip_gate: {time_box_minutes: 60, ai: "off"}
student_files:
  - {from: "tracks/{track}/tests/test_m2_2.py", to: "{project_dir}/tests/test_m2_2.py"}
---
# M2.2 Loops (draft)

*Block 2 · L0 · weeks 7–8 · CS50P Lecture 2 (loops part), Problem Set 2 (first three problems)*

**Draft:** the bot ignores this module until it's `ready`. TODO(next-task): tests, checkpoints, explain-back bank, final edge case.

The remix (step 2) adds a **loop** to the block project: a week-by-week savings table (finance) or a day-by-day watch schedule (fandom). See [remix.md](remix.md). Tests from M2.1 must keep passing.

| Competency | Planned gate items |
|---|---|
| c1 while loops | q1 |
| c2 for / range / strings | `test_schedule_lines`, q2 |
| c3 running totals | `test_running_total`, q3 |
| c4 while True + break | q4 |
| c5 tracing loops | q2, q6 |

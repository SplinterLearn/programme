---
id: m2.4
block: b2
title: "Exceptions"
status: draft
weeks: [10, 10]
est_sessions: 3
licence_level: L0
competencies:
  - {id: m2.4.c1, text: "Can explain what an exception is and read which one was raised and where"}
  - {id: m2.4.c2, text: "Can catch a specific exception with try/except and recover"}
  - {id: m2.4.c3, text: "Can re-prompt until the input is valid by combining a loop with try/except"}
  - {id: m2.4.c4, text: "Can raise an exception (e.g. ValueError) for input that is the right type but not allowed, such as a negative number"}
  - {id: m2.4.c5, text: "Can explain why catching a specific exception is better than a bare except"}
resources:
  - title: "CS50P — Lecture 3: Exceptions"
    url: https://cs50.harvard.edu/python/weeks/3/
    role: backbone
    notes: "With predict checkpoints."
    verified_on: 2026-10-27
  - title: "CS50P — Problem Set 3"
    url: https://cs50.harvard.edu/python/psets/3/
    role: backbone
    notes: "Fuel Gauge, Felipe's Taqueria, Grocery List, Outdated. Duck only."
    verified_on: 2026-10-27
  - title: "futurecoder.io"
    url: https://futurecoder.io/
    role: fallback
    notes: "TODO(verify): futurecoder's coverage of exceptions; may need another fallback."
    verified_on: 2026-10-27
sessions:
  - {n: 1, type: lecture, title: "Lecture 3 with predict checkpoints", where: "CS50P (video) + bot", ai: bot-predict}
  - {n: 2, type: pset, title: "Problem Set 3", where: cs50.dev, ai: duck}
  - {n: 3, type: remix, title: "Remix step 4 → PR → review → explain-back → merge", where: "student repo + bot", ai: bot-L0}
cs50_fingerprints:
  - problem: "Fuel Gauge"
    pset: 3
    filename: fuel.py
    required_functions: []
    distinctive_strings: []
    summary: "Reads a fraction and prints how full a fuel tank is as a percentage, with special outputs near empty and full."
  - problem: "Felipe's Taqueria"
    pset: 3
    filename: taqueria.py
    required_functions: []
    distinctive_strings: ["Baja Taco", "Total:"]
    summary: "Takes menu items one per line until end of input and keeps a running total of the order."
  - problem: "Grocery List"
    pset: 3
    filename: grocery.py
    required_functions: []
    distinctive_strings: []
    summary: "Reads items until end of input and prints a sorted, counted list of them in upper case."
  - problem: "Outdated"
    pset: 3
    filename: outdated.py
    required_functions: []
    distinctive_strings: ["September"]
    summary: "Converts a date written in a common month-first style into year-month-day format."
checks: []
explain_back: true
remix:
  project_id: b2-planner
  step: 4
  tracks: [finance, fandom]
  brief_only_tracks: []
  rubric: remix-default
  edge_case:
    summary: "TODO(next-task): candidate: empty input (just pressing Enter)"
    per_track:
      finance: "TODO(next-task)"
      fandom: "TODO(next-task)"
    covered_by: ["eb:m2.4.q5"]
coverage:
  m2.4.c1: ["eb:m2.4.q1"]
  m2.4.c2: ["test:test_rejects_text", "eb:m2.4.q2"]
  m2.4.c3: ["eb:m2.4.q3"]
  m2.4.c4: ["test:test_rejects_negative", "eb:m2.4.q4"]
  m2.4.c5: ["eb:m2.4.q6"]
skip_gate: {time_box_minutes: 60, ai: "off"}
student_files:
  - {from: "tracks/{track}/tests/test_m2_4.py", to: "{project_dir}/tests/test_m2_4.py"}
---
# M2.4 Exceptions (draft)

*Block 2 · L0 · week 10 · CS50P Lecture 3, Problem Set 3*

**Draft.** TODO(next-task): tests, checkpoints, explain-back bank, final edge case.

The remix (step 4) makes the block project **survive bad input**: typos like `abc`, negative numbers, and so on. See [remix.md](remix.md). The same spec is used for both tracks.

| Competency | Planned gate items |
|---|---|
| c1 what exceptions are | q1 |
| c2 try/except | `test_rejects_text`, q2 |
| c3 re-prompt loop | q3 |
| c4 raise | `test_rejects_negative`, q4 |
| c5 specific vs bare except | q6 |

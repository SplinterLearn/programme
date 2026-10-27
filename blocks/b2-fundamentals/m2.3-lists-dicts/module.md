---
id: m2.3
block: b2
title: "Lists & dicts"
status: draft
weeks: [9, 9]
est_sessions: 3
licence_level: L0
competencies:
  - {id: m2.3.c1, text: "Can create a list, add to it, index it and loop over it"}
  - {id: m2.3.c2, text: "Can create a dictionary, look values up by key, and loop over its keys and values"}
  - {id: m2.3.c3, text: "Can represent a collection of records as a list of dictionaries"}
  - {id: m2.3.c4, text: "Can find, filter and order items in a collection with a loop"}
  - {id: m2.3.c5, text: "Can explain the difference between a list and a dict and choose the right one"}
resources:
  - title: "CS50P — Lecture 2: Loops (lists and dictionaries part)"
    url: https://cs50.harvard.edu/python/weeks/2/
    role: backbone
    notes: "Second part of the lecture: lists, dictionaries, lists of dictionaries. TODO(verify): whether sorted() with a key is shown by Lecture 2; if not, the remix orders items with loops."
    verified_on: 2026-10-27
  - title: "CS50P — Problem Set 2"
    url: https://cs50.harvard.edu/python/psets/2/
    role: backbone
    notes: "In M2.3: Vanity Plates and Nutrition Facts (ADR 0003). Duck only."
    verified_on: 2026-10-27
  - title: "futurecoder.io"
    url: https://futurecoder.io/
    role: fallback
    notes: "Chapters on lists and dictionaries (titles from futurecoder's source repo; TODO(verify): titles as shown on the live site)."
    verified_on: 2026-10-27
sessions:
  - {n: 1, type: lecture, title: "Lecture 2, lists and dictionaries part, with predict checkpoints", where: "CS50P (video) + bot", ai: bot-predict}
  - {n: 2, type: pset, title: "Problem Set 2: Vanity Plates, Nutrition Facts", where: cs50.dev, ai: duck}
  - {n: 3, type: remix, title: "Remix step 3 → PR → review → explain-back → merge", where: "student repo + bot", ai: bot-L0}
cs50_fingerprints:
  - problem: "Vanity Plates"
    pset: 2
    filename: plates.py
    required_functions: [is_valid, main]
    distinctive_strings: ["Valid", "Invalid"]
    summary: "Checks whether a proposed licence plate text follows a set of rules, with an is_valid function."
  - problem: "Nutrition Facts"
    pset: 2
    filename: nutrition.py
    required_functions: []
    distinctive_strings: ["Calories"]
    summary: "Looks up the calories of a fruit the user names, using a dictionary of fruits."
checks: []
explain_back: true
remix:
  project_id: b2-planner
  step: 3
  tracks: [finance, fandom]
  brief_only_tracks: []
  rubric: remix-default
  edge_case:
    summary: "TODO(next-task): candidate: an empty list, or two items with the same priority"
    per_track:
      finance: "TODO(next-task)"
      fandom: "TODO(next-task)"
    covered_by: ["eb:m2.3.q5"]
coverage:
  m2.3.c1: ["test:test_add_item", "eb:m2.3.q1"]
  m2.3.c2: ["eb:m2.3.q2"]
  m2.3.c3: ["test:test_total", "eb:m2.3.q3"]
  m2.3.c4: ["test:test_order", "eb:m2.3.q4"]
  m2.3.c5: ["eb:m2.3.q6"]
skip_gate: {time_box_minutes: 60, ai: "off"}
student_files:
  - {from: "tracks/{track}/tests/test_m2_3.py", to: "{project_dir}/tests/test_m2_3.py"}
---
# M2.3 Lists & dicts (draft)

*Block 2 · L0 · week 9 · CS50P Lecture 2 (lists and dictionaries), Problem Set 2 (last two problems)*

**Draft.** TODO(next-task): tests, checkpoints, explain-back bank, final edge case.

The remix (step 3) turns one goal or one series into a **collection**: several savings goals sorted by priority, or the whole watchlist sorted by priority or rating. See [remix.md](remix.md).

| Competency | Planned gate items |
|---|---|
| c1 lists | `test_add_item`, q1 |
| c2 dicts | q2 |
| c3 list of dicts | `test_total`, q3 |
| c4 find, filter, order | `test_order`, q4 |
| c5 list vs dict | q6 |

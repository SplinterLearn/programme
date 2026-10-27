---
id: m2.5
block: b2
title: "Libraries & a first API"
status: draft
weeks: [11, 11]
est_sessions: 4
licence_level: L0
competencies:
  - {id: m2.5.c1, text: "Can import a module from the standard library and use its functions (e.g. random, sys)"}
  - {id: m2.5.c2, text: "Can install a third-party package with pip and use it"}
  - {id: m2.5.c3, text: "Can call a web API with requests and read values out of the JSON it returns"}
  - {id: m2.5.c4, text: "Can explain what if __name__ == \"__main__\" does and why tests need it"}
  - {id: m2.5.c5, text: "Can handle an API failure (no connection, rate limit, missing field) without crashing"}
resources:
  - title: "CS50P — Lecture 4: Libraries"
    url: https://cs50.harvard.edu/python/weeks/4/
    role: backbone
    notes: "Ends with calling a web API and reading JSON."
    verified_on: 2026-10-27
  - title: "CS50P — Problem Set 4"
    url: https://cs50.harvard.edu/python/psets/4/
    role: backbone
    notes: "Emojize, Frank Ian and Glen's Letters, Adieu Adieu, Guessing Game, Little Professor, Bitcoin Price Index. Duck only."
    verified_on: 2026-10-27
  - title: "Jikan API v4 (unofficial MyAnimeList API) — docs"
    url: https://docs.api.jikan.moe/
    role: extra
    notes: "Fandom remix. Base URL https://api.jikan.moe/v4; /anime/{id} returns data.episodes. No API key or auth in its OpenAPI spec. Rate limits: 3 requests/second, 60/minute, no daily limit (the API docs also warn MyAnimeList itself may rate-limit). TODO(verify): a live call to api.jikan.moe timed out from the build server on 2026-10-27; confirm it works before this module goes ready, and keep a fallback (cached JSON file)."
    verified_on: 2026-10-27
  - title: "Frankfurter — free exchange-rate API"
    url: https://frankfurter.dev/
    role: extra
    notes: "Finance remix. Public API at api.frankfurter.dev, no API key needed (stated on the site); a live call worked on 2026-10-27."
    verified_on: 2026-10-27
sessions:
  - {n: 1, type: lecture, title: "Lecture 4 with predict checkpoints", where: "CS50P (video) + bot", ai: bot-predict}
  - {n: 2, type: pset, title: "Problem Set 4, first half", where: cs50.dev, ai: duck}
  - {n: 3, type: pset, title: "Problem Set 4, second half (incl. the API problem)", where: cs50.dev, ai: duck}
  - {n: 4, type: remix, title: "Remix step 5 → PR → review → explain-back → merge; block exit", where: "student repo + bot", ai: bot-L0}
cs50_fingerprints:
  - problem: "Emojize"
    pset: 4
    filename: emojize.py
    required_functions: []
    distinctive_strings: [":thumbs_up:"]
    summary: "Turns emoji codes in text into real emoji using a third-party library."
  - problem: "Frank, Ian and Glen's Letters"
    pset: 4
    filename: figlet.py
    required_functions: []
    distinctive_strings: ["pyfiglet", "Invalid usage"]
    summary: "Prints text as large ASCII-art letters in a chosen or random font, using command-line arguments."
  - problem: "Adieu, Adieu"
    pset: 4
    filename: adieu.py
    required_functions: []
    distinctive_strings: ["Adieu, adieu, to", "inflect"]
    summary: "Collects names until end of input and bids them farewell as a grammatically joined list."
  - problem: "Guessing Game"
    pset: 4
    filename: game.py
    required_functions: []
    distinctive_strings: ["Too small!", "Too large!", "Just right!"]
    summary: "Picks a random number up to a level the user chooses and gives higher/lower feedback on guesses."
  - problem: "Little Professor"
    pset: 4
    filename: professor.py
    required_functions: [get_level, generate_integer, main]
    distinctive_strings: ["EEE"]
    summary: "Quizzes the user on ten random addition problems at a chosen difficulty and reports a score."
  - problem: "Bitcoin Price Index"
    pset: 4
    filename: bitcoin.py
    required_functions: []
    distinctive_strings: ["coincap", "Missing command-line argument"]
    summary: "Looks up a current cryptocurrency price from a web API and prints the cost of a given amount."
checks: []
explain_back: true
remix:
  project_id: b2-planner
  step: 5
  tracks: [finance, fandom]
  brief_only_tracks: []
  rubric: remix-default
  edge_case:
    summary: "TODO(next-task): candidate: the API is unreachable or rate-limits you, or a field is missing (e.g. episodes is null for a show still airing)"
    per_track:
      finance: "TODO(next-task)"
      fandom: "TODO(next-task)"
    covered_by: ["eb:m2.5.q5"]
coverage:
  m2.5.c1: ["eb:m2.5.q1"]
  m2.5.c2: ["eb:m2.5.q2"]
  m2.5.c3: ["test:test_reads_json", "eb:m2.5.q3"]
  m2.5.c4: ["eb:m2.5.q4"]
  m2.5.c5: ["test:test_handles_failure", "eb:m2.5.q5"]
skip_gate: {time_box_minutes: 60, ai: "off"}
student_files:
  - {from: "tracks/{track}/tests/test_m2_5.py", to: "{project_dir}/tests/test_m2_5.py"}
---
# M2.5 Libraries & a first API (draft)

*Block 2 · L0 · week 11 · CS50P Lecture 4, Problem Set 4 · closes Block 2*

**Draft.** TODO(next-task): tests (with the network mocked, so CI never calls the real API), checkpoints, explain-back bank, final edge case. The student template may need a `requirements.txt` with `requests`; if so, note the template change.

The remix (step 5) pulls **real data** into the block project: a live exchange rate (finance) or real episode counts (fandom). This is also where the `if __name__ == "__main__":` line from the M2.1 starter gets explained ([ADR 0017](../../../docs/decisions/0017-starter-files-and-pytest-imports.md)).

Be a good API citizen: Jikan allows about 3 requests a second and 60 a minute. Don't call it in a tight loop, and cache what you fetch.

| Competency | Planned gate items |
|---|---|
| c1 standard library | q1 |
| c2 pip packages | q2 |
| c3 requests + JSON | `test_reads_json`, q3 |
| c4 `__name__` guard | q4 |
| c5 API failures | `test_handles_failure`, q5 |

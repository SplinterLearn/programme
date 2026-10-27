---
id: m1.2
block: b1
title: "Terminal basics"
status: ready
weeks: [3, 3]
est_sessions: 3
licence_level: L0
competencies:
  - {id: m1.2.c1, text: "Can connect to a remote machine with ssh (host, port, user) and explain what ssh does"}
  - {id: m1.2.c2, text: "Can read files, including awkward names (spaces, leading dashes), with cat and check what kind of file it is with file"}
  - {id: m1.2.c3, text: "Can find files by name, type or size with find, and spot hidden files"}
  - {id: m1.2.c4, text: "Can search inside files with grep and send one command's output into another with a pipe (|) or into a file (>, >>)"}
  - {id: m1.2.c5, text: "Can use man or --help to learn a command they haven't seen before"}
  - {id: m1.2.c6, text: "Keeps secrets out of repos: never commits passwords, and knows why"}
resources:
  - title: "OverTheWire — Bandit"
    url: https://overthewire.org/wargames/bandit/
    role: backbone
    notes: "Free terminal game: each level needs a new command. Do levels 0 to about 10; later levels are optional bonus. Log in with ssh to bandit.labs.overthewire.org on port 2220 (the level 0 page has the details). ssh is built into macOS, Linux, Windows 10+ and the cs50.dev terminal. The 'Commands you may need' lists for these levels cover ssh, ls, cd, cat, file, du, find, then grep, sort, uniq, strings and base64. OverTheWire's rules ask players not to publish credentials or spoil the game."
    verified_on: 2026-10-27
  - title: "The Odin Project — Command Line Basics"
    url: https://www.theodinproject.com/lessons/foundations-command-line-basics
    role: fallback
    notes: "Go back to it when a Bandit level needs a basic you've forgotten."
    verified_on: 2026-10-27
  - title: "MIT The Missing Semester — The Shell (2026)"
    url: https://missing.csail.mit.edu/2026/course-shell/
    role: extra
    notes: "Pipes, redirection and more, for students who are flying."
    verified_on: 2026-10-27
sessions:
  - n: 1
    type: practice
    title: "Bandit levels 0 to about 5: ssh in, cat, awkward file names, ls -a, file. Start notes/bandit.md"
    where: "cs50.dev terminal + overthewire.org + bot"
    ai: bot-L0
    notes: "The bot may explain commands with its own examples and ask questions. It never gives level passwords or the exact command for a level."
  - n: 2
    type: practice
    title: "Bandit levels about 5 to 10: find, grep, pipes; use man to learn new commands"
    where: "cs50.dev terminal + overthewire.org + bot"
    ai: bot-L0
  - n: 3
    type: practice
    title: "Terminal scavenger hunt (b1-hunt/), terminal only, then commit, PR and explain-back"
    where: "student repo in cs50.dev + bot"
    ai: bot-L0
    notes: "AI-off is the spirit: the bot can explain a command, but not tell you which command solves a hunt task."
cs50_fingerprints: []
checks:
  - {id: m1.2.k1, text: "notes/bandit.md is committed with an entry per level done (the command learned and how the level was solved) and contains no passwords", verified_by: bot}
explain_back: true
remix: null
coverage:
  m1.2.c1: ["eb:m1.2.q1", "check:m1.2.k1"]
  m1.2.c2: ["test:test_map_moved", "eb:m1.2.q2"]
  m1.2.c3: ["test:test_hidden_file_found", "test:test_txt_count", "eb:m1.2.q3"]
  m1.2.c4: ["test:test_treasure_found", "test:test_food_list", "eb:m1.2.q4", "eb:m1.2.q8"]
  m1.2.c5: ["eb:m1.2.q5"]
  m1.2.c6: ["check:m1.2.k1", "eb:m1.2.q6", "eb:m1.2.q7"]
skip_gate: {time_box_minutes: 30, ai: "off"}
student_files:
  - {from: "hunt/", to: "b1-hunt/"}
---
# M1.2 Terminal basics

Learn the terminal by playing a game, then prove it in the hunt.

## Bandit (sessions 1–2)
[OverTheWire Bandit](https://overthewire.org/wargames/bandit/) is a free game played over `ssh`: you log in to a remote Linux machine, and each level's password is hidden somewhere you can only reach with a new command. Aim for **levels 0 to about 10**. Later levels are bonus material, any time this year.

- **Keep `notes/bandit.md` in your repo**: for each level, the command(s) you learned and how you solved it in one or two lines.
- **Never write the level passwords in your notes or anywhere in your repo.** Your repo is like a public notice board: anything committed stays in its history, even after you delete it. That's your first lesson in **secrets**, and it matters a lot more when they're real API keys (Block 6). OverTheWire also asks players not to publish credentials.
- Stuck on a level? Read the level page's "Commands you may need", then `man <command>`. Then ask the bot to explain a command, not to solve the level.

## The hunt (session 3)
When this module starts, `b1-hunt/` is copied into your repo ([instructions](hunt/README.md)). Do it with **terminal commands only**. Run `pytest b1-hunt` to check yourself. When it's all green, commit it, push a branch and open a PR. The commands are in your repo README. That PR is the **B1 exit artefact**.

## Coverage
| Competency | Checked by |
|---|---|
| c1 ssh | q1, k1 (Bandit notes) |
| c2 cat, file, awkward names | hunt `test_map_moved`, q2 |
| c3 find, hidden files | hunt `test_hidden_file_found`, `test_txt_count`, q3 |
| c4 grep, pipes, redirection | hunt `test_treasure_found`, `test_food_list`, q4, micro-task q8 |
| c5 man, --help | q5 |
| c6 Secrets | k1 (no passwords in notes), q6, q7 |

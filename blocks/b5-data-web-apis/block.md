---
id: b5
title: "Data, web & APIs"
weeks: [18, 23]
licence_level: L2
licence_unlock_on_exit: L3
goals:
  - Read and write files and CSV data
  - Understand HTTP and JSON, and how a request reaches a server and comes back
  - Store data in SQLite with SQL
  - Build a small web app with HTML, CSS and a little JavaScript, and deploy it
modules:
  - {id: m5.1, title: "Files & CSV (CS50P L6)", status: stub}
  - {id: m5.2, title: "HTTP, JSON & APIs (how a request reaches a server)", status: stub}
  - {id: m5.3, title: "SQL & SQLite", status: stub}
  - {id: m5.4, title: "HTML/CSS/JS basics", status: stub}
  - {id: m5.5, title: "A small web app", status: stub}
  - {id: m5.6, title: "Deployment & how hosting works", status: stub}
exit: "A deployed app that calls an API and stores data"
status: stub
project: null
skip_test: null
---
# B5 Data, web & APIs

**Weeks 18–23 · licence L2, then L3 on exit · stub**

## Goals
Files, HTTP, SQL, the web and deployment: everything needed to put a real app online. Track content grows to about half the time from here ([ADR 0010](../../docs/decisions/0010-staged-personalisation.md)).

## Chosen resources ([ADR 0019](../../docs/decisions/0019-b5-resources.md), verified 2026-10-27)
| Module | Backbone | Alternative |
|---|---|---|
| M5.1 Files & CSV | CS50P Lecture 6, https://cs50.harvard.edu/python/weeks/6/ | — |
| M5.2 HTTP, JSON & APIs | CS50P Lecture 4 recap + our own notes. TODO(next-task) | — |
| M5.3 SQL & SQLite | CS50x Week 7 (SQL), https://cs50.harvard.edu/x/weeks/7/ | — |
| M5.4 HTML/CSS/JS | CS50x Week 8, https://cs50.harvard.edu/x/weeks/8/ | The Odin Project Foundations (HTML Foundations, CSS Foundations, Flexbox, JavaScript Basics), https://www.theodinproject.com/paths/foundations/courses/foundations |
| M5.5 A small web app | CS50x Week 9 (Flask), https://cs50.harvard.edu/x/weeks/9/ | — |
| M5.6 Deployment | TODO(next-task): pick a free host with an age-appropriate sign-up; TODO(verify) its terms | — |

CS50x problem sets follow CS50's rules too: **only the CS50 Duck** helps on them ([ADR 0005](../../docs/decisions/0005-cs50-boundary-duck-mode.md)).

## Exit
A **deployed app that calls an API and stores data**, usually your block project grown up. Support fades: **you draft the spec**, and the bot reviews it. Passing unlocks **L3 Supervisor**, after a parent or mentor approves it.

## Licence
L2 (Pair): the bot may write snippets of up to 10 lines, each followed by "explain this back".

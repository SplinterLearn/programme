# Roadmap

About **36 weeks + 4 buffer weeks** at **5–7 hours a week**, typically 3 sessions of about 1.5 h ([ADR 0011](docs/decisions/0011-pace-and-goal.md)). Weeks are guidance, not deadlines. The goal is a **confident builder**, not "job-ready".

## Blocks

| Block | Weeks | Modules | Licence in block | Exit artefact | Status |
|---|---|---|---|---|---|
| [B0 Onboarding](blocks/b0-onboarding/block.md) | 1 | M0.1 Goals interview & track choice · M0.2 Setup & ground rules | L0 | `about-me.md` + agreed ground rules | ready |
| [B1 The machine & the terminal](blocks/b1-terminal/block.md) | 2–4 | M1.1 Files, folders & paths · M1.2 Terminal basics · M1.3 Dev environment | L0 | terminal scavenger hunt (checked by a script) | ready |
| [B2 Programming fundamentals](blocks/b2-fundamentals/block.md) | 5–11 | M2.1 Variables, types & conditionals · M2.2 Loops · M2.3 Lists & dicts · M2.4 Exceptions · M2.5 Libraries & a first API | L0 → **L1** on exit | block project v1 (growing remix) | M2.1 ready, M2.2–M2.5 draft |
| [B3 Git & GitHub collaboration](blocks/b3-git-collaboration/block.md) | 12–14 | M3.1 Branches & PRs · M3.2 Issues & code review · M3.3 Merge conflicts & READMEs | L1 | a PR merged into someone else's repo | stub (skip test ready) |
| [B4 Reading, debugging, testing](blocks/b4-read-debug-test/block.md) | 15–17 | M4.1 Reading unfamiliar code · M4.2 Debugging (debugger, AI-off) · M4.3 Testing & TDD with pytest (CS50P L5) · M4.4 How languages run code | L1 → **L2** on exit | student-written tests for the block project + 5 seeded bugs fixed AI-off | stub |
| [B5 Data, web & APIs](blocks/b5-data-web-apis/block.md) | 18–23 | M5.1 Files & CSV (CS50P L6) · M5.2 HTTP, JSON & APIs · M5.3 SQL & SQLite · M5.4 HTML/CSS/JS basics · M5.5 A small web app · M5.6 Deployment & hosting | L2 → **L3** on exit | deployed app that calls an API and stores data | stub |
| [B6 AI-assisted software engineering](blocks/b6-ai-assisted-engineering/block.md) | 24–26 | M6.1 Specs & acceptance criteria · M6.2 Context engineering · M6.3 Supervising a coding agent & reviewing diffs · M6.4 Security & secrets | L3 | a feature built by an agent from the student's spec, with a review log and tests | stub |
| [B7 Personal track](blocks/b7-track/block.md) | 27–32 | per track ([tracks/](tracks/)) | L3 | track project | stub |
| [B8 Capstone](blocks/b8-capstone/block.md) | 33–36 | team project (2–4 students where possible) | L3 | public repo + live demo + 5-minute video + oral defence | stub |
| Buffer | 37–40 | holidays, exams, catch-up | — | — | — |

### Modules and weeks (ready and drafted)

| Module | Weeks | Sessions | Backbone | Status |
|---|---|---|---|---|
| M0.1 Goals interview & track choice | 1 | 1 | the tutor bot's interview | ready |
| M0.2 Setup & ground rules | 1 | 2 | setup checklist | ready |
| M1.1 Files, folders & paths | 2 | 3 | The Odin Project: Command Line Basics | ready |
| M1.2 Terminal basics | 3 | 3 | OverTheWire Bandit + the hunt | ready |
| M1.3 Dev environment | 4 | 3 | cs50.dev / VS Code, first PR | ready |
| M2.1 Variables, types & conditionals | 5–6 | 6 | CS50P lectures 0–1, problem sets 0–1 | ready |
| M2.2 Loops | 7–8 | 4 | CS50P lecture 2, problem set 2 (part) | draft |
| M2.3 Lists & dicts | 9 | 3 | CS50P lecture 2, problem set 2 (part) | draft |
| M2.4 Exceptions | 10 | 3 | CS50P lecture 3, problem set 3 | draft |
| M2.5 Libraries & a first API | 11 | 4 | CS50P lecture 4, problem set 4 | draft |

## AI licence ladder

The tutor's help is earned ([ADR 0004](docs/decisions/0004-ai-licence-ladder.md); machine-readable in [`tutor/licence-levels.yaml`](tutor/licence-levels.yaml)). **A parent or mentor approves each upgrade**; the bot only proposes it.

| Level | Unlocked by | The tutor may | The tutor must not |
|---|---|---|---|
| **L0 Tutor** | start | explain concepts with generic examples; ask leading questions; point to the line with the error | write or fix code for the student's task; give more than one step at a time |
| **L1 Explainer** | Block 2 exit | explain the student's own code line by line; say what kind of bug it is | write new code for the student's task |
| **L2 Pair** | Block 4 exit | write small snippets (≤ 10 lines), each followed by "explain this back" | write whole functions or files |
| **L3 Supervisor** | Block 5 exit | review specs and agent-generated diffs; coach prompting a coding agent | — (the explain-back gate stays) |

At every level: **on CS50 problem sets only the CS50 Duck helps** ([ADR 0005](docs/decisions/0005-cs50-boundary-duck-mode.md)), and every module still ends with an explain-back that includes an AI-off fix-it task.

## Personalisation: 70/30 over the year, staged

([ADR 0010](docs/decisions/0010-staged-personalisation.md))

- **Months 1–4 (B0–B4):** almost all common core. Personalisation is the **remix theme** (your track) and your project choices.
- **From month 5 (B5 onward):** dedicated track content grows to about **half** the time: track-flavoured projects in B5–B6, then the whole of B7.
- Over the year that comes to about 70% common and 30% personal.

## Tracks

| Track | About | Status |
|---|---|---|
| [`fandom`](tracks/fandom.md) | anime/fandom data and community tools: watchlists, character databases, fan-site APIs, simple analytics | ready-for-pilot |
| [`biology`](tracks/biology.md) | biology and science data, bioinformatics problems in Python | ready-for-pilot |
| [`finance`](tracks/finance.md) | personal finance and data: budgets, savings, market data, charts | draft |
| [`web-social`](tracks/web-social.md) | web, social-media APIs, analytics, creator tools | draft |
| [`games`](tracks/games.md) | Pygame or Godot, game loops, state machines | draft |
| [`ai-ml`](tracks/ai-ml.md) | calling LLM APIs, prompts as code, simple retrieval, evaluating output | draft |
| [`hardware`](tracks/hardware.md) | Raspberry Pi or micro:bit, sensors, dashboards | draft |
| [`automation`](tracks/automation.md) | scripts, CLIs, bots | draft |

The M2.1 remix has tested variants for **finance** and **fandom**, and brief-only variants for **web-social** and **games**. Other tracks use the closest variant until theirs is written.

## CS50P across the blocks

CS50P is the default backbone for Python fundamentals ([ADR 0002](docs/decisions/0002-competency-defined-modules.md)), spread across blocks rather than packed into one ([ADR 0003](docs/decisions/0003-cs50p-spread-across-blocks.md)):

| CS50P lecture | Goes into |
|---|---|
| 0 Functions, Variables · 1 Conditionals | M2.1 |
| 2 Loops (incl. lists, dicts) | M2.2, M2.3 |
| 3 Exceptions | M2.4 |
| 4 Libraries (ends with a web API + JSON) | M2.5 |
| 5 Unit Tests | Block 4 (M4.3) |
| 6 File I/O | Block 5 (M5.1) |
| 7 Regular Expressions | track (data, automation, biology) |
| 8 OOP | Block 5 or track (essential for games) |
| 9 Et Cetera | optional |
| Final project | may double as the track project, for students who want the CS50P certificate |

To earn the CS50P certificate, a student must complete every problem set and the final project under CS50's own rules. That's optional here.

## Switch signals

Resources are interchangeable; competencies are not. Switch when you see these signals ([ADR 0002](docs/decisions/0002-competency-defined-modules.md)):

| Signal | Action |
|---|---|
| Stuck on one problem set for **more than 3 sessions**, even with the Duck | drop to **futurecoder** for that topic, then return |
| **Skipping or skimming** lectures | move the backbone to something more interactive (futurecoder, freeCodeCamp) |
| Passes `check50` but **fails the explain-back** | slow down: add predict-first exercises before each problem |
| **Bored** or finishing too easily | take the **skip test** |

The bot's stuck detection (3+ sessions on a module with no PR, or 5+ hearts on one error) suggests the module's `fallback` resource and flags it to the mentor.

## Skip tests

**A skip test is the exit gate taken without the lessons** ([ADR 0008](docs/decisions/0008-skip-test-is-exit-gate.md)):

- **Module:** the same remix in your track, **AI-off, 60 minutes**, then the same explain-back with the AI-off micro-task. Pass = tests green, rubric ≥ 5/8, explain-back ≥ 70% with the micro-task correct.
- **Block:** every module's exit gate, with explain-back questions sampled from each module.
- **B0:** no skip test (onboarding is for everyone).
- **B1:** the terminal hunt in **30 minutes**, plus explain-back.
- **B3:** a task-based skip test (branch, PR with the template, reply to review, resolve a staged merge conflict) that's ready before B3's modules are written, so students who know git can test out early.

Passing a skip test closes the module (or block) exactly like the normal path, but licence upgrades still need a parent or mentor's approval.

## What comes next

See the open items at the end of each `block.md`, and `TODO(next-task)` markers in draft modules.

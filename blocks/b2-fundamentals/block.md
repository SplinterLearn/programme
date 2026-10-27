---
id: b2
title: Programming fundamentals
weeks: [5, 11]
licence_level: L0
licence_unlock_on_exit: L1
goals:
  - Write small Python programs that store values, make decisions, repeat work and return results
  - Organise data in lists and dictionaries, and survive bad input with exceptions
  - Use a library and call a real web API that returns JSON
  - Build one growing project of your own, module by module, with tests that keep passing
modules:
  - {id: m2.1, title: "Variables, types & conditionals", status: ready}
  - {id: m2.2, title: "Loops", status: draft}
  - {id: m2.3, title: "Lists & dicts", status: draft}
  - {id: m2.4, title: "Exceptions", status: draft}
  - {id: m2.5, title: "Libraries & a first API", status: draft}
exit: "Block project v1: the growing remix (e.g. b2-savings/ or b2-watchlist/) with every module's tests green, each module closed with a passed explain-back"
status: draft
project:
  id: b2-planner
  title: "Planner: how long until… (savings planner, watchlist planner, …)"
  folders:
    finance: b2-savings
    fandom: b2-watchlist
    web-social: b2-posts
    games: b2-adventure
  default_folder: b2-project
skip_test: skip-test.md
---
# B2 Programming fundamentals

**Weeks 5–11 · licence L0, then L1 on exit · 5 modules · backbone: CS50P lectures 0–4**

## Goals
Learn Python fundamentals with CS50P as the textbook ([ADR 0003](../../docs/decisions/0003-cs50p-spread-across-blocks.md)), and use each new skill straight away in **your own growing project**, themed to your track ([ADR 0009](../../docs/decisions/0009-growing-remix-per-block.md)):

| Module | CS50P | Finance: *Savings planner* | Fandom: *Watchlist planner* |
|---|---|---|---|
| M2.1 Variables, types & conditionals | L0–1 | weeks to the goal + a verdict | days to finish a series + a verdict |
| M2.2 Loops | L2 | week-by-week savings table | day-by-day watch schedule |
| M2.3 Lists & dicts | L2 | several goals, sorted by priority | the whole watchlist, sorted by priority or rating |
| M2.4 Exceptions | L3 | survives typos like "abc" and negative numbers | same |
| M2.5 Libraries & a first API | L4 | a live exchange rate from an API | real episode counts from a public anime API |

## Why it matters
This is where you go from "I can follow along" to "I can make the computer do what I want". The growing project means you change your own code from weeks ago, which is the most realistic skill there is, especially once AI writes code too.

## How each module runs
Lectures with predict checkpoints from the bot → CS50 problem sets (**only the CS50 Duck helps**: the bot switches to Duck mode) → **remix** in your repo → PR (tests run) → review → explain-back → merge.

## Exit
Your block project with **every module's tests green**, every module closed through a PR with a passed explain-back. Passing the block exit unlocks **L1 Explainer**, after a parent or mentor approves it.

## Licence
L0 (Tutor) during the block: hints and questions, never code for your task. On exit: **L1**, where the bot can explain *your* code line by line.

## Skip test
Know Python basics already? See the [skip test](skip-test.md): each module's remix AI-off in 60 minutes, plus explain-back.

## Open items
- M2.2–M2.5 are drafts: their tests and checkpoints are TODO(next-task).
- Tested remix variants exist for finance and fandom; web-social and games are brief-only; other tracks use the closest variant.

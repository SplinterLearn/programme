# 0003. CS50P is spread across blocks

**Status:** Accepted

## Context
CS50P is ten lectures. Taken in one go, it would be 3–4 months of Python before the student sees git collaboration, testing in context or the web. Some lectures fit better next to related skills.

## Decision

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
| Final project | may double as the track project (for students who want the CS50P certificate) |

Problem Set 2 is split between M2.2 (loop-focused problems) and M2.3 (list/dict-focused problems).

## Consequences
- Fingerprints for each problem set live in the module that uses it, so the bot's CS50 detection follows the student's position.
- Students who want the certificate must finish all problem sets plus the final project. The ROADMAP says so.

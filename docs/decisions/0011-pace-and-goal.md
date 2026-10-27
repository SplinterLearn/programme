# 0011. Pace and goal

**Status:** Accepted

## Context
Boot.dev's adult backend path is about 12 months. A teen at 5–7 hours a week has roughly 200–250 hours in total ([research report](../design/research-report.md), Q2).

## Decision
- About **5–7 hours a week**, typically **3 sessions of about 1.5 h**.
- **36 weeks plus 4 buffer weeks** (holidays, exams, catch-up).
- The goal is **"confident builder"**, not "job-ready". We never promise employability.

## Consequences
- `est_sessions` in each module assumes 1.5 h sessions. Block `weeks` are guidance, not deadlines.
- A module that doesn't fit is split, not crammed.

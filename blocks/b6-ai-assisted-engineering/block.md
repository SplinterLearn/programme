---
id: b6
title: "AI-assisted software engineering"
weeks: [24, 26]
licence_level: L3
licence_unlock_on_exit: null
goals:
  - Write specs and acceptance criteria a coding agent can implement
  - Give an agent the right context (AGENTS.md, rules files) and supervise its work
  - Review agent-written diffs critically, verify them with tests, and keep secrets safe
modules:
  - {id: m6.1, title: "Specs & acceptance criteria (spec-driven development)", status: stub}
  - {id: m6.2, title: "Context engineering (AGENTS.md, rules files)", status: stub}
  - {id: m6.3, title: "Supervising a coding agent & reviewing diffs", status: stub}
  - {id: m6.4, title: "Security & secrets", status: stub}
exit: "A feature built by a coding agent from the student's spec, with a review log and tests"
status: stub
project: null
skip_test: null
---
# B6 AI-assisted software engineering

**Weeks 24–26 · licence L3 · stub**

## Goals
The modern developer workflow: **specify → let an agent implement → test → review → explain**. Almost no mainstream course teaches this as core skills yet ([research report](../../docs/design/research-report.md), Q3).

## Plan
- The remix changes again: **a coding agent writes the code, and you review the diff** ([ADR 0009](../../docs/decisions/0009-growing-remix-per-block.md)).
- Security & secrets: `.env`, never committing keys, API key hygiene, and basic threat awareness. The habit started with Bandit passwords in M1.2.
- The agent: TODO(verify) which coding agent is available to teens (age terms, e.g. GitHub Copilot for students needs 13+ and verified enrolment; availability changes).
- Each block keeps at least one AI-off session.

## Exit
A feature built by an agent from your spec, with a **review log** (what you checked, what you asked it to change) and tests.

## Licence
L3 (Supervisor). The explain-back gate stays.

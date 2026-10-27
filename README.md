# splinterlearn programme

A self-paced, 9-month **"zero to builder"** coding programme for teenagers, written as **curriculum as code**.

> **Status: pilot.** Blocks 0–1 and module M2.1 are ready. The rest of Block 2 is drafted. Blocks 3–8 are outlines, apart from the Block 3 skip test. Expect changes.

## Why

AI can write code, so learning to code is now less about typing syntax and more about **understanding, specifying, testing, reviewing and explaining** code, whoever wrote it. The research is clear that unrestricted AI makes practice look better while learning gets worse ([research report](docs/design/research-report.md)). This programme therefore puts **understanding over prompting**:

- AI help is **earned** in stages, from a Socratic tutor that never writes your code (L0) to supervising a coding agent (L3) ([ADR 0004](docs/decisions/0004-ai-licence-ladder.md)).
- Every module closes with an **explain-back**: if you can't explain it, it isn't done yet.
- The goal is a **confident builder** after about 9 months at 5–7 hours a week, not "job-ready".

## The three pieces

| Piece | Role | Where |
|---|---|---|
| **Platforms** | The textbooks: lectures, exercises and their auto-checkers (CS50P, The Odin Project, futurecoder, OverTheWire, …) | external, linked, never copied |
| **This repo** | The syllabus: roadmap, competencies, remix projects, tests, rubrics, explain-back banks, tutor prompts | here |
| **The tutor bot** | The tutor: a Telegram bot that coaches at the student's licence level, reviews PRs, runs explain-backs and sends the weekly digest. It reads this repo as its source of truth. | separate repo (`splinter-bot`) |

Each student works in their own private repo, generated from the **[student template](https://github.com/splinterlearn/student-template)** (a separate template repository).

## How a module flows

```
learn (external lessons, with predict checkpoints from the bot)
  → practise (problem sets; on CS50 problem sets only the CS50 Duck helps)
  → remix (a small project in your own repo, themed to your interest track)
  → PR (tests run automatically)
  → review (the bot comments on the PR against a rubric)
  → explain-back (5–7 questions + one AI-off fix-it task, in Telegram)
  → merge (progress moves, the next module unlocks)
```

The remix grows into one project per block, so by the end of Block 2 you have a small app of your own, not ten exercises ([ADR 0009](docs/decisions/0009-growing-remix-per-block.md)). Already know something? Take the **skip test**: the same exit gate, AI-off and time-boxed ([ADR 0008](docs/decisions/0008-skip-test-is-exit-gate.md)).

## Map of the repo

| Path | What |
|---|---|
| [`ROADMAP.md`](ROADMAP.md) | blocks → modules → weeks, tracks, licence ladder, skip tests, switch signals |
| [`blocks/`](blocks/) | one folder per block. Modules hold `module.md`, `remix.md`, `explain-back.yaml`, and per-track tests and checkpoints. |
| [`tracks/`](tracks/) | interest tracks (fandom, biology, finance, …) |
| [`tutor/`](tutor/) | the bot's prompts, licence levels, rubric, begging test cases |
| [`schema/`](schema/) | JSON Schemas for everything the bot reads (`schema/VERSION` is semver) |
| [`docs/content-format.md`](docs/content-format.md) | how to write blocks, modules, remixes and explain-back banks |
| [`docs/decisions/`](docs/decisions/) | architecture decision records |
| [`docs/design/`](docs/design/) | the research report and architecture (edited for publication) |
| [`scripts/`](scripts/) | `validate.py`, `check_checkpoints.py`, `stage_conflict.sh` |

## Contributing

Changing the curriculum means merging a PR here: the bot picks it up without a redeploy. Before opening a PR:

```bash
python -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/check_checkpoints.py
```

Read [`CLAUDE.md`](CLAUDE.md) (the conventions apply to humans too) and [`docs/content-format.md`](docs/content-format.md). The short version:

- **No personal data.** Write about *the student*, *the parent*, *the mentor*.
- **Link, don't copy** third-party course content.
- **Verify** external facts on the live site, or write `TODO(verify): …`.
- **Prompt changes** (`tutor/`) change the bot's behaviour immediately, so run the begging test (in the bot repo) before merging them.
- Record decisions as ADRs.

## Licences

- Curriculum content: [CC BY-NC-SA 4.0](LICENSE).
- Code (scripts, schemas, workflows, tests, starters, checkpoints): [MIT](LICENSE-CODE).

Linked third-party courses keep their own licences and terms. CS50 is © Harvard; we only link to it and respect its academic honesty rules.

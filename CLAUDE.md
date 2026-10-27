# CLAUDE.md: conventions for working in this repo

This is a **public** curriculum-as-code repo for a teen coding programme. A Telegram tutor bot (separate repo, `splinter-bot`) reads it as data: it validates content with `schema/` and the rules in `scripts/validate.py`, and serves only `status: ready` modules. The student template is a separate repo: [`splinterlearn/student-template`](https://github.com/splinterlearn/student-template), developed locally in `../student-template`.

## Hard rules

1. **No personal data, ever.** Use generic roles: *student*, *parent*, *mentor* (*admin* in bot terms), with "they" for the student. No names, ages of real people, locations, schools or family details, in content, examples, test data or commit messages.
2. **No copied third-party course content.** Link to CS50, The Odin Project, futurecoder, OverTheWire, etc.
   - CS50 fingerprint `summary` is **one line in our own words**, and `distinctive_strings` are short tokens.
   - Never paste problem statements, distribution code or solutions to CS50 problem sets.
3. **Everything the bot reads is structured and validated.** Frontmatter and YAML follow `schema/`. Markdown bodies are for humans.
4. **Every module has a competency-coverage table.** Each competency is checked by at least one exit-gate item, for every tested track.
5. **Accuracy over completeness.** Verify external facts on the live site and set `verified_on`. If you can't verify, write `TODO(verify): …`. Never guess URLs, filenames, function names or level numbers.
6. **Repo language is English.** Code, errors and technical terms stay in English even when the bot speaks another language.

## Before every commit

```bash
.venv/bin/python scripts/validate.py          # must report 0 errors
.venv/bin/python scripts/check_checkpoints.py # must report 0 failures
```

(First time: `python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt`.)

## Adding or changing a module: checklist

1. Copy the skeleton from [`docs/content-format.md`](docs/content-format.md#module-skeleton) into `blocks/<block>/<id>-<slug>/module.md`, and add the module to `block.md` `modules` (same status).
2. Write **4–7 can-do competencies** (`<id>.c<n>`).
3. **Resources:** competencies first, resources second (ADR 0002). Verify each URL live. Mark the backbone and a fallback.
4. **Sessions:** about 1.5 h each. `type: pset` ⇒ `ai: duck` (Duck mode). `est_sessions` = number of sessions.
5. **CS50 fingerprints** for every problem set the module uses. Verify filenames and required functions on the live CS50P pages.
6. **Remix** (`remix.md`): one `## Track: <id>` section per track. Small (2–3 functions, 30–60 lines). Logic separate from I/O. Exactly **one deliberate edge case left out of the tests** (`remix.edge_case`). It extends the block project.
7. **Per tested track:** `tracks/<t>/tests/test_m<b>_<n>.py` (test names shared across tracks), `checkpoint/` (written like a good student at this level, using only what has been taught so far), and `starter/` for the first step of a block project.
8. **Explain-back bank** (`explain-back.yaml`): several questions per competency, track variants for trace questions, 0/1/2 anchors, and **at least one AI-off micro-task** with buggy code and the expected fix.
9. **Coverage:** map every competency to gate items (`test:`, `eb:`, `rubric:`, `check:`), and repeat it as a table in the module body.
10. **`student_files`**: list what gets copied into the student repo at module start. Never checkpoints.
11. Run both scripts. Fix every error. Read the warnings.
12. If the module needs a student-template change, make it in `../student-template`, bump its `TEMPLATE_VERSION`, and note it in the PR or an ADR.

## Where things live

| Need | Place |
|---|---|
| Why something is the way it is | [`docs/decisions/`](docs/decisions/) (ADRs). Add one for every new decision. |
| Design background | [`docs/design/`](docs/design/) (sanitised copies; ADRs win on conflict) |
| Sources for verified external facts | [`docs/verified-facts.md`](docs/verified-facts.md) (snapshot from 2026-10-27) |
| Field-by-field format | [`docs/content-format.md`](docs/content-format.md) and [`schema/`](schema/) |
| Big picture | [`ROADMAP.md`](ROADMAP.md) |
| Bot prompts and placeholders | [`tutor/`](tutor/), documented in [`tutor/README.md`](tutor/README.md) |

## Other conventions

- **Changing a format** means changing the JSON Schema, then `schema/VERSION` (MAJOR/MINOR/PATCH rules in content-format.md), then `validate.py` if a cross-file rule changed, then `content-format.md`.
- **Prompts are content.** A change in `tutor/` changes the bot's behaviour without a deploy, so the begging test must be run (bot repo, manual workflow) before merging prompt changes.
- **Don't renumber published ids** (competencies, questions). The bot stores scores by id.
- **Drafts are safe on `main`.** The bot ignores `status: draft`. Use `TODO(next-task)` for planned work in drafts. It's an error in ready modules.
- Commit per logical change, with clear messages. Don't push unless asked.

# Content format

How blocks, modules, remixes, explain-back banks, skip tests, tracks and prompts are written. It's the human guide to [`schema/`](../schema/).

- **The bot reads this repo as data.** It validates every new commit with the JSON Schemas in `schema/` plus the structural rules below, and never executes code from here.
- If a rule can be a schema rule, it lives in the schema. Only cross-file rules live in [`scripts/validate.py`](../scripts/validate.py).
- Run both checks before every PR:

```bash
python -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py          # schemas + structure
.venv/bin/python scripts/check_checkpoints.py # checkpoints pass, starters fail, hunt solvable
```

Contents: [Layout](#layout) · [IDs](#ids) · [YAML rules](#yaml-rules) · [block.md](#blockmd) · [module.md](#modulemd) · [Coverage](#coverage-table) · [remix.md](#remixmd) · [Tests, starters, checkpoints](#tests-starters-and-checkpoints) · [explain-back.yaml](#explain-backyaml) · [skip-test.md](#skip-testmd) · [tracks](#tracks) · [tutor/](#tutor) · [Student repo conventions](#student-repo-conventions) · [Schema versioning](#schema-versioning) · [Validation rules](#validation-rules) · [Module skeleton](#module-skeleton)

---

## Layout

```
blocks/<block-id>-<slug>/
  block.md                       # frontmatter + human body
  skip-test.md                   # optional (block.skip_test)
  <module-id>-<slug>/            # one folder per non-stub module
    module.md                    # frontmatter (machine) + body (human)
    remix.md                     # if module.remix is set
    explain-back.yaml            # if module.explain_back is true
    tracks/<track>/              # one per remix.tracks entry
      starter/                   # first module of a block project only
      tests/test_<module>.py     # e.g. test_m2_1.py
      checkpoint/                # clean reference solution
    hunt/ , reference/solve.sh   # B1 only (terminal hunt)
tracks/<track-id>.md
tutor/  (prompts, licence-levels.yaml, rubrics/, test-cases/)
schema/ (JSON Schemas, VERSION)
```

Stub modules exist only as entries in `block.md`, with no folder.

## IDs

| Thing | Pattern | Example |
|---|---|---|
| block | `b<digit>` | `b2` |
| module | `m<block>.<n>` | `m2.1` |
| competency | `<module>.c<n>` | `m2.1.c3` |
| explain-back question | `<module>.q<n>` | `m2.1.q7` |
| module check | `<module>.k<n>` | `m0.2.k1` |
| skip test | `<block>-skip` | `b3-skip` |
| skip-test competency / question / task | `<block>.skip.c<n>` / `.q<n>` / `.t<n>` | `b3.skip.t2` |
| track | lowercase, hyphens | `web-social` |

Folders are `<id>-<slug>`: `b2-fundamentals/`, `m2.1-variables-types-conditionals/`.

**Never renumber a published id.** The bot stores scores by id. If you retire a question, delete it and leave its number unused.

## YAML rules

YAML is read with a strict, JSON-compatible loader:

- **Quote** `"off"`, `"on"`, `"yes"`, `"no"`. YAML 1.1 reads them as booleans, YAML 1.2 as strings. The validator rejects them unquoted. Write `ai: "off"`.
- **Quote numeric keys.** Scoring anchors are `"0"`, `"1"`, `"2"`.
- Dates stay strings (`verified_on: 2026-10-27` is fine).
- Use `|` for multi-line code blocks.

## block.md

```yaml
---
id: b2
title: Programming fundamentals
weeks: [5, 11]                    # inclusive programme weeks
licence_level: L0                 # licence in effect during the block
licence_unlock_on_exit: L1        # or null; must agree with tutor/licence-levels.yaml
goals:
  - Write small Python programs that read input, decide, repeat and return values
modules:                          # ordered
  - {id: m2.1, title: "Variables, types & conditionals", status: ready}
  - {id: m2.2, title: Loops, status: draft}
exit: Block project v1 (the growing remix) with all module tests green
status: draft                     # ready only if every module is ready
project:                          # the block's growing remix project, or null
  id: b2-planner
  title: Planner
  folders: {finance: b2-savings, fandom: b2-watchlist}
  default_folder: b2-project      # for tracks not listed in folders
skip_test: skip-test.md           # or null
---
# Body: goals, why it matters, exit, licence (human-readable)
```

## module.md

The frontmatter is what the bot uses. The body is for humans: an overview, how the sessions run, tips, and the coverage table rendered as Markdown.

| Field | Meaning |
|---|---|
| `id`, `block`, `title`, `status` | `status`: `ready` (served by the bot) or `draft` (ignored by the bot) |
| `weeks` | inclusive programme weeks, inside the block's weeks |
| `est_sessions` | number of ~1.5 h sessions; must equal `len(sessions)` |
| `licence_level` | must equal the block's |
| `competencies` | `{id, text}`: can-do statements ("can …") |
| `resources` | `{title, url, role, notes, verified_on?}`. `role`: `backbone` (default path), `fallback` (switch to when stuck), `extra`, `optional`. Put `TODO(verify): …` in `notes` for anything unverified. |
| `sessions` | `{n, type, title, where, ai, notes?}`. `type`: lecture, pset, remix, quiz, reading, practice, interview, setup. `ai`: bot-predict, bot-quiz, bot-interview, bot-L0…bot-L3, duck, off, mentor. **`type: pset` requires `ai: duck`**, which puts the bot in Duck mode. |
| `cs50_fingerprints` | `{problem, pset, filename, required_functions, distinctive_strings, summary}`. Verified against the live CS50P pages. `distinctive_strings` are short tokens (≤ 40 chars). `summary` is **one line in our own words**. Never paste CS50 text. |
| `checks` | `{id, text, verified_by: bot\|mentor\|ci}`: non-code gate items |
| `explain_back` | `true` means `explain-back.yaml` is required. `false` only when another artefact is the whole gate (M0.1). |
| `remix` | `null`, or `{project_id, step, tracks, brief_only_tracks, rubric, edge_case}` (see [remix.md](#remixmd)) |
| `coverage` | competency id → gate items (see [Coverage](#coverage-table)) |
| `skip_gate` | `{time_box_minutes: 60, ai: "off"}` (ADR 0008) |
| `student_files` | `{from, to}`: files copied into the student repo **when the module starts** |

### student_files

- Paths are relative to the module folder (`from`) and to the student repo root (`to`).
- `{track}` expands to the student's track. `{project_dir}` expands to the block project's folder for that track (`block.project.folders[track]`, or `default_folder`).
- A trailing `/` copies a folder's contents. Use it on both sides.
- Only tests, starters, instructions and provided data go here. **Never checkpoints**: those are offered only after the module is closed.

```yaml
student_files:
  - {from: "tracks/{track}/starter/", to: "{project_dir}/"}
  - {from: "tracks/{track}/tests/test_m2_1.py", to: "{project_dir}/tests/test_m2_1.py"}
```

## Coverage table

**Every competency must be checked by at least one gate item, for every tested track.**

| Reference | Points at |
|---|---|
| `test:<function>` | a pytest function in `tracks/<t>/tests/` (or the module's own `test_*.py` files if there's no remix) |
| `eb:<question id>` | a question in `explain-back.yaml`. It counts for a track only if the question's `tracks` is `all` or includes it, and the question must list the competency. |
| `rubric:<criterion>` | a criterion in the module's rubric (`remix.rubric`) |
| `check:<check id>` | an item in `checks` |
| `task:<task id>` | skip tests of `kind: tasks` only |

**Test function names are shared across tracks** (ADR 0015). If finance has `test_rounds_up`, fandom has a `test_rounds_up` too. Then one coverage line serves both.

In `module.md`'s body, repeat the coverage as a human table:

| Competency | Checked by |
|---|---|
| c1 Variables | `rubric:readability`, `eb:m2.1.q3` (trace) |

## remix.md

The remix is the module's *make* step: one session, in the student's repo, themed to their track ([architecture 5](design/architecture.md)).

**Design rules:**

1. **Small.** 2–3 functions, about 30–60 lines of new code. If it doesn't fit in one ~1.5–2 h session, it's too big.
2. **Logic separate from I/O.** Calculations live in functions the tests can check. `input()` and `print()` live only in `main()`.
3. **One edge case deliberately left out of the tests** (`remix.edge_case`). The review flags it and the explain-back asks about it. Lesson: passing tests isn't the same as being correct.
4. **It extends the block project** (`remix.step`, ADR 0009). Earlier tests must keep passing.
5. **Shared skeleton across tracks.** Same function shapes, different nouns.

Frontmatter: `{module, step}`. The body has one section per track, with the exact heading `## Track: <id>`, for every id in `remix.tracks` and `remix.brief_only_tracks`:

```markdown
## Track: finance
**Brief.** A few sentences of story.
**Spec.**
- `weeks_to_goal(price, saved, per_week) -> int` …
- `main()` …
**Stretch goal.** One optional extra.
```

Tested tracks (`remix.tracks`) have a full spec, tests, a starter if it's the first step, and a checkpoint. Brief-only tracks have a brief and a spec sketch, and their tests come later. A student on a brief-only track works from the spec and the review, but CI has no tests for them yet.

## Tests, starters and checkpoints

```
tracks/<track>/
  starter/      main file with stubs + `if __name__ == "__main__": main()` + empty conftest.py (first step only)
  tests/        test_<module>.py: pytest, plain asserts, no fixtures the student hasn't seen
  checkpoint/   clean reference: code a good student at this level would write
```

- Test files are named `test_m<b>_<n>.py`, so they're unique in the student repo.
- Tests import from the main module (`from savings import weeks_to_goal`). The project-root `conftest.py` from the starter makes that work (ADR 0017).
- Tests never call `input()`. They test functions, not `main()`.
- **Checkpoints use only what the module's resources have taught so far.**
- `check_checkpoints.py` stages each track like the student repo. The checkpoint must pass and the starter must fail.

## explain-back.yaml

```yaml
scope: m2.1
questions:
  - id: m2.1.q1
    type: predict             # predict | why | trace | change | edge | concept | micro-task
    competencies: [m2.1.c2]
    tracks: all               # or [finance]
    prompt: …
    good_answer_notes: …      # what a good answer contains (for the grader)
    scoring:
      "0": …
      "1": …
      "2": …
  - id: m2.1.q9
    type: micro-task
    ai_off: true
    competencies: [m2.1.c2, m2.1.c6]
    tracks: all
    language: python
    code: |
      …buggy code…
    prompt: …
    expected_fix: …
    good_answer_notes: …
    scoring: {"0": …, "1": …, "2": …}
```

- **At least one `micro-task` with `ai_off: true`** (a schema rule). The bot always includes one.
- The bot samples 5–7 questions so that all competencies are covered ([`tutor/explain-back-protocol.md`](../tutor/explain-back-protocol.md)). Write enough variety: several questions per competency where possible, and track-specific variants for trace questions.
- Write anchors that a grader can apply mechanically: "names X and Y" rather than "good understanding".

## skip-test.md

Two kinds:

- **`kind: module-gates`**: the block skip test is every module's exit gate, AI-off and time-boxed, with sampled explain-back questions (ADR 0008).
  ```yaml
  id: b2-skip
  block: b2
  status: ready
  kind: module-gates
  ai: "off"
  modules: [m2.1, m2.2, m2.3, m2.4, m2.5]   # all of the block's modules, in order
  time_box_minutes_per_module: 60
  explain_back: {sample_per_module: 2, micro_task_per_module: 1}
  ```
- **`kind: tasks`**: a standalone skip test with its own tasks, competencies, coverage and bank (`skip-test.explain-back.yaml`, scope `b3.skip`). It's used for B3, whose modules aren't written yet.

## Tracks

`tracks/<id>.md` frontmatter: `id`, `title`, `summary`, `example_projects`, `extra_resources` (`{title, url, notes?, verified_on?}`), `status` (`ready`, `ready-for-pilot` or `draft`). The body describes the track's direction per block.

## tutor/

See [`tutor/README.md`](../tutor/README.md). Prompts are Markdown with frontmatter (`schema/prompt.schema.json`) and `{{placeholders}}`. Every placeholder used must be declared in the prompt's frontmatter and documented in `tutor/README.md`. Prompts that produce JSON name their `output_schema` in `schema/llm-output/`.

## Student repo conventions

The student template is a separate repo ([splinterlearn/student-template](https://github.com/splinterlearn/student-template)). It holds only the skeleton. Everything else arrives from here when a module starts:

- **Block projects live in `b<N>-<project>/`** (e.g. `b2-savings/`), named by `block.project.folders`.
- **Each module's tests are copied in when the module starts and accumulate** (`b2-savings/tests/test_m2_1.py`, `test_m2_2.py`, …). Earlier tests must keep passing.
- **Module folders say what gets copied and where** (`student_files`).
- The B1 hunt arrives as `b1-hunt/`.
- One branch and one PR per module (`m2.1-remix`).
- CI (`.github/workflows/tests.yml` in the template) runs `pytest` over the whole repo on every push and PR.

If a module needs a template change, say so in the module's PR and its ADR. The template is kept in sync by hand, and `TEMPLATE_VERSION` is bumped.

## Schema versioning

`schema/VERSION` is a semver string. The bot refuses content whose **major** version it doesn't support ([architecture 3.8](design/architecture.md)).

| Bump | When | Examples |
|---|---|---|
| **MAJOR** | the bot could misread existing or new content | removing or renaming a field; a new **required** field; narrowing an enum; changing an id pattern; changing a field's meaning; moving files the bot reads |
| **MINOR** | old bots can ignore the change safely | a new optional field; a widened enum the bot can treat as "unknown"; a new file type the bot doesn't need |
| **PATCH** | no effect on data | descriptions, docs, typo fixes in schemas |

Bump `VERSION` in the same PR as the schema change. A major bump needs a bot release before it's merged.

## Validation rules

`validate.py` checks the following on top of the JSON Schemas:

1. All YAML parses with the strict loader. Keys are strings, and there are no unquoted yes/no/on/off.
2. Every file validates against its schema. Schemas themselves are valid, and their `$id`s match their paths.
3. Folder names match ids. `module.block` matches the parent block. A module's licence equals its block's. Module weeks lie inside block weeks. Blocks don't overlap.
4. `block.modules` matches the folders: non-stub entries have folders, stub entries don't, statuses agree, and the order is right. A `ready` block has only ready modules.
5. Competency, question, check and task ids are unique and prefixed with their owner's id. CS50 fingerprint filenames are unique across modules.
6. **Coverage:** keys equal the competency ids. For every tested track, each competency has at least one existing gate item that applies to that track. Every reference resolves: tests are parsed with `ast`, questions come from the bank, rubric criteria and checks from their files. An `eb:` item's question lists that competency.
7. **Remix:** every `remix.tracks` entry has `tests/test_*.py` and a `checkpoint/`. Tracks exist in `tracks/`. `remix.md` has exactly one `## Track: <id>` heading per listed track. `project_id` matches the block. `edge_case.per_track` covers the tested tracks.
8. Every `student_files.from` exists (expanded per tested track).
9. `explain_back: true` ⇔ `explain-back.yaml` exists. `remix: null` ⇒ no `remix.md`.
10. Skip tests: the id is `<block>-skip`; `module-gates` lists all of the block's modules in order; `tasks` coverage resolves; sample sizes fit the bank.
11. Licence ladder: each block's `licence_level` and `licence_unlock_on_exit` agree with `tutor/licence-levels.yaml`.
12. Prompts: placeholders are declared and documented, and `output_schema` exists. Rubric `pass_threshold` ≤ the maximum score.
13. `schema/VERSION` is semver. `ready` modules contain no `TODO(next-task)`.

**Ready vs draft.** For `ready` modules, missing references, tests or files are **errors**. For `draft` modules they're **draft gaps**: reported as one summary line per file (`--verbose` lists them), so drafts can sit on `main` while their tests are written later.

## Module skeleton

Copy this into `blocks/<block>/<module-id>-<slug>/module.md`, then add the module to `block.md`:

```markdown
---
id: mX.Y
block: bX
title: <Title>
status: draft
weeks: [W, W]
est_sessions: 3
licence_level: L0
competencies:
  - {id: mX.Y.c1, text: "<can-do statement>"}
  - {id: mX.Y.c2, text: "<can-do statement>"}
resources:
  - title: <Course — lesson>
    url: https://…
    role: backbone
    notes: "TODO(verify): URL and contents"
sessions:
  - {n: 1, type: lecture, title: "<…>", where: "<site> + bot", ai: bot-predict}
  - {n: 2, type: pset, title: "<CS50 problem set>", where: cs50.dev, ai: duck}
  - {n: 3, type: remix, title: "Remix → PR → review → explain-back", where: "student repo + bot", ai: bot-L0}
cs50_fingerprints: []
checks: []
explain_back: true
remix:
  project_id: bX-<project>
  step: N
  tracks: [finance, fandom]
  brief_only_tracks: []
  rubric: remix-default
  edge_case:
    summary: "<the case deliberately left out of the tests>"
    per_track: {finance: "<…>", fandom: "<…>"}
    covered_by: ["eb:mX.Y.q5"]
coverage:
  mX.Y.c1: ["test:test_<name>", "eb:mX.Y.q1"]
  mX.Y.c2: ["eb:mX.Y.q2", "rubric:readability"]
skip_gate: {time_box_minutes: 60, ai: "off"}
student_files:
  - {from: "tracks/{track}/tests/test_mX_Y.py", to: "{project_dir}/tests/test_mX_Y.py"}
---
# MX.Y <Title>

<Overview: what the student builds and why it matters.>

## Sessions
<How each session runs; predict checkpoints; when Duck mode applies.>

## Coverage
| Competency | Checked by |
|---|---|
| c1 … | … |
```

**Checklist for adding a module** (also in [CLAUDE.md](../CLAUDE.md)):

1. Competencies are can-do statements, 4–7 per module.
2. Resources are verified on the live site (`verified_on`) or marked `TODO(verify)`.
3. Pset sessions are `ai: duck`. Fingerprints are verified, and summaries are one line in our own words.
4. `remix.md` has a section per track. Specs follow the design rules, with exactly one deliberate untested edge case.
5. Tests, starter (first step only) and checkpoint exist for each tested track.
6. The explain-back bank has several questions per competency and at least one AI-off micro-task.
7. The coverage table has no gaps (the validator proves it).
8. `validate.py` and `check_checkpoints.py` pass.

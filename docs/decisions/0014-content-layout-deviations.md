# 0014. Content layout: deviations from architecture.md

**Status:** Accepted

## Context
[architecture 2.1](../design/architecture.md) sketched a module folder (`tests/`, `checkpoints/`, `explain-back.md`, `rubric.md`). The task brief and the need for machine validation refine this.

## Decision
- **Explain-back banks are YAML** (`explain-back.yaml`), validated by `schema/explain-back.schema.json`.
- **Per-track folders:** `tracks/<track>/{starter/, tests/, checkpoint/}` inside a module, because tests and checkpoints differ by track.
- **`starter/`** (new): stub files given to the student when the block project starts (see [0017](0017-starter-files-and-pytest-imports.md)).
- **Rubrics live in `tutor/rubrics/<id>.yaml`** and modules reference one (`remix.rubric`), because most modules share the default.
- **LLM output schemas** in `schema/llm-output/` define the JSON the bot expects back from review, grading, guard and onboarding prompts.
- **`block.md` `modules` is a list of objects** `{id, title, status}` (not bare ids), so stub modules can exist as titles without folders.
- **Modules may define `checks`** (non-code gate items verified by the bot or the mentor, e.g. "commits use the noreply email") and may set `explain_back: false` (M0.1 only), and `remix` may be `null` (B0/B1).
- **The B1 hunt** lives in `blocks/b1-terminal/m1.2-terminal-basics/hunt/`, with `reference/solve.sh` used only by CI to prove the hunt checker is passable.
- **`requirements-dev.txt`** pins tooling for CI.

## Consequences
- `docs/content-format.md` is the authoritative human guide. `schema/` is the authoritative machine contract.

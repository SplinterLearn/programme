# 0015. Coverage references and shared test names

**Status:** Accepted

## Context
Every competency must be checked by at least one gate item, for every track a student might take. The bot and validate.py must resolve these references mechanically.

## Decision
- `coverage` maps each competency id to gate items written as typed references:
  `test:<pytest function name>`, `eb:<question id>`, `rubric:<criterion id>`, `check:<check id>`.
- **Test function names are shared across tracks.** Finance and fandom both have `test_rounds_up`, so one coverage table serves all tested tracks.
- Coverage is checked **per tested track**: an `eb:` item counts for a track only if the question's `tracks` is `all` or includes it.
- Missing references are **errors** in `ready` modules and **warnings** in `draft` modules.

## Consequences
- Adding a track means writing tests with the same function names, or extending coverage.
- The bot can compute "which competencies did this explain-back sample cover" from the same data.

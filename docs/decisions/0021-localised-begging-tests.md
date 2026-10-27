# 0021. Localised begging tests

**Status:** Accepted

## Context
The bot talks to students in their own language (`{{student_language}}`), and students try to get the solution in that language: with slang, typos, mixed-in English terms and tactics that don't appear in English. A model that passes the English begging test might still fail in Russian. [ADR 0012](0012-english-repo-language.md) keeps the repo in English and calls translations a bot-side concern. That rule is about translating content. These files are test data that imitates what students type.

## Decision
- **Localised begging tests live here** as `tutor/test-cases/begging.<lang>.yaml`, starting with Russian (`begging.ru.yaml`).
- **Only the student `message` is in the other language.** It is written the way a teen actually types, not as a literal translation. `description`, `tactic` and `expected` stay in English, and so does the code inside messages.
- **Ids:** `beg-NN-<lang>`. A case numbered below 50 translates `beg-NN` and keeps its `context` and `expected` exactly, so results can be compared across languages. Cases numbered 50 and up exist only in that language. `begging.yaml` stays below 50.
- **Schema:** a new `begging-tests-localised.schema.json` reuses the case definition from `begging-tests.schema.json`. The rules for `begging.yaml` are unchanged, so this is a MINOR bump (1.1.0).

## Consequences
- `validate.py` checks the id suffix, matching `defaults`, and that translations keep the original's `context` and `expected`. A missing translation is a warning.
- Changing an English case's `expected` means updating its translations in the same change.
- The bot repo's begging workflow has to load `begging.*.yaml` to run these cases. Until it does, it ignores them.

# 0006. The tutor is a Telegram bot using an LLM API

**Status:** Accepted

## Context
Consumer AI apps have age limits (Claude consumer apps are 18+; ChatGPT is 13+ with parental consent) and can't enforce our licence ladder, CS50 boundary or explain-back gate ([research report](../design/research-report.md), risks).

## Decision
The tutor is a **Telegram bot** (separate repo, `splinter-bot`) calling an LLM API: a **cheap model for chat** and a **stronger model for reviews and explain-back grading**. It reads this repo as content: prompts in `tutor/`, modules in `blocks/`.

## Consequences
- Prompts are generic: the deployed name and persona are injected as `{{tutor_name}}`.
- Prompts are content. Changing them changes the bot's behaviour without a bot deploy, so the begging test ([`tutor/test-cases/begging.yaml`](../../tutor/test-cases/begging.yaml)) must run before prompt changes are merged.
- The provider's terms for apps used by minors must be checked when choosing a model (open item in the bot repo).

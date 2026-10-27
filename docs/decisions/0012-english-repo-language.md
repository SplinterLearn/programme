# 0012. Repo language is English

**Status:** Accepted

## Context
The programme may serve students who speak different languages. Code, error messages and documentation for the tools are in English.

## Decision
Everything in this repo is in **English**. The bot may talk to a student in another language (`{{student_language}}`), but **code, error messages and technical terms stay in English**.

## Consequences
- Prompts tell the model to reply in the student's language and keep technical terms in English.
- Translations, if any, are a bot-side concern, not repo content.

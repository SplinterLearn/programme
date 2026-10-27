# tutor/: the bot's prompts and rules

Everything here is **content**: the bot (`splinter-bot`, a separate repo) loads it from its validated clone of this repo. **Changing a prompt changes the bot's behaviour without a bot deploy**, so run the begging test ([`test-cases/begging.yaml`](test-cases/begging.yaml), a manual workflow in the bot repo) before merging prompt changes.

| File | Used for | Model | Output |
|---|---|---|---|
| [`system-prompt.md`](system-prompt.md) | every chat turn: persona, licence rules, Duck mode, safety | cheap | chat text |
| [`context.md`](context.md) | the per-turn context appended after the system prompt (module, profile, session) | cheap | — |
| [`licence-levels.yaml`](licence-levels.yaml) | the L0–L3 ladder, rendered into `{{licence_rules}}` | — | — |
| [`onboarding-interview.md`](onboarding-interview.md) | M0.1 goals interview | cheap | chat, then [onboarding-summary JSON](../schema/llm-output/onboarding-summary.schema.json) |
| [`review-prompt.md`](review-prompt.md) | PR review against a rubric | strong | [review JSON](../schema/llm-output/review.schema.json) with a Markdown comment |
| [`explain-back-protocol.md`](explain-back-protocol.md) | `/check`: sampling and pass rules (Part 1), grading prompt (Part 2) | strong | [grade JSON](../schema/llm-output/explain-back-grade.schema.json) per answer; the bot computes the [result JSON](../schema/llm-output/explain-back-result.schema.json) |
| [`output-guard-prompt.md`](output-guard-prompt.md) | checks every draft reply before sending | cheap | [guard JSON](../schema/llm-output/output-guard.schema.json) |
| [`rubrics/remix-default.yaml`](rubrics/remix-default.yaml) | default remix rubric (pass 5/8) | — | — |
| [`test-cases/begging.yaml`](test-cases/begging.yaml) | about 20 "give me the answer" messages with expected behaviour, for choosing models | — | — |

Prompt files have frontmatter ([`schema/prompt.schema.json`](../schema/prompt.schema.json)): `id`, `purpose`, `model_tier`, `cache_layer`, `placeholders` and `output_schema`. `validate.py` checks that every `{{placeholder}}` used in a prompt is declared in its frontmatter **and documented below**. Only the body (after the frontmatter) is sent to the model.

## Placeholders

The bot fills these with plain text (Markdown is fine), never with HTML. Everything a student typed is inserted as **data**: the bot wraps it in clear delimiters and never lets it override the instructions.

| Placeholder | Filled with | Source | Used in |
|---|---|---|---|
| `{{tutor_name}}` | the deployed bot's name and persona name | bot config | system-prompt, onboarding-interview, review-prompt, explain-back-protocol |
| `{{licence_level}}` | `L0`, `L1`, `L2` or `L3` | bot DB (student) | system-prompt, review-prompt, output-guard-prompt |
| `{{licence_rules}}` | the current level rendered from `licence-levels.yaml`: name, summary, `may`, `must_not`, `max_code_lines`, plus the `always` rules | this repo | system-prompt, review-prompt, output-guard-prompt |
| `{{student_language}}` | the language to talk in, e.g. `English`, `Deutsch` | bot DB (onboarding `preferred_language`) | onboarding-interview, review-prompt, explain-back-protocol |
| `{{tracks}}` | for each `tracks/*.md`: id, title, summary | this repo | onboarding-interview |
| `{{module}}` | the current `module.md`: frontmatter as YAML **without** `cs50_fingerprints`, plus the body | this repo (pinned per student at module start) | context, review-prompt |
| `{{remix}}` | `remix.md` intro plus the student's `## Track:` section only | this repo (pinned) | context, review-prompt, output-guard-prompt |
| `{{track}}` | the student's track id | bot DB | context, review-prompt |
| `{{cs50_summaries}}` | one line per CS50 problem in the current block: problem, pset, filename, required functions, summary (from `cs50_fingerprints`) | this repo | context |
| `{{student_profile}}` | short profile: nickname (optional, chosen by the student), language, track, strengths, recurring confusions (e.g. "`=` vs `==`, 2×"), hearts left. No personal details. | bot DB | context |
| `{{mode}}` | `normal`, `duck`, `predict`, `quiz`, `retro`, `explain-back` or `skip-test` | bot state | context, explain-back-protocol, output-guard-prompt |
| `{{session}}` | today's session from `module.md` `sessions` (n, type, title, where, ai, notes), or "no active session" | this repo + bot state | context |
| `{{conversation_summary}}` | rolling summary of earlier turns in this module | bot DB | context |
| `{{recent_turns}}` | the last ~10 turns, oldest first, labelled `student:` / `tutor:` | bot DB | context |
| `{{rubric}}` | the module's rubric YAML (`remix.rubric`) | this repo | review-prompt |
| `{{edge_case}}` | `remix.edge_case.summary` plus the student's track entry from `per_track` | this repo | review-prompt |
| `{{pr_title}}`, `{{pr_body}}` | the PR's title and description | GitHub | review-prompt |
| `{{commits}}` | one line per commit: short SHA and message | GitHub | review-prompt |
| `{{diff}}` | the PR diff, provided test files excluded, truncated with a note if very long | GitHub | review-prompt |
| `{{test_results}}` | the CI conclusion and failing test names (or "not available yet") | GitHub checks | review-prompt |
| `{{question}}` | one question from `explain-back.yaml` as YAML (prompt, type, code, good_answer_notes, scoring, expected_fix) | this repo | explain-back-protocol |
| `{{answer}}`, `{{follow_up_answer}}` | the student's answer, and their answer to the one follow-up (empty if none) | chat | explain-back-protocol |
| `{{student_code}}` | the relevant file(s) from the student's merged-or-open PR | GitHub | explain-back-protocol |
| `{{student_message}}`, `{{draft_reply}}` | the student's last message and the tutor's draft reply | chat | output-guard-prompt |

## Cache-friendly order (chat turns)

The context is always built in this fixed order, so the provider can cache the repeated prefix ([architecture 3.3](../docs/design/architecture.md)):

| Layer | Content | Changes | Cached |
|---|---|---|---|
| 1 | `system-prompt.md` with `{{tutor_name}}`, `{{licence_level}}`, `{{licence_rules}}` | per deployment and licence level | yes (shared by every student at that level) |
| 2 | `context.md`, module part: `{{module}}`, `{{remix}}`, `{{track}}`, `{{cs50_summaries}}` | per module and track | yes |
| 3 | `context.md`, profile part: `{{student_profile}}` | rarely | small |
| 4 | `context.md`, session part: `{{mode}}`, `{{session}}`, `{{conversation_summary}}`, `{{recent_turns}}` | every turn | no |
| 5 | the student's message, as the user turn | every turn | no |

Rules:
- **Nothing dynamic goes above where it's needed.** The mode, hearts and time live in layers 3–4, never in layer 1. The language is in the profile (layer 3), so layer 1 can be shared across students.
- Review, grading, guard and onboarding prompts are single calls: put their static instructions first (the prompt body up to the first per-call placeholder), then the per-call data. Their `cache_layer` in frontmatter says where their first variable part sits.
- Every result the bot stores (review, explain-back, log) is stamped with the content commit SHA it used ([architecture 3.8](../docs/design/architecture.md)).

## JSON outputs

The bot validates every JSON output against its schema in [`schema/llm-output/`](../schema/llm-output/). If it doesn't validate, the bot retries once with the validation error appended, then falls back (review: post a "review delayed" note and alert the admin; guard: treat as `gives_away: true`; grade: ask the mentor).

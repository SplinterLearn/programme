# 0020. Explain-back scoring details

**Status:** Accepted

## Context
The task and [architecture 6.5](../design/architecture.md) set the explain-back's shape: 5–7 sampled questions plus an AI-off micro-task, graded 0–2, pass at ≥ 70% with the micro-task correct, retry after 12 h with different questions. A few details were open.

## Decision
- **The percentage excludes the micro-task.** `percent = total / (2 × non-micro-task questions)`. The micro-task is a separate must-pass (as in the architecture's "10/12 + fix-it ✅").
- **Sampling covers competencies that have `eb:` items in `coverage`.** Competencies checked only by tests, checks or rubric criteria are covered by those gate items.
- **One follow-up per question at most.** The grader may ask a single clarifying question and then decides. It never teaches or hints.
- **`suspected_ai_use` never fails a check automatically.** It triggers one live follow-up and a flag to the mentor.
- **Skip-test mode:** the explain-back is time-boxed to **30 minutes**, after the remix's own time box. Feedback is shown at the end, and unanswered questions score 0.
- **Normal mode:** no time limit. The session can pause and resume.
- **The bot computes the session result** (`explain-back-result.schema.json`). The LLM only grades single answers.

## Consequences
- Grades are reproducible per answer and auditable (rationale plus content SHA).
- The 30-minute skip-test limit is a first guess. Revisit it after the pilot.

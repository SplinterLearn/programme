---
id: explain-back-protocol
purpose: "The explain-back check (/check): how the bot samples questions, runs the session and decides pass/fail; plus the grading prompt the strong model gets for each answer."
model_tier: strong
cache_layer: 2
placeholders: [tutor_name, student_language, mode, question, answer, follow_up_answer, student_code]
output_schema: schema/llm-output/explain-back-grade.schema.json
---
# Part 1: protocol (for the bot; not sent to the model)

The explain-back closes every module that has `explain_back: true`. The review is about the code; the explain-back is about the **student**: can they explain what they built?

## When
- After the PR review, when the student sends `/check`. Tests must be green first.
- **Skip-test mode:** the same gate, run right after the time-boxed, AI-off remix (or the B3 tasks).

## Sampling (5–7 questions + 1 AI-off micro-task)
From the module's `explain-back.yaml`:
1. **Eligible:** questions whose `tracks` is `all` or includes the student's track. On a retry, **exclude every question asked in earlier attempts** of this module, if the bank still allows full coverage. Otherwise reuse the fewest possible.
2. **Micro-task:** pick one `type: micro-task` question with `ai_off: true`, a different one from the last attempt if available. It's always included.
3. **Coverage:** pick 5–7 other questions so that **every competency that has an `eb:` item in the module's `coverage`** is covered by at least one picked question (or the micro-task). Competencies covered only by tests, checks or rubric criteria are already checked by those gate items. Use a greedy set cover: prefer questions that cover uncovered competencies, then variety of `type`.
4. **Always include**, when they exist: one `trace` question on the student's own code, and one `edge` question about the module's deliberate edge case (`remix.edge_case.covered_by`).
5. **Extras** (they count towards the 7): if the review listed `explain_back_prep` items, turn one into a question. If the student swapped in a checkpoint after the previous module, ask them to explain one difference between their version and the checkpoint.
6. **Block skip test:** `sample_per_module` questions from each module plus `micro_task_per_module` micro-tasks, covering all competencies of each module where possible.

## Running it
- Start: *"Explain-back for M2.1: 6 questions + 1 tiny fix-it task. No AI for the fix-it part, just you and your editor. Ready?"*
- One question at a time, in the student's language (technical terms in English). Show `code` blocks exactly as written in the bank.
- After each answer, call the grading prompt (Part 2). If it returns a `follow_up`, ask it **once**, then grade again with both answers. Show the student the score and the short `feedback` (e.g. *"✅ 2/2, perfect trace"*), unless the mode is skip-test, where feedback comes at the end.
- **No tutoring during the explain-back.** If the student asks for help, the bot only clarifies what the question means. Hearts aren't used.
- **Micro-task:** the student fixes the code in their editor **without any AI**, runs it, and pastes the fix plus one sentence on what was wrong.
- **Time limits:** normal mode has none (the session can be paused and resumed; state is kept). In **skip-test mode** the explain-back is time-boxed to **30 minutes** after the remix's own time box (`skip_gate.time_box_minutes`). Unanswered questions score 0 ([ADR 0020](../docs/decisions/0020-explain-back-scoring-details.md)).

## Scoring and pass
- Each non-micro-task question scores 0–2 against its `scoring` anchors.
- `percent = 100 × total / (2 × number of non-micro-task questions)`.
- **Pass = percent ≥ 70 AND the micro-task is correct** (`micro_task_correct: true`).
- Example: 6 questions, 10/12 = 83% + fix-it ✅ → **PASS**.
- `suspected_ai_use: true` on any answer doesn't fail the check automatically. The bot asks one live follow-up on that question, and flags it to the mentor in the digest.

## After
- **Pass:** set the PR status `tutor/explain-back` to `success`, comment with the score, celebrate, and stamp the result with the content commit SHA (`schema/llm-output/explain-back-result.schema.json`). If this closes a block, propose the licence upgrade to the parent/mentor (they approve; the bot never upgrades on its own).
- **Not yet:** status stays `pending`. Tell the student kindly what to revise (the competencies with low scores, never the answers). They can **retry after 12 hours, with different questions**.
- Explain-back answers are stored as transcripts. The mentor can read them.

---

# Part 2: grading prompt (sent to the strong model for each answer)

You are {{tutor_name}}'s grader. Grade **one** answer from a teenage student in an explain-back check. Be fair and consistent: use the anchors, not your own standard. A short, informal or misspelled answer that shows the idea gets full marks. A long answer that never states the key idea doesn't. Mode: {{mode}}.

## The question (from the bank, with anchors)
{{question}}

## The student's code (relevant excerpt from their PR, for trace, why and change questions)
{{student_code}}

## The student's answer
{{answer}}

## Their answer to your follow-up (empty if none was asked)
{{follow_up_answer}}

## How to grade
1. Compare the answer with `good_answer_notes` and pick the anchor (`"0"`, `"1"` or `"2"`) it matches best. If it's between two anchors, pick the lower one, unless a follow-up was already asked (then decide).
2. For **trace/why/change** questions, judge against the student's own code when it differs from the reference, as long as their code is correct.
3. For a **micro-task**: `micro_task_correct` is `true` only if the pasted fix would work **and** the student names the cause (and the line, if the question asks). Set the score from the anchors too. For other types, set `micro_task_correct` to `null`.
4. If the answer is ambiguous and **one short question** would settle it, put it in `follow_up` (in {{student_language}}) and still give a provisional score. Never use the follow-up to teach or hint the answer. If a follow-up answer is already present, set `follow_up` to `null`.
5. `suspected_ai_use`: `true` only if the answer reads like pasted AI output (polished essay style, terms far beyond the module, contradicts their own code). Never accuse the student in `feedback`.
6. `feedback`: 1–2 friendly sentences in {{student_language}} (technical terms in English). Say what was good, and for a low score which idea is missing, **without giving the answer away** (they may retry).
7. `rationale`: for the mentor, in English. Which anchor and why.

## Output
Only one JSON object matching `schema/llm-output/explain-back-grade.schema.json`, with no other text:

```json
{"question_id": "m2.1.q3", "score": 2, "micro_task_correct": null, "rationale": "Correct values at each step incl. % remainder 100 → +1 → 4.", "feedback": "✅ Perfect trace, you clearly know what % does.", "suspected_ai_use": false, "follow_up": null}
```

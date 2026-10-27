---
id: b3-skip
block: b3
status: ready
kind: tasks
ai: "off"
time_box_minutes: 60
competencies:
  - {id: b3.skip.c1, text: "Can create a branch, commit to it in small meaningful steps and push it"}
  - {id: b3.skip.c2, text: "Can open a pull request with a filled-in template and explain why PRs exist"}
  - {id: b3.skip.c3, text: "Can respond to a review comment with a follow-up commit and a reply"}
  - {id: b3.skip.c4, text: "Can resolve a merge conflict, deciding deliberately which side (or which combination) wins"}
  - {id: b3.skip.c5, text: "Can explain what a branch and a merge conflict are"}
tasks:
  - id: b3.skip.t1
    title: "In your repo, create a branch b3-skip from main and make at least two small commits with clear messages (e.g. add notes/git.md, then extend it)"
    check: "Bot: the branch exists with 2+ commits authored by the student (noreply email) and non-empty messages."
  - id: b3.skip.t2
    title: "Push the branch and open a PR to main with the PR template filled in"
    check: "Bot: the PR exists, from b3-skip, and every template section has content."
  - id: b3.skip.t3
    title: "The bot leaves a review comment on your PR; respond with a follow-up commit and a reply to the comment"
    check: "Bot: a new commit after the review comment, and a reply on the comment thread."
  - id: b3.skip.t4
    title: "Run scripts/stage_conflict.sh (from the programme repo) to create a scratch repo with a merge conflict; resolve it following the team's decision in NOTES.md, commit the merge, and paste the output of stage_conflict.sh --check"
    check: "Student pastes the --check output: no conflict markers, the decided value kept, both non-conflicting changes kept, merge committed."
explain_back: {file: skip-test.explain-back.yaml, sample: 4, micro_tasks: 1}
coverage:
  b3.skip.c1: ["task:b3.skip.t1", "eb:b3.skip.q1"]
  b3.skip.c2: ["task:b3.skip.t2", "eb:b3.skip.q2"]
  b3.skip.c3: ["task:b3.skip.t3", "eb:b3.skip.q3"]
  b3.skip.c4: ["task:b3.skip.t4", "eb:b3.skip.q5", "eb:b3.skip.q6"]
  b3.skip.c5: ["eb:b3.skip.q1", "eb:b3.skip.q4"]
---
# B3 skip test: git & GitHub collaboration

Ready **before** Block 3's modules are written, so students who already know git can test out early ([ADR 0008](../../docs/decisions/0008-skip-test-is-exit-gate.md)). **AI-off, 60 minutes** for the tasks, then the explain-back.

## Tasks
1. **Branch.** Create `b3-skip` from `main`, and make at least two small commits with clear messages.
2. **PR.** Push it and open a PR to `main`, filling in the PR template (what I built / what was hard / one question / checklist).
3. **Review.** The bot leaves a review comment. Respond with a follow-up commit *and* a reply on the comment.
4. **Merge conflict.** Get the programme repo's [`scripts/stage_conflict.sh`](../../scripts/stage_conflict.sh), and run it in your cs50.dev terminal:
   ```bash
   bash stage_conflict.sh ~/conflict-practice
   ```
   It makes a scratch repo where two teammates edited the same line, and starts the merge. Resolve the conflict following the team decision in `NOTES.md`, keep everyone's other changes, and commit the merge. Then run:
   ```bash
   bash stage_conflict.sh --check ~/conflict-practice
   ```
   and paste its output to the bot.

## Explain-back
4 questions from [the bank](skip-test.explain-back.yaml) plus the AI-off micro-task (resolving conflict markers by hand). Pass at ≥ 70% with the micro-task correct.

## If you pass
Block 3's mechanics are done. **Still do the peer PR** (B3's exit artefact: a PR merged into someone else's repo). It's the part of B3 that's about people, not commands.

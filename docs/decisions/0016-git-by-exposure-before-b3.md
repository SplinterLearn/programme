# 0016. Git by exposure before Block 3

**Status:** Accepted

## Context
Every module from Block 1 onward closes with a PR in the student repo, but git collaboration is taught in Block 3. Without some git earlier, the module loop can't run.

## Decision
- **M0.2** has the student clone their repo (in cs50.dev or locally) and make a first commit using copy-paste commands from the template README.
- The student template README lists **"the git commands you'll use until Block 3"** (clone, switch to a new branch, add, commit, push) and how to open a PR on github.com.
- **M1.3** explains what those commands do (still without branches or merges in depth).
- **Block 3** teaches git properly: branches, PRs, review, conflicts.

## Consequences
- Students "learn by exposure" first, like CI in Block 2 ([architecture 6.4](../design/architecture.md)).
- Students who already know git can take the B3 skip test.

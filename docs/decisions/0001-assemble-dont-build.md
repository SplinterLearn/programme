# 0001. Assemble, don't build

**Status:** Accepted

## Context
No single platform covers terminal → git → fundamentals → testing → web → AI-assisted engineering for self-paced teens ([research report](../design/research-report.md), Q3–Q4). Writing our own interactive lessons would take years and still be worse than CS50P, The Odin Project or futurecoder.

## Decision
Learning content comes from existing free platforms. This repo is only the **thin layer** around them: roadmap, competencies, remix projects, tests, rubrics, explain-back banks, tutor prompts and the student template (a separate repo).

## Consequences
- We link to external courses and never copy their content (see [0018](0018-public-repo-generic-roles.md)).
- We depend on third-party sites staying up and stable. Resource facts are verified live and dated (`verified_on`), or marked `TODO(verify)`.
- Authoring effort goes into remixes, tests and explain-back banks, not lessons.

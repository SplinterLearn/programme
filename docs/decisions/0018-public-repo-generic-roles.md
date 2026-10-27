# 0018. Public repo: generic roles, sanitised docs, no copied course content

**Status:** Accepted

## Context
The repo is public. The design docs were written for one pilot family and contain personal details. Third-party courses are copyrighted.

## Decision
- Write only in generic roles: *student*, *parent*, *mentor* (*admin* in bot terms). No names, ages of real people, locations, schools or family details. Use "they" for the student.
- `docs/design/` holds **sanitised copies** with an "edited for publication" banner.
- **Never copy third-party course content.** Link to it. CS50 fingerprint summaries are one line in our own words. Distinctive strings are short tokens (≤ 4 words). No problem statements, distribution code or solutions.
- External facts are verified on the live site (with `verified_on`), or marked `TODO(verify): …`.

## Consequences
- The final check of each task greps for personal data and copied text.
- Fingerprints are a little weaker than full-text matching. The classifier fallback covers the gap.

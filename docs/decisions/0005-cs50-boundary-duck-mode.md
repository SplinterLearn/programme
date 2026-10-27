# 0005. CS50 boundary and Duck mode

**Status:** Accepted

## Context
CS50's academic honesty rules allow only CS50's own AI (the CS50 Duck) on problem sets. A tutor bot that helped with them would push the student to break those rules.

## Decision
- On CS50 problem sets **only the CS50 Duck may help**. The tutor redirects (no heart charged).
- Sessions of `type: pset` force `ai: duck` (a JSON Schema rule). In those sessions the bot is in **Duck mode**: plan, motivation and breaks only; every technical question goes to the Duck.
- Outside pset sessions, pasted CS50 code is detected by **fingerprints** (`cs50_fingerprints` in `module.md`: filename, required functions, short distinctive tokens) and then by a classifier over our own one-line summaries.
- **Solutions to CS50 problem sets never go in the student repo** (it's a different repo, and CS50 work lives in cs50.dev / submit50).

## Consequences
- Fingerprint summaries are one line, in our own words. We never paste problem statements (see [0018](0018-public-repo-generic-roles.md)).
- The remix exists partly so the tutor *can* help: it's the student's own work ([architecture 5.1](../design/architecture.md)).

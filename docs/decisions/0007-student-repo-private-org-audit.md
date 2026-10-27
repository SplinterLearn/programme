# 0007. Student repo: private, in a free org, audited not locked

**Status:** Accepted

## Context
Branch protection on private repos needs a paid GitHub plan. The student must not be able to remove the bot's GitHub App or webhooks.

## Decision
- One **private** repo per student, in a **free GitHub org owned by the parent/mentor**. The student has the **Write** role (not Admin).
- **No branch protection.** The bot **audits** merges and direct pushes to `main` ([architecture 3.4](../design/architecture.md)). A merge without green tests and a passed explain-back counts as "merged early".
- Progress, badges and licence upgrades count **only modules closed properly**.
- The student's git `user.email` is their **GitHub noreply address from day one** (M0.2 setup check).
- Student repos are generated from the separate **student-template** repo (a GitHub template repository).

## Consequences
- The template's workflow and PR template are part of the gate. Template changes are made by hand in existing student repos.
- M0.2 includes a check that commits use the noreply email.

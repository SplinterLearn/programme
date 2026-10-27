---
id: m0.2
block: b0
title: "Setup & ground rules"
status: ready
weeks: [1, 1]
est_sessions: 2
licence_level: L0
competencies:
  - {id: m0.2.c1, text: "Has a GitHub account (13+) and can explain why their commits use the GitHub noreply email instead of a real address"}
  - {id: m0.2.c2, text: "Can log in to cs50.dev with GitHub, open its terminal and run a command there"}
  - {id: m0.2.c3, text: "Can clone their repo, commit a change and push it using the copy-paste git commands"}
  - {id: m0.2.c4, text: "Can state the five ground rules in their own words, including who may help on CS50 problem sets"}
  - {id: m0.2.c5, text: "Can explain how hearts, the AI licence ladder and the weekly digest work"}
resources:
  - title: "GitHub Terms of Service — minimum age 13"
    url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
    role: backbone
    notes: "Section B.3: you must be 13 or older (some countries set a higher age). The parent/mentor creates the org and invites the student."
    verified_on: 2026-10-27
  - title: "GitHub Docs — Setting your commit email address"
    url: https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address
    role: backbone
    notes: "How to find your noreply address (ID+USERNAME@users.noreply.github.com) and turn on 'Keep my email addresses private'."
    verified_on: 2026-10-27
  - title: "cs50.dev — Visual Studio Code for CS50"
    url: https://cs50.dev/
    role: backbone
    notes: "CS50's browser-based VS Code (Codespaces). Log in with GitHub. Nothing to install."
    verified_on: 2026-10-27
  - title: "Visual Studio Code (desktop)"
    url: https://code.visualstudio.com/
    role: optional
    notes: "Optional local editor for later. cs50.dev is the default so every student has the same setup."
sessions:
  - n: 1
    type: setup
    title: "Accounts and tools: GitHub account and privacy settings, join the org, cs50.dev login, start the Telegram tutor"
    where: "github.com + cs50.dev + Telegram, with the parent or mentor"
    ai: mentor
    notes: "Follow the setup checklist in the body. The parent/mentor does the org invite."
  - n: 2
    type: setup
    title: "First commit: clone your repo in cs50.dev, set the noreply email, commit about-me.md, push. Then ground rules and a short explain-back"
    where: "cs50.dev + Telegram (tutor bot)"
    ai: bot-L0
    notes: "Copy-paste git commands from the student repo README (ADR 0016). Understanding them comes in M1.3 and Block 3."
cs50_fingerprints: []
checks:
  - {id: m0.2.k1, text: "GitHub account exists and the student is a member of the org with the Write role on their repo", verified_by: mentor}
  - {id: m0.2.k2, text: "Every commit in the student repo uses a users.noreply.github.com author email", verified_by: bot}
  - {id: m0.2.k3, text: "cs50.dev opens with the student's GitHub login and its terminal runs a command", verified_by: mentor}
  - {id: m0.2.k4, text: "First commit (about-me.md) pushed to the student repo by the student", verified_by: bot}
  - {id: m0.2.k5, text: "Ground rules read together and agreed by the student and the parent/mentor", verified_by: mentor}
explain_back: true
remix: null
coverage:
  m0.2.c1: ["check:m0.2.k1", "check:m0.2.k2", "eb:m0.2.q1", "eb:m0.2.q7"]
  m0.2.c2: ["check:m0.2.k3"]
  m0.2.c3: ["check:m0.2.k4", "eb:m0.2.q6"]
  m0.2.c4: ["check:m0.2.k5", "eb:m0.2.q2", "eb:m0.2.q3"]
  m0.2.c5: ["eb:m0.2.q4", "eb:m0.2.q5"]
skip_gate: null
student_files: []
---
# M0.2 Setup & ground rules

Two sessions: get everything working, then agree how the course works.

## Setup checklist (session 1, with the parent or mentor)

1. **GitHub account.** You must be **13 or older** (GitHub's terms). Pick a username that **isn't your real name**.
2. **Email privacy.** In GitHub → Settings → Emails, tick **"Keep my email addresses private"** and copy your **noreply address**. It looks like `12345678+username@users.noreply.github.com`.
3. **Join the org.** The parent/mentor invites you to the programme's GitHub org and generates your private repo from the [student template](https://github.com/splinterlearn/student-template). You get the **Write** role.
4. **cs50.dev.** Open [cs50.dev](https://cs50.dev/) and log in with GitHub. Wait for VS Code to load, click into the terminal and type `ls`. This is your workspace for the year.
5. **The tutor.** Open the tutor bot in Telegram and press Start (the parent/mentor registers you first).

## First commit (session 2)

In the cs50.dev terminal, copy these one line at a time, replacing the parts in `<…>`:

```bash
git config --global user.name "<your GitHub username>"
git config --global user.email "<your noreply address>"
git clone https://github.com/<org>/<your-repo>.git
cd <your-repo>
```

Then open `about-me.md`, paste in the draft from M0.1, save, and:

```bash
git add about-me.md
git commit -m "Add about-me"
git push
```

Refresh your repo on github.com: your commit is there. You don't need to understand these commands yet. M1.3 explains them, and Block 3 teaches git properly ([ADR 0016](../../../docs/decisions/0016-git-by-exposure-before-b3.md)).

## The five ground rules

1. **The bot is your tutor, not your answer machine.** At your level it gives hints, not code.
2. **CS50 problem sets: only the CS50 Duck.** The bot will send you to [cs50.ai](https://cs50.ai/). That's CS50's rule, not ours.
3. **Every module closes with an explain-back.** If you can't explain it, it isn't done yet, and that's fine.
4. **Some problems will take several sittings.** Being stuck is part of the job.
5. **Your parents (or mentor) see a weekly summary.** You'll see it too. They can also read your chats with the bot. This is how the course works for everyone; it isn't spying.

## How the course works

- **Hearts ❤️:** you have 10. Each question to the bot costs one, and they refill over time. It's not about money: it nudges you to think for a minute before asking. Problem-set redirects to the Duck are free.
- **The AI licence ladder:** the bot's help grows as you show understanding. L0 Tutor (now: hints and questions) → L1 Explainer (after Block 2) → L2 Pair (after Block 4) → L3 Supervisor (after Block 5). Each step needs your parent or mentor's OK. See [ROADMAP](../../../ROADMAP.md#ai-licence-ladder).
- **The weekly digest:** every Sunday your parent/mentor gets a short summary: modules done, time spent, recurring confusions, and your question for the live session.
- **Never paste secrets** (passwords, keys) or personal details into the bot, your repo or any AI tool.

## Coverage

| Competency | Checked by |
|---|---|
| c1 GitHub + noreply | k1, k2 (bot checks commit emails), q1, micro-task q7 |
| c2 cs50.dev | k3 |
| c3 First commit | k4, q6 |
| c4 Ground rules | k5, q2, q3 |
| c5 Hearts, ladder, digest | q4, q5 |

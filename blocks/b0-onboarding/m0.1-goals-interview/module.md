---
id: m0.1
block: b0
title: "Goals interview & track choice"
status: ready
weeks: [1, 1]
est_sessions: 1
licence_level: L0
competencies:
  - {id: m0.1.c1, text: "Can say what they want to be able to build, and why (goals and one or two dream projects)"}
  - {id: m0.1.c2, text: "Can pick a track hypothesis from the track list and give a reason for it"}
  - {id: m0.1.c3, text: "Can describe their current experience honestly (terminal, Python, git, web), so the right skip tests are offered"}
  - {id: m0.1.c4, text: "Can say what belongs in about-me.md and what must stay out (no personal details)"}
resources: []
sessions:
  - n: 1
    type: interview
    title: "Goals interview with the tutor bot (about 30-45 minutes), then agree about-me.md with the mentor"
    where: "Telegram (tutor bot) + mentor"
    ai: bot-interview
    notes: "The bot runs tutor/onboarding-interview.md and produces a structured summary and a draft about-me.md. The mentor reviews both."
cs50_fingerprints: []
checks:
  - {id: m0.1.k1, text: "Interview completed; the bot stored the structured summary (goals, track ranking, experience flags, time budget)", verified_by: bot}
  - {id: m0.1.k2, text: "Draft about-me.md reviewed with the mentor: goals and experience in the student's own words, no personal details", verified_by: mentor}
  - {id: m0.1.k3, text: "Track hypothesis chosen and recorded (it can change at any block boundary)", verified_by: mentor}
  - {id: m0.1.k4, text: "Skip-test offers from the experience flags discussed (take now, later, or not at all)", verified_by: mentor}
explain_back: false
remix: null
coverage:
  m0.1.c1: ["check:m0.1.k1", "check:m0.1.k2"]
  m0.1.c2: ["check:m0.1.k3"]
  m0.1.c3: ["check:m0.1.k1", "check:m0.1.k4"]
  m0.1.c4: ["check:m0.1.k2"]
skip_gate: null
student_files: []
---
# M0.1 Goals interview & track choice

The first conversation with the tutor bot. It's an interview, not a test: there are no wrong answers.

## How it runs
1. The parent or mentor registers the student with the bot (admin command). The student opens the bot in Telegram and presses **Start**.
2. The bot runs the interview from [`tutor/onboarding-interview.md`](../../../tutor/onboarding-interview.md): at most about 12 questions, one at a time, about
   - **goals**: what you'd like to be able to build by the end of the year;
   - **interests**: what you spend your free time on (it maps to the [tracks](../../../tracks/));
   - **experience**: terminal, Python, git, websites; this decides which skip tests to offer;
   - **time budget**: how many sessions a week are realistic;
   - **dream projects**: one or two things you'd build if you could.
3. The bot sends back a short summary and a **draft `about-me.md`**. You edit it until it sounds like you.
4. With the mentor: agree the track hypothesis and the skip-test offers. The draft is committed in M0.2 as your first commit.

## Privacy
`about-me.md` lives in your repo, which may become public one day (portfolio). It contains goals, track and experience only. **No real name, age, school, town, photos or contact details.** The bot never asks for those, and if you type them, it'll suggest leaving them out.

## What the bot stores
The structured summary ([`schema/llm-output/onboarding-summary.schema.json`](../../../schema/llm-output/onboarding-summary.schema.json)) goes into the bot's database, not your repo. It's used to theme your remixes and to offer skip tests.

## Gate
There is no explain-back. The gate is the interview output, checked by the bot and the mentor.

| Competency | Checked by |
|---|---|
| c1 Goals & dream projects | k1 interview summary, k2 about-me.md reviewed |
| c2 Track hypothesis | k3 track recorded |
| c3 Honest experience | k1 summary experience flags, k4 skip-test offers discussed |
| c4 No personal details | k2 about-me.md reviewed |

M0.1 can't be skipped (`skip_gate: null`).

> **Edited for publication.** This is a copy of the original research report, edited for this public repo: references to the pilot family (a parent and their child) were replaced with generic roles. Findings, figures and sources are unchanged and have not been re-verified; where this report conflicts with the task brief, `architecture.md` or the ADRs in `docs/decisions/`, those win.

# Building a Zero-to-Builder AI-Assisted Coding Programme for Teens: Evidence, Design, and Build-vs-Assemble Verdict

Your core design is sound, but the evidence points to one essential change. A 9-month, modular, self-paced programme with an AI tutor can work, but only if AI access is earned in stages. Early on, the AI acts as a Socratic tutor that does not hand over code. It becomes a code generator only after the teen can read, trace, and debug code without it. Rigorous studies (Bastani et al., PNAS 2025; Anthropic 2026) show that unrestricted AI makes practice look better while learning gets worse, and debugging takes the biggest hit.\[1\]\[2\] No single platform covers your full programme, so the best route is to **assemble** existing free resources and add a thin custom layer that you build yourself: the curriculum map, placement tests, the AI-tutor configuration and "AI licence" gates, and the assessment rubrics.

## TL;DR

- **Validated with changes:** 9 months is about right for "confident builder" (not "job-ready") at roughly 5–7 hours a week. Keep 70/30 as the year-long total, but schedule it in stages: months 1–4 are almost all common core with interest-themed examples, and the personalised track grows to about 50% of time in months 5–9. Most important, gate AI use with an "AI licence" ladder, because unguarded AI reduced learning in RCTs (17% worse closed-book exam scores for high-schoolers given plain GPT-4; 50% vs 67% quiz scores for developers learning a new library).\[1\]\[2\]
- **Pedagogy that works without syllabus-heavy syntax drilling:** PRIMM/Use-Modify-Create, Parsons problems, worked examples, explain-back checks, project-based learning, mastery gates with placement tests, and light gamification plus social stakes. Social stakes matter because self-paced courses lose most learners (3–6% certification among all registered edX learners, against 44–56% among those who paid).\[3\]
- **No turnkey platform exists:** CS50, The Odin Project, freeCodeCamp, Boot.dev, Khan Academy/Khanmigo, CodeAI (formerly Code.org), and Hack Club each cover parts. Most still teach language syntax first, and several actively ban or discourage AI. Age rules matter: Claude's consumer apps are 18+, ChatGPT is 13+ with parental consent, and GitHub plus free Copilot Student are 13+.\[4\]\[5\] Build the "AI-era software engineering" layer yourself.

## Key Findings

1. **AI help without guardrails harms learning; guardrailed AI tutoring can help a lot.** In a field experiment with nearly 1,000 maths students at a large high school in Turkey (Fall semester 2023–24), a plain GPT-4 interface raised practice scores by 48%, but those students then scored 17% worse than controls on a closed-book exam. A safeguarded tutor that gave hints rather than answers raised practice scores by 127% and removed the harm, though it did not significantly improve exam results (Bastani et al., PNAS 122(26), 2025, which concludes that "without guardrails, students attempt to use GPT-4 as a 'crutch' during practice problem sessions, and subsequently perform worse on their own"). The students using plain AI were also overconfident about how much they had learned.\[6\] By contrast, a carefully engineered Harvard physics AI tutor (N=194 in the analysis) produced more than double the learning gains of an active-learning lecture, in a median of 49 minutes (Kestin et al., Scientific Reports 2025).\[7\]\[8\] Its design was explicit: brief responses, "only give away ONE STEP AT A TIME," and full worked solutions placed in the prompt to stop it inventing answers.\[8\]
2. **How the AI is used matters more than whether it is used.** In Anthropic's RCT (52 mostly junior developers learning an unfamiliar Python library), the AI group scored 50% vs 67% on a follow-up quiz (Cohen's d = 0.738). The biggest gap was on debugging questions, and the AI group was not significantly faster. However, participants who asked conceptual questions or requested explanations scored 65% or higher. Those who delegated, gradually leaned more on the AI, or let it debug for them averaged below 40%. Anthropic expects agentic tools to have an even larger effect.\[2\]
3. **AI widens gaps between learners.** Prather et al. (ICER 2024) found that stronger novices used AI to go faster, while struggling novices developed an "illusion of competence": they thought they understood more than they did.\[9\]\[10\] Kazemitabaar et al. (CHI 2023; 69 learners aged 10–17) found that AI code generators raised task completion during training without hurting retention a week later. Learners with more prior knowledge benefited most.\[11\]\[12\] **Implication:** fundamentals first, then AI.
4. **Self-paced courses fail mainly on motivation, not content.** Across MIT/Harvard edX courses, certification among all registrants was 3.13–5.91%, and 52% of registrants never started. Among paying verified-track learners, it was 44–56% (Reich & Ruipérez-Valiente, Science 2019).\[3\]\[13\] Commitment, stakes and identity matter more than the quality of the material.
5. **The established courses are split on AI.** CS50 allows only its own AI "duck" and bans ChatGPT, Claude and Copilot except on final projects.\[14\] The Odin Project says "We do not recommend using AI tools for your learning."\[15\] Code.org has rebranded as CodeAI, and its free AI Foundations course has students build web apps "with AI as a creative partner."\[16\]\[17\] Hack Club's challenges ("You Ship, We Ship," or YSWS) often count only "non-AI hours."\[18\]\[19\] No mainstream curriculum yet teaches the full modern workflow: specifications, agent supervision, code review of AI pull requests, and context engineering.

## Question 1 — How teens should learn coding, especially with AI

### Learning-science practices that fit a "language-light" programme

| Practice | Evidence | How to use it here |
|---|---|---|
| **PRIMM** (Predict–Run–Investigate–Modify–Make) / Use-Modify-Create | Sentance et al. (2019): 493 students aged 11–14 in 13 schools; the PRIMM group outperformed controls on post-tests after 8–12 weeks\[20\] | Default lesson template. It fits AI-era coding naturally, because most of a modern developer's job is *reading and modifying* code they didn't write. |
| **Parsons problems** (reorder scrambled code lines) | Ericson, Margulieux & Rick (Koli Calling 2017): significantly less time than fixing or writing the equivalent code, with "no statistically significant difference in the learning performance, or in student retention of the knowledge one week later"; Ericson's Georgia Tech dissertation found that adaptation "helped more learners successfully solve Parsons problems" | Fast concept checks and a way into each new idea without drilling syntax |
| **Worked examples / faded scaffolding** | Classic cognitive-load research; Parsons-as-scaffolding studies show higher practice performance and the same post-test scores\[21\] | Start every new topic with a fully worked example, then a partly completed one, then an independent task |
| **Project-based learning** | Chen & Yang (2019) meta-analysis in Educational Research Review: mean effect size d+ = 0.71, "a medium to large positive effect on students' academic achievement compared with traditional instruction" | Every block ends in a shipped artefact |
| **Mastery learning + placement tests** | Standard mastery design; low-cost assessments like Parsons problems are sensitive measures of learning\[22\] | Skip-tests per module; nobody advances on a "pass" they didn't earn |
| **Spaced retrieval** | Robust general learning-science finding | Weekly 10-minute AI-generated review quizzes on earlier blocks |
| **Gamification** | Sailer & Homner (2020) meta-analysis: g = .49 cognitive, .36 motivational, .25 behavioural; motivational effects less stable; game fiction and social interaction moderate behavioural outcomes\[23\]\[24\] | Use XP, streaks and badges as a thin layer. Real motivation should come from meaningful projects and an audience. |
| **Self-determination theory** (autonomy, competence, relatedness) | Widely used motivation framework | Autonomy = interest track and project choice; competence = visible mastery gates; relatedness = peers via Hack Club and GitHub collaboration |
| **Explain-back / self-explanation** | Self-explanation research; CS50 now runs quizzes as "20 minutes long interactive conversations with the CS50 Duck"\[25\] | Every module ends with an oral or chat "defend your code" check |

### Design rules for AI use (the "AI licence" ladder)

Treat AI as a privilege unlocked by demonstrated understanding.

- **Level 0 – Tutor only (Blocks 0–2):** The AI is a Socratic tutor that never writes solution code. Model it on CS50's Duck, whose updated prompt says "do not diagnose errors or provide future steps, but rather … ask them leading questions or hints."\[26\] Rate limits help. CS50 gives each student 10 "hearts," regaining one every three minutes.\[27\]
- **Level 1 – Explainer (Blocks 2–3):** The AI may explain code the student pastes in and suggest hints, but cannot write new code.
- **Level 2 – Pair programmer (Blocks 4–5):** The AI may generate snippets. Every accepted snippet must be explained back and covered by a test. This matches the "generation-then-comprehension" and "hybrid code-explanation" patterns that scored well in Anthropic's study.\[2\]
- **Level 3 – Agent supervisor (Block 6 onward):** The student writes a specification and acceptance tests first, the agent implements, and the student reviews the diff as a pull request. Each block includes one "AI-off" session to keep debugging skills sharp.

Guardrails leak, and your design must assume this. Even CS50's Duck, which is built specifically not to hand out solutions, included code blocks in about 22% of all responses (48% of conversations) before CS50 tuned it with few-shot examples.\[26\] Check your tutor's behaviour regularly. Major providers also offer learning modes, such as Claude Code's "Learning"/"Explanatory" output styles and ChatGPT Study Mode, which Anthropic recommends for building understanding.\[2\]

### AI tutors for feedback and grading

LLM grading is now usable for formative feedback but not as the only judge. In one university intro-programming course, GPT-4o agreed exactly with human graders on 80% of 6,345 answers. Most disagreements came from humans missing errors or from GPT-4o grading ambiguous cases more strictly. 77% of students found the feedback helpful, but 30% said that preliminary AI grades lower than their final grades made them anxious.\[28\] **Use this hierarchy:**\[29\] automated tests decide whether the code works; an AI rubric reviewer comments on quality; an AI "viva" (an oral exam where the teen defends their work) checks understanding; and a parent or peer reviews the block capstones when available. Avoid treating AI grades as final for teens.

## Question 2 — Proposed programme structure (36 weeks plus a buffer)

**Load assumption:** 5–7 hours/week, about 200–250 hours in total. For comparison, Boot.dev estimates about 12 months for its adult backend career path.\[30\] "Confident builder in 9 months" is realistic; "job-ready" is not, and you shouldn't promise it.

| Block | Weeks | Core content | AI level | Exit artefact / skip test |
|---|---|---|---|---|
| **0. Onboarding & goals** | 1 | Interview with the AI tutor about goals and interests; generate a personal roadmap; set up accounts with parent consent; learning-how-to-learn; AI ethics and privacy rules | 0 | Written "why I'm here" plus a chosen track hypothesis |
| **1. The machine & the terminal** | 2–4 | Files and folders, paths, terminal navigation, editors (VS Code), installing tools, first `git init`/commit | 0 | Terminal scavenger hunt; skip test = timed terminal tasks |
| **2. Programming fundamentals (Python, PRIMM)** | 5–11 | Variables, types, conditionals, loops, functions, lists/dicts, reading tracebacks, decomposition; examples themed to the teen's interest | 0→1 | 3 small programs + Parsons/trace test; skip test = predict-the-output + modify tasks |
| **3. Git & GitHub collaboration** | 12–14 | Branches, pull requests, code review, issues, merge conflicts, README writing; first peer PR | 1 | PR merged into a peer's or Hack Club repo; skip test = resolve a staged conflict |
| **4. Reading, debugging, testing** | 15–17 | Debugger, print-debugging, reading unfamiliar code, unit tests (pytest), test-first thinking | 1→2 | Fix 5 seeded bugs AI-off; add tests to a provided repo |
| **5. Data, the web, and APIs** | 18–23 | HTTP, JSON, calling APIs, a simple database (SQLite/SQL), HTML/CSS/JS basics, a small web app, deployment to a free host | 2 | Deployed app that calls an API and stores data |
| **6. AI-assisted software engineering** | 24–26 | Spec writing, acceptance criteria, context engineering (project docs/rules files), supervising a coding agent, reviewing AI diffs, verifying output, security & secrets (`.env`, API key hygiene, never committing keys), basic threat awareness | 3 | Feature built by an agent from the teen's spec, with a review log and tests |
| **7. Personalised track** | 27–32 (with track-flavoured projects from week 18) | See tracks below | 3 | Track project |
| **8. Capstone (collaborative)** | 33–36 | Team of 2–4 via Hack Club or friends: issues, PRs, reviews, product thinking, docs, demo | 3 | Public repo + live demo + 5-minute video + oral defence |
| **Buffer** | 37–40 | Holidays, exams, catch-up | — | — |

**Personalised tracks:**
- **Finance/Data:** pandas, charts, Jupyter, APIs for market data, simple backtests (with an ethics note).
- **Web/Social/Creator:** front-end frameworks, social and analytics APIs, auth, hosting.
- **Games:** Pygame or Godot, game loops, state machines.
- **AI/ML:** calling LLM APIs, prompts as code, retrieval (RAG) basics, evaluating model output.
- **Hardware:** Raspberry Pi/micro:bit, sensors, IoT dashboards.
- **Automation/Tools:** scripts, CLIs, bots.

**On the 70/30 split:** keep it as an overall budget, but don't make it a fixed weekly ratio. Teens need the shared base (terminal, git, fundamentals, debugging, HTTP) before a specialism means anything. Personalisation should start on day 1 through *themed examples and project choice* (low cost, high autonomy), and grow into dedicated track content from about month 5.

**Placement:** each block has a 30–60 minute skip test made of predict-the-output, modify, debug and explain-back tasks, never multiple-choice alone. A student who already knows git would test out of Block 3's mechanics but should still do the peer-PR artefact. A teen who knows Python basics would test out of most of Block 2 but would likely need Block 1.

## Question 3 — Existing curricula: are they up to date?

| Programme | Paradigm | AI stance | Verdict |
|---|---|---|---|
| **CS50x / CS50P (Harvard)** | Strong CS fundamentals, C → Python → web | Built-in guardrailed AI tutor (CS50 Duck), used by about 211,000 students by Nov 2024; bans other AI except on final projects\[14\]\[26\] | Best-in-class AI tutor model; too syntax- and C-heavy as the backbone for a teen from zero |
| **The Odin Project** | Real tools from day one: command line, Git, local setup, projects\[31\] | "We do not recommend using AI tools for your learning"\[15\] | Excellent for git/terminal/web; anti-AI and web-only |
| **freeCodeCamp** | Browser exercises + certifications | No AI-native workflow verified | Good drill and practice; certificates are increasingly discounted because AI can solve the challenges\[32\] |
| **Boot.dev** | Gamified backend (Python, Go, SQL, Docker) | AI tutor "Boots" gives hints rather than answers\[33\] | Strongest gamified self-paced option; adult career focus; $59/mo or $399/yr\[33\] |
| **Khan Academy + Khanmigo** | JS, HTML, Python, SQL lessons | Socratic tutor that reviews code\[34\]\[35\] | Cheap, teen-appropriate; US-only, and a parent must sign up for under-18s\[34\] |
| **CodeAI (formerly Code.org)** | Rebranded June 2, 2026; AI Foundations high-school course\[36\] | Students learn how AI works, then build web apps with AI as a creative partner, reading and fixing AI-generated code\[37\] | Most AI-adapted mainstream curriculum, but designed for teacher-led classrooms |
| **Raspberry Pi Foundation / Code Club** | Research-led (PRIMM originated with its Chief Learning Officer, Sue Sentance)\[38\] | Not verified in this research | Good pedagogy source |
| **Hack Club** | Teens 13–18 ship projects for rewards (YSWS)\[39\]\[40\] | Varies by challenge; several count only non-AI hours or forbid AI\[18\]\[19\] | Best community/peer layer |
| **Vibe-coding courses** (DeepLearning.AI × Replit, Coursera/Scrimba, Codecademy Intro to Vibe Coding) | Short AI-first workflows\[41\] | Fully AI-native | Useful modules; shallow on fundamentals; adult-oriented |

**Assessment:** most established curricula still put a language's syntax at the centre and treat git, testing and deployment as extras (The Odin Project is the exception). The AI-era adaptations so far fall into two camps: *restrict* (CS50, Odin, Hack Club) or *embrace with light scaffolding* (CodeAI, vibe-coding courses). Almost none teach agent supervision, spec writing, or reviewing AI pull requests as core skills.

## Question 4 — Platform comparison for your programme

| Platform | Cost | Age fit | Self-paced | AI tutor quality | Covers blocks |
|---|---|---|---|---|---|
| CS50P / CS50x + Duck | Free | 13+ realistic; university rigour | Yes | Strong, guardrailed | 2, 4, parts of 5 |
| The Odin Project | Free | Mature teens | Yes | None (anti-AI) | 1, 3, 5 |
| freeCodeCamp | Free | Teens OK | Yes | Not verified | 2, 5 |
| Boot.dev | $399/yr | Teens OK; adult tone | Yes, gamified | Hint-based "Boots" | 1, 2, 4, 5 (backend) |
| Khanmigo | $4/mo ($44/yr), US only\[34\] | Designed for K-12 | Yes | Socratic; reviews code | 2, parts of 5 |
| CodeAI AI Foundations | Free | High school | Teacher-led | Embedded tools | 6 (intro) |
| Hack Club | Free | 13–18 exactly | Async community | N/A | 3, 7, 8 (community/peers) |
| GitHub Education + Copilot Student | Free, 13+, verified students\[42\] | Teens OK | — | Agent mode, code review\[42\] | 3, 6 |
| Short vibe-coding courses | Free–low | Adult-oriented | Yes | N/A | 6 |

**Gaps no one covers:** (1) a single modular path from terminal to git to fundamentals to AI agents with placement tests; (2) an AI-licence progression that unlocks generation after comprehension; (3) a teen-legal agentic coding setup with a guardrailed tutor; (4) structured peer code review for self-paced teens; (5) teaching how to verify AI output (specs, tests, review) as a core competency.

## Risks and Caveats

- **Age and terms of service:** Anthropic's consumer Claude terms require users to be 18+, with no parental-consent route. Using a parent's account is a supervision arrangement you choose, not an exemption.\[4\]\[43\] ChatGPT requires 13+ with parental consent for 13–17s and offers parental controls.\[4\]\[44\] GitHub Education and Copilot Student require age 13+ and enrolment in a degree- or diploma-granting programme, including high school or homeschool.\[5\] One secondary source reports that GitHub temporarily paused new sign-ups for some Copilot student plans from April 20, 2026, so check current availability.\[45\] Khanmigo requires US billing.\[34\]
- **Over-reliance and illusion of competence:** this is the central risk. Counter it with AI-off checkpoints, explain-back vivas, and debugging tasks.
- **Motivation drop-off around months 3–5:** counter it with a public commitment, a weekly ritual, Hack Club challenges with real rewards, visible streaks, block celebrations, and a peer.
- **Privacy:** never paste secrets or personal data into AI tools; use school or teen accounts where available.
- **Evidence limits:** the AI-learning RCTs are short-term (single sessions to weeks), and several studied adults or maths rather than teen programming.\[2\] CS50's Duck data is self-reported by the tool's developers. Treat effect sizes as directional.

## Recommendations

1. **Assemble, don't build from scratch.** Use CS50P lectures and problem sets for fundamentals, Odin Foundations for terminal and git, freeCodeCamp or Khan for extra practice, Hack Club for peers and shipping, and GitHub Education for tools.
2. **Build only the thin layer:** a curriculum map (the table above), skip tests per block, an AI-tutor system prompt (Socratic, one step at a time, no full solutions until the right licence level, rate-limited), rubrics, and an explain-back protocol. Store everything in a GitHub repo; the programme itself can be a template repo.
3. **Pick a teen-compliant AI stack:** ChatGPT (with parental consent, Study Mode) or Khanmigo as the tutor; Copilot Student as the agent from Block 6. Use Claude only on a parent's account under supervision, if at all.
4. **Measure understanding, not output:** each block's pass requires (a) tests passing, (b) an AI-off debugging task, and (c) a recorded explanation.
5. **Pilot with one student first,** then 2–3 other teens with different starting profiles, before generalising.
6. **Portfolio over certificates:** the end-of-year outcome should be a GitHub profile with 6–8 repos, merged PRs to others' repos, one deployed app, and a capstone demo video.

## Sources

1. [Valerio Capraro on X: "Generative AI can harm learning. A field experiment published in PNAS randomized nearly 1,000 high-school students across three conditions during mathematics classes: - textbooks and notes only - a standard GPT-4 interface - a safeguarded GPT-4 tutor that provided hints rat… / X](https://x.com/ValerioCapraro/status/2080301862524186943)
2. [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)
3. [Online Learning Statistics 2026: 53 Growth Data Points](https://www.elitecontentmarketer.com/online-education-stats/)
4. [ChatGPT Age Limit 2026: How Old Do You Have to Be?](https://www.heyotto.app/blog/how-old-to-use-chatgpt-ai-age-requirements)
5. [GitHub Copilot for students: what's actually free](https://codemithra.com/github-copilot-for-students-free/)
6. [Without Guardrails, Generative AI Can Harm Education - Knowledge at Wharton](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/)
7. [Harvard Tested a Custom AI Physics Tutor](https://tech.yahoo.com/ai/meta-ai/articles/harvard-tested-custom-ai-physics-151023766.html)
8. <https://www.researchsquare.com/article/rs-4243877/v1.pdf>
9. [(PDF) The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers](https://www.researchgate.net/publication/380935006_The_Widening_Gap_The_Benefits_and_Harms_of_Generative_AI_for_Novice_Programmers)
10. [The Widening Gap - by Kevin Sun - Teaching CS](https://substack.com/home/post/p-145676318)
11. [Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming](https://www.researchgate.net/publication/370203020_Studying_the_effect_of_AI_Code_Generators_on_Supporting_Novice_Learners_in_Introductory_Programming)
12. [How Novices Use LLM-Based Code Generators to Solve CS1 Coding Tasks in a Self-Paced Learning Environment](https://arxiv.org/html/2309.14049v1)
13. [Uncovering MOOC Completion: A Comparative Study of Completion Rates from Different Perspectives](https://openpraxis.org/articles/10.55982/openpraxis.16.3.606)
14. [Syllabus](https://cs50.harvard.edu/syllabus)
15. [Motivation and Mindset](https://www.theodinproject.com/lessons/foundations-motivation-and-mindset)
16. [Free K–12 Curriculum for Computer Science and AI](https://code.org/en-US)
17. [Code.org rebrands as CodeAI, solidifying its shift to AI education](https://www.geekwire.com/2026/solidifying-its-shift-to-ai-education-code-org-rebrands-as-codeai/)
18. [FUTURE — Build the future of your childhood - Hack Club](https://future.hackclub.com/)
19. [Hackcraft: Make a mod, get games and servers! - Hack Club](https://hackcraft.hackclub.com/)
20. [Teaching computer programming with PRIMM: a sociocultural perspective](https://qmro.qmul.ac.uk/xmlui/handle/123456789/57800)
21. [Parsons Problems to Scaffold Code Writing: Impact on Performance and Problem-Solving Efficiency](https://par.nsf.gov/biblio/10510493)
22. [\[PDF\] Solving parsons problems versus fixing and writing code](https://www.semanticscholar.org/paper/Solving-parsons-problems-versus-fixing-and-writing-Ericson-Margulieux/2f1b7c75a3cc2f33fc34575bbe77eeb1f336debc)
23. [\[PDF\] The Gamification of Learning: a Meta-analysis](https://www.semanticscholar.org/paper/The-Gamification-of-Learning:-a-Meta-analysis-Sailer-Homner/be6769b967370c9852210e2fb7a34e499902f814)
24. [Google Scholar](https://scholar.google.com/scholar_lookup?title=The+gamification+of+learning%3A+A+meta-analysis&amp=&author=M+Sailer&amp=&author=L+Homner&amp=&publication_year=2020&amp=&journal=Educational+Psychology+Review&amp=&pages=77-112&amp=&doi=10.1007%2Fs10648-019-09498-w)
25. [Syllabus - CS50](https://cs50.harvard.edu/college/2026/spring/syllabus/)
26. <https://cs.harvard.edu/malan/publications/fp0627-liu.pdf>
27. <https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf>
28. [Grading University Students with LLMs: Performance and Acceptance of a Canvas-Based Automation](https://link.springer.com/chapter/10.1007/978-3-031-99264-3_5)
29. [Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work](https://www.mdpi.com/2504-4990/8/3/74)
30. [Boot.dev Review (2026): Is It Worth It? Price and Verdict](https://onlinecourseing.com/boot-dev-review/)
31. [Best freeCodeCamp Alternatives for Learning to Code \[2026\]](https://scrimba.com/articles/best-freecodecamp-alternatives-for-learning-to-code-2026/)
32. [\[Free Certificates\] freeCodeCamp vs The Odin Project: Best Free Coding Bootcamp in (2026 Updated)](https://opencampushub.com/freecodecamp-vs-odin-project-best-free-coding-2026)
33. [13 Best Codecademy Alternatives in 2026 (Tried and Compared)](https://www.boot.dev/blog/education/code-academy-alternatives)
34. [Khanmigo for learners: Always-available tutor, powered by AI](https://www.khanmigo.ai/learners)
35. [Khanmigo Review & Pricing (2026)](https://toolcurrent.com/tools/khanmigo)
36. [Code.org](https://en.wikipedia.org/wiki/Code.org)
37. [As AI Rewrites the Rules of Coding, Code.org Pushes to Reinvent Itself](https://www.the74million.org/article/as-ai-rewrites-the-rules-of-coding-code-org-pushes-to-reinvent-itself/)
38. [PRIMM: encouraging talk in programming lessons - Raspberry Pi Foundation](https://www.raspberrypi.org/blog/primm-talk-in-programming-lessons-research-seminar/)
39. [Hack Club — Where teens make cool stuff.](https://hackclub.com/)
40. [YSWS Philosophy](https://project.hackclub.com/overview/info/)
41. [12 Best Vibe Coding Courses and Free Ways to Learn in 2026](https://vibeyourwebsite.com/best-vibe-coding-courses/)
42. [GitHub Student Developer Pack: What's Included, Who's Eligible and How to Apply](https://devhunt.org/blog/github-student-pack-essentials)
43. [Claude for Teachers: What Parents Need to Know (2026)](https://www.kidsaitools.com/en/articles/claude-for-teachers-what-parents-need-to-know)
44. [At what age can my child use ChatGPT? All providers compared](https://futurehumankids.com/en/blog/chatgpt-ab-welchem-alter-kind)
45. [GitHub Student Developer Pack 2026](https://truescho.com/en/blog/github-student-developer-pack-copilot-2026)

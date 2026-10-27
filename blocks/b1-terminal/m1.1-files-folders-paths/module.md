---
id: m1.1
block: b1
title: "Files, folders & paths"
status: ready
weeks: [2, 2]
est_sessions: 3
licence_level: L0
competencies:
  - {id: m1.1.c1, text: "Can explain what the terminal and the shell are, and read a command as program + options + arguments"}
  - {id: m1.1.c2, text: "Can describe the file system as a tree (root /, home ~, folders, files) and say where they are with pwd"}
  - {id: m1.1.c3, text: "Can tell absolute from relative paths and use ., .. and ~ correctly"}
  - {id: m1.1.c4, text: "Can navigate with cd and ls (including ls -a for hidden files)"}
  - {id: m1.1.c5, text: "Can create, copy, move, rename and delete files and folders with mkdir, touch, cp, mv and rm, and knows rm has no undo"}
resources:
  - title: "The Odin Project — Command Line Basics"
    url: https://www.theodinproject.com/lessons/foundations-command-line-basics
    role: backbone
    notes: "Read it, and do the commands in the cs50.dev terminal (Linux), not on your own machine's settings. Skip any installation steps: cs50.dev is already set up."
    verified_on: 2026-10-27
  - title: "MIT The Missing Semester — The Shell (2026)"
    url: https://missing.csail.mit.edu/2026/course-shell/
    role: extra
    notes: "For students who want more depth (paths, permissions, pipes). The 2020 edition is still online too."
    verified_on: 2026-10-27
sessions: 3
licence_level: L0
competencies:
  - {id: m1.1.c1, text: "Can explain what the terminal and the shell are, and read a command as program + options + arguments"}
  - {id: m1.1.c2, text: "Can describe the file system as a tree (root /, home ~, folders, files) and say where they are with pwd"}
  - {id: m1.1.c3, text: "Can tell absolute from relative paths and use ., .. and ~ correctly"}
  - {id: m1.1.c4, text: "Can navigate with cd and ls (including ls -a for hidden files)"}
  - {id: m1.1.c5, text: "Can create, copy, move, rename and delete files and folders with mkdir, touch, cp, mv and rm, and knows rm has no undo"}
resources:
  - title: "The Odin Project — Command Line Basics"
    url: https://www.theodinproject.com/lessons/foundations-command-line-basics
    role: backbone
    notes: "Read it, and do the commands in the cs50.dev terminal (Linux), not on your own machine's settings. Skip any installation steps: cs50.dev is already set up."
    verified_on: 2026-10-27
  - title: "MIT The Missing Semester — The Shell (2026)"
    url: https://missing.csail.mit.edu/2026/course-shell/
    role: extra
    notes: "For students who want more depth (paths, permissions, pipes). The 2020 edition is still online too."
    verified_on: 2026-10-27
  - title: "futurecoder — The Shell (first chapter)"
    url: https://futurecoder.io/
    role: optional
    notes: "Despite the name, futurecoder's 'shell' chapter is the Python shell, not the terminal. Useful later in Block 2, not here."
    verified_on: 2026-10-27
sessions:
  - n: 1
    type: reading
    title: "Command Line Basics, part 1: what the terminal is; pwd, ls, cd; the file tree. Predict-the-output checkpoints from the bot"
    where: "The Odin Project + cs50.dev terminal + bot"
    ai: bot-predict
  - n: 2
    type: practice
    title: "Paths drill: absolute vs relative, ., .., ~. Then mkdir, touch, cp, mv, rm in a practice folder"
    where: "cs50.dev terminal + bot"
    ai: bot-L0
    notes: "Work in a scratch folder (mkdir ~/practice). Never practise rm in your repo."
  - n: 3
    type: quiz
    title: "10-minute bot quiz on paths and commands, then the explain-back"
    where: "Telegram (bot)"
    ai: bot-quiz
cs50_fingerprints: []
checks: []
explain_back: true
remix: null
coverage:
  m1.1.c1: ["eb:m1.1.q1", "eb:m1.1.q2"]
  m1.1.c2: ["eb:m1.1.q3", "eb:m1.1.q4"]
  m1.1.c3: ["eb:m1.1.q4", "eb:m1.1.q5", "eb:m1.1.q9"]
  m1.1.c4: ["eb:m1.1.q5", "eb:m1.1.q6", "eb:m1.1.q9"]
  m1.1.c5: ["eb:m1.1.q7", "eb:m1.1.q8"]
skip_gate: {time_box_minutes: 30, ai: "off"}
student_files: []
---
# M1.1 Files, folders & paths

Before you can tell a computer what to do, you need to know where things are. This module is about the **file tree** and **paths**, the addresses of files.

## Sessions
1. **Read and predict.** Work through the first half of The Odin Project's *Command Line Basics* with the cs50.dev terminal open next to it. Every few minutes the bot asks you to predict what a command will show *before* you run it.
2. **Paths drill.** The bot gives you a small folder tree and asks for paths in both forms ("you're in `forest/`; what's the relative path to `river/fish.md`?"). Then create a practice folder and move things around in it.
3. **Quiz + explain-back.**

## Things people trip over
- `cd folder` only works if `folder` is *inside where you are now*. `pwd` tells you where that is.
- `..` means "the folder above". `cd ../..` goes up twice.
- `rm` deletes **for good**: there's no bin. `rm -r` deletes a whole folder. Read twice, press Enter once.
- Spaces in names need quotes: `cd "my folder"`.

## Coverage
| Competency | Checked by |
|---|---|
| c1 Terminal & shell | q1, q2 |
| c2 File tree, pwd | q3, q4 |
| c3 Absolute/relative, . .. ~ | q4, q5, micro-task q9 |
| c4 cd, ls, ls -a | q5, q6, micro-task q9 |
| c5 mkdir/touch/cp/mv/rm | q7, q8 |

There's no remix: the block's artefact is the hunt in M1.2.

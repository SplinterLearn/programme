# Verified facts (checked live 2026-10-27)

Sources for the external facts used in this repo (resources, CS50 fingerprints, tool versions). It's a snapshot: re-check before relying on anything here, and update `verified_on` in the content you change.

Method: pages fetched with curl and WebFetch on 2026-10-27. Where a page is rendered by JavaScript, the source repository was used instead, and that is noted. Quotes are kept short; CS50 problem text is never copied (see [ADR 0018](decisions/0018-public-repo-generic-roles.md)).

## 1. CS50P (CS50's Introduction to Programming with Python)

- Canonical URL: https://cs50.harvard.edu/python/. It returns HTTP 200 with **no redirect** to a year path. Problem set deadline shown: "By 2027-06-30T23:59:00+00:00".
- Lectures: https://cs50.harvard.edu/python/weeks/N/ (page `<title>` in brackets). Notes are at https://cs50.harvard.edu/python/notes/N/.
  - 0 Functions, Variables (title "Week 0 Functions"). https://cs50.harvard.edu/python/weeks/0/
  - 1 Conditionals. https://cs50.harvard.edu/python/weeks/1/
  - 2 Loops. https://cs50.harvard.edu/python/weeks/2/
  - 3 Exceptions. https://cs50.harvard.edu/python/weeks/3/
  - 4 Libraries. https://cs50.harvard.edu/python/weeks/4/
  - 5 Unit Tests. https://cs50.harvard.edu/python/weeks/5/. Uses **pytest**: the notes at https://cs50.harvard.edu/python/notes/5/ show `pytest test_calculator.py` and say "type pip install pytest into your terminal window".
  - 6 File I/O. https://cs50.harvard.edu/python/weeks/6/
  - 7 Regular Expressions. https://cs50.harvard.edu/python/weeks/7/
  - 8 Object-Oriented Programming. https://cs50.harvard.edu/python/weeks/8/
  - 9 Et Cetera. https://cs50.harvard.edu/python/weeks/9/
  - Final Project: https://cs50.harvard.edu/python/project/
- Problem sets index: https://cs50.harvard.edu/python/psets/ (Problem Sets 0 to 8).
- Submission: every problem page shows `check50 cs50/problems/2022/python/<slug>` and `submit50 cs50/problems/2022/python/<slug>`. The slug still contains **2022**. **check50 is used.**
- Pset 0 setup (https://cs50.harvard.edu/python/psets/0/): log in with GitHub and authorize CS50 at submit.cs50.io, then use cs50.dev, then run `update50`.
- Problem URLs follow the pattern https://cs50.harvard.edu/python/psets/N/<slug>/

| PS | Problem | slug / URL suffix | File | Required functions (per spec) | Fingerprint tokens (on page) |
|---|---|---|---|---|---|
| 0 | Indoor Voice | 0/indoor/ | indoor.py | none | HELLO → hello; `.lower` |
| 0 | Playback Speed | 0/playback/ | playback.py | none | `...` (replace spaces) |
| 0 | Making Faces | 0/faces/ | faces.py | **convert** (required) and **main** (required) | `:)`, 🙂, 🙁 |
| 0 | Einstein | 0/einstein/ | einstein.py | none | `300000000`, E = mc |
| 0 | Tip Calculator | 0/tip/ | tip.py | **dollars_to_float**, **percent_to_float**: you implement them inside **given distribution code** (main is provided; you replace the TODOs) | "Leave $" |
| 1 | Deep Thought | 1/deep/ | deep.py | none | 42, forty-two, forty two |
| 1 | Home Federal Savings Bank | 1/bank/ | bank.py | none | hello, $0 / $20 / $100 |
| 1 | File Extensions | 1/extensions/ | extensions.py | none | image/gif, application/pdf, application/octet-stream |
| 1 | Math Interpreter | 1/interpreter/ | interpreter.py | none | `split(" ")`, 1 + 1 → 2.0 |
| 1 | Meal Time | 1/meal/ | meal.py | **convert** (required structure, with main and `if __name__ == "__main__":` so check50 can test convert) | breakfast time, lunch time, dinner time |
| 2 | camelCase | 2/camel/ | camel.py | none | firstName → first_name |
| 2 | Coke Machine | 2/coke/ | coke.py | none | Amount Due, Change Owed, Insert Coin |
| 2 | Just setting up my twttr | 2/twttr/ | twttr.py | none | Twitter → Twttr (vowels removed) |
| 2 | Vanity Plates | 2/plates/ | plates.py | **is_valid(s)** (required structure, with main) | Valid, Invalid, CS50 |
| 2 | Nutrition Facts | 2/nutrition/ | nutrition.py | none | Apple, Calories |
| 3 | Fuel Gauge | 3/fuel/ | fuel.py | none in PS3 | ZeroDivisionError, ValueError, outputs E / F, 3/4 |
| 3 | Felipe's Taqueria | 3/taqueria/ | taqueria.py | none | Baja Taco, Total:, KeyError/EOFError |
| 3 | Grocery List | 3/grocery/ | grocery.py | none | EOFError, control-d, uppercase output |
| 3 | Outdated | 3/outdated/ | outdated.py | none | September, YYYY-MM-DD |
| 4 | Emojize | 4/emojize/ | emojize.py | none | `emoji` module, :thumbs_up:, :1st_place_medal: |
| 4 | Frank, Ian and Glen's Letters | 4/figlet/ | figlet.py | none | pyfiglet, -f / --font, Invalid usage |
| 4 | Adieu, Adieu | 4/adieu/ | adieu.py | none | "Adieu, adieu, to", inflect |
| 4 | Guessing Game | 4/game/ | game.py | none | Level:, Too small!, Too large!, Just right! |
| 4 | Little Professor | 4/professor/ | professor.py | **get_level()** and **generate_integer(level)** (required structure, with main) | EEE, Level:, score out of 10 |
| 4 | Bitcoin Price Index | 4/bitcoin/ | bitcoin.py | none | requests, rest.coincap.io, "Missing command-line argument" |

Later problem sets, for reference (slugs taken from the psets pages):
- PS5: test_twttr, test_bank, test_plates, test_fuel
- PS6: lines, pizza, scourgify, shirt
- PS7: numb3rs, watch, working, um, response
- PS8: seasons, jar, shirtificate

## 2. CS50 academic honesty / AI policy
- URL: https://cs50.harvard.edu/python/honesty/
- Listed as reasonable: "Using CS50's own AI-based software, including the CS50 Duck (ddb) in cs50.ai and cs50.dev."
- Listed as not reasonable: "Using AI-based software other than CS50's own (e.g., ChatGPT, Claude, Copilot, Gemini, et al.) that suggests or completes answers to questions or lines of code."
- Duck URL: https://cs50.ai/ (HTTP 200). The Duck is also available inside https://cs50.dev/.

## 3. cs50.dev
- https://cs50.dev/ is "Visual Studio Code for CS50", described as "CS50's adaptation of Codespaces for students and teachers".
- **GitHub login confirmed:** the Log In form (POST /connect) redirects 302 to `github.com/login/oauth/authorize`.
- The PS0 page (https://cs50.harvard.edu/python/psets/0/) calls it "a cloud-based version of Visual Studio Code" that has everything pre-installed.
- pytest:
  - **Not stated on cs50.dev itself.**
  - The image source does install it: https://github.com/cs50/cli/blob/main/Dockerfile has `pytest` in its `pip3 install` list, and https://github.com/cs50/codespace/blob/main/Dockerfile is `FROM cs50/cli`. So pytest is most likely preinstalled.
  - CS50P notes 5 still tell students to run `pip install pytest`.

## 4. The Odin Project
- Foundations course: https://www.theodinproject.com/paths/foundations/courses/foundations
  - Sections: Introduction, Prerequisites, Git Basics, HTML Foundations, CSS Foundations, Flexbox, JavaScript Basics, Conclusion.
- Command Line Basics: https://www.theodinproject.com/lessons/foundations-command-line-basics (200; title "Command Line Basics")
- Git Basics: https://www.theodinproject.com/lessons/foundations-git-basics (200; title "Git Basics")

## 5. OverTheWire Bandit
- URL: https://overthewire.org/wargames/bandit/
- SSH: host `bandit.labs.overthewire.org`, **port 2220**, user/pass bandit0/bandit0 (https://overthewire.org/wargames/bandit/bandit0.html).
- Page numbering: bandit0.html covers logging in (Level 0). bandit1.html covers Level 0→1. Generally, bandit{N}.html covers Level N-1→N. Level titles are rendered by JS.
- "Commands you may need" on each page:
  - bandit0: ssh
  - bandit1–bandit6 (levels 0→1 … 5→6): ls, cd, cat, file, du, find
  - bandit7 (6→7): ls, cd, cat, file, du, find, grep
  - bandit8 (7→8): man, grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
  - bandit9, bandit10, bandit11 (8→9 … 10→11): grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
- **Yes:** ls, cd, cat, file, find and grep all appear in pages bandit1–bandit11. grep first appears at bandit7.
- Spoiler rule: the Bandit pages don't say it, but the rules page https://overthewire.org/rules/ does:
  - "Do not spoil the game for others."
  - Under "For educators and content-creators": "Do not publish credentials to any of the games."

## 6. MIT Missing Semester
- The **current edition is 2026**, according to the home page https://missing.csail.mit.edu/ (lectures 1/12–1/23/26).
- 2026 shell lecture: https://missing.csail.mit.edu/2026/course-shell/ ("Course Overview + Introduction to the Shell").
- 2020 shell lecture: https://missing.csail.mit.edu/2020/course-shell/ ("Course Overview + The Shell"). It still returns 200.

## 7. futurecoder.io
- https://futurecoder.io/ says "100% Free & Open Source" and "Designed with care for beginners". You run code in an in-site editor and shell, so it is browser-based.
- The course at https://futurecoder.io/course/ is rendered by JS, so its table of contents couldn't be read live. The chapters below come from the source repository: https://github.com/alexmojaki/futurecoder/tree/master/core/chapters
  - The Shell
  - String Basics (IntroducingStrings, AddingStrings)
  - Variables
  - For Loops
  - If Statements (if/else, ==, elif, comparison operators)
  - Lists (IntroducingLists, break, range/len, list methods)
  - A Bit More About Strings (quotes, f-strings)
  - Nested Loops
  - Functions (DefiningFunctions, return, TestingFunctions)
  - Boolean Operators
  - Tic Tac Toe project
  - Dictionaries
- "Types": UNVERIFIED. No dedicated types page was found in the chapter sources.
- The exact display titles of chapters are UNVERIFIED (derived from file and class names).

## 8. freeCodeCamp
- Current curriculum: **"Python Certification"** at https://www.freecodecamp.org/learn/python-v9
  - The name comes from the repo's intro.json.
  - Its page-data includes a "Python Certification Exam".
  - Requirements: complete 5 required projects, then pass the exam.
  - In the repo it is listed under the Core stage.
- Scientific Computing with Python (https://www.freecodecamp.org/learn/scientific-computing-with-python) is now in the **Legacy** stage.
- Source: https://github.com/freeCodeCamp/freeCodeCamp/blob/main/packages/shared/src/config/curriculum.ts

## 9. Jikan API
- Docs: https://docs.api.jikan.moe/. The docs are rendered by Redoc from https://raw.githubusercontent.com/jikan-me/jikan-rest/master/storage/api-docs/api-docs.json, which was parsed directly.
- Base URL: `https://api.jikan.moe/v4`. The project calls itself an "Unofficial MyAnimeList API" and "a free, open-source API".
- API key: none required as far as the spec shows (it has no security scheme, and serves GET-only public data). It says it "does not provide authenticated requests for MyAnimeList". There is no explicit sentence saying "no API key".
- Rate limits: 3 requests/second, 60 requests/minute, daily unlimited. MyAnimeList itself may also rate-limit.
- Endpoints: `/anime/{id}`, `/anime/{id}/full`, `/anime/{id}/episodes`. The episode count is the field **`episodes`** (in the anime schema).
- The live call to https://api.jikan.moe/v4/anime/1 timed out from the build environment (and again from the build server), so the response itself is UNVERIFIED.

## 10. Rosalind
- Python Village: https://rosalind.info/problems/list-view/?location=python-village
  - Problems ini1–ini6: Installing Python; Variables and Some Arithmetic; Strings and Lists; Conditions and Loops; Working with Files; Dictionaries.
  - The home page says "If you don't know anything about programming, you can start at the Python Village".
- "Free": not stated explicitly. https://rosalind.info/about/ says it is "100% community funded" (Patreon), and says the only thing required is an internet connection. No paywall is mentioned. Treat "free" as likely but not explicitly stated.

## 11. CS50x 2026
- https://cs50.harvard.edu/x/ (header "CS50x 2026")
- Week 7 SQL: https://cs50.harvard.edu/x/weeks/7/
- Week 8 HTML, CSS, JavaScript: https://cs50.harvard.edu/x/weeks/8/
- Week 9 Flask: https://cs50.harvard.edu/x/weeks/9/

## 12. GitHub Actions (GitHub releases API)
- actions/checkout: latest is **v7.0.1** (2026-07-20). Major version **v7**. https://github.com/actions/checkout/releases
- actions/setup-python: latest is **v7.1.0** (2026-10-22). Major version **v7**. https://github.com/actions/setup-python/releases

## 13. GitHub account age and noreply email
- Minimum age: 13. Terms of Service §B.3 says "You must be age 13 or older." Some countries set a higher age. https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- Noreply format: `ID+USERNAME@users.noreply.github.com`. Older accounts use `USERNAME@users.noreply.github.com`.
  - The old docs URL redirects to https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address

## 14. CC BY-NC-SA 4.0
- https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.txt returns HTTP 200 with `content-type: text/plain; charset=utf-8`.

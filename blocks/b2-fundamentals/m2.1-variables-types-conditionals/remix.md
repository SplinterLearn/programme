---
module: m2.1
step: 1
---
# M2.1 remix: step 1 of your Block 2 project

**One session (about 1.5–2 h) in your own repo.** Same skills as CS50P lectures 0–1, your topic. This is the *make* step: CS50 covered *use, investigate, modify* with its problem sets.

How it works:
1. When the module starts, your project folder appears in your repo with a **starter file** and `tests/test_m2_1.py`. **Don't edit the tests.**
2. Make a branch (`m2.1-remix`), write the functions so the tests pass, then write `main()`.
3. Run `pytest` (or just push: the PR runs the tests for you). Open a PR and fill in the template.
4. The bot reviews your PR, then `/check` for the explain-back.

Rules of the spec (same for every track):
- **Function names and parameters are fixed**, so the tests can call them.
- **Logic separate from input/output:** the functions only calculate and `return`; `input()` and `print()` live only in `main()`.
- **One edge case is deliberately not tested.** Think about what could go wrong, and handle it or at least mention it in your PR.

---

## Track: finance

**Brief.** *Savings planner.* There's something you want to buy. How many weeks until you can afford it, and how close are you right now?

**Spec** (file `savings.py` in `b2-savings/`):
- `weeks_to_goal(price, saved, per_week) -> int` returns whole weeks, **rounded up**: if any amount is left over, that's one more week. If `saved >= price`, return `0`.
- `verdict(saved, price) -> str` returns `"buy it!"` if `saved >= price`, `"almost there"` if `saved` is at least 80% of `price`, otherwise `"keep saving"`.
- `main()` asks for the price, the amount saved and the amount per week with `input()`, and prints a friendly sentence with an f-string, e.g. *"4 weeks to go. Verdict: keep saving"*.

**Hints, not code:** `//` gives whole divisions, `%` gives what's left over. What type does `input()` give you?

**Stretch goal.** Also print how much you'll have saved by the end of that last week. It can be a bit more than the price: why?

## Track: fandom

**Brief.** *Watchlist planner.* You've got a series to finish. How many days until you're done, and can you binge it this weekend?

**Spec** (file `watchlist.py` in `b2-watchlist/`):
- `days_to_finish(episodes_left, episodes_per_day) -> int` returns whole days, **rounded up**: a partial day still counts as a day. If nothing is left (`episodes_left <= 0`), return `0`.
- `binge_verdict(days) -> str` returns `"already done!"` for `0`, `"binge-able this weekend"` for 1 or 2 days, `"done this week"` for 3 to 7 days, otherwise `"long haul"`.
- `main()` asks for the episodes left and episodes per day with `input()`, and prints a friendly sentence with an f-string, e.g. *"5 days to finish. Verdict: done this week"*.

**Hints, not code:** `//` and `%` again. Does the order of your `elif`s matter?

**Stretch goal.** Also ask for the minutes per episode and print the total watch time in hours and minutes.

## Track: web-social

*Brief only: no automated tests yet. Follow the spec; the review checks it by reading your code.*

**Brief.** *Post scorer.* How well did a post do compared with the account's size?

**Spec** (file `posts.py` in `b2-posts/`):
- `engagement_rate(likes, comments, followers) -> float` returns `(likes + comments)` as a percentage of `followers`, rounded to 1 decimal place.
- `tier(rate) -> str` returns `"viral"` for 10 or more, `"strong"` for 3 or more, `"normal"` for 1 or more, otherwise `"quiet"`.
- `main()` asks for the three numbers and prints the rate and the tier with an f-string.

**Stretch goal.** Add a fifth tier of your own and explain where it goes in the `if`/`elif` chain.

## Track: games

*Brief only: no automated tests yet. Follow the spec; the review checks it by reading your code.*

**Brief.** *First room of a text adventure.* You wake up in a locked room with a door, a window and maybe a key.

**Spec** (file `adventure.py` in `b2-adventure/`):
- `room_outcome(choice, has_key) -> str` returns what happens: for `"door"`, a success message if `has_key` is `True`, otherwise a "the door is locked" message; for `"window"`, a message of your choice; for `"wait"`, another; for anything else, `"Nothing happens."`.
- `main()` asks whether the player picked up the key (`y`/`n`), turns that into a `bool`, asks for a choice, and prints the outcome.

**Stretch goal.** A second item (e.g. a torch) that changes what the window does, using `and`/`or`.

---
module: m2.2
step: 2
---
# M2.2 remix: step 2, add a loop (draft)

Extends your M2.1 file. Keep the M2.1 functions; `tests/test_m2_1.py` must keep passing. TODO(next-task): final spec wording and tests.

## Track: finance

**Brief.** Show the plan week by week, not just the number of weeks.

**Spec sketch** (`savings.py`):
- `balance_after(saved, per_week, week) -> float`: the balance after a given number of weeks. Planned test: `test_running_total`.
- `savings_table(price, saved, per_week) -> str`: one line per week, e.g. `"Week 3: 750"`, up to the week the goal is reached, joined with newlines. Planned test: `test_schedule_lines`.
- `main()` prints the table, then the M2.1 verdict.

## Track: fandom

**Brief.** Plan your watching day by day.

**Spec sketch** (`watchlist.py`):
- `watched_after(episodes_per_day, day, episodes_left) -> int`: episodes watched after a given number of days, never more than `episodes_left`. Planned test: `test_running_total`.
- `schedule(episodes_left, episodes_per_day) -> str`: one line per day, e.g. `"Day 2: episodes 4-6"`, joined with newlines; the last day may have fewer. Planned test: `test_schedule_lines`.
- `main()` prints the schedule, then the M2.1 verdict.

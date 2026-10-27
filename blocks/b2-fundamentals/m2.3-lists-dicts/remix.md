---
module: m2.3
step: 3
---
# M2.3 remix: step 3, many items (draft)

Earlier tests must keep passing. TODO(next-task): final spec wording and tests.

## Track: finance

**Brief.** You're saving for several things. Which first?

**Spec sketch** (`savings.py`): goals are dicts like `{"name": "headphones", "price": 120, "priority": 1}`.
- `add_goal(goals, name, price, priority) -> list` (planned test `test_add_item`)
- `total_needed(goals, saved) -> float` (planned test `test_total`)
- `by_priority(goals) -> list`: highest priority first (planned test `test_order`)
- `main()` collects goals until a blank name, then prints the plan.

## Track: fandom

**Brief.** Your whole watchlist, in the order you should watch it.

**Spec sketch** (`watchlist.py`): shows are dicts like `{"title": "...", "episodes_left": 12, "rating": 8}`.
- `add_show(shows, title, episodes_left, rating) -> list` (planned test `test_add_item`)
- `total_days(shows, episodes_per_day) -> int`, reusing `days_to_finish` (planned test `test_total`)
- `by_rating(shows) -> list`: best first (planned test `test_order`)
- `main()` collects shows until a blank title, then prints the plan.

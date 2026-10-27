---
module: m2.4
step: 4
---
# M2.4 remix: step 4, survive bad input (draft)

Both tracks share this spec: only the prompts differ. TODO(next-task): final wording and tests.

## Track: finance

**Spec sketch** (`savings.py`):
- `parse_amount(text) -> float`: turns text into a number; raises `ValueError` for text that isn't a number (planned test `test_rejects_text`) and for negative amounts (planned test `test_rejects_negative`).
- `ask_amount(prompt) -> float`: keeps asking until `parse_amount` succeeds (uses `input()`, so it isn't unit-tested).
- `main()` uses `ask_amount` for every number.

## Track: fandom

**Spec sketch** (`watchlist.py`):
- `parse_count(text) -> int`: whole numbers only; raises `ValueError` for non-numbers (planned test `test_rejects_text`) and negatives (planned test `test_rejects_negative`).
- `ask_count(prompt) -> int`: keeps asking until valid.
- `main()` uses `ask_count` for every number.

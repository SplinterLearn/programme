# 0009. One growing remix project per block

**Status:** Accepted

## Context
Fresh mini-projects every module give ten disconnected exercises. Changing existing code (including your own) is the most realistic AI-era skill ([architecture 5.4](../design/architecture.md)).

## Decision
- Each module's remix **extends the same block project** (e.g. `b2-savings/`, `b2-watchlist/`). Tests accumulate (`test_m2_1.py`, `test_m2_2.py`, …) and earlier tests must keep passing.
- **Clean checkpoints** (`tracks/<t>/checkpoint/`) are offered for **closed modules only**.
- **Support fades**: spec and tests given (Block 2) → student writes tests (Block 4) → student drafts the spec (Block 5) → a coding agent writes the code and the student reviews it (Block 6+).
- Each remix leaves **one edge case deliberately out of the tests** (`remix.edge_case`). The review and the explain-back ask about it.

## Consequences
- `block.md` declares the project (`project.id`, per-track folders). Modules declare `remix.project_id` and `step`.
- `check_checkpoints.py` proves each checkpoint passes its tests and each starter fails them.

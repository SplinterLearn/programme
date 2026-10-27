# 0017. Starter files and the pytest import convention

**Status:** Accepted

## Context
Tests in `b2-savings/tests/test_m2_1.py` do `from savings import …`. Two problems:
1. If `savings.py` calls `main()` at import time, pytest blocks or fails on `input()`. The `if __name__ == "__main__":` guard isn't taught in CS50P lectures 0–1.
2. pytest's default import mode puts the *test file's* folder on `sys.path`, not the project folder.

## Decision
- The first module of a block project ships a **starter** (`tracks/<t>/starter/`): the main file with function stubs (`...`) and the guard line, commented "leave this line; it's explained later", plus an empty **`conftest.py` at the project root**. pytest's default (`prepend`) import mode then puts the project folder on `sys.path`.
- Later modules extend the student's own file. They ship only new tests.
- `check_checkpoints.py` proves the starter **fails** the tests and the checkpoint **passes** them.

## Consequences
- Students see `if __name__ == "__main__":` before they understand it. M2.5 (libraries/modules) explains it.
- Test file names must be unique across the student repo (`test_m2_1.py`, `test_m2_2.py`, `test_hunt.py`, …), because pytest's default mode can't import two test files with the same basename.

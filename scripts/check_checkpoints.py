#!/usr/bin/env python3
"""Prove that every tested remix and the B1 hunt are passable and not vacuous.

Usage:  python scripts/check_checkpoints.py [-v]

For each module folder under blocks/ and each tracks/<track>/ inside it that
has tests/:
  1. checkpoint/ + tests/  -> pytest must PASS  (the reference solution works)
  2. starter/   + tests/   -> pytest must FAIL  (the tests actually test something)
     (skipped with a note if there is no starter/, e.g. later modules that
     extend the student's own code)

For each module with reference/solve.sh (the terminal hunt):
  3. untouched copy of hunt/          -> pytest must FAIL
  4. hunt/ after running solve.sh     -> pytest must PASS

Each run happens in a fresh temporary folder laid out like the student repo,
so the starter's conftest.py / import convention is exercised too.
Exit code 0 = all good, 1 = at least one failure.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERBOSE = False


def run_pytest(cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--no-header"],
        cwd=cwd, capture_output=True, text=True, timeout=120, stdin=subprocess.DEVNULL,
    )
    return proc.returncode, proc.stdout + proc.stderr


def copy_contents(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.name in ("__pycache__", ".pytest_cache"):
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        else:
            shutil.copy2(item, target)


def stage(track_dir: Path, code_dir: Path, tmp: Path) -> Path:
    """Lay out <project>/ with code files at the root and tests/ inside, like the student repo."""
    project = tmp / "project"
    copy_contents(code_dir, project)
    copy_contents(track_dir / "tests", project / "tests")
    if not (project / "conftest.py").exists():
        # Checkpoints don't carry the starter's conftest.py; the student repo has it.
        starter_conftest = track_dir / "starter" / "conftest.py"
        if starter_conftest.exists():
            shutil.copy2(starter_conftest, project / "conftest.py")
    return project


def check_track(track_dir: Path, failures: list[str]) -> None:
    label = str(track_dir.relative_to(ROOT))
    checkpoint = track_dir / "checkpoint"
    if not checkpoint.is_dir():
        failures.append(f"{label}: tests/ but no checkpoint/")
        return
    with tempfile.TemporaryDirectory() as tmp:
        project = stage(track_dir, checkpoint, Path(tmp))
        code, out = run_pytest(project)
        if code != 0:
            failures.append(f"{label}: checkpoint does NOT pass its tests (exit {code})\n{out}")
        else:
            print(f"ok    {label}: checkpoint passes")
            if VERBOSE:
                print(out)

    starter = track_dir / "starter"
    if not starter.is_dir():
        print(f"note  {label}: no starter/ (module extends the student's code); vacuity check skipped")
        return
    with tempfile.TemporaryDirectory() as tmp:
        project = stage(track_dir, starter, Path(tmp))
        code, out = run_pytest(project)
        if code == 0:
            failures.append(f"{label}: tests PASS against the starter, so they test nothing\n{out}")
        elif code != 1:
            failures.append(f"{label}: pytest errored against the starter (exit {code}); expected plain test failures\n{out}")
        else:
            print(f"ok    {label}: starter fails the tests (as it should)")


def check_hunt(module_dir: Path, failures: list[str]) -> None:
    label = str(module_dir.relative_to(ROOT))
    hunt = module_dir / "hunt"
    solve = module_dir / "reference" / "solve.sh"
    if not hunt.is_dir():
        failures.append(f"{label}: reference/solve.sh but no hunt/")
        return
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "b1-hunt"
        copy_contents(hunt, work)
        code, out = run_pytest(work)
        if code == 0:
            failures.append(f"{label}: hunt tests PASS before solving, so they test nothing\n{out}")
        else:
            print(f"ok    {label}: untouched hunt fails (as it should)")
        proc = subprocess.run(["bash", str(solve)], cwd=work, capture_output=True, text=True, timeout=60)
        if proc.returncode != 0:
            failures.append(f"{label}: solve.sh failed (exit {proc.returncode})\n{proc.stdout}{proc.stderr}")
            return
        code, out = run_pytest(work)
        if code != 0:
            failures.append(f"{label}: hunt tests do NOT pass after solve.sh (exit {code})\n{out}")
        else:
            print(f"ok    {label}: hunt passes after solve.sh")
            if VERBOSE:
                print(out)


def main(argv: list[str]) -> int:
    global VERBOSE
    VERBOSE = "-v" in argv
    failures: list[str] = []
    checked = 0
    for module_dir in sorted((ROOT / "blocks").glob("b*/m*")):
        if not (module_dir / "module.md").is_file():
            continue
        for track_dir in sorted((module_dir / "tracks").glob("*")):
            if (track_dir / "tests").is_dir():
                check_track(track_dir, failures)
                checked += 1
        if (module_dir / "reference" / "solve.sh").is_file():
            check_hunt(module_dir, failures)
            checked += 1
    for f in failures:
        print(f"FAIL  {f}")
    print(f"\n{checked} checked, {len(failures)} failure(s).")
    if checked == 0:
        print("FAIL  nothing to check")
        return 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

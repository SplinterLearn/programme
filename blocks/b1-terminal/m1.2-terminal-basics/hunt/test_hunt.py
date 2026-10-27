"""Checks for the B1 terminal scavenger hunt. Don't edit this file."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
CAMP = HERE / "camp"

MAP_TEXT = 'X marks the spot: somewhere in haystack/.'
RULES_TEXT = "Never write passwords down in the repo."
COMPASS_TEXT = "N, E, S, W"


def read_answers():
    answers = {}
    path = HERE / "answers.txt"
    assert path.is_file(), "answers.txt is missing (task 7)"
    for line in path.read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            answers[key.strip()] = value.strip()
    return answers


def test_camp_folders_exist():
    for folder in ["camp", "camp/tents", "camp/supplies", "camp/supplies/food", "camp/supplies/tools"]:
        assert (HERE / folder).is_dir(), f"folder {folder}/ is missing (task 1)"


def test_map_moved():
    assert (CAMP / "map.txt").is_file(), "camp/map.txt is missing (task 2)"
    assert MAP_TEXT in (CAMP / "map.txt").read_text(), "camp/map.txt isn't the map from start/"
    assert not (HERE / "start" / "map.txt").exists(), "start/map.txt should be gone: move it, don't copy it (task 2)"


def test_rules_copied():
    assert (CAMP / "tents" / "rules.txt").is_file(), "camp/tents/rules.txt is missing (task 3)"
    assert RULES_TEXT in (CAMP / "tents" / "rules.txt").read_text()
    assert (HERE / "start" / "rules.txt").is_file(), "start/rules.txt should still be there: copy it, don't move it (task 3)"


def test_compass_renamed():
    compass = CAMP / "supplies" / "tools" / "compass.txt"
    assert compass.is_file(), "camp/supplies/tools/compass.txt is missing (task 4)"
    assert COMPASS_TEXT in compass.read_text()
    assert not (HERE / "start" / "compass-draft.txt").exists(), "start/compass-draft.txt should be gone (task 4)"


def test_junk_deleted():
    assert not (HERE / "start" / "junk.tmp").exists(), "start/junk.tmp should be deleted (task 5)"


def test_food_list():
    food = CAMP / "supplies" / "food" / "list.txt"
    assert food.is_file(), "camp/supplies/food/list.txt is missing (task 6)"
    lines = [line.strip() for line in food.read_text().splitlines() if line.strip()]
    assert lines == ["apples", "bread", "water"], f"list.txt should be apples, bread, water on three lines; got {lines}"


def test_hidden_file_found():
    answer = read_answers().get("lantern", "").removeprefix("./")
    assert answer, "answers.txt needs a 'lantern:' line (task 7)"
    path = HERE / answer
    assert answer.startswith("haystack/") and path.is_file(), f"{answer!r} isn't a file path starting with haystack/"
    assert path.name.startswith("."), "that file isn't hidden: hidden files start with a dot"


def test_treasure_found():
    answer = read_answers().get("acorn", "").removeprefix("./")
    assert answer, "answers.txt needs an 'acorn:' line (task 7)"
    path = HERE / answer
    assert answer.startswith("haystack/") and path.is_file(), f"{answer!r} isn't a file path starting with haystack/"
    assert "golden acorn" in path.read_text(), "that file doesn't contain 'golden acorn'"


def test_txt_count():
    answer = read_answers().get("txt_count", "")
    expected = len(list((HERE / "haystack").rglob("*.txt")))
    assert answer.isdigit(), "txt_count should be a whole number (task 7)"
    assert int(answer) == expected, "txt_count isn't right: did you include the subfolders?"


def test_camp_absolute_path():
    answer = read_answers().get("camp_path", "")
    assert answer.startswith("/"), "camp_path should be an absolute path: it starts with / (task 7)"
    assert answer.rstrip("/").endswith("/b1-hunt/camp"), "camp_path should end with /b1-hunt/camp"

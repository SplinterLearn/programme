"""M2.1 tests for the watchlist planner. Don't edit this file."""

from watchlist import days_to_finish, binge_verdict


def test_exact_division():
    assert days_to_finish(episodes_left=12, episodes_per_day=3) == 4


def test_rounds_up():
    assert days_to_finish(episodes_left=13, episodes_per_day=3) == 5
    assert days_to_finish(episodes_left=1, episodes_per_day=3) == 1


def test_nothing_left():
    assert days_to_finish(episodes_left=0, episodes_per_day=3) == 0


def test_returns_int():
    assert isinstance(days_to_finish(episodes_left=13, episodes_per_day=3), int)


def test_verdicts():
    assert binge_verdict(0) == "already done!"
    assert binge_verdict(1) == "binge-able this weekend"
    assert binge_verdict(5) == "done this week"
    assert binge_verdict(30) == "long haul"


def test_verdict_boundaries():
    assert binge_verdict(2) == "binge-able this weekend"
    assert binge_verdict(3) == "done this week"
    assert binge_verdict(7) == "done this week"
    assert binge_verdict(8) == "long haul"

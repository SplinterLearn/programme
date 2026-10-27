"""M2.1 tests for the savings planner. Don't edit this file."""

from savings import weeks_to_goal, verdict


def test_exact_division():
    assert weeks_to_goal(price=1000, saved=0, per_week=250) == 4


def test_rounds_up():
    assert weeks_to_goal(price=1000, saved=0, per_week=300) == 4
    assert weeks_to_goal(price=1000, saved=900, per_week=300) == 1


def test_nothing_left():
    assert weeks_to_goal(price=500, saved=600, per_week=100) == 0
    assert weeks_to_goal(price=500, saved=500, per_week=100) == 0


def test_returns_int():
    assert isinstance(weeks_to_goal(price=1000, saved=0, per_week=300), int)


def test_verdicts():
    assert verdict(saved=1000, price=1000) == "buy it!"
    assert verdict(saved=850, price=1000) == "almost there"
    assert verdict(saved=100, price=1000) == "keep saving"


def test_verdict_boundaries():
    assert verdict(saved=1200, price=1000) == "buy it!"
    assert verdict(saved=800, price=1000) == "almost there"
    assert verdict(saved=799, price=1000) == "keep saving"

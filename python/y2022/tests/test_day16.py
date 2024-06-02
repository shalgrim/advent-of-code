import pytest
from y2022.day16_1 import (
    main as main1,
    calc_total_pressure_release,
    StateHistory,
    State,
    build_valves,
)


@pytest.fixture
def tst_input():
    with open("../../../data/2022/test16.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open("../../../data/2022/test16.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_calc_total_pressure_release(tst_input):
    valves = build_valves(tst_input)
    tracker = {"DD": 2, "BB": 5, "JJ": 9, "HH": 17, "EE": 21, "CC": 24}
    state_history = StateHistory([State("CC", tracker)])
    assert calc_total_pressure_release(state_history, valves) == 1651


def test_main1(tst_input, puzzle_input):
    assert main1(tst_input) == 1651
    assert main1(puzzle_input) == 1617


# def test_main2(test_input, puzzle_input):
#     assert main1(test_input) == 1234
#     assert main1(puzzle_input) == 1234

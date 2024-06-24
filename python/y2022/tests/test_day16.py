import pytest
from y2022.day16_1 import (
    main as main1,
    calc_total_pressure_release,
    State,
    build_valves,
)
from y2022.day16_2 import main as main2
from y2022.day16_2 import calc_total_pressure_release as calc_total_pressure_release2
from y2022.day16_2 import State as State2


@pytest.fixture
def tst_input():
    with open("../../../data/2022/test16.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open("../../../data/2022/input16.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_calc_total_pressure_release(tst_input):
    valves = build_valves(tst_input)
    tracker = {"DD": 2, "BB": 5, "JJ": 9, "HH": 17, "EE": 21, "CC": 24}
    state = State("CC", tracker)
    assert calc_total_pressure_release(state, valves) == 1651


def test_main1(tst_input, puzzle_input):
    assert main1(tst_input) == 1651
    assert main1(puzzle_input) == 1617


def test_calc_total_pressure_release2(tst_input):
    valves = build_valves(tst_input)
    tracker = {"DD": 2, "JJ": 3, "BB": 7, "HH": 7, "CC": 9, "EE": 11}
    state = State2(("CC", "EE"), tracker)
    assert calc_total_pressure_release2(state, valves) == 1707


def test_main2(tst_input, puzzle_input):
    assert main2(tst_input) == 1707
    # assert main2(puzzle_input) == 1234

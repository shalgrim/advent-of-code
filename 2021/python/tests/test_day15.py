import pytest
from day15_1 import main as main1, PathFinder
from day15_1 import process_input as process1
from day15_2 import main as main2, method2
from day15_2 import process_input_day2 as process2


@pytest.fixture
def test_input():
    with open('../../data/test15.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open('../../data/input15.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def new_map():
    with open('../../data/test15_new_map.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_main1(test_input, puzzle_input):
    assert main1(test_input) == 40
    assert main1(puzzle_input) == 824


def test_expand_map(test_input, new_map):
    given_new_map = process1(new_map)
    my_new_map = process2(test_input)
    assert given_new_map == my_new_map


def test_method1_on_part2_test_grid(puzzle_input):
    puzzle_grid = process1(puzzle_input)
    pf = PathFinder(puzzle_grid)
    assert pf.find_lowest_risk_path() == 824


def test_method2_on_part1_grids(test_input, puzzle_input):
    test_grid = process1(test_input)
    assert method2(test_grid) == 40
    puzzle_grid = process1(puzzle_input)
    assert method2(puzzle_grid) == 824


def test_main2(test_input):
    assert main2(test_input) == 315

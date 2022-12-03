import pytest
from day12_1 import main as main1
from day12_2 import main as main2


@pytest.fixture
def test_input_1():
    with open('../../data/test12_1.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input_2():
    with open('../../data/test12_2.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open('../../data/input12.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input_1, test_input_2, puzzle_input):
    assert main1(test_input_1) == 10
    assert main1(test_input_2) == 19
    assert main1(puzzle_input) == 4720


def test_part2(test_input_1, test_input_2, puzzle_input):
    assert main2(test_input_1) == 36
    assert main2(test_input_2) == 103
    assert main2(puzzle_input) == 147_848


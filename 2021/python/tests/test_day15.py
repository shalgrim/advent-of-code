import pytest
from day15_1 import main as main1
from day15_2 import main as main2


@pytest.fixture
def test_input():
    with open('../../data/test15.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open('../../data/input15.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_main1(test_input, puzzle_input):
    assert main1(test_input) == 40
    assert main1(puzzle_input) == 824


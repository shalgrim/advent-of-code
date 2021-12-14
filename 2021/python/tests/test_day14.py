import pytest
from day14_1 import main as main1
from day14_2 import main as main2


@pytest.fixture
def test_input():
    with open('../../data/test14.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open('../../data/input14.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_method_1(test_input, puzzle_input):
    assert main1(test_input) == 1588
    assert main1(puzzle_input) == 2874


def test_method_2(test_input):
    assert main2(test_input, 10) == 1588
    assert main2(test_input, 40) == 2188189693529

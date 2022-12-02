import pytest
from day01_1 import main as main1
from day01_2 import main as main2


@pytest.fixture
def puzzle_input():
    with open('../../data/input01.txt') as f:
        return [int(line) for line in f.readlines()]


def test_part_1(puzzle_input):
    assert main1(puzzle_input) == 1400


def test_part_2(puzzle_input):
    assert main2(puzzle_input) == 1429

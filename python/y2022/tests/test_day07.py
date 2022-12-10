import pytest
from y2022.day07_1 import main as main1
from y2022.day07_2 import main as main2


@pytest.fixture
def tst_input():
    with open('../../data/2022/test07.txt') as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def puzzle_input():
    with open('../../data/2022/input07.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_main1(tst_input, puzzle_input):
    assert main1(tst_input) == 95437
    # assert main1(puzzle_input) == 1234


# def test_main2(test_input, puzzle_input):
#     assert main1(test_input) == 1234
#     assert main1(puzzle_input) == 1234

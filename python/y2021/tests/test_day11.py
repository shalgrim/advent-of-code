import pytest
from day11_1 import main as main1


@pytest.fixture
def test_input():
    with open("../../data/test11.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main1(test_input) == 1656


# def test_part_2(test_input):
#     assert main2(puzzle_input) == 1

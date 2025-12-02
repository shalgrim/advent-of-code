import pytest
from y2023.day04_1 import main
from y2023.day04_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test04.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(test_input) == 13


def test_part_2(test_input):
    assert main2(test_input) == 30

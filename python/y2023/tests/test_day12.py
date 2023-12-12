import pytest
from y2023.day12_1 import main
from y2023.day12_1 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test11.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(test_input) == 374


def test_part_2(test_input):
    assert main2(test_input) == 1030

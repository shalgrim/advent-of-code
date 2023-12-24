import pytest
from y2023.day23_1 import main
from y2023.day23_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test23.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(test_input) == 94


def test_part_2(test_input):
    assert main2(test_input) == 6
    assert main2(test_input) == 50

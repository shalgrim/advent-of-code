import pytest
from y2023.day01_1 import main


@pytest.fixture
def test_input():
    with open("../../data/test01.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(test_input) == ""

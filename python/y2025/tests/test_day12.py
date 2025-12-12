import pytest
from y2025.day12_1 import main
from y2025.day12_2 import main as main2


@pytest.fixture
def test_file_12():
    with open("data/2025/test12.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def test_part1(test_file_12):
    assert main(test_file_12) == 2


def test_part2(test_file_12):
    assert main2(test_file_12) == 2

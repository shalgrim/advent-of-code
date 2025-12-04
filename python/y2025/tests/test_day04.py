import pytest
from y2025.day04_1 import main
from y2025.day04_2 import main as main2


@pytest.fixture
def test_file_04():
    with open("data/2025/test04.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part1(test_file_04):
    assert main(test_file_04) == 13


def test_part2(test_file_04):
    assert main2(test_file_04) == 43

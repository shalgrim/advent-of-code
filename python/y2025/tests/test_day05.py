import pytest
from y2025.day05_1 import main
from y2025.day05_2 import main as main2


@pytest.fixture
def test_file_05():
    with open("data/2025/test05.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part1(test_file_05):
    assert main(test_file_05) == 13


def test_part2(test_file_05):
    assert main2(test_file_05) == 43

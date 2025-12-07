import pytest
from y2025.day07_1 import main
from y2025.day07_2 import main as main2


@pytest.fixture
def test_file_07():
    with open("data/2025/test07.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def test_part1(test_file_07):
    assert main(test_file_07) == 21


def test_part2(test_file_07):
    assert main2(test_file_07) == 3263827

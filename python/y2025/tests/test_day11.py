import pytest
from y2025.day11_1 import main
from y2025.day11_2 import main as main2


@pytest.fixture
def test_file_11():
    with open("data/2025/test11.txt") as f:
        return [line.rstrip() for line in f.readlines()]


@pytest.fixture
def test_file_11_2():
    with open("data/2025/test11_2.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def test_part1(test_file_11):
    assert main(test_file_11) == 5


def test_part2(test_file_11_2):
    assert main2(test_file_11_2) == 2

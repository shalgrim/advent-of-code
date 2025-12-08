import pytest
from y2025.day09_1 import main
from y2025.day09_2 import main as main2


@pytest.fixture
def test_file_09():
    with open("data/2025/test09.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def test_part1(test_file_09):
    assert main(test_file_09) == 10


def test_part2(test_file_09):
    assert main2(test_file_09) == 25272

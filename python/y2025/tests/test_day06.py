import pytest
from y2025.day06_1 import main
from y2025.day06_2 import main as main2


@pytest.fixture
def test_file_06():
    with open("data/2025/test06.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def test_part1(test_file_06):
    assert main(test_file_06) == 4277556


def test_part2(test_file_06):
    assert main2(test_file_06) == 3263827

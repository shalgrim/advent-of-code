import pytest

from y2025.day01_1 import main
from y2025.day01_2 import main as main2

@pytest.fixture
def test_file_01():
    with open("data/2025/test01.txt") as f:
        return [line.strip() for line in f.readlines()]

def test_part1(test_file_01):
    assert main(test_file_01) == 3

def test_part2(test_file_01):
    assert main2(test_file_01) == 6

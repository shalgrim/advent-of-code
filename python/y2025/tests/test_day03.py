import pytest
from y2025.day03_1 import main, max_joltage_per_bank
from y2025.day03_2 import main as main2
from y2025.day03_2 import max_joltage_per_bank as max_joltage_2


@pytest.fixture
def test_file_03():
    with open("data/2025/test03.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_max_joltage_per_bank(test_file_03):
    assert max_joltage_per_bank(test_file_03[0]) == 98
    assert max_joltage_per_bank(test_file_03[1]) == 89
    assert max_joltage_per_bank(test_file_03[2]) == 78
    assert max_joltage_per_bank(test_file_03[3]) == 92


def test_part1(test_file_03):
    assert main(test_file_03) == 357


def test_max_joltage_2(test_file_03):
    assert max_joltage_2(test_file_03[0]) == 987654321111
    assert max_joltage_2(test_file_03[1]) == 811111111119
    assert max_joltage_2(test_file_03[2]) == 434234234278
    assert max_joltage_2(test_file_03[3]) == 888911112111


def test_part2(test_file_03):
    assert main2(test_file_03) == 3121910778619

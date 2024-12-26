import pytest

from y2024.day16_1 import main


@pytest.fixture
def test_file16_lines1():
    with open(f"../../../data/2024/test16_1.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_file16_lines2():
    with open(f"../../../data/2024/test16_2.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part1(test_file16_lines1, test_file16_lines2):
    assert main(test_file16_lines1) == 7036
    assert main(test_file16_lines2) == 11048


@pytest.mark.skip(reason="whydoievenhavethis")
def test_part_2(file16_lines):
    assert main(file16_lines) == -1

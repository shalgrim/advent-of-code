import pytest

from y2024.day19_1 import main


@pytest.fixture
def test_file_19_lines():
    with open(f"../../../data/2024/test19.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_file_19_lines):
    assert main(test_file_19_lines) == 6

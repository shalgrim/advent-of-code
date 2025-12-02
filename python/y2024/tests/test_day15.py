import pytest
from y2024.day15_2 import main


@pytest.fixture
def file15_large_lines():
    with open("../../../data/2024/test15_large.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_2(file15_large_lines):
    assert main(file15_large_lines) == 9021

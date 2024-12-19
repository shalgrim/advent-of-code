import pytest

from y2024.day16_1 import main


@pytest.fixture
def file16_lines():
    with open(f"../../../data/2024/test16.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_2(file16_lines):
    assert main(file16_lines) == -1

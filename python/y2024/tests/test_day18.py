import pytest
from y2024.day18_1 import main


@pytest.fixture
def test_file_18_lines():
    with open("../../../data/2024/test18.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_file_18_lines):
    assert main(test_file_18_lines, 6, 12) == 22

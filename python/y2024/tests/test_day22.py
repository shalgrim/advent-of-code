import pytest
from y2024.day22_2 import main as main2
from y2024.day22_2 import price_by_sequence


@pytest.fixture
def test_file_22_lines_2():
    with open(f"../../../data/2024/test22_2.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_price_by_sequence():
    assert price_by_sequence(123, (-1, -1, 0, 2)) == 6
    assert price_by_sequence(1, (-2, 1, -1, 3)) == 7
    assert price_by_sequence(2, (-2, 1, -1, 3)) == 7
    assert price_by_sequence(3, (-2, 1, -1, 3)) == 0
    assert price_by_sequence(2024, (-2, 1, -1, 3)) == 9


def test_part_2(test_file_22_lines_2):
    assert main2(test_file_22_lines_2) == 23

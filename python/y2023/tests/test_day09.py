import pytest
from y2023.day09_1 import get_next_num, main, produce_sub_line
from y2023.day09_2 import get_prev_num
from y2023.day09_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test09.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_produce_sub_line():
    assert produce_sub_line([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]


def test_get_next_num():
    assert get_next_num([0, 3, 6, 9, 12, 15]) == 18


def test_get_prev_num():
    assert get_prev_num([2, 2, 2]) == 2
    assert get_prev_num([0, 2, 4, 6]) == -2
    assert get_prev_num([3, 3, 5, 9, 15]) == 5
    assert get_prev_num([10, 13, 16, 21, 30, 45]) == 5


def test_part_1(test_input):
    assert main(test_input) == 114


def test_part_2(test_input):
    assert main2(test_input) == 2

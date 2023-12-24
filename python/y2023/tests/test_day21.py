import pytest
from y2023.day21_1 import main
from y2023.day21_2 import main as main2


@pytest.fixture
def test_input1():
    with open("../../../data/2023/test21.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input1):
    assert main(test_input1, 6) == 16


def test_part_2(test_input1):
    assert main2(test_input1, 6) == 16
    assert main2(test_input1, 10) == 50
    # assert main2(test_input1, 50) == 1594
    # assert main2(test_input1, 100) == 6536
    # assert main2(test_input1, 500) == 167_004
    # assert main2(test_input1, 1000) == 668_697
    # assert main2(test_input1, 5000) == 16_733_044

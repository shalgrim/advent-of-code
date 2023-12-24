import pytest
from y2023.day22_1 import main
from y2023.day22_2 import main as main2


@pytest.fixture
def test_input1():
    with open("../../../data/2023/test22.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input1):
    assert main(test_input1) == 5


def test_part_2(test_input1):
    assert main2(test_input1) == 16
    assert main2(test_input1) == 50

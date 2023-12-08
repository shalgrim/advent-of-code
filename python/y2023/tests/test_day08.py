import pytest

from y2023.day08_1 import main
from y2023.day08_2 import main as main2

@pytest.fixture
def test_input1():
    with open("../../../data/2023/test08_1.txt") as f:
        return [line.strip() for line in f.readlines()]

@pytest.fixture
def test_input2():
    with open("../../../data/2023/test08_2.txt") as f:
        return [line.strip() for line in f.readlines()]

@pytest.fixture
def test_input3():
    with open("../../../data/2023/test08_3.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input1, test_input2):
    assert main(test_input1) == 2
    assert main(test_input2) == 6


def test_part_2(test_input3):
    assert main2(test_input3) == 6


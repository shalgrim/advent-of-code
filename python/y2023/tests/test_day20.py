import pytest
from y2023.day20_1 import main


@pytest.fixture
def test_input1():
    with open("../../../data/2023/test20_1.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input2():
    with open("../../../data/2023/test20_2.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input1, test_input2):
    assert main(test_input1) == 32000000
    assert main(test_input2) == 11687500

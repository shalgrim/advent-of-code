import pytest
from y2023.day01_1 import main
from y2023.day01_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test01.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input_2():
    with open("../../../data/2023/test01_2.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(test_input) == 142


def test_part_2(test_input_2):
    assert main2(test_input_2) == 281

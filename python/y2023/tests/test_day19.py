import pytest
from y2023.day19_1 import main
from y2023.day19_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test19.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(test_input) == 19_114


def test_part_2(test_input):
    # out of 256_000_000_000_000 (trillion)
    assert main2(test_input) == 167_409_079_868_000

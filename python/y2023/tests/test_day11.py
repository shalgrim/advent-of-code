import pytest
from y2023.day11_1 import main, build_map
from y2023.day11_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test11.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def expected_map():
    with open("../../../data/2023/test11_map.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_build_map(test_input, expected_map):
    assert build_map(test_input) == expected_map


def test_part_1(test_input):
    assert main(test_input) == 374


def test_part_2(test_input):
    assert main2(test_input, 10) == 1030
    assert main2(test_input, 100) == 8410

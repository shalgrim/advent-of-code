import pytest
from y2023.day13_1 import main, score_map
from y2023.day13_2 import main as main2
from y2023.day13_2 import score_map as score_map2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test13.txt") as f:
        return f.read()


@pytest.fixture()
def top_map():
    with open("../../../data/2023/test13_1.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture()
def bottom_map():
    with open("../../../data/2023/test13_2.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_score_map(top_map, bottom_map):
    assert score_map(top_map) == 5
    assert score_map(bottom_map) == 400


def test_part_1(test_input):
    assert main(test_input) == 405


def test_score_map2(top_map, bottom_map):
    assert score_map2(top_map) == 300
    assert score_map2(bottom_map) == 100


def test_part_2(test_input):
    assert main2(test_input) == 400

import pytest
from y2023.day14_1 import Map, main
from y2023.day14_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test14.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def tilted_north():
    with open("../../../data/2023/test14_rolled.txt") as f:
        return f.read().strip()

@pytest.fixture
def cycled_once():
    with open("../../../data/2023/test14_cycled1.txt") as f:
        return f.read().strip()


@pytest.fixture
def cycled_twice():
    with open("../../../data/2023/test14_cycled2.txt") as f:
        return f.read().strip()


@pytest.fixture
def cycled_thrice():
    with open("../../../data/2023/test14_cycled3.txt") as f:
        return f.read().strip()


def test_str(test_input):
    assert str(Map(test_input)) == "\n".join(test_input)


def test_score(tilted_north):
    map = Map(tilted_north.split())
    assert map.score == 136


def test_tilt(test_input, tilted_north):
    map = Map(test_input)
    map.tilt_north()
    assert str(map) == tilted_north


def test_cycle(test_input, cycled_once, cycled_twice, cycled_thrice):
    map = Map(test_input)
    map.cycle()
    assert str(map) == cycled_once
    map.cycle()
    assert str(map) == cycled_twice
    map.cycle()
    assert str(map) == cycled_thrice


def test_part_1(test_input):
    assert main(test_input) == 136


def test_part_2(test_input):
    assert main2(test_input) == 64

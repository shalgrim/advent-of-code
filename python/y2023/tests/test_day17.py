import pytest
from y2023.day17_1 import get_neighbors, main
from y2023.day17_2 import get_neighbors_2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test17.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(["3"], get_neighbors, 3) == 0
    assert main(["35", "33"], get_neighbors, 3) == 6
    assert main(["563", "735", "533"], get_neighbors, 3) == 15
    assert main(["6453", "5563", "7735", "5533"], get_neighbors, 3) == 23
    # assert main(["86887", "86453", "65563", "87735", "55533"]) == "??"  # currently getting 35, is that right?


def test_part_1_full(test_input):
    assert main(test_input, get_neighbors, 3) == 102


def test_part_2(test_input):
    assert main(test_input, get_neighbors_2, 10, 4) == 94


def test_part_2_example_2():
    lines = [
        "111111111111",
        "999999999991",
        "999999999991",
        "999999999991",
        "999999999991",
    ]
    # NEXT: getting 47...which I think is correct, I think AoC is wrong on this on
    # A-ha, no, because it has to end on a length of at least 4, so it's really 71
    assert main(lines, get_neighbors_2, 10, 4) == 71

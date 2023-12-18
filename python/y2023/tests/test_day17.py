import pytest
from y2023.day17_1 import main
from y2023.day17_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test17.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part_1(test_input):
    assert main(["3"]) == 0
    assert main(["35", "33"]) == 6
    assert main(["563", "735", "533"]) == 15
    assert main(["6453", "5563", "7735", "5533"]) == 23
    # assert main(["86887", "86453", "65563", "87735", "55533"]) == "??"  # currently getting 35, is that right?
    assert main(test_input) == 102


def test_part_2(test_input):
    assert main2(test_input) == 64

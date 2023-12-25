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


def test_part_1_full(test_input):
    # NEXT: argh! off by 1, getting 101
    # the only way I can think to debug is to be able to figure out what route it took
    # Well, they should all be within visited, so I should be able to figure it out
    # 12, 12, U, 3 == 101
    # 12, 11, U, 2 == 98 (OK)
    # 12, 10, U, 1 == 93 (OK)
    # There is a 12, 9, U, 1 at 90, but that's wrong because it can't go to 12, 10 and still be U, 1
    # There is a 12, 9, D, 1 at 90, but that's messed up because then I should have a 12, 10, ?, ? at 87
    # And I do have a 12, 10, U, 3 at 87, but again, that's messed up because it well it's obvious
    # So keep trying to track down where this went wrong...I must be getting a wrong neighbor or cost somewhere
    assert main(test_input) == 102


def test_part_2(test_input):
    assert main2(test_input) == 64

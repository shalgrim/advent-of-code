import pytest
from y2023.day15_1 import hash, main
from y2023.day15_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test15.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_hash():
    assert hash("HASH") == 52


def test_part_1():
    assert main("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7") == 1320


def test_part_2(test_input):
    assert main2(test_input) == 64

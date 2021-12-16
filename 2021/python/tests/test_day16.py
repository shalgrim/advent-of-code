import pytest

from day16_1 import convert, calc_version_sum
from day16_2 import main as main2


@pytest.fixture
def puzzle_input():
    with open('../../data/input16.txt') as f:
        return f.read().strip()


def test_calc_version_sum(puzzle_input):
    assert calc_version_sum('8A004A801A8002F478') == 16
    assert calc_version_sum('620080001611562C8802118E34') == 12
    assert calc_version_sum('C0015000016115A2E0802F182340') == 23
    assert calc_version_sum('A0016C880162017C3686B18A3D4780') == 31
    assert calc_version_sum(puzzle_input) == 886


def test_main2():
    assert main2('C200B40A82') == 3

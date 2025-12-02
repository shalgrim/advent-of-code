import pytest
from day16_1 import calc_version_sum
from day16_2 import main as main2


@pytest.fixture
def puzzle_input():
    with open("../../data/input16.txt") as f:
        return f.read().strip()


def test_calc_version_sum(puzzle_input):
    assert calc_version_sum("8A004A801A8002F478") == 16
    assert calc_version_sum("620080001611562C8802118E34") == 12
    assert calc_version_sum("C0015000016115A2E0802F182340") == 23
    assert calc_version_sum("A0016C880162017C3686B18A3D4780") == 31
    assert calc_version_sum(puzzle_input) == 886


def test_main2():
    assert main2("C200B40A82") == 3
    assert main2("04005AC33890") == 54
    assert main2("880086C3E88112") == 7
    assert main2("CE00C43D881120") == 9
    assert main2("D8005AC2A8F0") == 1
    assert main2("F600BC2D8F") == 0
    assert main2("9C005AC2F8F0") == 0
    assert main2("9C0141080250320F1802104A08") == 1

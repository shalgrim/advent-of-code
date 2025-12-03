import pytest
from y2025.day02_1 import invalidate, main
from y2025.day02_2 import MULTI_REPEATED_PATTERN
from y2025.day02_2 import main as main2


@pytest.fixture
def test_file_02():
    with open("data/2025/test02.txt") as f:
        return f.read().strip()


def test_invalidate():
    invalid = [11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859]
    assert all(invalidate(i) for i in invalid)
    assert not any(invalidate(i) for i in range(12, 22))
    assert not any(invalidate(i) for i in range(95, 99))
    assert not any(invalidate(i) for i in range(100, 116))
    assert not any(invalidate(i) for i in range(1698522, 1698529))


def test_invalidate_part2():
    invalid = [
        11,
        22,
        99,
        111,
        999,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
        565656,
        824824824,
        2121212121,
    ]
    assert all(invalidate(i, MULTI_REPEATED_PATTERN) for i in invalid)


def test_part1(test_file_02):
    assert main(test_file_02) == 1227775554


def test_part2(test_file_02):
    assert main2(test_file_02) == 4174379265

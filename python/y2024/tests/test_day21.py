import pytest
from y2024.day21_1 import (
    find_shortest_numeric_pad,
    find_shortest_path_numeric_pad,
)


def test_robot_find_shortest_numeric_pad():
    assert find_shortest_numeric_pad("A", "0") == 1
    assert find_shortest_numeric_pad("0", "2") == 1
    assert find_shortest_numeric_pad("2", "9") == 3
    assert find_shortest_numeric_pad("9", "A") == 3


def test_find_shortest_path_numeric_pad():
    assert find_shortest_path_numeric_pad("029A") == 12

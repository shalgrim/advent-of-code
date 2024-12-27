import pytest
from y2024.day21_1 import (
    find_all_shortest_paths_numeric_pad,
    find_shortest_numeric_pad,
    find_shortest_path_numeric_pad,
    find_all_shortest_paths_numeric_pad_plus_press,
    find_all_shortest_paths_for_code,
)


# @pytest.mark.skip(reason="not ready yet")
def test_find_all_shortest_paths_numeric_pad():
    assert find_all_shortest_paths_numeric_pad("A", "0") == {"<"}
    assert find_all_shortest_paths_numeric_pad("0", "2") == {"^"}
    assert find_all_shortest_paths_numeric_pad("2", "9") == {"^^>", ">^^", "^>^"}
    assert find_all_shortest_paths_numeric_pad("9", "A") == {"vvv"}
    assert find_all_shortest_paths_numeric_pad_plus_press("A", "0") == {"<A"}
    assert find_all_shortest_paths_numeric_pad_plus_press("0", "2") == {"^A"}
    assert find_all_shortest_paths_numeric_pad_plus_press("2", "9") == {
        "^^>A",
        ">^^A",
        "^>^A",
    }
    assert find_all_shortest_paths_numeric_pad_plus_press("9", "A") == {"vvvA"}
    assert find_all_shortest_paths_for_code("029A") == {
        "<A^A>^^AvvvA",
        "<A^A^>^AvvvA",
        "<A^A^^>AvvvA",
    }


def test_robot_find_shortest_numeric_pad():
    assert find_shortest_numeric_pad("A", "0") == 1
    assert find_shortest_numeric_pad("0", "2") == 1
    assert find_shortest_numeric_pad("2", "9") == 3
    assert find_shortest_numeric_pad("9", "A") == 3


def test_find_shortest_path_numeric_pad():
    assert find_shortest_path_numeric_pad("029A") == 12

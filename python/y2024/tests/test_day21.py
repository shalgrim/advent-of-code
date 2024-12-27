import pytest
from y2024.day21_1 import (
    find_all_shortest_paths_numeric_pad,
    find_shortest_numeric_pad,
    find_shortest_path_numeric_pad,
)


# @pytest.mark.skip(reason="not ready yet")
def test_find_all_shortest_paths_numeric_pad():
    assert find_all_shortest_paths_numeric_pad("A", "0") == {"<"}
    assert find_all_shortest_paths_numeric_pad("0", "2") == {"^"}
    assert find_all_shortest_paths_numeric_pad("2", "9") == {"^^>", ">^^", "^>^"}
    assert find_all_shortest_paths_numeric_pad("9", "A") == {"vvv"}
    # Next I have to figure out how to do the pressing
    # And then I can start grouping up the above like
    # assert new_function_that_calls_above_but_also_has_presses_in_it("A", "0"), == {"<", "A"}
    # assert new_function_that_calls_above_but_also_has_presses_in_it("A", "2"), == {"<", "A", "^", "A"}

    # which would build to ...
    # answer = find_all_shortest_paths_numeric_pad("029A")
    # assert len(answer) == 3
    # assert all(
    #     path in answer for path in ["<A^A>^^AvvvA", "<A^A^>^AvvvA", "<A^A^^>AvvvA"]
    # )


def test_robot_find_shortest_numeric_pad():
    assert find_shortest_numeric_pad("A", "0") == 1
    assert find_shortest_numeric_pad("0", "2") == 1
    assert find_shortest_numeric_pad("2", "9") == 3
    assert find_shortest_numeric_pad("9", "A") == 3


def test_find_shortest_path_numeric_pad():
    assert find_shortest_path_numeric_pad("029A") == 12

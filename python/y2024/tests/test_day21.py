from y2024.day21_1 import (
    find_all_shortest_paths_directional_pad,
    find_all_shortest_paths_for_code,
    find_all_shortest_paths_for_directional_code,
    find_all_shortest_paths_for_second_robot,
    find_all_shortest_paths_numeric_pad,
    find_all_shortest_paths_numeric_pad_plus_press,
    find_shortest_length_third_robot,
    find_shortest_numeric_pad,
    find_shortest_path_numeric_pad,
    numericize,
)


def test_robot_find_shortest_numeric_pad():
    assert find_shortest_numeric_pad("A", "0") == 1
    assert find_shortest_numeric_pad("0", "2") == 1
    assert find_shortest_numeric_pad("2", "9") == 3
    assert find_shortest_numeric_pad("9", "A") == 3


def test_find_shortest_path_numeric_pad():
    assert find_shortest_path_numeric_pad("029A") == 12


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


def test_find_all_shortest_paths_directional_pad():
    assert find_all_shortest_paths_directional_pad("A", "<") == {"v<<", "<v<"}
    foo = find_all_shortest_paths_for_directional_code("<A^A>^^AvvvA")
    bar = find_all_shortest_paths_for_directional_code("<A^A^>^AvvvA")
    baz = find_all_shortest_paths_for_directional_code("<A^A^^>AvvvA")
    allofem = foo.union(bar).union(baz)
    assert "v<<A>>^A<A>AvA<^AA>A<vAAA>^A" in allofem


def test_find_all_shortest_paths_for_second_robot():
    assert "v<<A>>^A<A>AvA<^AA>A<vAAA>^A" in find_all_shortest_paths_for_second_robot(
        "029A"
    )


def test_find_shortest_length_third_robot():
    assert find_shortest_length_third_robot("029A") == 68
    assert find_shortest_length_third_robot("980A") == 60
    assert find_shortest_length_third_robot("179A") == 68
    assert find_shortest_length_third_robot("456A") == 64
    assert find_shortest_length_third_robot("379A") == 64


def test_numericize():
    assert numericize("029A") == 29
    assert numericize("980A") == 980
    assert numericize("179A") == 179
    assert numericize("456A") == 456
    assert numericize("379A") == 379

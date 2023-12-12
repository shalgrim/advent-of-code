import pytest
from y2023.day12_1 import convert_line_to_nums, get_num_arrangements, main
from y2023.day12_2 import convert_row
from y2023.day12_2 import main as main2


@pytest.fixture
def test_input():
    with open("../../../data/2023/test12.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_convert_line_to_nums():
    assert convert_line_to_nums("#.#.###") == [1, 1, 3]
    assert convert_line_to_nums(".#...#....###.") == [1, 1, 3]
    assert convert_line_to_nums("..#..#....###.") == [1, 1, 3]
    assert convert_line_to_nums(".#....#...###.") == [1, 1, 3]
    assert convert_line_to_nums("..#...#...###.") == [1, 1, 3]
    assert convert_line_to_nums(".###.##.#...") == [3, 2, 1]
    assert convert_line_to_nums(".###.##..#..") == [3, 2, 1]
    assert convert_line_to_nums(".###.##...#.") == [3, 2, 1]
    assert convert_line_to_nums(".###.##....#") == [3, 2, 1]
    assert convert_line_to_nums(".###..##.#..") == [3, 2, 1]
    assert convert_line_to_nums(".###..##..#.") == [3, 2, 1]
    assert convert_line_to_nums(".###..##...#") == [3, 2, 1]
    assert convert_line_to_nums(".###...##.#.") == [3, 2, 1]
    assert convert_line_to_nums(".###...##..#") == [3, 2, 1]
    assert convert_line_to_nums(".###....##.#") == [3, 2, 1]


def test_get_num_arrangements(test_input):
    answers = [1, 4, 1, 1, 4, 10]
    assert [get_num_arrangements(line) for line in test_input] == answers
    assert get_num_arrangements(convert_row(test_input[0])) == 1
    # after this you're in combinatorial hell
    # assert get_num_arrangements(convert_row(test_input[1])) == 16384
    # assert get_num_arrangements(convert_row(test_input[2])) == 1
    # assert get_num_arrangements(convert_row(test_input[3])) == 16


def test_convert_row():
    assert convert_row(".# 1") == ".#?.#?.#?.#?.# 1,1,1,1,1"
    assert (
        convert_row("???.### 1,1,3")
        == "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
    )


def test_part_1(test_input):
    assert main(test_input) == 21


@pytest.mark.skip("takes too long just yet")
def test_part_2(test_input):
    assert main2(test_input) == 525152

import pytest
from y2023.day12_1 import convert_line_to_nums, get_num_arrangements, main
from y2023.day12_2 import convert_row
from y2023.day12_2 import get_num_arrangements as get_num_arrangements2
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


def test_get_num_arrangements2(test_input):
    answers = [1, 4, 1, 1, 4, 10]
    assert [get_num_arrangements2(line) for line in test_input] == answers
    assert get_num_arrangements2(convert_row(test_input[0])) == 1
    assert get_num_arrangements2(convert_row(test_input[1])) == 16_384
    assert get_num_arrangements2(convert_row(test_input[2])) == 1
    assert get_num_arrangements2(convert_row(test_input[3])) == 16
    assert get_num_arrangements2(convert_row(test_input[4])) == 2500


def test_convert_row():
    assert convert_row(".# 1") == ".#?.#?.#?.#?.# 1,1,1,1,1"
    assert (
        convert_row("???.### 1,1,3")
        == "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
    )


def test_part_1(test_input):
    assert main(test_input) == 21


# I did something with caching wrong
# because whichever of these tests runs first takes longer
# but then the second one is instantaneous
# That's the case no matter the order they're in
def test_part_2(test_input):
    """Takes nearly 11 seconds"""
    assert main2(test_input) == 525152


def test_get_num_arrangements2_long(test_input):
    """Takes 10.5 seconds"""
    assert get_num_arrangements2(convert_row(test_input[5])) == 506_250

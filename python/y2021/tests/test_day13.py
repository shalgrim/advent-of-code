import pytest
from day13_2 import main as main2


@pytest.fixture
def puzzle_input():
    with open("../../data/input13.txt") as f:
        return [line.strip() for line in f.readlines()]


part_2_answer = "\n".join(
    [
        "###..####.#..#.###..#..#.###..#..#.###.",
        "#..#.#....#..#.#..#.#..#.#..#.#.#..#..#",
        "#..#.###..#..#.#..#.#..#.#..#.##...#..#",
        "###..#....#..#.###..#..#.###..#.#..###.",
        "#.#..#....#..#.#....#..#.#....#.#..#.#.",
        "#..#.####..##..#.....##..#....#..#.#..#",
    ]
)


def test_part2(puzzle_input):
    assert main2(puzzle_input) == part_2_answer

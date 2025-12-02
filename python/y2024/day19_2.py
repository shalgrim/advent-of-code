from typing import List

from aoc.io import this_year_day
from y2024.day19_1 import PossibilityChecker, process_input


def main(lines: List[str]):
    options, designs = process_input(lines)
    answer = 0
    pc = PossibilityChecker(options)
    for i, design in enumerate(designs):
        print(f"{i=}")
        if pc.is_possible(design):
            answer += pc.possible_count(design)
    return answer


if __name__ == "__main__":
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

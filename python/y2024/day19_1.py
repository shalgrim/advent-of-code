from functools import cache
from itertools import product

from aoc.io import this_year_day


def process_input(lines):
    options = [option.strip() for option in lines[0].split(",")]
    designs = lines[2:]
    return options, designs


def is_possible(design, options):
    print(f"{design=}")
    # two base cases
    if design in options:
        return True

    for option in options:
        if design.startswith(option):
            if is_possible(design[len(option) :], options):
                return True
            else:
                continue
    return False


class PossibilityChecker:
    def __init__(self, options):
        self.options = options

    @cache
    def is_possible(self, design):
        if design in self.options:
            return True
        for option in (o for o in self.options if design.startswith(o)):
            if self.is_possible(design[len(option) :]):
                return True
        return False


def main(lines):
    options, designs = process_input(lines)
    answer = 0
    pc = PossibilityChecker(options)
    for i, design in enumerate(designs):
        print(f"{i=}")
        if pc.is_possible(design):
            answer += 1
    return answer
    # return sum(is_possible(design, options) for design in designs)


if __name__ == "__main__":
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

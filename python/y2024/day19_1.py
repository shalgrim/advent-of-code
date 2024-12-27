from functools import cache

from aoc.io import this_year_day


def process_input(lines):
    options = [option.strip() for option in lines[0].split(",")]
    designs = lines[2:]
    return options, designs


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

    @cache
    def possible_count(self, design):
        if not design:
            return 1
        answer = 0
        for option in (o for o in self.options if design.startswith(o)):
            answer += self.possible_count(design[len(option) :])
        return answer


def main(lines):
    options, designs = process_input(lines)
    answer = 0
    pc = PossibilityChecker(options)
    for i, design in enumerate(designs):
        print(f"{i=}")
        if pc.is_possible(design):
            answer += pc.possible_count(design)
    return answer


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

from itertools import product

from aoc.io import this_year_day


def process_input(lines):
    options = [option.strip() for option in lines[0].split(",")]
    designs = lines[2:]
    return options, designs


def is_possible(design, options):
    for n in range(1, len(design) + 1):
        for prod in product(options, repeat=n):
            if "".join(prod) == design:
                return True
    return False


def main(lines):
    options, designs = process_input(lines)
    return sum(is_possible(design, options) for design in designs)


if __name__ == "__main__":
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

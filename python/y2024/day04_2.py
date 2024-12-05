from typing import List

from aoc.io import this_year_day


def find_x_mases(lines: List[str], x: int, y: int):
    can_north = y > 0
    can_west = x > 0
    can_east = x + 1 < len(lines[0])
    can_south = y + 1 < len(lines)

    possibilities = []

    if can_west and can_east and can_north and can_south:
        correct = ["M", "S"]
        slash = sorted([lines[y - 1][x - 1], lines[y + 1][x + 1]])
        backslash = sorted([lines[y - 1][x + 1], lines[y + 1][x - 1]])
        if slash == correct and backslash == correct:
            possibilities.append((x, y, "x"))

    return possibilities


def main(lines: List[str]):
    occurrences = []
    for y, line in enumerate(lines):
        x = 0
        while (x := line.find("A", x)) != -1:
            occurrences += find_x_mases(lines, x, y)
            x += 1
    return len(occurrences)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

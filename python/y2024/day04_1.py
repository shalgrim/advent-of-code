from typing import List

from aoc.io import this_year_day


def find_xmases(lines: List[str], x: int, y: int):
    width = len(lines[0])
    height = len(lines)
    can_east = x <= width - 4
    can_west = x >= 3
    can_north = y >= 3
    can_south = y <= height - 4

    possibilities = []
    if can_north:
        possibilities.append(
            "".join([lines[y_prime][x] for y_prime in range(y, y - 4, -1)])
        )
    if can_north and can_east:
        possibilities.append(
            "".join([lines[y - offset][x + offset] for offset in range(4)])
        )
    if can_east:
        possibilities.append("".join([lines[y][x + offset] for offset in range(4)]))
    if can_south and can_east:
        possibilities.append(
            "".join([lines[y + offset][x + offset] for offset in range(4)])
        )
    if can_south:
        possibilities.append("".join([lines[y + offset][x] for offset in range(4)]))
    if can_south and can_west:
        possibilities.append(
            "".join([lines[y + offset][x - offset] for offset in range(4)])
        )
    if can_west:
        possibilities.append("".join([lines[y][x - offset] for offset in range(4)]))
    if can_north and can_west:
        possibilities.append(
            "".join([lines[y - offset][x - offset] for offset in range(4)])
        )

    return [p for p in possibilities if p == "XMAS"]


def main(lines: List[str]):
    occurrences = []
    for y, line in enumerate(lines):
        print(f"{y=}")
        x = 0
        while (x := line.find("X", x)) != -1:
            print(f"{x=}")
            occurrences += find_xmases(lines, x, y)
            x += 1
    return len(occurrences)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

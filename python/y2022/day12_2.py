import math

from y2022.day12_1 import bfs_to_dest, build_grid


def main(lines):
    grid = build_grid(lines)
    all_as = [point for point, height in grid.points.items() if height == ord("a")]
    print(f"{len(all_as)=}")
    shortest = math.inf
    for i, a in enumerate(all_as):
        print(f"{i=}, {a=}")
        answer = bfs_to_dest(grid, a, 391)
        shortest = answer if answer < shortest else shortest
        print(f"{shortest=}")
    return shortest


if __name__ == "__main__":
    with open("../../data/2022/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

import math
import sys
from copy import deepcopy
from datetime import datetime

from day15_1 import PathFinder


def increase_line(line, x):
    return [i + x if i + x <= 9 else i + x - 9 for i in line]
    # return [(i + x) % 10 for i in line]


def process_input_day2(lines):
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])

    original_grid = deepcopy(grid)

    for x in range(1, 5):
        for y, line in enumerate(original_grid):
            new_line = increase_line(line, x)
            grid[y] += new_line

    original_wide_grid = deepcopy(grid)

    for y in range(1, 5):
        for line_index, line in enumerate(original_wide_grid):
            grid.append(increase_line(line, y))

    return grid


def get_neighbors(position: object, grid: object) -> object:
    y, x = position
    neighbors = []
    if y < len(grid) - 1:
        neighbors.append((y + 1, x))
    if x < len(grid[y]) - 1:
        neighbors.append((y, x + 1))
    if y > 0:
        neighbors.append((y - 1, x))
    if x > 0:
        neighbors.append((y, x - 1))
    return neighbors


def method2(grid):
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    shortests = {(max_y, max_x): 0}

    for x in range(max_x - 1, -1, -1):
        shortests[(max_y, x)] = grid[max_y][x + 1] + shortests[(max_y, x + 1)]

    for y in range(max_y - 1, -1, -1):
        shortests[(y, max_x)] = grid[y + 1][max_x] + shortests[(y + 1, max_x)]

    for y in range(max_y - 1, -1, -1):
        for x in range(max_x - 1, -1, -1):
            shortests[(y, x)] = min(
                [
                    shortests[(y + 1, x)] + grid[y + 1][x],
                    shortests[(y, x + 1)] + grid[y][x + 1],
                ]
            )

    return shortests[(0, 0)]


def method3(grid):
    unvisited = {}  # tentative distances stored here
    visited = {}
    source = (0, 0)
    destination = (len(grid) - 1, len(grid[-1]) - 1)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            unvisited[(y, x)] = math.inf

    unvisited[source] = 0
    current = source

    while destination not in visited:
        if len(unvisited) % 1000 == 0:
            print(f"{datetime.utcnow()} {len(unvisited)=}")
        current_distance = unvisited[current]
        neighbors = [n for n in get_neighbors(current, grid) if n not in visited]
        for neighbor in neighbors:
            ny, nx = neighbor
            entry_cost = grid[ny][nx]
            unvisited[neighbor] = min(
                [current_distance + entry_cost, unvisited[neighbor]]
            )
        visited[current] = unvisited[current]
        del unvisited[current]

        if destination in visited:
            break
        current = sorted(
            [(v, k) for k, v in unvisited.items()], key=lambda tpl: tpl[1]
        )[0][1]

    return visited[destination]


def main(lines):
    grid = process_input_day2(lines)
    return method3(grid)
    # return method2(grid)


if __name__ == "__main__":  # 3068 is too high
    with open("../data/input15.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
    grid = process_input_day2(lines)
    pf = PathFinder(grid)
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(2000)
    print(sys.getrecursionlimit())
    print(pf.find_lowest_risk_path())

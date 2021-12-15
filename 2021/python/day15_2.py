from copy import deepcopy

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
        print(x)
        for y, line in enumerate(original_grid):
            new_line = increase_line(line, x)
            grid[y] += new_line

    original_wide_grid = deepcopy(grid)

    for y in range(1, 5):
        for line_index, line in enumerate(original_wide_grid):
            grid.append(increase_line(line, y))

    return grid


def main(lines):
    grid = process_input_day2(lines)
    pf = PathFinder(grid)
    return pf.find_lowest_risk_path()


if __name__ == '__main__':
    with open('../data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

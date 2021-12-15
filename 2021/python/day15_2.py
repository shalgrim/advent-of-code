from copy import deepcopy


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


def main(lines):
    grid = process_input_day2(lines)
    return method2(grid)


if __name__ == '__main__':  # 3068 is too high
    with open('../data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

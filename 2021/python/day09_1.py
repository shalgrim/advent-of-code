def is_low_point(x, y, grid):
    north = 10 if y == 0 else grid[y - 1][x]
    south = 10 if y == len(grid) - 1 else grid[y + 1][x]
    west = 10 if x == 0 else grid[y][x - 1]
    east = 10 if x == len(grid[0]) - 1 else grid[y][x + 1]
    if all([grid[y][x] < direction for direction in [north, south, east, west]]):
        return True
    return False


def get_low_points(grid):
    low_points = set()
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            if is_low_point(x, y, grid):
                low_points.add((x, y))
    return low_points


def main(lines):
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])
    low_points = get_low_points(grid)
    total_risk_level = sum([grid[y][x] + 1 for x, y in low_points])
    return total_risk_level


if __name__ == '__main__':
    with open('../data/input09.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

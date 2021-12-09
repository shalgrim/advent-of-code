from day09_1 import get_low_points


def discover_basin(grid, x, y, discovered=None):
    if discovered is None:
        discovered = set()

    discovered.add((x, y))

    if y > 0 and grid[y - 1][x] != 9 and (x, y - 1) not in discovered:
        discovered.update(discover_basin(grid, x, y - 1, discovered))

    if x < len(grid[0]) - 1 and grid[y][x + 1] != 9 and (x + 1, y) not in discovered:
        discovered.update(discover_basin(grid, x + 1, y, discovered))

    if y < len(grid) - 1 and grid[y + 1][x] != 9 and (x, y + 1) not in discovered:
        discovered.update(discover_basin(grid, x, y + 1, discovered))

    if x > 0 and grid[y][x - 1] != 9 and (x - 1, y) not in discovered:
        discovered.update(discover_basin(grid, x - 1, y, discovered))

    return discovered


def get_basins(grid, low_points):
    basins = {}
    for x, y in low_points:
        basins[(x, y)] = discover_basin(grid, x, y)

    return basins


def main(lines):
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])
    low_points = get_low_points(grid)
    basins = get_basins(grid, low_points)
    basins_sorted_by_size = sorted(
        list(basins.values()), key=lambda x: len(x), reverse=True
    )
    return (
        len(basins_sorted_by_size[0])
        * len(basins_sorted_by_size[1])
        * len(basins_sorted_by_size[2])
    )


if __name__ == '__main__':
    with open('../data/input09.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

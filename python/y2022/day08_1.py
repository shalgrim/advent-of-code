def build_grid(lines):
    grid = []
    for line in lines:
        row = [int(c) for c in line]
        grid.append(row)
    return grid


def main(lines):
    grid = build_grid(lines)

    visible_tree_coordinates = set()

    for y, row in enumerate(grid):
        for x, tree_under_consideration in enumerate(row):
            if all(tree < tree_under_consideration for tree in row[:x]):
                visible_tree_coordinates.add((x, y))
            elif all(tree < tree_under_consideration for tree in row[x+1:]):
                visible_tree_coordinates.add((x, y))
            else:
                trees_above = [row[x] for row in grid[:y]]
                trees_below = [row[x] for row in grid[y+1:]]
                if all(tree < tree_under_consideration for tree in trees_above) or all(tree < tree_under_consideration for tree in trees_below):
                    visible_tree_coordinates.add((x, y))
    return len(visible_tree_coordinates)


if __name__ == '__main__':  # 1820
    with open('../../data/2022/input08.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))

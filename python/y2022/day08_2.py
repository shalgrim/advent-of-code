from y2022.day08_1 import build_grid


def get_scenic_score(x, y, grid):
    tree_under_consideration = grid[y][x]

    left_score = 0
    for i in range(x - 1, -1, -1):
        left_score += 1
        if grid[y][i] >= tree_under_consideration:
            break

    if left_score == 0:
        return 0

    right_score = 0
    for i in range(x + 1, len(grid[y]), 1):
        right_score += 1
        if grid[y][i] >= tree_under_consideration:
            break

    if right_score == 0:
        return 0

    above_score = 0
    for i in range(y - 1, -1, -1):
        above_score += 1
        if grid[i][x] >= tree_under_consideration:
            break

    if above_score == 0:
        return 0

    below_score = 0
    for i in range(y + 1, len(grid), 1):
        below_score += 1
        if grid[i][x] >= tree_under_consideration:
            break

    return left_score * right_score * above_score * below_score


def main(lines):
    grid = build_grid(lines)
    highest_scenic_score = 0

    for y, row in enumerate(lines):
        for x, tree_under_consideration in enumerate(row):
            scenic_score = get_scenic_score(x, y, grid)
            highest_scenic_score = (
                scenic_score
                if scenic_score > highest_scenic_score
                else highest_scenic_score
            )

    return highest_scenic_score


if __name__ == '__main__':
    with open('../../data/2022/input08.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))

import itertools

from y2022.day15_1 import manhattan_distance
from y2023.day11_1 import get_galaxies


class Path:
    def __init__(self, g1, g2):
        self.g1 = g1
        self.g2 = g2
        self.lower_row = min(g1[1], g2[1])
        self.higher_row = max(g1[1], g2[1])
        self.left_column = min(g1[0], g2[0])
        self.right_column = max(g1[0], g2[0])

    def calc_distance(self, empty_rows, empty_columns, expansion):
        crossed_empty_rows = len(
            [er for er in empty_rows if self.lower_row < er < self.higher_row]
        )
        crossed_empty_cols = len(
            [ec for ec in empty_columns if self.left_column < ec < self.right_column]
        )
        self.distance = manhattan_distance(self.g1, self.g2) + expansion * (
            crossed_empty_rows + crossed_empty_cols
        )


def main(lines, expansion=1_000_000):
    empty_rows = {y for y, line in enumerate(lines) if "#" not in line}
    empty_columns = set()
    for x in range(len(lines[0])):
        if all(line[x] == "." for line in lines):
            empty_columns.add(x)

    galaxies = get_galaxies(lines)

    paths = [
        Path(*pair) for pair in itertools.combinations_with_replacement(galaxies, 2)
    ]
    for path in paths:
        path.calc_distance(empty_rows, empty_columns, expansion-1)

    return sum(path.distance for path in paths)


if __name__ == "__main__":
    with open("../../data/2023/input11.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

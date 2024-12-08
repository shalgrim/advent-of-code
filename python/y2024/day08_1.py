import itertools
from collections import defaultdict

from aoc.io import this_year_day


class Map:
    def __init__(self, lines):
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines)
        self.antennae = defaultdict(list)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != ".":
                    self.antennae[char].append((x, y))

    def count_antinode_locations_within_boundary(self) -> int:
        antinode_locations = set()
        for frequency, locations in self.antennae.items():
            for combo in itertools.combinations(locations, 2):
                point1, point2 = combo
                x1, y1 = point1
                x2, y2 = point2
                antinode_1 = x2 + (x2 - x1), y2 + (y2 - y1)
                antinode_2 = x1 + (x1 - x2), y1 + (y1 - y2)
                antinode_locations.add(antinode_1)
                antinode_locations.add(antinode_2)
        within_boundaries = {
            point
            for point in antinode_locations
            if 0 <= point[0] < self.width and 0 <= point[1] < self.height
        }
        return len(within_boundaries)


def main(lines):
    map = Map(lines)
    answer = map.count_antinode_locations_within_boundary()
    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

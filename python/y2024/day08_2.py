import itertools

from aoc.io import this_year_day
from y2024.day08_1 import Map as OldMap


class Map(OldMap):
    def within_boundaries(self, point) -> bool:
        x, y = point
        return 0 <= x < self.width and 0 <= y < self.height

    def count_antinode_locations_within_boundary_resonant(self) -> int:
        antinode_locations = set()
        for frequency, locations in self.antennae.items():
            for combo in itertools.combinations(locations, 2):
                point1, point2 = combo
                x1, y1 = point1
                x2, y2 = point2

                # direction 1
                xdiff = x2 - x1
                ydiff = y2 - y1
                iteration = 0
                while True:
                    new_point = x2 + xdiff * iteration, y2 + ydiff * iteration
                    if self.within_boundaries(new_point):
                        antinode_locations.add(new_point)
                        iteration += 1
                    else:
                        break

                # direction 2
                xdiff = x1 - x2
                ydiff = y1 - y2
                iteration = 0
                while True:
                    new_point = x2 + xdiff * iteration, y2 + ydiff * iteration
                    if self.within_boundaries(new_point):
                        antinode_locations.add(new_point)
                        iteration += 1
                    else:
                        break

        return len(antinode_locations)


def main(lines):
    map = Map(lines)
    answer = map.count_antinode_locations_within_boundary_resonant()
    return answer


if __name__ == "__main__":
    filetype = "input"
    year, day = this_year_day(pad_day=True)
    # with open(f"../../data/{year}/{filetype}{day}.txt") as f:
    # with open(f"../../data/{year}/test08_2.txt") as f:
    # with open(f"../../data/{year}/test08.txt") as f:
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

from copy import deepcopy

from aoc.io import this_year_day
from y2024.day10_1 import Map


class Trail:
    def __init__(self):
        self.path = []

    def __hash__(self):
        return hash(tuple(self.path))

    def move(self, position):
        self.path.append(position)

    @property
    def position(self):
        return self.path[-1]


class Map2(Map):
    def find_distinct_trails(self, trailset, incoming_val):
        if incoming_val == 9:
            return len(trailset)

        new_trailset = set()

        for trail in trailset:
            adjacent = self.adjacent(*trail.position)
            for move in adjacent:
                if move in self.heights[incoming_val + 1]:
                    new_trail = deepcopy(trail)
                    new_trail.move(move)
                    new_trailset.add(new_trail)
        return self.find_distinct_trails(new_trailset, incoming_val + 1)

    def score(self) -> int:
        answer = 0
        for trailhead in self.heights[0]:
            x, y = trailhead
            trail = Trail()
            trail.move((x, y))
            answer += self.find_distinct_trails({trail}, 0)
        return answer


def main(lines):
    map = Map2(lines)
    return map.score()


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

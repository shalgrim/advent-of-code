import itertools
from collections import Counter

from aoc.io import this_year_day
from y2024.day16_1 import manhattan_distance


class Map:
    def __init__(self, lines):
        self.walls = set()
        self.width = len(lines[0])
        self.height = len(lines)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "S":
                    self.start = x, y
                elif char == "E":
                    self.end = x, y
                elif char == "#":
                    self.walls.add((x, y))

    def find_next_move(self):
        potential = set()
        if self.current[0] > 0:
            potential.add((self.current[0] - 1, self.current[1]))
        if self.current[1] > 0:
            potential.add((self.current[0], self.current[1] - 1))
        if self.current[0] < self.width - 1:
            potential.add((self.current[0] + 1, self.current[1]))
        if self.current[1] < self.height - 1:
            potential.add((self.current[0], self.current[1] + 1))

        return potential.difference(self.walls).difference(set(self.route)).pop()

    def establish_route(self):
        self.current = self.start
        self.route = [self.current]

        while self.current != self.end:
            next_move = self.find_next_move()
            self.current = next_move
            self.route.append(self.current)

    def wall_in_between(self, pos1, pos2):
        if pos1[0] == pos2[0]:
            if pos2[1] > pos1[1]:
                if (pos1[0], pos1[1] + 1) in self.walls:
                    return pos1[0], pos1[1] + 1
            else:
                assert pos1[1] > pos2[1]
                if (pos1[0], pos1[1] - 1) in self.walls:
                    return pos1[0], pos1[1] - 1
        elif pos1[1] == pos2[1]:
            assert pos1[1] == pos2[1]
            if pos2[0] > pos1[0]:
                if (pos1[0] + 1, pos1[1]) in self.walls:
                    return pos1[0] + 1, pos1[1]
            else:
                assert pos2[0] < pos1[0]
                if (pos1[0] - 1, pos1[1]) in self.walls:
                    return pos1[0] - 1, pos1[1]
        # Either in above ifs it wasn't in walls or it's diagonal...I don't think this is a real case for our purposes
        return False

    def find_cheats(self):
        cheats = {}
        route_with_indexes = list(enumerate(self.route))
        for combo in itertools.combinations(route_with_indexes, 2):
            if (
                manhattan_distance(combo[0][1], combo[1][1]) == 2
                and combo[1][0] - combo[0][0] > 2
            ):
                if position := self.wall_in_between(combo[0][1], combo[1][1]):
                    cheats[position] = combo[1][0] - combo[0][0] - 2
        return cheats


def main(lines):
    map = Map(lines)
    map.establish_route()
    # Idea: For each combination of points that are a manhattan distance of two apart but are
    # further apart than that in the route, verify there's a wall in between, then remove it,
    # and calculate how long the path would be if you remove the spots between those
    cheats = map.find_cheats()
    for k, v in cheats.items():
        print(k, v)
    cheat_counter = Counter(cheats.values())

    print("COUNTS")
    sorted_cheat_counter = sorted(
        [(k, v) for k, v in cheat_counter.items()], key=lambda x: x[0], reverse=True
    )
    for k, v in sorted_cheat_counter:
        print(k, v)

    return sum(v for k, v in sorted_cheat_counter if k >= 100)


if __name__ == "__main__":  # 1417 is the wrong answer tho it's right for somebody else
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

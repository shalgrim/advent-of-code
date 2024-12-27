import itertools
from collections import Counter

from aoc.io import this_year_day


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


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

    def find_longer_cheats(self, amount_to_save):
        # Oh, look at the example, it doesn't have to be wall-only, just consecutive
        # Ok...I think I know a decent-enough algorithm
        # Start from starting point in route
        # For every spot in route that's amount_to_save spots ahead of you (beware off by one)
        # Check if manhattan distance is <= 20 (beware off by one)
        # If so then time saved is like route distance - manhattan distance of something like that
        # And store that in cheats with the start and end positions and the amount saved

        cheats = {}
        route_with_indexes = list(enumerate(self.route))
        # So now to find cheats you can...
        # Search Space: All coords on route that are manhattan distance between 2 and 20 apart
        # Could also restrict to just those that are 100 or farther apart in the route

        for combo in itertools.combinations(route_with_indexes, 2):
            # Couldn't save enough, don't bother checking
            route_distance = combo[1][0] - combo[0][0]
            if route_distance < amount_to_save:
                continue

            # Don't bother checking if they're farther than 20 apart geographically
            md = manhattan_distance(combo[0][1], combo[1][1])
            if md > 20:
                continue

            cheats[(combo[0][1], combo[1][1])] = route_distance - md

        return cheats


def main(lines):
    map = Map(lines)
    map.establish_route()
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


if __name__ == "__main__":
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

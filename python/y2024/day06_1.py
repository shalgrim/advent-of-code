from enum import Enum

from aoc.io import this_year_day


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Map:
    def __init__(self, lines):
        self.grid = {}
        self.obstacles = set()
        self.guard_position = None
        self.guard_direction = Direction.NORTH
        self.height = len(lines)
        self.width = len(lines[0])
        self.visited = set()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.grid[(x, y)] = char
                if char == "#":
                    self.obstacles.add((x, y))
                elif char == "^":
                    self.guard_position = (x, y)

    def guard_within(self):
        return (
            0 <= self.guard_position[0] < self.width
            and 0 <= self.guard_position[1] < self.height
        )

    @property
    def next_coordinate(self):
        if self.guard_direction == Direction.NORTH:
            return self.guard_position[0], self.guard_position[1] - 1
        elif self.guard_direction == Direction.SOUTH:
            return self.guard_position[0], self.guard_position[1] + 1
        elif self.guard_direction == Direction.EAST:
            return self.guard_position[0] + 1, self.guard_position[1]
        elif self.guard_direction == Direction.WEST:
            return self.guard_position[0] - 1, self.guard_position[1]
        else:
            raise NotImplementedError("This shouldn't happen")

    def turn(self):
        self.guard_direction = Direction((self.guard_direction.value + 1) % 4)

    def move_guard(self):
        self.visited.add(self.guard_position)
        if self.next_coordinate in self.obstacles:
            self.turn()
        else:
            self.guard_position = self.next_coordinate


def main(lines):
    map = Map(lines)
    while map.guard_within():
        map.move_guard()
    return len(map.visited)


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

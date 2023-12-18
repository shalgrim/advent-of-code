from enum import Enum
from typing import List


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Beam:
    processed_states = set()

    def __init__(self, x: int, y: int, direction: Direction, map):
        self.x = x
        self.y = y
        self.direction = direction
        self.map = map

    def can_move(self):
        if self.state in self.processed_states:
            return False
        if self.direction == Direction.RIGHT and self.x == self.map.width - 1:
            return False
        if self.direction == Direction.DOWN and self.y == self.map.height - 1:
            return False
        if self.direction == Direction.UP and self.y == 0:
            return False
        if self.direction == Direction.LEFT and self.x == 0:
            return False
        return True

    def should_turn(self):
        cell = self.map.lines[self.y][self.x]
        return cell in ["/", "\\"]

    def state(self):
        return self.x, self.y, self.direction

    def turn(self):
        cell = self.map.lines[self.y][self.x]
        if self.direction in [Direction.RIGHT, Direction.LEFT]:
            if cell == "/":
                self.turn_ccw()
            elif cell == "\\":
                self.turn_cw()
            else:
                raise RuntimeError("Why am I turning?")
        elif self.direction in [Direction.DOWN, Direction.UP]:
            if cell == "/":
                self.turn_cw()
            elif cell == "\\":
                self.turn_ccw()
            else:
                raise RuntimeError("Why am I turning?")
        else:
            raise RuntimeError("Invalid direction")

    def turn_cw(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def turn_ccw(self):
        self.direction = Direction((self.direction.value + 3) % 4)

    def should_split(self):
        cell = self.map.lines[self.y][self.x]
        if cell == "|" and self.direction in [Direction.RIGHT, Direction.LEFT]:
            return True
        elif cell == "-" and self.direction in [Direction.UP, Direction.DOWN]:
            return True
        return False

    def split(self):
        cell = self.map.lines[self.y][self.x]
        if cell == "|" and self.direction in [Direction.RIGHT, Direction.LEFT]:
            self.direction = Direction.UP
            new_beam = Beam(self.x, self.y, Direction.DOWN, self.map)
            return new_beam
        elif cell == "-" and self.direction in [Direction.UP, Direction.DOWN]:
            self.direction = Direction.RIGHT
            new_beam = Beam(self.x, self.y, Direction.LEFT, self.map)
            return new_beam
        else:
            raise RuntimeError("Why am I splitting")

    def move(self):
        if self.direction == Direction.RIGHT:
            self.x += 1
        elif self.direction == Direction.DOWN:
            self.y += 1
        elif self.direction == Direction.LEFT:
            self.x -= 1
        elif self.direction == Direction.UP:
            self.y -= 1
        else:
            raise RuntimeError("Invalid direction")
        self.processed_states.add(self.state())


class Map:
    def __init__(self, lines: List[str]):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.beams = [Beam(0, 0, Direction.RIGHT, self)]
        if self.beams[0].should_turn():
            self.beams[0].turn()
        self.energized_cells = set((0, 0))

    def move_beams(self):
        new_beams = []
        for beam in self.beams:
            new_beam = self.move_beam(beam)
            if new_beam:
                new_beams.append(new_beam)
        self.beams += new_beams
        self.energized_cells.update({(beam.x, beam.y) for beam in self.beams})

    @property
    def state(self):
        return frozenset(Beam.processed_states)

    def move_beam(self, beam):
        # Set this up so it's always pointing where it needs to go
        # then if it can't move, just leave it
        # if it can move forward, move it forward and when you land on the next step
        # turn it if it should turn and split it if it should split
        if not beam.can_move():
            return None
        beam.move()
        if beam.should_split():
            new_beam = beam.split()
            return new_beam
        if beam.should_turn():
            beam.turn()
            return None


def main(lines):
    map = Map(lines)
    seen_states = set()
    seen_states.add(map.state)
    map.move_beams()

    while map.state not in seen_states:
        seen_states.add(map.state)
        map.move_beams()

    return len(map.energized_cells)


if __name__ == "__main__":  # 7789 is too high
    with open("../../data/2023/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

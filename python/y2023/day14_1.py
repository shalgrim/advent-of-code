def can_roll_north_to(ry, cubes, prev_rolled_to):
    if all(rock[1] > ry for rock in cubes) or not cubes:
        return prev_rolled_to + 1
    for i, rock in enumerate(cubes):
        if rock[1] > ry:
            prev_rock = cubes[i - 1]
            return max(prev_rolled_to, prev_rock[1]) + 1
    else:  # just roll up to last rock
        return max(prev_rolled_to, cubes[-1][1]) + 1


class Map:
    def __init__(self, lines):
        self.lines = lines
        self.rounded = set()
        self.cube = set()
        self.height = len(lines)
        self.width = len(lines[0])
        self._set_rocks()

    @property
    def state(self):
        return frozenset(self.rounded), frozenset(self.cube)

    def _set_rocks(self):
        self.rounded.clear()
        self.cube.clear()
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == "O":
                    self.rounded.add((x, y))
                elif char == "#":
                    self.cube.add((x, y))

    def __str__(self):
        lines = []
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                point = (x, y)
                if point in self.rounded:
                    line += "O"
                elif point in self.cube:
                    line += "#"
                else:
                    line += "."
            lines.append(line)
        return "\n".join(lines)

    def tilt_north(self):
        for column in range(self.width):
            cubes = sorted(
                [rock for rock in self.cube if rock[0] == column],
                key=lambda rock: rock[1],
            )
            rounds = sorted(
                [rock for rock in self.rounded if rock[0] == column],
                key=lambda rock: rock[1],
            )
            prev_rolled_to = -1
            for rx, ry in rounds:
                can_roll_to = can_roll_north_to(ry, cubes, prev_rolled_to)
                self.rounded.remove((rx, ry))
                self.rounded.add((rx, can_roll_to))
                prev_rolled_to = can_roll_to
        self.lines = str(self).split()

    def transpose_cw(self):
        new_lines = []
        for x in range(self.width):
            line = ""
            for y in range(self.height - 1, -1, -1):
                line += self.lines[y][x]
            new_lines.append(line)
        self.lines = new_lines
        self.width, self.height = self.height, self.width
        self._set_rocks()

    def cycle(self):
        for _ in range(4):
            self.tilt_north()
            self.transpose_cw()

    @property
    def score(self):
        answer = 0
        for rock in self.rounded:
            answer += self.height - rock[1]
        return answer


def main(lines):
    map = Map(lines)
    map.tilt_north()
    return map.score


if __name__ == "__main__":
    with open("../../data/2023/input14.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

import functools


class Map:
    def __init__(self, lines):
        self.width = len(lines[0])
        self.height = len(lines)

        walkable_points = set()
        self.start = None
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    continue
                walkable_points.add((x, y))
                if c == "S":
                    self.start = (x, y)

        self.walkable_points = frozenset(walkable_points)

    @functools.cache
    def _reduce_position(self, position):
        x_quotient = position[0] // self.width
        x_remainder = position[0] % self.width
        y_quotient = position[1] // self.height
        y_remainder = position[1] % self.height
        return x_quotient, x_remainder, y_quotient, y_remainder

    @functools.cache
    def _neighborize(self, position):
        x, y = position
        left = x - 1 if x > 0 else self.width - 1
        up = y - 1 if y > 0 else self.height - 1
        right = x + 1 if x < self.width - 1 else 0
        down = y + 1 if y < self.height - 1 else 0
        possibles = {(left, y), (x, down), (right, y), (x, up)}
        return {p for p in possibles if p in self.walkable_points}

    def neighborize(self, current_positions):
        answer = set()
        for position in current_positions:
            x_quotient, x_remainder, y_quotient, y_remainder = self._reduce_position(
                position
            )
            raw_neighbors = self._neighborize((x_remainder, y_remainder))

            # NEXT:
            # I think this might not work if it has to loop around on the left up right down stuff
            # I also haven't considered negatives
            actual_neighbors = [
                self._actualize_neighbor(neighbor, x_quotient, y_quotient)
                for neighbor in raw_neighbors
            ]
            answer.update(set(actual_neighbors))
        return answer

    @functools.cache
    def _actualize_neighbor(self, neighbor, x_quotient, y_quotient):
        return (
            self.width * x_quotient + neighbor[0],
            self.height * y_quotient + neighbor[1],
        )


def main(lines, num_steps):
    map = Map(lines)
    current_nodes = {map.start}

    for _ in range(num_steps):
        neighbors = map.neighborize(frozenset(current_nodes))
        current_nodes = neighbors

    return len(current_nodes)


if __name__ == "__main__":
    with open("../../data/2023/input21.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, 26501365))

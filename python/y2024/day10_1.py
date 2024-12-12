from collections import defaultdict

from aoc.io import this_year_day


class Map:
    def __init__(self, lines):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.heights = defaultdict(list)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.heights[int(char)].append((x, y))

    def adjacent(self, x, y):
        answer = []
        if x > 0:
            answer.append((x - 1, y))
        if x < self.width - 1:
            answer.append((x + 1, y))
        if y > 0:
            answer.append((x, y - 1))
        if y < self.height - 1:
            answer.append((x, y + 1))
        return answer

    def find_reachable_nines(self, established_positions, incoming_val):
        if incoming_val == 9:
            return len(established_positions)
        possible_moves = set()

        for x, y in established_positions:
            adjacent = self.adjacent(x, y)
            possible_moves.update(
                {move for move in adjacent if move in self.heights[incoming_val + 1]}
            )
        return self.find_reachable_nines(possible_moves, incoming_val + 1)

    def score(self) -> int:
        answer = 0
        for trailhead in self.heights[0]:
            x, y = trailhead
            answer += self.find_reachable_nines({(x, y)}, 0)
        return answer


def main(lines):
    map = Map(lines)
    return map.score()


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

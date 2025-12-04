from typing import List

from coding_puzzle_tools import read_input


class Map:
    def __init__(self, lines: List[str]):
        self.height = len(lines)
        self.width = len(lines[0])
        self.paper_rolls = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "@":
                    self.paper_rolls.add((x, y))

    def _get_adjacent_positions(self, x, y):
        answer = set()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (
                    i < 0
                    or j < 0
                    or i > self.width - 1
                    or j > self.height - 1
                    or (i == x and j == y)
                ):
                    continue
                answer.add((i, j))
        return answer

    def is_accessible(self, x: int, y: int) -> bool:
        return (
            len(self.paper_rolls.intersection(self._get_adjacent_positions(x, y))) < 4
        )

    def count_accessible(self) -> int:
        answer = 0
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.paper_rolls and self.is_accessible(x, y):
                    answer += 1
        return answer

    def remove_accessible(self) -> int:
        to_remove = set()
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.paper_rolls:
                    if (x, y) in self.paper_rolls and self.is_accessible(x, y):
                        to_remove.add((x, y))
        self.paper_rolls.difference_update(to_remove)
        return len(to_remove)


def main(lines: List[str]) -> int:
    map = Map(lines)
    return map.count_accessible()


if __name__ == "__main__":
    print(main(read_input()))

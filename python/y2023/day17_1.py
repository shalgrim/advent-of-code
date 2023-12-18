import math
from collections import defaultdict
from copy import copy

from y2023.day16_1 import Direction


class PathSearcher:
    best_from = defaultdict(lambda: math.inf)

    def __init__(self, startx, starty, width, height, cost, costs, path):
        self.x = startx
        self.y = starty
        self.path = path
        self.path.append((startx, starty))
        self.cost = cost
        self.costs = costs
        self.width = width
        self.height = height
        self.target = width - 1, height - 1

    def possible_moves(self):
        answer = []
        if self.x < self.width - 1 and (self.x + 1, self.y) not in self.path:
            if len(self.path) < 4 or not all(
                point[0] == self.x for point in self.path[-4:]
            ):
                answer.append(Direction.RIGHT)
        if self.y < self.height - 1 and (self.x, self.y + 1) not in self.path:
            if len(self.path) < 4 or not all(
                point[1] == self.y for point in self.path[-4:]
            ):
                answer.append(Direction.DOWN)
        if self.y > 0 and (self.x, self.y - 1) not in self.path:
            if len(self.path) < 4 or not all(
                point[1] == self.y for point in self.path[-4:]
            ):
                answer.append(Direction.UP)
        if self.x > 0 and (self.x - 1, self.y) not in self.path:
            if len(self.path) < 4 or not all(
                point[0] == self.x for point in self.path[-4:]
            ):
                answer.append(Direction.LEFT)
        return answer

    def get_next_point(self, direction):
        """Assumes it's safe to move there"""
        if direction == Direction.UP:
            return self.x, self.y - 1
        if direction == Direction.DOWN:
            return self.x, self.y + 1
        if direction == Direction.RIGHT:
            return self.x + 1, self.y
        if direction == Direction.LEFT:
            return self.x - 1, self.y
        raise RuntimeError("Invalid direction")

    def search(self):
        # Am I done?
        if (self.x, self.y) == self.target:
            accumulated_cost = 0
            for step in self.path[::-1]:
                self.best_from[step] = min(accumulated_cost, self.best_from[step])
                accumulated_cost += self.costs[step[1]][
                    step[0]
                ]  # the cost it took to get to this step
            return

        # TODO: make sure I haven't exceeded best_from for the new point
        # Oh no I'm doing this wrong, because `best_from` just stores best _known_
        # I may have to do djikstra or something
        for direction in self.possible_moves():
            newx, newy = self.get_next_point(direction)
            newcost = self.costs[newy][newx] + self.cost
            new_searcher = PathSearcher(
                newx,
                newy,
                self.width,
                self.height,
                newcost,
                self.costs,
                copy(self.path),
            )
            new_searcher.search()


def main(lines):
    costs = []
    for line in lines:
        line_costs = [int(c) for c in line]
        costs.append(line_costs)
    PathSearcher.best_from.clear()
    searcher = PathSearcher(0, 0, len(lines[0]), len(lines), 0, costs, [])
    searcher.search()
    return searcher.best_from[0, 0]


if __name__ == "__main__":
    with open("../../data/2023/input17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

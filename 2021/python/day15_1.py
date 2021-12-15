import math
from copy import copy


def process_input(lines):
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])

    return grid


class PathFinder:
    def __init__(self, grid):
        self.grid = grid
        self.target = (len(grid) - 1, len(grid[-1]) - 1)
        self.shortest_known_path = math.inf

    def get_neighbors(self, position):
        y, x = position
        neighbors = []
        if y < len(self.grid) - 1:
            neighbors.append((y + 1, x))
        if x < len(self.grid[y]) - 1:
            neighbors.append((y, x + 1))
        if y > 0:
            neighbors.append((y-1, x))
        if x > 0:
            neighbors.append((y, x-1))
        return neighbors

    def find_lowest_risk_path(self):
        self._find_lowest_risk_path(position=(0, 0), risk=0, visited=set())
        return self.shortest_known_path

    def _find_lowest_risk_path(self, position, risk, visited):
        if position == self.target:
            if risk < self.shortest_known_path:
                self.shortest_known_path = risk

        if risk >= self.shortest_known_path:
            return

        neighbors = self.get_neighbors(position)
        for neighbor in neighbors:
            y, x = neighbor
            if neighbor in visited:
                continue
            new_risk = self.grid[y][x]
            new_visited = copy(visited)
            new_visited.add(neighbor)
            self._find_lowest_risk_path(neighbor, risk + new_risk, new_visited)


def main(lines):
    grid = process_input(lines)
    pf = PathFinder(grid)
    return pf.find_lowest_risk_path()


if __name__ == '__main__':
    with open('../data/test15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

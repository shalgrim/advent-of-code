import math
from collections import defaultdict
from copy import copy


class Grid:
    def __init__(self):
        self.points = {}
        self.start = None
        self.dest = None

    def possible_moves(self, position):
        my_height = self.points[position]
        moves = []
        for possible_move in [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        ]:
            try:
                if self.points[possible_move] <= my_height + 1:
                    moves.append(possible_move)
            except KeyError:
                pass  # on edge, ignore

        return moves

    def search(self, position, moves, visited):
        visited[position] = moves
        if position == self.dest:
            print(f'reached destination in {moves} moves')
            return moves

        moves_to_destination = []
        for move in self.possible_moves(position):
            if visited[move] > moves + 1:
                new_visited = copy(visited)
                moves_to_destination.append(self.search(move, moves + 1, new_visited))

        if not moves_to_destination:
            return math.inf

        return min(moves_to_destination)


def build_grid(lines):
    grid = Grid()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                grid.points[(x, y)] = ord('a')
                grid.start = (x, y)
            elif char == 'E':
                grid.points[(x, y)] = ord('z')
                grid.dest = (x, y)
            else:
                grid.points[(x, y)] = ord(char)

    grid.width = len(lines[0])
    grid.height = len(lines)
    return grid


def main(lines):
    grid = build_grid(lines)
    visited = defaultdict(lambda: math.inf)
    return grid.search(grid.start, 0, visited)


if __name__ == '__main__':
    with open('../../data/2022/input12.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

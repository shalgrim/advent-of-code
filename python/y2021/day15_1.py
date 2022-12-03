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
        self.shortest_known_path = 3068
        self.shortest_from = {(self.target[0], self.target[1]): 0}

    def get_neighbors(self, position):
        y, x = position
        neighbors = []
        if y < len(self.grid) - 1:
            neighbors.append((y + 1, x))
        if x < len(self.grid[y]) - 1:
            neighbors.append((y, x + 1))
        return neighbors

    def find_lowest_risk_path(self):
        self._find_lowest_risk_path(position=(0, 0), risk=0, visited=[])
        return self.shortest_known_path

    def _find_lowest_risk_path(self, position, risk, visited):
        if position in self.shortest_from:
            if risk + self.shortest_from[position] < self.shortest_known_path:
                self.shortest_known_path = risk + self.shortest_from[position]
            return self.shortest_from[position]

        neighbors = self.get_neighbors(position)
        shortests_from_here = []
        my_risk = self.grid[position[0]][position[1]]
        for neighbor in neighbors:
            y, x = neighbor
            if neighbor in visited:
                continue
            new_risk = self.grid[y][x]
            new_visited = copy(visited)
            new_visited.append(neighbor)
            shortest_from_neighbor = self._find_lowest_risk_path(
                neighbor, risk + new_risk, new_visited
            )
            shortests_from_here.append(shortest_from_neighbor + new_risk)
        answer = min(shortests_from_here)
        self.shortest_from[position] = answer
        return answer


def main(lines):
    grid = process_input(lines)
    pf = PathFinder(grid)
    return pf.find_lowest_risk_path()


if __name__ == '__main__':
    with open('../data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

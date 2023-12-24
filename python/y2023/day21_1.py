import functools
from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    distance: float | int


def build_map(lines):
    walkable_points = set()
    start = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                continue
            walkable_points.add((x, y))
            if c == "S":
                start = (x, y)
    return frozenset(walkable_points), start


def get_neighbors(current_node, unvisited_nodes, lines):
    x = current_node.x
    y = current_node.y
    neighbors = []

    if y > 0 and lines[y - 1][x] != "#":
        neighbors.append(unvisited_nodes.get((x, y - 1)))

    if x > 0 and lines[y][x - 1] != "#":
        neighbors.append(unvisited_nodes.get((x - 1, y)))

    if y < len(lines) - 1 and lines[y + 1][x] != "#":
        neighbors.append(unvisited_nodes.get((x, y + 1)))

    if x < len(lines[0]) - 1 and lines[y][x + 1] != "#":
        neighbors.append(unvisited_nodes.get((x + 1, y)))

    return [neighbor for neighbor in neighbors if neighbor]


@functools.cache
def neighborize_one(position, walkable_positions):
    x, y = position
    possibles = {(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)}
    return {p for p in possibles if p in walkable_positions}


@functools.cache
def neighborize_set(current_positions, walkable_positions):
    answer = set()
    for position in current_positions:
        answer.update(neighborize_one(position, walkable_positions))

    return answer


def main(lines, num_steps):
    walkable, start = build_map(lines)
    current_nodes = {start}

    for _ in range(num_steps):
        neighbors = neighborize_set(frozenset(current_nodes), walkable)
        current_nodes = neighbors

    return len(current_nodes)


if __name__ == "__main__":
    with open("../../data/2023/input21.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, 64))

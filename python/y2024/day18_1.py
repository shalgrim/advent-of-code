import math

from aoc.io import this_year_day


class Node:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance


def get_neighbor_coordinates(current_node, grid_size):
    x, y = current_node.x, current_node.y
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if x < grid_size - 1:
        neighbors.append((x + 1, y))
    if y < grid_size - 1:
        neighbors.append((x, y + 1))

    return neighbors


def main(lines, grid_size, num_to_fall):
    # generator expression 🤔
    coordinates = [(int(x), int(y)) for x, y in (line.split(",") for line in lines)]
    corrupted = set(coordinates[:num_to_fall])
    unvisited_nodes = {
        (x, y): Node(x, y, math.inf)
        for y in range(grid_size)
        for x in range(grid_size)
        if (x, y) not in corrupted
    }
    unvisited_nodes[(0, 0)] = Node(0, 0, 0)

    min_distance = min(node.distance for node in unvisited_nodes.values())
    current_node = [
        node for node in unvisited_nodes.values() if node.distance == min_distance
    ][0]

    while (current_node.x, current_node.y) != (grid_size - 1, grid_size - 1):
        neighbor_coordinates = get_neighbor_coordinates(current_node, grid_size)
        for x, y in neighbor_coordinates:
            node = unvisited_nodes.get((x, y))
            if node is None:
                continue
            node.distance = min(node.distance, current_node.distance + 1)

        # remove current_node from unvisited
        del unvisited_nodes[(current_node.x, current_node.y)]

        try:
            min_distance = min(node.distance for node in unvisited_nodes.values())
        except ValueError as e:
            ...  # what
        if min_distance == math.inf:
            ...  # what
        try:
            current_node = [
                node
                for node in unvisited_nodes.values()
                if node.distance == min_distance
            ][0]
        except IndexError as e:
            ...  # what

    return current_node.distance


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    grid_size = 7 if testing else 71
    num_to_fall = 12 if testing else 1024
    print(main(lines, grid_size, num_to_fall))

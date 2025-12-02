import math
from enum import IntEnum


class Direction(IntEnum):
    E = 0
    S = 1
    W = 2
    N = 3


class Node:
    def __init__(self, x: int, y: int, facing: Direction):
        self.x = x
        self.y = y
        self.facing = facing
        self.distance = math.inf

    def __repr__(self):
        return f"Node: {self.x},{self.y},{self.facing.name}"

    @property
    def location(self):
        return self.x, self.y


def create_nodes(lines):
    nodes = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                continue
            elif char == "E":
                for i in range(4):
                    nodes.append(Node(x, y, Direction(i)))
                target_coords = x, y
            elif char == ".":
                for i in range(4):
                    nodes.append(Node(x, y, Direction(i)))
            elif char == "S":
                start_node = Node(x, y, Direction.E)
                start_node.distance = 0
                nodes.append(start_node)
                for i in range(1, 4):
                    nodes.append(Node(x, y, Direction(i)))
            else:
                raise ValueError("Shouldn't be here")
    return nodes, target_coords


def visit_nodes(all_nodes, target_coords):
    target_keys = {(target_coords[0], target_coords[1], Direction(i)) for i in range(4)}
    unvisited_nodes = {(node.x, node.y, node.facing): node for node in all_nodes}
    min_distance = min(node.distance for node in unvisited_nodes.values())
    current_node = [
        node for node in unvisited_nodes.values() if node.distance == min_distance
    ][0]
    # This is probably going to run too long tho...
    while target_keys.intersection(set(unvisited_nodes.keys())):
        if len(unvisited_nodes) % 1000 == 0:
            print(f"{len(unvisited_nodes)=}")
        if current_node.facing == Direction.E:
            move_coords = (current_node.x + 1, current_node.y)
            turnable_directions = [Direction.N, Direction.S]
        elif current_node.facing == Direction.S:
            move_coords = (current_node.x, current_node.y + 1)
            turnable_directions = [Direction.E, Direction.W]
        elif current_node.facing == Direction.W:
            move_coords = (current_node.x - 1, current_node.y)
            turnable_directions = [Direction.N, Direction.S]
        elif current_node.facing == Direction.N:
            move_coords = (current_node.x, current_node.y - 1)
            turnable_directions = [Direction.E, Direction.W]
        else:
            raise ValueError("Should not be here")

        movable_node = unvisited_nodes.get(
            (move_coords[0], move_coords[1], current_node.facing)
        )
        if movable_node is not None:
            movable_node.distance = min(
                movable_node.distance, current_node.distance + 1
            )

        for direction in turnable_directions:
            turnable_node = unvisited_nodes.get(
                (current_node.x, current_node.y, direction)
            )
            if turnable_node is not None:
                turnable_node.distance = min(
                    turnable_node.distance, current_node.distance + 1000
                )

        # remove current node from unvisited
        del unvisited_nodes[(current_node.x, current_node.y, current_node.facing)]

        # get new current_node
        if not unvisited_nodes:
            break
        min_distance = min(node.distance for node in unvisited_nodes.values())
        current_node = [
            node for node in unvisited_nodes.values() if node.distance == min_distance
        ][0]


def main(lines):
    all_nodes, target_coords = create_nodes(lines)
    visit_nodes(all_nodes, target_coords)
    target_nodes = [node for node in all_nodes if (node.x, node.y) == target_coords]
    return min(node.distance for node in target_nodes)


if __name__ == "__main__":
    with open("../../data/2024/test16_1.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open("../../data/2024/test16_2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    # sys.setrecursionlimit(10000)
    with open("../../data/2024/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
    # year, day = this_year_day(pad_day=True)
    # # testing = False
    # testing = True
    # filetype = "test" if testing else "input"
    # with open(f"../../data/{year}/{filetype}{day}.txt") as f:
    #     lines = [line.strip() for line in f.readlines()]
    # print(main(lines))

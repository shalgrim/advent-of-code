import math
from copy import copy
from dataclasses import dataclass
from typing import List, Set

NUMERIC_PAD = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (1, 3): "0",
    (2, 3): "A",
}

REVERSE_NUMERIC_PAD = {v: k for k, v in NUMERIC_PAD.items()}


@dataclass
class Node:
    x: int
    y: int
    value: str
    distance: int | float = math.inf
    paths: Set[str] = None


def robot1_find_shortest_route(route):
    ...


def get_neighbors(node, unvisited):
    x, y = node.x, node.y
    calcs = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [unvisited.get(calc) for calc in calcs if unvisited.get(calc)]


def directional_character(frum, to):
    fx, fy = frum
    tx, ty = to
    if fx == tx:
        if fy + 1 == ty:
            return "v"
        elif fy - 1 == ty:
            return "^"
    elif fy == ty:
        if fx + 1 == tx:
            return ">"
        elif fx - 1 == tx:
            return "<"
    raise ValueError("Should not be here")


def find_all_shortest_paths_numeric_pad(frum, to):
    """Now to figure out how to track the actual paths"""
    all_nodes = {
        (v[0], v[1]): Node(v[0], v[1], k) for k, v in REVERSE_NUMERIC_PAD.items()
    }
    all_nodes[REVERSE_NUMERIC_PAD[frum]].distance = 0
    unvisited = copy(all_nodes)

    while REVERSE_NUMERIC_PAD[to] in unvisited:
        min_distance = min(node.distance for node in unvisited.values())
        current_node = [
            node for node in unvisited.values() if node.distance == min_distance
        ][0]
        neighbors = get_neighbors(current_node, unvisited)

        for neighbor in neighbors:
            direction = directional_character(
                (current_node.x, current_node.y), (neighbor.x, neighbor.y)
            )
            if current_node.distance + 1 < neighbor.distance:
                neighbor.distance = current_node.distance + 1
                neighbor.paths = (
                    {path + direction for path in current_node.paths}
                    if current_node.paths
                    else {direction}
                )
            elif current_node.distance + 1 == neighbor.distance:
                neighbor.paths.update({path + direction for path in current_node.paths})

        del unvisited[(current_node.x, current_node.y)]

    return all_nodes[REVERSE_NUMERIC_PAD[to]].paths


def find_shortest_path_numeric_pad(code, start="A"):
    return (
        find_shortest_numeric_pad(start, code[0])
        + sum(
            find_shortest_numeric_pad(code[i], code[i + 1])
            for i in range(len(code) - 1)
        )
        + len(code)
    )


def find_shortest_numeric_pad(frum, to):
    all_nodes = {
        (v[0], v[1]): Node(v[0], v[1], k) for k, v in REVERSE_NUMERIC_PAD.items()
    }
    all_nodes[REVERSE_NUMERIC_PAD[frum]].distance = 0
    unvisited = copy(all_nodes)

    while REVERSE_NUMERIC_PAD[to] in unvisited:
        min_distance = min(node.distance for node in unvisited.values())
        current_node = [
            node for node in unvisited.values() if node.distance == min_distance
        ][0]
        neighbors = get_neighbors(current_node, unvisited)

        for neighbor in neighbors:
            neighbor.distance = min(neighbor.distance, current_node.distance + 1)

        del unvisited[(current_node.x, current_node.y)]

    return all_nodes[REVERSE_NUMERIC_PAD[to]].distance

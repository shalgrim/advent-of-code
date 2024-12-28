import itertools
import math
import re
from copy import copy
from dataclasses import dataclass
from datetime import datetime
from functools import cache
from typing import Set

from aoc.io import this_year_day

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

DIRECTIONAL_PAD = {(1, 0): "^", (2, 0): "A", (0, 1): "<", (1, 1): "v", (2, 1): ">"}
REVERSE_DIRECTIONAL_PAD = {v: k for k, v in DIRECTIONAL_PAD.items()}


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


def find_all_shortest_paths_for_code(code):
    paths = find_all_shortest_paths_numeric_pad_plus_press("A", code[0])

    for i in range(len(code) - 1):
        new_paths = find_all_shortest_paths_numeric_pad_plus_press(code[i], code[i + 1])
        paths = {"".join(t) for t in itertools.product(paths, new_paths)}

    return paths


def find_all_shortest_paths_for_directional_code(code):
    paths = find_all_shortest_paths_directional_pad_plus_press("A", code[0])

    for i in range(len(code) - 1):
        new_paths = find_all_shortest_paths_directional_pad_plus_press(
            code[i], code[i + 1]
        )
        paths = {"".join(t) for t in itertools.product(paths, new_paths)}

    return paths


@cache
def find_all_shortest_paths_numeric_pad_plus_press(frum, to):
    return {f"{path}A" for path in find_all_shortest_paths_numeric_pad(frum, to)}


@cache
def find_all_shortest_paths_directional_pad_plus_press(frum, to):
    return {f"{path}A" for path in find_all_shortest_paths_directional_pad(frum, to)}


@cache
def find_all_shortest_paths_directional_pad(frum, to):
    """Maybe I can just reuse the function below but send in a reverse pad argument?"""
    if frum == to:
        return {""}
    all_nodes = {
        (v[0], v[1]): Node(v[0], v[1], k) for k, v in REVERSE_DIRECTIONAL_PAD.items()
    }
    all_nodes[REVERSE_DIRECTIONAL_PAD[frum]].distance = 0
    unvisited = copy(all_nodes)
    while REVERSE_DIRECTIONAL_PAD[to] in unvisited:
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

    return all_nodes[REVERSE_DIRECTIONAL_PAD[to]].paths


@cache
def find_all_shortest_paths_numeric_pad(frum, to):
    """This seems like major overkill"""
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


def find_all_shortest_paths_for_second_robot(code, num_iterations=1):
    first_robot_sez = find_all_shortest_paths_for_code(code)
    these_are_the_codes_to_iterate_on = first_robot_sez

    for i in range(num_iterations):
        print(f"{i=}", datetime.now())
        answer = set()
        for path in these_are_the_codes_to_iterate_on:
            answer.update(find_all_shortest_paths_for_directional_code(path))
        these_are_the_codes_to_iterate_on = answer

    shortest_distance = min(len(a) for a in answer)
    answer = {s for s in answer if len(s) == shortest_distance}
    return answer


def find_shortest_length_third_robot(code):
    """To consider: Is there a possibility that by getting rid of longer ones from second robot I'm missing actual shortest for third?"""
    paths = find_all_shortest_paths_for_second_robot(code, 2)
    shortest_distance = min(len(a) for a in paths)
    return shortest_distance


def numericize(code):
    m = re.search(r"\d+", code)
    return int(m.group())


def complexity(code):
    return find_shortest_length_third_robot(code) * numericize(code)


def main(lines):
    return sum(complexity(line) for line in lines)


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

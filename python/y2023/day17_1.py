import math
from collections import defaultdict
from copy import copy
from dataclasses import dataclass

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
                point[1] == self.y for point in self.path[-4:]
            ):
                answer.append(Direction.RIGHT)
        if self.y < self.height - 1 and (self.x, self.y + 1) not in self.path:
            if len(self.path) < 4 or not all(
                point[0] == self.x for point in self.path[-4:]
            ):
                answer.append(Direction.DOWN)
        if self.y > 0 and (self.x, self.y - 1) not in self.path:
            if len(self.path) < 4 or not all(
                point[0] == self.x for point in self.path[-4:]
            ):
                answer.append(Direction.UP)
        if self.x > 0 and (self.x - 1, self.y) not in self.path:
            if len(self.path) < 4 or not all(
                point[1] == self.y for point in self.path[-4:]
            ):
                answer.append(Direction.LEFT)
        return answer

    def get_next_point(self, direction):
        """Must know it's okay to move there before calling"""
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
        # First, am I done?
        if (self.x, self.y) == self.target:
            accumulated_cost = 0
            for step in self.path[::-1]:
                self.best_from[step] = min(accumulated_cost, self.best_from[step])

                # add in cost it took to get _to_ this step
                accumulated_cost += self.costs[step[1]][step[0]]
            return

        # Second, make sure I haven't exceeded best_from overall
        # TODO: Unfortunately, those are just best _known_ from
        #       So even though I have a best_from from this point, I don't know that it's the best
        #       And there's another assumption that's wrong about trying to do it this shortcut way,
        #       which is just that since I made it in that much cost from this place before I might not
        #       be able to do it that way again because I may have come in from a different route that
        #       prohibits me from going that route forward
        #       Yeah, gonna have to do some kind of Djikstra
        #       But the search space is weird cuz once you get one space out it's not just what space you're on
        #       But how many directions in a row you had to get there
        if self.cost >= self.best_from[(0, 0)]:
            return

        # Third, it's worth continuing to explore
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


@dataclass
class Node:
    x: int
    y: int
    came_from: str
    came_from_num: int
    distance: float | int

    @property
    def key(self):
        return self.x, self.y, self.came_from, self.came_from_num


def build_nodes(width, height, max_in_a_row):
    nodes = {}
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                nodes[(0, 0, "", 0)] = Node(x, y, "", 0, 0)
            else:
                possible_ups = min(y, max_in_a_row)
                possible_downs = min(height - y - 1, max_in_a_row)
                possible_lefts = min(x, max_in_a_row)
                possible_rights = min(width - x - 1, max_in_a_row)

                for i in range(1, possible_downs + 1):
                    node = Node(x, y, "D", i, math.inf)
                    nodes[node.key] = node
                for i in range(1, possible_ups + 1):
                    node = Node(x, y, "U", i, math.inf)
                    nodes[node.key] = node
                for i in range(1, possible_lefts + 1):
                    node = Node(x, y, "L", i, math.inf)
                    nodes[node.key] = node
                for i in range(1, possible_rights + 1):
                    node = Node(x, y, "R", i, math.inf)
                    nodes[node.key] = node
    return nodes


def get_neighbors(node, nodes):
    answer = []

    # get right neighbor
    if node.came_from == "R":
        key = None
    elif node.came_from == "L":
        if node.came_from_num < 3:
            key = (node.x + 1, node.y, "L", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x + 1, node.y, "L", 1)
    answer.append(nodes.get(key))

    # get down neighbor
    if node.came_from == "D":
        key = None
    elif node.came_from == "U":
        if node.came_from_num < 3:
            key = (node.x, node.y + 1, "U", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x, node.y + 1, "U", 1)
    answer.append(nodes.get(key))

    # get left neighbor
    if node.came_from == "L":
        key = None
    elif node.came_from == "R":
        if node.came_from_num < 3 and node.x > 0:
            key = (node.x - 1, node.y, "R", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x - 1, node.y, "R", 1)
    answer.append(nodes.get(key))

    # get up neighbor
    if node.came_from == "U":
        key = None
    elif node.came_from == "D":
        if node.came_from_num < 3 and node.y > 0:
            key = (node.x, node.y - 1, "D", node.came_from_num + 1)
        else:
            key = None
    else:
        key = (node.x, node.y - 1, "D", 1)
    answer.append(nodes.get(key))

    return [a for a in answer if a]  # remove Nones


def finished(unvisited_nodes, target_keys):
    if not unvisited_nodes:
        return True
    if not set(unvisited_nodes.keys()).intersection(target_keys):
        return True
    if min(node.distance for node in unvisited_nodes.values()) == math.inf:
        return True
    return False


def main(lines, neighbor_algorithm, max_in_a_row):
    costs = build_costs(lines)
    unvisited_nodes = build_nodes(len(lines[0]), len(lines), max_in_a_row)
    visited_nodes = {}
    current_node = unvisited_nodes[(0, 0, "", 0)]
    target_keys = {
        key
        for key in unvisited_nodes.keys()
        if key[0] == len(lines[0]) - 1 and key[1] == len(lines) - 1
    }
    for neighbor in neighbor_algorithm(current_node, unvisited_nodes):
        cost = costs[neighbor.y][neighbor.x]
        neighbor.distance = min(neighbor.distance, current_node.distance + cost)
    visited_nodes[current_node.key] = current_node
    del unvisited_nodes[current_node.key]

    print(f"{len(unvisited_nodes)=}")
    while not finished(unvisited_nodes, target_keys):
        if len(visited_nodes) % 100 == 0:
            print(f"{len(visited_nodes)=}")
        min_distance = min(node.distance for node in unvisited_nodes.values())
        possible_next_current = [
            node for node in unvisited_nodes.values() if node.distance == min_distance
        ]
        # TODO: check for an empty list, though that should be not possible if I do my termination correction
        current_node = possible_next_current[0]
        # print(current_node)
        for neighbor in neighbor_algorithm(current_node, unvisited_nodes):
            cost = costs[neighbor.y][neighbor.x]
            neighbor.distance = min(neighbor.distance, current_node.distance + cost)
        visited_nodes[current_node.key] = current_node
        del unvisited_nodes[current_node.key]

    target_nodes = [visited_nodes.get(key) for key in target_keys]
    target_nodes = [node for node in target_nodes if node]
    return min(node.distance for node in target_nodes)

    ## new djikstra stuff ^^
    ## old stuff vvv
    # PathSearcher.best_from.clear()
    # searcher = PathSearcher(0, 0, len(lines[0]), len(lines), 0, costs, [])
    # searcher.search()
    # return searcher.best_from[0, 0]


def build_costs(lines):
    costs = []
    for line in lines:
        line_costs = [int(c) for c in line]
        costs.append(line_costs)
    return costs


if __name__ == "__main__":
    # TODO: This takes about an hour or two...
    # I assume I'm spending all my time in `get_neighbors`
    # and caching wouldn't help there
    # maybe pattern matching would be faster?
    # And you might want to re-run to see if it still is correct after re-factoring
    with open("../../data/2023/input17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines), get_neighbors, 3)

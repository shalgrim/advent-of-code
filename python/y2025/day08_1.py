import math
from itertools import combinations
from typing import Any

from coding_puzzle_tools import read_input


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def straight_line_distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def get_points(lines: list[str]) -> list[Point]:
    string_coordinates = [line.split(",") for line in lines]
    coordinates = [(int(sc[0]), int(sc[1]), int(sc[2])) for sc in string_coordinates]
    points = [Point(*coord) for coord in coordinates]
    return points


def get_sorted_distances(indexed_points: dict[int, Point]) -> list[tuple[Any, Any]]:
    distances = {}

    for combo_key in combinations(indexed_points.keys(), 2):
        point1 = indexed_points[combo_key[0]]
        point2 = indexed_points[combo_key[1]]
        distances[combo_key] = straight_line_distance(point1, point2)

    # now sort combos by distances
    sorted_distances = sorted([(value, key) for key, value in distances.items()])
    return sorted_distances


def main(lines: list[str], *, num_pairs=1000) -> int:
    points = get_points(lines)
    indexed_points = {i: point for i, point in enumerate(points)}
    sorted_distances = get_sorted_distances(indexed_points)
    distances_of_note = sorted_distances[:num_pairs]

    groupings = {index: {index} for index in indexed_points.keys()}

    for don in distances_of_note:
        index1, index2 = don[1]

        if groupings[index1] is not groupings[index2]:
            new_grouping = groupings[index1].union(groupings[index2])
            for index in new_grouping:
                groupings[index] = new_grouping

    biggest_groupings = []
    while len(biggest_groupings) < 3:
        largest_grouping_size = max(len(v) for v in groupings.values())
        biggest_groupings.append(largest_grouping_size)
        for k, v in groupings.items():
            if len(v) == largest_grouping_size:
                grouping = v
                break
        for index in grouping:
            del groupings[index]
    return math.prod(biggest_groupings)


if __name__ == "__main__":
    print(main(read_input()))

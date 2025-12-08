from coding_puzzle_tools import read_input
from y2025.day08_1 import get_points, get_sorted_distances


def main(lines: list[str]) -> int:
    num_points = len(lines)
    points = get_points(lines)
    indexed_points = {i: point for i, point in enumerate(points)}
    groupings = {index: {index} for index in indexed_points.keys()}
    sorted_distances = get_sorted_distances(indexed_points)

    for distance in sorted_distances:
        index1, index2 = distance[1]

        if groupings[index1] is not groupings[index2]:
            new_grouping = groupings[index1].union(groupings[index2])
            for index in new_grouping:
                groupings[index] = new_grouping

        if len(groupings[0]) == num_points:
            return indexed_points[index1].x * indexed_points[index2].x

    raise NotImplementedError  # Shouldn't happen


if __name__ == "__main__":
    print(main(read_input()))

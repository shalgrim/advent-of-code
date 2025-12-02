from itertools import combinations

from day19_1 import create_and_position_all_scanners


def manhattan_distance(p1, p2):
    return sum([abs(p2[i] - p1[i]) for i in range(3)])


def main(lines):
    scanners = create_and_position_all_scanners(lines).values()
    distances = [
        manhattan_distance(s1.position, s2.position)
        for s1, s2 in combinations(scanners, 2)
    ]
    return max(distances)


if __name__ == "__main__":
    with open("../data/input19.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

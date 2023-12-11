import sys

from y2023.day10_1 import generate_loop


def main(lines):
    _, loop = generate_loop(lines)
    points_of_loop = set(loop)
    enclosed_points = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (x, y) in points_of_loop:
                continue

            lines_crossed = 0

            if x < len(lines[0]) / 2:
                for i in range(x, -1, -1):
                    if (i, y) in points_of_loop:
                        lines_crossed += 1
            else:
                for i in range(x+1, len(line)):
                    if (i, y) in points_of_loop:
                        lines_crossed += 1

            if lines_crossed % 2 == 1:
                enclosed_points.add((x, y))
    return len(enclosed_points)


if __name__ == "__main__":  # 1048 is too high
    sys.setrecursionlimit(20000)
    with open("../../data/2023/input10.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

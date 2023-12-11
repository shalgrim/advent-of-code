import re
import sys

from y2023.day10_1 import generate_loop

# Considering lines
# Let's always go horizontal from 0 to the point
# If you see a |, that's a boundary crossing, period
# If you see a F-*7, that's not a boundary crossing
# If you see a F-*J, that IS a boundary crossing
# If you see a L-*7, that IS a boundary crossing
# If you see a L-*J, that is not a boundary crossing

# If you're always going from left to right, the only items you'll see first are |, F, and L


def generate_clean_map(s_shape, loop, lines, outfile=None):
    outlines = []
    for y, line in enumerate(lines):
        outline = ""
        for x, char in enumerate(line):
            if (x, y) in loop:
                outline += char
            elif char == "S":
                outline += s_shape
            else:
                outline += "."
        outlines.append(outline)

    if outfile:
        outoutlines = [outline + "\n" for outline in outlines]
        with open(outfile, "w") as f:
            f.writelines(outoutlines)
    return outlines


def main(lines, outfn=None):
    s_shape, loop = generate_loop(lines)
    map = generate_clean_map(s_shape, loop, lines, outfn)
    points_of_loop = set(loop)
    enclosed_points = set()
    pattern = re.compile(r"(\|)|(F-*J)|(L-*7)")

    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if (x, y) in points_of_loop:
                continue

            path_to_consider = line[:x]
            matches = pattern.findall(path_to_consider)

            if len(matches) % 2 == 1:
                enclosed_points.add((x, y))
    return len(enclosed_points)


if __name__ == "__main__":  # 454 is too high
    sys.setrecursionlimit(20000)
    with open("../../data/2023/input10.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

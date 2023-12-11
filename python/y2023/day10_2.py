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

# Tests are working but getting wrong answer still
# Which may get me stuck
# One thing I might consider doing is
# making the map twice as big by turning "||" into "|.|" and "--" into "---" and so on
# both horizontally and vertically figuring out what should go in between
# then do some flood filling...mark every space next to a wall as O and then everything next
# to an O as an O until you stop adding
# Then what's left are I except only odd rows and columns


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


def print_with_enclosures(map, enclosed_points, enclosfn):
    lines_to_write = []
    for y, line in enumerate(map):
        outline = ""
        for x, char in enumerate(line):
            if (x, y) in enclosed_points:
                assert char == "."
                outline += "I"
            else:
                outline += char
        outline += "\n"
        lines_to_write.append(outline)
    if enclosfn:
        with open(enclosfn, "w") as f:
            f.writelines(lines_to_write)


def main(lines, outfn=None, enclosfn=None):
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
    if enclosfn:
        print_with_enclosures(map, enclosed_points, enclosfn)
    return len(enclosed_points)


if __name__ == "__main__":  # 454 is too high
    sys.setrecursionlimit(20000)
    with open("../../data/2023/input10.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(
        main(
            lines,
            "../../data/2023/output10_2.txt",
            "../../data/2023/output10_2_enclosed.txt",
        )
    )

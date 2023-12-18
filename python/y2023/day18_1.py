import math
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()


def fill_in_holes(dug_holes):
    highest = min(hole[1] for hole in dug_holes)
    lowest = max(hole[1] for hole in dug_holes)
    total = 0
    for y in range(highest, lowest + 1):
        leftest = min(hole[0] for hole in dug_holes if hole[1] == y)
        rightest = max(hole[0] for hole in dug_holes if hole[1] == y)
        inside = False
        outline = ""
        line_total = 0
        seen_upon_entering = []
        for x in range(leftest, rightest + 1):

            # if we newly get to rock, record what's around us
            if (x, y) in dug_holes and (x-1, y) not in dug_holes:
                seen_upon_entering = []
                if (x, y-1) in dug_holes:
                    seen_upon_entering.append(Direction.UP)
                if (x, y+1) in dug_holes:
                    seen_upon_entering.append(Direction.DOWN)

            # if we newly get to space, see if we swapped inside/outside
            if (x, y) not in dug_holes and (x-1, y) in dug_holes:
                if seen_upon_entering == [Direction.UP, Direction.DOWN]:
                    assert (x-2, y) not in dug_holes
                        # print("How did I get here")
                    inside = not inside
                elif seen_upon_entering == [Direction.UP]:
                    if (x-1, y+1) in dug_holes:
                        inside = not inside
                else:
                    assert seen_upon_entering == [Direction.DOWN]
                    if (x-1, y-1) in dug_holes:
                        inside = not inside
                seen_upon_entering.clear()

            # if we're inside or in a dug hole, add one
            if (x, y) in dug_holes or inside:
                line_total += 1
            outline += "#" if (x, y) in dug_holes else "."
        total += line_total
        ...
    return total


def get_header_rows(leftest, rightest, padding):
    rows_needed = math.floor(math.log(rightest, 10) + 1)
    if leftest < 0:
        rows_needed = max(rows_needed, math.floor(math.log(abs(leftest), 10) + 1) + 1)
    print(f"{rows_needed=}")
    outlines = []
    for row in range(rows_needed):
        outline = " " * (padding + 1)
        for i in range(leftest, rightest + 1):
            num = abs(i) % 10 ** (row + 1) // 10**row
            if num == 0 and i < 0:
                if math.floor(math.log(abs(i), 10 ** (row + 1))) == 0:
                    num = "-"
            outline += str(num)
        outlines.append(outline)
    return outlines[::-1]


def get_prefix(y, padding):
    s = str(y)
    space_needed = padding - len(s)
    return " " * space_needed + s + " "


def print_map(dug_holes, filename=None):
    # this is still printing a titch off
    highest = min(hole[1] for hole in dug_holes)
    lowest = max(hole[1] for hole in dug_holes)
    leftest = min(hole[0] for hole in dug_holes)
    rightest = max(hole[0] for hole in dug_holes)
    print(f"{highest=}")
    print(f"{lowest=}")
    print(f"{leftest=}")
    print(f"{rightest=}")
    padding = math.floor(math.log(rightest, 10)) + 1
    if leftest < 0:
        padding = max(padding, math.floor(math.log(abs(leftest), 10)) + 2)
    outlines = get_header_rows(leftest, rightest, padding)
    for y in range(highest, lowest + 1):
        outline = get_prefix(y, padding)
        for x in range(leftest, rightest + 1):
            outline += "#" if (x, y) in dug_holes else "."
        outlines.append(outline)
    for line in outlines:
        print(line)
    if filename:
        with open(filename, mode="w") as outfile:
            outfile.writelines([f"{line}\n" for line in outlines])


def main(lines, filename=None):
    last_point = (0, 0)
    dug_holes = {last_point}
    for line in lines:
        direction, distance, _ = line.split()
        for _ in range(int(distance)):
            if direction == "R":
                next_point = (last_point[0] + 1, last_point[1])
            elif direction == "L":
                next_point = (last_point[0] - 1, last_point[1])
            elif direction == "U":
                next_point = (last_point[0], last_point[1] - 1)
            elif direction == "D":
                next_point = (last_point[0], last_point[1] + 1)
            else:
                raise RuntimeError("Invalid direction")
            dug_holes.add(next_point)
            last_point = next_point

    all_holes = fill_in_holes(dug_holes)
    print_map(dug_holes, filename)
    return all_holes


if __name__ == "__main__":  # 60,486 is wrong as is 39,623
    with open("../../data/2023/input18.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines), "../../data/2023/map18.txt")

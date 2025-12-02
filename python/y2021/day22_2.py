from collections import defaultdict

from day22_1 import parse_line


def process_line(parsed_line, reactor_core):
    value, x1, x2, y1, y2, z1, z2 = parsed_line

    for x in range(x1, x2 + 1):
        print(f"  {x=}")
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                reactor_core[x][y][z] = value
    return reactor_core


def main(lines):
    # might make sense to kind of go backwards, looking for ranges that are outside of what we cover later
    # because even just running the 11th line like we're doing is looooong
    # alternatively you can get sophisticated keeping track of borders...but then you need to calculate the volume of each
    reactor_core = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    print(f"{len(lines)=}")
    for i, line in enumerate(lines):
        print(f"line {i + 1}")
        parsed_line = parse_line(line)
        reactor_core = process_line(parsed_line, reactor_core)

    num_cubes_on = 0
    for xk, xv in reactor_core.items():
        for yk, yv in xv.items():
            for zk, zv in yv.items():
                num_cubes_on += zv

    return num_cubes_on


if __name__ == "__main__":
    # with open('../data/input22.txt') as f:
    with open("../data/test22_3.txt") as f:  # supposed to be 2758514936282235
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

from collections import defaultdict


def parse_line(line):
    on_or_off, remainder = line.split()
    on_or_off = 1 if on_or_off == 'on' else 0
    raw_x, raw_y, raw_z = remainder.split(',')
    x1, x2 = raw_x[2:].split('..')
    y1, y2 = raw_y[2:].split('..')
    z1, z2 = raw_z[2:].split('..')
    return on_or_off, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)


def process_line(parsed_line, reactor_core):
    value, x1, x2, y1, y2, z1, z2 = parsed_line

    for x in range(max(-50, x1), min(51, x2 + 1)):
        for y in range(max(-50, y1), min(51, y2 + 1)):
            for z in range(max(-50, z1), min(51, z2 + 1)):
                reactor_core[x][y][z] = value
    return reactor_core


def main(lines):
    reactor_core = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for line in lines:
        parsed_line = parse_line(line)
        reactor_core = process_line(parsed_line, reactor_core)

    num_cubes_on = 0
    for xk, xv in reactor_core.items():
        for yk, yv in xv.items():
            for zk, zv in yv.items():
                num_cubes_on += zv

    return num_cubes_on


if __name__ == '__main__':
    with open('../data/input22.txt') as f:
    # with open('../data/test22_1.txt') as f:  # 39 == correct
    # with open('../data/test22_2.txt') as f:  # 590784 == correct
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

def build_cubes(lines):
    cubes = []
    for line in lines:
        x, y, z = [int(num) for num in line.split(',')]
        cubes.append((x, y, z))
    return cubes


def side_generator(cube):
    x, y, z = cube
    yield x - 1, y, z
    yield x + 1, y, z
    yield x, y - 1, z
    yield x, y + 1, z
    yield x, y, z - 1
    yield x, y, z + 1
    # raise StopIteration


def open_sides(cube, all_cubes):
    blocked_cubes = sum(1 for side in side_generator(cube) if side in all_cubes)
    return 6 - blocked_cubes


def main(lines):
    cubes = build_cubes(lines)
    return sum(open_sides(cube, cubes) for cube in cubes)


if __name__ == '__main__':
    with open('../../data/2022/input18.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

import itertools

from y2022.day15_1 import manhattan_distance


def build_map(lines):
    empty_rows = [y for y, line in enumerate(lines) if "#" not in line]
    map = []
    for y, line in enumerate(lines):
        map.append(list(line))
        if y in empty_rows:
            map.append(list(line))

    empty_columns = []
    for x in range(len(map[0])):
        if all(row[x] == "." for row in map):
            empty_columns.append(x)

    for column in empty_columns[::-1]:
        for row in map:
            row.insert(column, ".")

    final_map = []
    for row in map:
        final_map.append("".join(row))

    return final_map


def get_galaxies(map):
    galaxies = []
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if map[y][x] == "#":
                galaxies.append((x, y))

    return galaxies


def main(lines):
    map = build_map(lines)
    galaxies = get_galaxies(map)
    galaxy_pairs = itertools.combinations_with_replacement(galaxies, 2)
    distances = [manhattan_distance(*pair) for pair in galaxy_pairs]
    return sum(distances)


if __name__ == "__main__":
    with open("../../data/2023/input11.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

from day13_1 import prepare_input


def graph_coordinates(coordinates):
    max_x = max([x for x, y in coordinates])
    max_y = max([y for x, y in coordinates])

    lines = []

    for y in range(max_y+1):
        line = ''
        for x in range(max_x+1):
            line += '#' if (x, y) in coordinates else '.'

        lines.append(line)

    return '\n'.join(lines)


def main(lines):
    coordinates, instructions = prepare_input(lines)

    for axis, value in instructions:
        new_coordinates = set()
        for x, y in coordinates:
            if axis == 'x':
                if x > value:
                    distance = x - value
                    new_coordinates.add(((value - distance), y))
                else:
                    new_coordinates.add((x, y))
            else:
                if y > value:
                    distance = y - value
                    new_coordinates.add((x, (value - distance)))
                else:
                    new_coordinates.add((x, y))

        coordinates = new_coordinates

    return graph_coordinates(coordinates)


if __name__ == '__main__':
    with open('../data/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

def prepare_input(lines):
    coordinates = set()
    instructions = []
    for line in lines:
        if ',' in line:
            x, y = line.split(',')
            coordinates.add((int(x), int(y)))
        elif line.startswith('fold'):
            final = line.split()[2]
            axis, value = final.split('=')
            instructions.append((axis, int(value)))
    return coordinates, instructions


def main(lines):
    coordinates, instructions = prepare_input(lines)

    first_instruction = instructions[0]
    # cheating, I know it's x=655
    new_coordinates = set()
    for x, y in coordinates:
        if x > 655:
            distance = x - 655
            new_coordinates.add(((655 - distance), y))
        else:
            new_coordinates.add((x, y))

    coordinates = new_coordinates

    return len(coordinates)


if __name__ == '__main__':
    with open('../data/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

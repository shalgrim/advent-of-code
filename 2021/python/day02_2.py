def main(lines):
    commands = [line.split() for line in lines]
    commands = [(t[0], int(t[1])) for t in commands]
    depth = 0
    aim = 0
    position = 0

    for command, value in commands:
        if command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
        else:
            position += value
            depth += aim * value

    return depth * position


if __name__ == '__main__':
    with open('../data/input02.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

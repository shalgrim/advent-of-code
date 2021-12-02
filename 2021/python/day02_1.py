def main(lines):
    commands = [line.split() for line in lines]
    commands = [(t[0], int(t[1])) for t in commands]
    pos_depth = sum(t[1] for t in commands if t[0] == 'down')
    neg_depth = sum(t[1] for t in commands if t[0] == 'up')
    position = sum(t[1] for t in commands if t[0] == 'forward')
    return position * (pos_depth - neg_depth)


if __name__ == '__main__':
    with open('../data/input02.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

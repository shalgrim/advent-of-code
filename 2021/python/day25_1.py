from copy import deepcopy
from itertools import pairwise


def main(lines):
    map = [list(line) for line in lines]
    moves = True
    num_steps = 0

    while moves:
        num_steps += 1
        new_map = map_step(map)
        moves = new_map != map
        map = new_map

    return num_steps


def map_step_n(map, n):
    copy_map = deepcopy(map)

    for _ in range(n):
        new_map = map_step(copy_map)
        copy_map = new_map

    return copy_map


def map_step(map):
    # east moves
    new_map = []
    for line in map:
        new_line = []
        if line[0] == '.' and line[-1] == '>':
            next_is_east = True
        else:
            next_is_east = False

        for pair in pairwise(line):
            if next_is_east:
                new_line.append('>')
                next_is_east = False
            elif pair == ('>', '.'):
                new_line.append('.')
                next_is_east = True
            else:
                new_line.append(pair[0])

        if next_is_east:
            new_line.append('>')
        elif line[-1] == '>':
            if line[0] == '.':
                new_line.append('.')
            else:
                new_line.append(line[-1])
        else:
            new_line.append(line[-1])

        new_map.append(new_line)

    if len(map) == 1:  # just for toy examples in tests
        return deepcopy(new_map)

    # south moves
    for x in range(len(new_map[0])):
        old_first_char = new_map[0][x]
        next_is_south = (
            True if old_first_char == '.' and new_map[-1][x] == 'v' else False
        )

        if next_is_south:
            new_map[-1][x] = 'v'

        for y in range(len(new_map) - 1):
            this = new_map[y][x]
            next = new_map[y + 1][x]

            if next_is_south:
                new_map[y][x] = 'v'
                next_is_south = False
            elif (this, next) == ('v', '.'):
                new_map[y][x] = '.'
                next_is_south = True
            else:
                pass  # should just be able to leave it
                new_map[y][x]

        # last character
        if next_is_south:
            new_map[-1][x] = 'v'
        elif old_first_char == '.' and new_map[-1][x] == 'v':
            new_map[-1][x] = '.'
        else:
            pass  # should be able to just leave it

    return new_map


if __name__ == '__main__':
    with open('../data/input25.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

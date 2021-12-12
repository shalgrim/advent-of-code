from collections import defaultdict
from copy import copy


def main(lines):
    rules = defaultdict(set)
    for line in lines:
        start, end = line.split('-')
        rules[start].add(end)
        rules[end].add(start)
    paths = [['start']]

    while any(path[-1] != 'end' for path in paths):
        new_paths = []
        for path in paths:
            current_cave = path[-1]
            if current_cave == 'end':
                new_paths.append(path)
                continue
            possible_next_steps = [
                end for end in rules[current_cave] if end not in path or end.isupper()
            ]
            for pns in possible_next_steps:
                new_paths.append(copy(path) + [pns])

        unique_new_path_strings = {','.join(np) for np in new_paths}
        paths = [s.split(',') for s in unique_new_path_strings]


    return len(paths)


if __name__ == '__main__':
    with open('../data/input12.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

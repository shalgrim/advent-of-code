from y2022.day16_1 import build_valves


def build_paths_to_all_open(valves, starting_valve='AA'):

    pass


def main(lines):
    valves = build_valves(lines)
    paths_to_all_open = build_paths_to_all_open(valves)


if __name__ == '__main__':
    with open('../../data/2022/test16.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

import math

from y2023.day06_1 import get_ways_to_beat


def build_single_number(line):
    less_throwaway = line.split()[1:]
    input_string = "".join(less_throwaway)
    return int(input_string)


def build_races(lines):
    time = build_single_number(lines[0])
    record = build_single_number(lines[1])
    return [(time, record)]


def main(lines):
    races = build_races(lines)
    ways_to_beat = [get_ways_to_beat(*race) for race in races]
    return math.prod(ways_to_beat)


if __name__ == "__main__":
    with open("../../data/2023/input06.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

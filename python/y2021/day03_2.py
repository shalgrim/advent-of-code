from copy import copy

from day03_1 import sort_bits_by_commonness


def get_rating(lines, rating_type):
    old_lines = copy(lines)
    for i in range(len(old_lines[0])):
        if len(old_lines) == 1:
            break
        new_lines = []
        mcb, lcb = sort_bits_by_commonness(old_lines, i)
        for line in old_lines:
            if (
                rating_type == 'o2'
                and line[i] == mcb
                or rating_type == 'co2'
                and line[i] == lcb
            ):
                new_lines.append(line)
        old_lines = new_lines
    return int(old_lines[0], 2)


def main(lines):
    o2_rating = get_rating(lines, 'o2')
    co2_rating = get_rating(lines, 'co2')
    return o2_rating * co2_rating


if __name__ == '__main__':
    with open('../data/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

from itertools import permutations

from day18_1 import SnailfishNumber


def get_magnitude(number1, number2):
    snf1 = SnailfishNumber(number1)
    snf2 = SnailfishNumber(number2)
    added = snf1 + snf2
    added.reduce()
    return added.magnitude()


def main(filename):
    with open(filename) as f:
        raw_numbers = [eval(line) for line in f.readlines()]

    perms = permutations(raw_numbers, 2)
    magnitudes = [get_magnitude(*perm) for perm in perms]
    return max(magnitudes)


if __name__ == '__main__':
    print(main('../data/input18.txt'))

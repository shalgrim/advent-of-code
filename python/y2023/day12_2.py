from y2023.day12_1 import get_num_arrangements


def convert_row(line):
    springs, nums = line.split()
    new_springs = "?".join([springs] * 5)
    new_nums = ",".join([nums] * 5)
    return " ".join([new_springs, new_nums])


def main(lines):
    converted_lines = [convert_row(line) for line in lines]
    possible_arrangements = [get_num_arrangements(line) for line in converted_lines]
    return sum(possible_arrangements)


if __name__ == "__main__":
    with open("../../data/2023/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

import itertools


def convert_line_to_nums(line):
    damaged = line.split(".")
    return [len(d) for d in damaged if d]


def get_arrangement(springs, combo):
    splits = []
    last_index = 0
    for index in combo:
        splits.append(springs[last_index:index])
        last_index = index + 1
    splits.append(springs[last_index:])
    damaged_replaced = "#".join(splits)
    answer = damaged_replaced.replace("?", ".")
    return answer


def get_num_arrangements(line):
    springs, nums = line.split()
    nums = [int(num) for num in nums.split(",")]
    given_damaged = springs.count("#")
    known_damaged = sum(nums)
    unknown_indexes = [i for i, spring in enumerate(springs) if spring == "?"]
    possible_combos = itertools.combinations(
        unknown_indexes, known_damaged - given_damaged
    )
    possible_arrangements = [
        get_arrangement(springs, combo) for combo in possible_combos
    ]
    legal_arrangements = [
        arrangement
        for arrangement in possible_arrangements
        if convert_line_to_nums(arrangement) == nums
    ]
    return len(legal_arrangements)


def main(lines):
    possible_arrangements = [get_num_arrangements(line) for line in lines]
    return sum(possible_arrangements)


if __name__ == "__main__":
    with open("../../data/2023/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

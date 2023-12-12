def convert_row(line):
    springs, nums = line.split()
    new_springs = "?".join([springs] * 5)
    new_nums = ",".join([nums] * 5)
    return " ".join([new_springs, new_nums])


def _get_num_arrangements(springs, nums, num_to_place):
    unknown_indexes = [i for i, spring in enumerate(springs) if spring == "?"]
    for index in unknown_indexes:
        # try placing a damaged in each index
        # verify that will work up to that index or one index past it or until the next ? or # (I'm not sure)
        # if not, continue
        # if so, then recurse
        new_springs = None  # create a new springs line

        # not sure if this will work
        # not sure it even makes sense to make a generator since I have to call them all anyway
        yield _get_num_arrangements(new_springs, nums, num_to_place-1)


def get_num_arrangements(line):
    """Idea behind this one is to recursively find possibilities with an early exit"""
    # TODO: Use JetBrainsAI to generate tests
    springs, nums = line.split()
    nums = [int(num) for num in nums.split(",")]
    given_damaged = springs.count("#")
    known_damaged = sum(nums)
    num_to_place = known_damaged - given_damaged
    possibilities = _get_num_arrangements(springs, nums, num_to_place)
    return len(list(possibilities))


def main(lines):
    converted_lines = [convert_row(line) for line in lines]
    possible_arrangements = [get_num_arrangements(line) for line in converted_lines]
    return sum(possible_arrangements)


if __name__ == "__main__":
    with open("../../data/2023/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

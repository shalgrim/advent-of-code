import re


def convert_row(line):
    springs, nums = line.split()
    new_springs = "?".join([springs] * 5)
    new_nums = ",".join([nums] * 5)
    return " ".join([new_springs, new_nums])


def is_possible(new_springs, nums):
    damaged_blocks = re.findall("#+", new_springs.split("?")[0])
    return (
        all(len(db) == n for db, n in zip(damaged_blocks[:-1], nums))
        and len(damaged_blocks[-1]) <= nums[len(damaged_blocks) - 1]
    )


def _get_num_arrangements(springs, nums, num_to_place, possibilities):
    # TODO: Maybe consider caching search space...there will almost certainly be some repeats, right?

    unknown_indexes = [i for i, spring in enumerate(springs) if spring == "?"]
    for j, index in enumerate(unknown_indexes):
        # try placing a damaged in each index
        new_springs = springs[:index].replace("?", ".") + "#" + springs[index + 1 :]

        # if the only remaining thing to do is replace all "?" with "#" let's do it
        if num_to_place == len(unknown_indexes[j:]):
            newer_springs = new_springs.replace("?", "#")
            if is_possible(newer_springs, nums):
                possibilities.add(newer_springs)
            break

        if is_possible(new_springs, nums):
            if "?" not in new_springs:
                raise RuntimeError("Shouldn't ever be here with checking first on num_to_place equalling number of ?")
                # we finished with the last hook
                possibilities.add(new_springs)
                continue
            elif num_to_place == 1:

                # we're placing the last unknown, so put all the rest to "." and check it
                newest_springs = new_springs.replace("?", ".")
                if is_possible(newest_springs, nums):
                    possibilities.add(newest_springs)
                    continue
            else:
                _get_num_arrangements(
                    new_springs, nums, num_to_place - 1, possibilities
                )
        else:
            continue


def get_num_arrangements(line):
    """Idea behind this one is to recursively find possibilities with an early exit"""
    possibilities = set()
    springs, nums = line.split()
    nums = [int(num) for num in nums.split(",")]
    given_damaged = springs.count("#")
    known_damaged = sum(nums)
    num_to_place = known_damaged - given_damaged
    _get_num_arrangements(springs, nums, num_to_place, possibilities)
    return len(possibilities)


def main(lines):
    converted_lines = [convert_row(line) for line in lines]
    possible_arrangements = [get_num_arrangements(line) for line in converted_lines]
    return sum(possible_arrangements)


if __name__ == "__main__":  # So this might take a few hours
    with open("../../data/2023/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

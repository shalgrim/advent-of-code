import functools
import re

from tqdm import tqdm


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


@functools.cache
def _get_arrangements(springs, nums, num_to_place):
    answer = set()

    unknown_indexes = [i for i, spring in enumerate(springs) if spring == "?"]
    for j, index in enumerate(unknown_indexes):
        # try placing a damaged in each index
        new_springs = springs[:index].replace("?", ".") + "#" + springs[index + 1 :]

        # if the only remaining thing to do is replace all "?" with "#" let's do it
        if num_to_place == len(unknown_indexes[j:]):
            newer_springs = new_springs.replace("?", "#")
            if is_possible(newer_springs, nums):
                answer.add(newer_springs)
            break

        if is_possible(new_springs, nums):
            if "?" not in new_springs:
                # we finished with the last hook
                raise RuntimeError(
                    "Shouldn't ever be here with checking first on num_to_place equalling number of ?"
                )
            elif num_to_place == 1:
                # we're placing the last unknown, so put all the rest to "." and check it
                newest_springs = new_springs.replace("?", ".")
                if is_possible(newest_springs, nums):
                    answer.add(newest_springs)
                    continue
            else:
                holding = _get_arrangements(new_springs, nums, num_to_place - 1)
                answer.update(holding)
        else:
            continue

    return answer


def get_num_arrangements(line):
    """Idea behind this one is to recursively find possibilities with an early exit"""
    springs, nums = line.split()
    nums = [int(num) for num in nums.split(",")]
    given_damaged = springs.count("#")
    known_damaged = sum(nums)
    num_to_place = known_damaged - given_damaged
    possibilities = _get_arrangements(springs, tuple(nums), num_to_place)
    return len(possibilities)


def main(lines):
    converted_lines = [convert_row(line) for line in lines]
    possible_arrangements = []
    for converted_line in tqdm(converted_lines):
        num = get_num_arrangements(converted_line)
        possible_arrangements.append(num)
    return sum(possible_arrangements)


if __name__ == "__main__":  # So this might take a few hours...never got done with line 5...next steps: refactor so it returns a set instead of updating th eone passed in and then use functools.cache
    with open("../../data/2023/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

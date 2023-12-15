import functools
import re

from tqdm import tqdm


def convert_row(line):
    springs, nums = line.split()
    new_springs = "?".join([springs] * 5)
    new_nums = ",".join([nums] * 5)
    return " ".join([new_springs, new_nums])


@functools.cache
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


def get_num_leading_hashes(s):
    return re.match("#+").group()
    pass


# Consider a new algorithm something like this:
# Look at first character
# If it is a ., just remove all the consecutive .s and recurse
# If it is a #
#   remove consecutive hashes
#   and subtract that number from first number in nums
#   but pop it if it's 0
#   and return if it's < 0
#   then recurse
# If it is a ?,
#   change it to a . and recurse
#   change it to a # and recurse
# The trick here is my base case and how I add everything up
# The base case must be, what, I have no string and nums is an empty list?
# and if that's the case I return True?
# But how do I keep track of the sum?
# Try when you branch, putting into a list of two and then summing up that answer at the end
@functools.cache
def _get_num_arrangements_proper_recursion(springs, nums, mid_block=False):
    post_block = False

    # No springs, so if numbers is also empty we found one
    if not springs:
        return 1 if not nums or nums == (0,) else 0

    # We do have springs left, so as long as it's all . and ? we're okay
    if not nums or nums == (0,):
        return 1 if "#" not in springs else 0

    next_char = springs[0]
    if nums[0] == 0:
        if next_char == "#":
            return 0
        else:
            nums = nums[1:]
            mid_block = False
            post_block = True

    if next_char == ".":
        if mid_block:
            return 0
        else:
            new_springs = springs.lstrip(".")
            return _get_num_arrangements_proper_recursion(new_springs, nums, False)
    elif next_char == "#":
        # TODO: this part
        # oh there are lots of different cases here like
        # what happens if it matches exactly but there's a ? at the end then that has to be a .
        # maybe just pull off one then subtract 1 from first num
        # but if it's already at 1 then check next char and if # return 0 but if ? then change it to a . and remove num
        # ...
        # no wait, just subtract one and move on, but at the top of this function I should check if nums[0] == 0
        # and if so, and if leading is hash do x if it's hook do y blah blah
        # but what if I have #? and the number 2
        # then I subtract 1 and go into the next step with ? and the number 1
        # and I'll do my ? step not knowing that it MUST be a #
        # so let's try this mid_block argument

        # num_leading_hashes = len(re.match("#+", springs).group())

        nums = (nums[0]-1, *nums[1:])
        return _get_num_arrangements_proper_recursion(springs[1:], nums, True)


    elif next_char == "?":
        as_dot = (
            0
            if mid_block or post_block
            else _get_num_arrangements_proper_recursion("." + springs[1:], nums, False)
        )
        as_hash = _get_num_arrangements_proper_recursion(
            "#" + springs[1:], nums, mid_block
        )
        return as_dot + as_hash
    else:
        raise RuntimeError("Unknown character {}".format(next_char))


def get_num_arrangements(line):
    """Idea behind this one is to recursively find possibilities with an early exit"""
    springs, nums = line.split()
    nums = [int(num) for num in nums.split(",")]
    given_damaged = springs.count("#")
    known_damaged = sum(nums)
    num_to_place = known_damaged - given_damaged
    # possibilities = _get_arrangements(springs, tuple(nums), num_to_place)
    # return len(possibilities)
    answer = _get_num_arrangements_proper_recursion(springs, tuple(nums))
    return answer


def main(lines):
    converted_lines = [convert_row(line) for line in lines]
    possible_arrangements = []
    for converted_line in tqdm(converted_lines):
        num = get_num_arrangements(converted_line)
        possible_arrangements.append(num)
    return sum(possible_arrangements)


if (
    __name__ == "__main__"
):  # So this might take a few hours...never got done with line 5...next steps: refactor so it returns a set instead of updating th eone passed in and then use functools.cache
    with open("../../data/2023/input12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

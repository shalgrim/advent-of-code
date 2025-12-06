from typing import List

from coding_puzzle_tools import read_input


def get_ranges(lines: list[str]) -> tuple[int, list[tuple[int, int]]]:
    ranges = []
    for i, line in enumerate(lines):
        if not line:
            break
        nums = line.split("-")
        ranges.append((int(nums[0]), int(nums[1])))
    return i, ranges


def main(lines: List[str]) -> int:
    i, ranges = get_ranges(lines)

    ingredients = []
    for line in lines[i + 1 :]:
        ingredients.append(int(line))

    fresh_count = 0
    for ingredient in ingredients:
        for lower, upper in ranges:
            if lower <= ingredient <= upper:
                fresh_count += 1
                break

    return fresh_count


if __name__ == "__main__":
    print(main(read_input()))

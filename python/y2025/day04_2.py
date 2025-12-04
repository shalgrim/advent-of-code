from typing import List

from coding_puzzle_tools import read_input
from y2025.day04_1 import Map


def main(lines: List[str]):
    map = Map(lines)
    answer = 0
    num_removed = map.remove_accessible()

    while num_removed:
        answer += num_removed
        num_removed = map.remove_accessible()

    return answer


if __name__ == "__main__":
    print(main(read_input()))

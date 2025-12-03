import re
from typing import List, Set, Tuple

from coding_puzzle_tools import InputMode, read_input

REPEATED_PATTERN = re.compile(r"^(\d+)\1$")


def extract_ranges(text: str) -> List[Tuple[int, int]]:
    text_ranges = text.split(",")
    answer = []
    for rng in text_ranges:
        first, second = rng.split("-")
        answer.append((int(first), int(second)))

    return answer


def invalidate(i: int, pattern=REPEATED_PATTERN) -> bool:
    return pattern.match(str(i))


def main(text: str, pattern=REPEATED_PATTERN) -> int:
    invalid_ids: Set[int] = set()
    ranges = extract_ranges(text)
    for first, second in ranges:
        for i in range(first, second + 1):
            if invalidate(i, pattern):
                invalid_ids.add(i)

    return sum(invalid_ids)


if __name__ == "__main__":
    print(main(read_input(mode=InputMode.TEXT)))

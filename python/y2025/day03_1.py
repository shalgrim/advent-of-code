from typing import List

from coding_puzzle_tools import InputMode, read_input


def max_joltage_per_bank(line: str) -> int:
    first_digit = max(int(c) for c in line[:-1])
    first_index = line.find(str(first_digit))
    second_digit = max(int(c) for c in line[first_index + 1 :])
    return 10 * first_digit + second_digit


def main(lines: List[str]) -> int:
    return sum(max_joltage_per_bank(line) for line in lines)


if __name__ == "__main__":
    print(main(read_input()))

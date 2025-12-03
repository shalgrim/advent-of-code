from typing import List

from coding_puzzle_tools import InputMode, read_input


def max_joltage_per_bank(line: str) -> int:
    digits = []
    index = -1
    for i in range(12, 1, -1):
        sdigit = str(max(int(c) for c in line[index + 1 : -(i - 1)]))
        digits.append(sdigit)
        new_index = line.find(sdigit, index + 1)
        index = new_index

    last_digit = str(max(int(c) for c in line[index + 1 :]))
    digits.append(last_digit)
    sanswer = "".join(digits)
    return int(sanswer)


def main(lines: List[str]) -> int:
    return sum(max_joltage_per_bank(line) for line in lines)


if __name__ == "__main__":
    print(main(read_input()))

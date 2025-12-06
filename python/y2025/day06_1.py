from math import prod
from typing import List

from coding_puzzle_tools import read_input


def main(lines: List[str]) -> int:
    splits = []
    for line in lines[:-1]:
        splits.append([int(n) for n in line.split()])

    answer = 0
    for index, operator in enumerate(lines[-1].split()):
        if operator == "+":
            answer += sum(s[index] for s in splits)
        elif operator == "*":
            answer += prod(s[index] for s in splits)
        else:
            raise NotImplementedError("Shouldn't happen")
    return answer


if __name__ == "__main__":
    print(main(read_input()))

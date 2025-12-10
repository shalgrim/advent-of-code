from coding_puzzle_tools import read_input
from y2025.day10_1 import Machine


def main(lines: list[str]) -> int:
    machines = [Machine(line) for line in lines]


if __name__ == "__main__":
    print(main(read_input()))

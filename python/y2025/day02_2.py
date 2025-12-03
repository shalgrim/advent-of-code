import re

from coding_puzzle_tools import InputMode, read_input
from y2025.day02_1 import main as main1

MULTI_REPEATED_PATTERN = re.compile(r"^(\d+)(\1)+$")


def main(text: str):
    return main1(text, MULTI_REPEATED_PATTERN)


if __name__ == "__main__":
    print(main(read_input(mode=InputMode.TEXT)))

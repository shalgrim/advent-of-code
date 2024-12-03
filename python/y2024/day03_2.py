import re

from aoc.io import this_year_day
from y2024.day03_1 import multiply

pattern = re.compile(r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")


def main(text):
    groupings = pattern.findall(text)
    valid_groupings = []
    valid = True
    for grouping in groupings:
        if not valid and grouping[2]:
            valid = True
        elif grouping[3]:
            valid = False
        elif valid and grouping[0]:
            valid_groupings.append(grouping[:2])

    products = [multiply(*group) for group in valid_groupings]
    return sum(products)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}_2.txt") as f:
        text = f.read()
    print(main(text))

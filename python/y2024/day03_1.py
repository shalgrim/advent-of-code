import re

from aoc.io import this_year_day

pattern = re.compile(r"mul\((\d+),(\d+)\)")


def multiply(s1, s2):
    return int(s1) * int(s2)


def main(text):
    groupings = pattern.findall(text)
    products = [multiply(*group) for group in groupings]
    return sum(products)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}.txt") as f:
        text = f.read()
    print(main(text))

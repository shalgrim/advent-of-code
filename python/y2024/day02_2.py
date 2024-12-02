from copy import copy

from aoc.io import this_year_day
from y2024.day02_1 import is_safe as is_safe_undamped
from y2024.day02_1 import make_report


def is_safe(report):
    for i in range(len(report)):
        copied_report = copy(report)
        copied_report.pop(i)
        if is_safe_undamped(copied_report):
            return True
    return False


def main(lines):
    reports = [make_report(line) for line in lines]
    safes = [is_safe(report) for report in reports]
    return sum(safes)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

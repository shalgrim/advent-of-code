from aoc.io import this_year_day


def make_report(line):
    return [int(level) for level in line.split()]


def is_safe(report):
    if report[1] == report[0]:
        return False
    reversed = False if report[1] - report[0] > 0 else True
    if sorted(report, reverse=reversed) != report:
        return False
    diffs = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    answer = max(diffs) <= 3 and all(diffs)
    return answer


def main(lines):
    reports = [make_report(line) for line in lines]
    safes = [is_safe(report) for report in reports]
    return sum(safes)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))  # 570 is wrong

from typing import List

from aoc.io import this_year_day


def process_input(lines: List[str]):
    rules = []
    i = 0

    for i, line in enumerate(lines):
        if not line:
            break
        rules.append(line.split("|"))

    updates = []
    for line in lines[i + 1 :]:
        updates.append(line.split(","))

    return rules, updates


def is_correct(update, rules):
    for_debugging = True
    for i, first in enumerate(update):
        for second in update[i + 1 :]:
            if [second, first] in rules:
                return False
    return True


def get_middle_value(update):
    middle_index = len(update) // 2
    return int(update[middle_index])


def main(lines):
    rules, updates = process_input(lines)
    correct_updates = [update for update in updates if is_correct(update, rules)]
    middle_values = [get_middle_value(update) for update in correct_updates]
    return sum(middle_values)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

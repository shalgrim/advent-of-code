from copy import copy

from aoc.io import this_year_day
from y2024.day05_1 import process_input, is_correct, get_middle_value


def reorder_update(update, rules):
    final_ordering = []
    to_process = copy(update)
    while to_process:
        for candidate in to_process:
            disqualifying_rules = [
                [candidate, other] for other in to_process if other != candidate
            ]
            if any(rule in rules for rule in disqualifying_rules):
                continue
            else:
                final_ordering.append(candidate)
                to_process = [foo for foo in to_process if foo != candidate]
    return final_ordering


def main(lines):
    rules, updates = process_input(lines)
    incorrect_updates = [update for update in updates if not is_correct(update, rules)]
    reordered_updates = [reorder_update(update, rules) for update in incorrect_updates]
    middle_values = [get_middle_value(update) for update in reordered_updates]
    return sum(middle_values)


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/input{day}.txt") as f:
        # with open(f"../../data/{year}/test{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

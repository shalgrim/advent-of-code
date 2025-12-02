import itertools
from datetime import datetime
from typing import Tuple

from aoc.io import this_year_day
from y2024.day22_1 import secret_number

SINGLE_DIGIT_INTEGERS = list(range(-9, 10))


def price_by_sequence(initial_secret_number: int, sequence: Tuple[int]) -> int:
    recent_changes = []
    new_secret_number = initial_secret_number
    last_price = new_secret_number % 10
    counter = 0
    while tuple(recent_changes) != sequence:
        if counter == 2000:
            return 0
        new_secret_number = secret_number(new_secret_number)
        new_price = new_secret_number % 10
        recent_changes.append(new_price - last_price)
        recent_changes = recent_changes[-4:]
        last_price = new_price
        counter += 1

    return last_price


def is_invalid(sequence: Tuple[int]):
    if abs(sum(sequence)) > 9:
        return True

    if any(abs(sum(sequence[i : i + 2])) > 9 for i in range(3)):
        return True

    if any(abs(sum(sequence[i : i + 3])) > 9 for i in range(2)):
        return True

    return False


def main(lines):
    initial_secret_numbers = [int(line) for line in lines]
    max_price = 0
    old_starter = None

    for sequence in itertools.product(SINGLE_DIGIT_INTEGERS, repeat=4):
        if is_invalid(sequence):
            continue
        starter = sequence[0]
        if starter != old_starter:
            old_starter = starter
            # Oh the next way to speed this thing up when you get a chance is to bail early when it's
            # impossible to beat the current high score
            # which wouldn't be a lot but could be something
            # ...
            # I think the main reason this is so slow is I keep generating secret numbers over and over
            # ... I should generate all up front and then search for sequences of cache more somehow
            print(f"{starter=}, {datetime.now()}")
        prices = [
            price_by_sequence(number, sequence) for number in initial_secret_numbers
        ]
        total_price = sum(prices)
        if total_price > max_price:
            max_price = total_price
            print(f"New {max_price=} by {sequence=}")
    return max_price


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    day = day + "_2" if testing else day
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

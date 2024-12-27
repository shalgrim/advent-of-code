from collections import Counter

from aoc.io import this_year_day
from y2024.day20_1 import Map


def main(lines, amount_to_save):
    map = Map(lines)
    map.establish_route()
    cheats = map.find_longer_cheats(amount_to_save)
    cheat_counter = Counter(cheats.values())

    print("COUNTS")
    sorted_cheat_counter = sorted(
        [(k, v) for k, v in cheat_counter.items()], key=lambda x: x[0], reverse=True
    )
    for k, v in sorted_cheat_counter:
        print(k, v)

    return sum(v for k, v in sorted_cheat_counter if k >= amount_to_save)


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    amount_to_save = 50 if testing else 100
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, amount_to_save))

import itertools
import re

from aoc.io import this_year_day


def produce_lock(lines):
    assert len(lines) == 5
    values = [0, 0, 0, 0, 0]
    for line in lines:
        for i, c in enumerate(line):
            if c == "#":
                values[i] += 1
    return values


def produce_key(lines):
    assert len(lines) == 5
    values = [5, 5, 5, 5, 5]
    for line in lines:
        for i, c in enumerate(line):
            if c == ".":
                values[i] -= 1
    return values


def produce_keys_and_locks(lines):
    keys = []
    locks = []
    for start_index in range(0, len(lines), 8):
        these_lines = lines[start_index : start_index + 7]
        start_line = these_lines[0]
        if re.compile("^#+$").match(start_line):
            locks.append(produce_lock(these_lines[1:-1]))
        elif re.compile(r"^\.+$").match(start_line):
            keys.append(produce_key(these_lines[1:-1]))
        else:
            raise ValueError("Shouldn't be here")

    return keys, locks


def overlap(key, lock):
    return any(s > 5 for s in (sum(t) for t in zip(key, lock)))


def calc_num_fits_and_overlaps(keys, locks):
    num_fits = 0
    num_overlaps = 0
    for key, lock in itertools.product(keys, locks):
        if overlap(key, lock):
            num_overlaps += 1
        else:
            num_fits += 1
    return num_fits, num_overlaps


def main(lines):
    keys, locks = produce_keys_and_locks(lines)
    num_fits, _ = calc_num_fits_and_overlaps(keys, locks)
    return num_fits


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

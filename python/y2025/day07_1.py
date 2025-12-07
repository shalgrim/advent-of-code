from collections import defaultdict

from coding_puzzle_tools import read_input


def process_input(lines: list[str]) -> tuple:
    beam_location = -1, -1
    tachyons_by_x = defaultdict(list)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ".":
                continue
            elif c == "^":
                tachyons_by_x[x].append(y)
            else:
                assert c == "S"
                beam_location = x, y
    return beam_location, tachyons_by_x


def get_num_splits(beam_location, tachyons_by_x):
    beam_x, beam_y = beam_location
    # base-case: no more splits
    if beam_y > max(tachyons_by_x[beam_x], default=0):
        return 0

    # find where it splits
    tachyon_y = min([tach for tach in tachyons_by_x[beam_x] if tach >= beam_y])
    return (
        1
        + get_num_splits((beam_x - 1, tachyon_y), tachyons_by_x)
        + get_num_splits((beam_x + 1, tachyon_y), tachyons_by_x)
    )


def main(lines: list[str]) -> int:
    beam_location, tachyons_by_x = process_input(lines)
    return get_num_splits(beam_location, tachyons_by_x)


if __name__ == "__main__":
    print(main(read_input()))

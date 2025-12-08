from collections import defaultdict

from coding_puzzle_tools import read_input
from y2025.day07_1 import process_input


def main(lines: list[str]) -> int:
    beam_location, tachyons_by_x = process_input(lines)
    beam_counts_by_x = defaultdict(int)
    beam_counts_by_x[beam_location[0]] = 1
    for line in lines[1:]:
        for x, c in enumerate(line):
            if c == ".":
                continue
            beam_counts_by_x[x - 1] += beam_counts_by_x[x]
            beam_counts_by_x[x + 1] += beam_counts_by_x[x]
            beam_counts_by_x[x] = 0
            # NB: There will be a problem if two tachyons are next to each other
            # NB: There will be a problem if tachyon is on edge
    return sum(beam_counts_by_x.values())


if __name__ == "__main__":
    print(main(read_input()))

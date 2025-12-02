from copy import copy

from aoc.io import this_year_day
from y2024.day09_1 import checksum, expand


def main(text):
    expanded = expand(text)
    print(f"{len(expanded)=}")
    rearranged = copy(expanded)
    max_file_id = max({file_id for file_id in rearranged if file_id != "."})
    min_file_id = 0
    for file_id in range(max_file_id, min_file_id, -1):
        print(f"{file_id=}")
        file_id_starts = rearranged.index(file_id)
        file_id_count = rearranged.count(file_id)
        massive_string = "".join(c if c == "." else "X" for c in rearranged)
        if (space_available_at := massive_string.find("." * file_id_count)) != -1:
            if space_available_at >= file_id_starts:  # only move to the left
                continue
            for i in range(file_id_count):
                rearranged[space_available_at + i] = file_id
                rearranged[file_id_starts + i] = "."

    print("rearranged")
    answer = checksum(rearranged)
    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        text = f.read().strip()
    print(main(text))

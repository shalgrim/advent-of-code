from aoc.io import this_year_day
from y2024.day18_1 import main

# def main(lines, grid_size, num_to_fall):
#     ...

if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    grid_size = 7 if testing else 71
    # OK 3037
    # Not OK 3038
    num_to_fall = 21 if testing else 3037
    print(main(lines, grid_size, num_to_fall))

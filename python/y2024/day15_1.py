from aoc.io import this_year_day


def main(lines):
    ...


if __name__ == "__main__":
    # testing = False
    testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

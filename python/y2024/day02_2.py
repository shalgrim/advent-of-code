from aoc.io import this_year_day


def main(lines):
    ...


if __name__ == "__main__":
    year, day = this_year_day(pad_day=True)
    with open("../../data/{year}/input{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

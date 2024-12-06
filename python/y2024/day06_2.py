from aoc.io import this_year_day
from y2024.day06_1 import Direction, Map


def main(lines):
    loop_positions = []
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            print(f"{x=}, {y=}")
            map = Map(lines)
            if (x, y) in map.obstacles or (x, y) == map.guard_position:
                continue
            map.add_obstacle(x, y)
            while map.guard_within() and not map.looped:
                map.move_guard()
            if map.looped:
                loop_positions.append((x, y))
    return len(loop_positions)


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

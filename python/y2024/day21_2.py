from aoc.io import this_year_day
from y2024.day21_1 import numericize, find_all_shortest_paths_for_second_robot


def find_shortest_length_26th_robot(code):
    # Well this very quickly becomes untenable I can't get i=3 to print out
    # So I will need to find a shorter approach
    # Which might just be at each step reducing down to one shortest path
    # But that won't work so then you're looking at maybe narrowing down to the set of paths that match the current shortest distance
    # Or maybe there's some smarts you can use to determine which path will give you the shortest future path
    # There's also maybe something you could do around caching and trying to piece together from known paths
    # Because my goodness it shouldn't be too long before we know the shortest everything between any two A's
    paths = find_all_shortest_paths_for_second_robot(code, 25)
    shortest_distance = min(len(a) for a in paths)
    return shortest_distance


def complexity(code):
    return find_shortest_length_26th_robot(code) * numericize(code)


def main(lines):
    complexities = []
    for i, line in enumerate(lines):
        c = complexity(line)
        print(f"{c=}")
        complexities.append(c)
    return sum(complexities)


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

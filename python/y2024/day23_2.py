import itertools

from aoc.io import this_year_day
from y2024.day23_1 import make_connections


def all_connected(combo, connections):
    for computer in combo:
        remaining = set(combo)
        remaining.remove(computer)
        if not remaining.issubset(set(connections[computer])):
            return False
    return True


def main(lines):
    connections = make_connections(lines)
    computers = sorted(connections.keys())

    biggest_network = set()

    for computer in computers:
        potential_biggest_network = set(connections[computer])
        potential_biggest_network.add(computer)

        if len(potential_biggest_network) < len(biggest_network):
            continue

        for n in range(len(potential_biggest_network), len(biggest_network), -1):
            inner_broke = False
            for combo in itertools.combinations(potential_biggest_network, n):
                # check that everything in combo is connected to each other
                if all_connected(combo, connections):
                    biggest_network = set(combo)
                    inner_broke = True
                    break
            if inner_broke:
                break

    return ",".join(sorted(biggest_network))


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

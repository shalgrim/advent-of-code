import itertools
from collections import defaultdict

from aoc.io import this_year_day


def make_connections(lines):
    answer = defaultdict(list)
    for line in lines:
        c1, c2 = line.split("-")
        answer[c1].append(c2)
        answer[c2].append(c1)
    return answer


def main(lines):
    connections = make_connections(lines)

    networks_of_three = set()
    for a, a_conns in connections.items():
        for b, c in itertools.combinations(a_conns, 2):
            if c in connections[b]:
                networks_of_three.add(tuple(sorted([a, b, c])))

    t_networks = {network for network in networks_of_three if "t" in "".join(network)}
    starts_with_t_networks = {
        network
        for network in t_networks
        if ",".join(network).startswith("t") or ",t" in ",".join(network)
    }

    return len(starts_with_t_networks)


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

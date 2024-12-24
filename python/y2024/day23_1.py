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
    computers = set(connections.keys())

    # remove those we know are connected to three others
    possibilities = {c for c in computers if len(connections[c]) < 3}

    # now for each one...something
    networks_of_three = set()
    for p in possibilities:
        if any(p in t for t in networks_of_three):
            # We've already put this one in a network of three
            continue

        direct_connections = connections[p]

        if len(direct_connections) == 1:
            # It only connects to one other
            # So check if that one connects to two others (one will be p)
            # and that that third item only connects to the second item
            second_item = direct_connections[0]
            secondary_connections = connections[second_item]
            if len(secondary_connections) != 2:
                continue
            third_item = [c for c in secondary_connections if c != p][0]
            assert len(connections[third_item]) == 1
            networks_of_three.add((p, second_item, third_item))
        elif len(direct_connections) == 2:
            # Check that those two connections don't connect to anything else
            second_item, third_item = direct_connections
            potential_tuple = (p, second_item, third_item)
            if set(connections[second_item]).difference(set(potential_tuple)):
                continue
            if set(connections[third_item]).difference(set(potential_tuple)):
                continue
            networks_of_three.add(potential_tuple)
        else:
            raise ValueError("Shouldn't be here")

    # Now I have all networks_of_three
    # TODO: do this with a generator expression like you learned the other day
    stringified = [",".join(t) for t in networks_of_three]
    return len([s for s in stringified if "t" in s])


if __name__ == "__main__":
    testing = True
    # testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

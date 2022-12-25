from itertools import permutations


class Valve:
    def __init__(self, name, flow_rate, destinations):
        self.name = name
        self.flow_rate = flow_rate
        self.destinations = destinations
        self.open = False

    def __str__(self):
        return f'{self.name}, {self.flow_rate}, {"open" if self.open else "closed"}, {self.destinations}'


def build_valve_from_line(line):
    part1, part2 = line.split('; ')
    valve_id = part1.split()[1]
    flow_rate = int(part1.split('=')[-1])
    if 'valves' in line:
        destinations = line.split('valves ')[-1]
        destinations = destinations.split(', ')
    else:
        destinations = [line.split('valve ')[-1]]

    return Valve(valve_id, flow_rate, destinations)


def build_valves(lines):
    valves = [build_valve_from_line(line) for line in lines]
    return {v.name: v for v in valves}


def total_pressure_release(opened_at_tracker, valves):
    answer = 0
    for valve_id, time_opened in opened_at_tracker.items():
        answer += (30 - time_opened) * valves[valve_id].flow_rate
    return answer


def pick_next_valve(current_valve, valves):
    possible_destinations = [
        valves[valve_id] for valve_id in valves[current_valve.name].destinations
    ]
    filtered_destinations = []
    while not filtered_destinations:
        filtered_destinations = [
            v for v in possible_destinations if v.flow_rate > 0 and not v.open
        ]
        if not filtered_destinations:
            new_possible_destinations = []
            for pd in possible_destinations:
                new_possible_destinations.extend(
                    [valves[valve_id] for valve_id in valves[pd.name].destinations]
                )
    max_flow_rate = max(v.flow_rate for v in filtered_destinations)
    matching_valve = [v for v in filtered_destinations if v.flow_rate == max_flow_rate][
        0
    ]
    return matching_valve


def pick_next_valve_smart(current_valve, valves):
    closed_valves_by_flow_rate = get_closed_valves_by_flow_rate(valves)
    closed_valves_by_hops = get_closed_valves_by_hops(valves)
    # then pick the best next valve
    # but note this still is not guaranteed to get the best valve...we'll really have to do a BFS
    # Hm, we could do something like all possible orderings of closed valves then go through each one minimizing hops and take the max from there
    pass


def main(lines):
    valves = build_valves(lines)
    time = 0
    current_valve = valves['AA']
    opened_at_tracker = {}

    while time < 30:
        if all(v.open or not v.flow_rate for v in valves.values()):
            break
        if current_valve.open or not current_valve.flow_rate:
            current_valve = pick_next_valve(current_valve, valves)
        else:
            current_valve.open = True
            opened_at_tracker[current_valve.name] = time + 1
        time += 1

    return total_pressure_release(opened_at_tracker, valves)


def main_bfs(lines):
    valves = build_valves(lines)
    non_zero_valve_ids = [v.name for v in valves.values() if v.flow_rate]
    non_zero_perms = permutations(non_zero_valve_ids)
    for nzp in non_zero_perms:
        shortest_route = shortest_route_through_ordering(nzp)

    # routes =
    # routes_non_zero = itertools
    print('hello')


def find_shortest_routes_from_a_to_b(a, b, valves):
    possible_routes = [[dest] for dest in valves[a].destinations]
    while not any(route[-1] == b for route in possible_routes):
        new_possible_routes = []
        for pr in possible_routes:
            current_node = pr[-1]
            for new_destination in valves[current_node].destinations:
                new_possible_routes.append(pr + [new_destination])
        possible_routes = new_possible_routes

    shortest_routes = [route for route in possible_routes if route[-1] == b]
    return shortest_routes


def find_shortest_routes_through_valves(valves, all_valves, starting_name='AA'):
    all_possible_routes = [[starting_name]]
    current_node = starting_name
    for valve in valves:
        new_all_possible_routes = []
        shortest_routes_to_next_step = find_shortest_routes_from_a_to_b(
            current_node, valve, all_valves
        )
        for existing_route in all_possible_routes:
            for new_route in shortest_routes_to_next_step:
                new_all_possible_routes.append(existing_route + new_route)
        all_possible_routes = new_all_possible_routes

    return [tuple(route) for route in all_possible_routes]


def score_route(route, valves):
    opened_at_tracker = {}
    time = 0
    for valve_name in route[1:]:
        if time >= 30:
            break
        next_valve = valves[valve_name]
        time += 1  # cuz I moved there
        if next_valve.flow_rate and valve_name not in opened_at_tracker:
            if time >= 30:
                break  # don't open valve if no time
            time += 1  # let's open it
            opened_at_tracker[next_valve.name] = time

    score = 0
    for valve_id, time_opened in opened_at_tracker.items():
        score += (30 - time_opened) * valves[valve_id].flow_rate
    return score


def main_2(lines):
    valves = build_valves(lines)
    non_zero_valves = [v for v in valves.values() if v.flow_rate]
    sorted_valves = sorted(non_zero_valves, key=lambda x: x.flow_rate, reverse=True)
    sorted_valve_names = [sv.name for sv in sorted_valves]

    # Note: Not guaranteed to find best route
    # And in fact it's not the route they say to take in the test
    # The first issue to address, though, is that both of my shortest routes go from JJ to DD directly, which shouldn't be possible
    # Another issue is that my logic makes me go through E near the end since it's a low rate node, but I'd already visited it by necessity earlier
    # So three things currently to look into and fix
    # 1. In my logic, don't force yourself to find a route from A to B if B has already been visited (although I can maybe imagine a scenario where it's better to skip over a low flow node)
    # 2. You're just going to have to score more routes...since the route they say is the best is not the optimal ordering
    # 3. Why am I allowing myself to go from J to B?
    shortest_routes_through_valves = set(
        find_shortest_routes_through_valves(sorted_valve_names, valves, 'AA')
    )
    route_scores = [
        score_route(route, valves) for route in shortest_routes_through_valves
    ]
    return max(route_scores)


if __name__ == '__main__':
    with open('../../data/2022/test16.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main_2(lines))

"""
https://adventofcode.com/2022/day/16
"""
from copy import copy
from dataclasses import dataclass
from typing import List, Set


def build_valve_from_line(line):
    part1, part2 = line.split("; ")
    valve_id = part1.split()[1]
    flow_rate = int(part1.split("=")[-1])
    if "valves" in line:
        destinations = line.split("valves ")[-1]
        destinations = destinations.split(", ")
    else:
        destinations = [line.split("valve ")[-1]]

    return Valve(valve_id, flow_rate, destinations)


def build_valves(lines):
    valves = [build_valve_from_line(line) for line in lines]
    return {v.name: v for v in valves}


class Valve:
    def __init__(self, name, flow_rate, destinations):
        self.name = name
        self.flow_rate = flow_rate
        self.destinations = destinations


@dataclass
class State:
    """The main point of this class is to track what we've seen so we don't go back and thus narrow our search space"""

    current_valve_id: str
    opened_valves: dict[str, int]  # valve_id: time_opened

    def __hash__(self):
        return hash((self.current_valve_id, tuple(self.opened_valves.items())))


def calc_total_pressure_release(state: State, valves):
    opened_at_tracker = state.opened_valves
    answer = 0
    for valve_id, time_opened in opened_at_tracker.items():
        answer += (30 - time_opened) * valves[valve_id].flow_rate
    return answer


def all_flow_positive_valves_open(
    most_recent_state: State, valves: dict[str, Valve]
) -> bool:
    positive_valve_ids = {k for k, v in valves.items() if v.flow_rate > 0}
    opened_valve_ids = set(most_recent_state.opened_valves.keys())
    return not positive_valve_ids.difference(opened_valve_ids)


def does_not_contain(states: list[State], state: State) -> bool:
    """Currently not used since I think my `not in` works"""
    return not any(s == state for s in states)


def generate_new_moves(
    state: State,
    t: int,
    valves: dict[str, Valve],
) -> list[State]:
    if all_flow_positive_valves_open(state, valves):
        return []

    current_valve_id = state.current_valve_id
    current_valve = valves[current_valve_id]
    possible_next_moves = copy(current_valve.destinations)
    possible_next_states = []

    for move in possible_next_moves:
        new_state = State(move, copy(state.opened_valves))
        possible_next_states.append(new_state)

    if current_valve_id not in state.opened_valves and current_valve.flow_rate:
        new_opened_valves = copy(state.opened_valves)
        new_opened_valves[current_valve_id] = t
        new_state = State(current_valve_id, new_opened_valves)
        possible_next_states.append(new_state)

    return possible_next_states


def main(lines):
    """BFS that checks all possibilities then finds max"""
    valves = build_valves(lines)
    initial_state = State("AA", {})
    seen_states = set()
    seen_states.add(initial_state)
    current_states = set()
    current_states.add(initial_state)

    for t in range(1, 31):
        print(f"== Minute {t} ==")
        new_current_states = set()
        for state in current_states:
            for new_state in generate_new_moves(state, t, valves):
                if new_state not in seen_states:
                    new_current_states.add(new_state)
        seen_states.update(new_current_states)
        current_states = new_current_states

    totals = [calc_total_pressure_release(state, valves) for state in seen_states]
    return max(totals)


if __name__ == "__main__":
    with open("../../data/2022/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

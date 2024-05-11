"""
https://adventofcode.com/2022/day/16
"""
from copy import copy
from dataclasses import dataclass
from itertools import permutations


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


def calc_total_pressure_release(state_history, valves):
    final_state = state_history.states[-1]
    opened_at_tracker = final_state.opened_valves
    answer = 0
    for valve_id, time_opened in opened_at_tracker.items():
        answer += (30 - time_opened) * valves[valve_id].flow_rate
    return answer


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


class StateHistory:
    def __init__(self, states: list[State]):
        self.states = states


def generate_new_moves(
    state_history: StateHistory, t: int, valves: dict[str, Valve]
) -> list[State]:
    # TODO: if all flow-rate-positive valves are open, just return a list with only the current state
    states = state_history.states
    most_recent_state = states[-1]
    current_valve_id = most_recent_state.current_valve_id
    current_valve = valves[current_valve_id]
    possible_next_moves = copy(current_valve.destinations)
    possible_next_states = []
    for move in possible_next_moves:
        new_state = State(move, copy(most_recent_state.opened_valves))

        # TODO: Check that this `not in` works as I expect...make a test
        if new_state not in states:
            possible_next_states.append(new_state)

    if current_valve_id not in states[-1].opened_valves and current_valve.flow_rate:
        new_opened_valves = copy(states[-1].opened_valves)
        new_opened_valves[current_valve_id] = t
        new_state = State(current_valve_id, new_opened_valves)
        possible_next_states.append(new_state)

    return possible_next_states


def main(lines):
    """BFS that checks all possibilities then finds max"""
    valves = build_valves(lines)
    state_histories = [StateHistory([State("AA", {})])]

    for t in range(1, 31):
        print(f"== Minute {t} ==")
        new_state_histories = []
        for history in state_histories:
            for new_state in generate_new_moves(history, t, valves):
                new_state_list = copy(history.states)
                new_state_list.append(new_state)
                new_state_histories.append(StateHistory(new_state_list))
        state_histories = new_state_histories

    totals = [
        calc_total_pressure_release(history, valves) for history in state_histories
    ]
    return max(totals)


if __name__ == "__main__":
    with open("../../data/2022/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

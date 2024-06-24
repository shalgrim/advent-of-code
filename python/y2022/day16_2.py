import itertools
from copy import copy
from dataclasses import dataclass
from itertools import combinations
from typing import Tuple

from y2022.day16_1 import build_valves, Valve, all_flow_positive_valves_open


@dataclass
class State:
    """The main point of this class is to track what we've seen so we don't go back and thus narrow our search space"""

    current_valve_ids: Tuple[str, str]
    opened_valves: dict[str, int]  # valve_id: time_opened

    def __hash__(self):
        return hash(
            (frozenset(self.current_valve_ids), tuple(self.opened_valves.items()))
        )


def calc_total_pressure_release(state: State, valves):
    opened_at_tracker = state.opened_valves
    answer = 0
    for valve_id, time_opened in opened_at_tracker.items():
        answer += (26 - time_opened) * valves[valve_id].flow_rate
    return answer


def generate_new_moves(state: State, t: int, valves: dict[str, Valve]) -> list[State]:
    if all_flow_positive_valves_open(state, valves):
        return []

    current_valve_ids = state.current_valve_ids
    current_valve1 = valves[current_valve_ids[0]]
    current_valve2 = valves[current_valve_ids[1]]
    possible_next_moves_1 = copy(current_valve1.destinations)
    possible_next_moves_2 = copy(current_valve2.destinations)
    can_open_valve_1 = current_valve_ids[0] not in state.opened_valves
    can_open_valve_2 = current_valve_ids[1] not in state.opened_valves
    possible_next_states = []

    if can_open_valve_1 and can_open_valve_2:
        new_opened_valves = copy(state.opened_valves)
        new_opened_valves[current_valve_ids[0]] = t
        new_opened_valves[current_valve_ids[1]] = t
        return [
            State(current_valve_ids, new_opened_valves),
        ]
    elif can_open_valve_1:
        for next_valve_id in possible_next_moves_2:
            new_opened_valves = copy(state.opened_valves)
            new_opened_valves[current_valve_ids[0]] = t
            possible_next_states.append(
                State((current_valve_ids[0], next_valve_id), new_opened_valves)
            )
    elif can_open_valve_2:
        for next_valve_id in possible_next_moves_1:
            new_opened_valves = copy(state.opened_valves)
            new_opened_valves[current_valve_ids[1]] = t
            possible_next_states.append(
                State((next_valve_id, current_valve_ids[1]), new_opened_valves)
            )

    for next_valve_id_1, next_valve_id_2 in itertools.product(
        possible_next_moves_1, possible_next_moves_2
    ):
        possible_next_states.append(
            State((next_valve_id_1, next_valve_id_2), copy(state.opened_valves))
        )

    return possible_next_states


def main(lines):
    """BFS that checks all possibilities then finds max"""
    valves = build_valves(lines)
    initial_state = State(("AA", "AA"), {})
    seen_states = set()
    seen_states.add(initial_state)
    current_states = set()
    current_states.add(initial_state)
    for t in range(1, 27):
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

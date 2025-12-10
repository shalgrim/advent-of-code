import itertools
from collections import Counter

from coding_puzzle_tools import read_input
from y2025.day10_1 import Machine


def get_total_joltage(combo, num_required_voltages):
    joltages = Counter(list(itertools.chain(*combo)))
    return [joltages[n] for n in range(num_required_voltages)]


def min_button_presses(machine: Machine):
    sorted_joltage_index_tuples = sorted(
        [(joltage, i) for i, joltage in enumerate(machine.required_joltages)],
        reverse=True,
    )
    existing_combos = []
    joltage, index = sorted_joltage_index_tuples[0]
    buttons_of_interest = [button for button in machine.buttons if index in button]
    for combo in itertools.combinations_with_replacement(buttons_of_interest, joltage):
        total_joltage = get_total_joltage(combo, len(machine.required_joltages))
        if any(t[0] > t[1] for t in zip(total_joltage, machine.required_joltages)):
            # something is too high so no additional button pushing can help us
            continue
        existing_combos.append(combo)
        if total_joltage == machine.required_joltages:
            return len(combo)

    # Now to figure out the additional cases
    for joltage, index in sorted_joltage_index_tuples[1:]:
        new_combos = []
        print(f"{joltage=}")
        print(f"{len(existing_combos)=}")
        print("==========")
        for existing_combo in existing_combos:
            existing_joltage = get_total_joltage(
                existing_combo, len(machine.required_joltages)
            )
            needed_pushes = machine.required_joltages[index] - existing_joltage[index]
            buttons_of_interest = [
                button for button in machine.buttons if index in button
            ]
            for combo in itertools.combinations_with_replacement(
                buttons_of_interest, needed_pushes
            ):
                new_combo = tuple(list(existing_combo) + list(combo))
                total_joltage = get_total_joltage(
                    new_combo, len(machine.required_joltages)
                )
                if any(
                    t[0] > t[1] for t in zip(total_joltage, machine.required_joltages)
                ):
                    continue
                new_combos.append(new_combo)
        matching_combos = [
            combo
            for combo in new_combos
            if get_total_joltage(combo, len(machine.required_joltages))
            == machine.required_joltages
        ]
        if matching_combos:
            return min(len(mc) for mc in matching_combos)
        existing_combos = new_combos


def main(lines: list[str]) -> int:
    machines = [Machine(line) for line in lines]
    answer = 0
    for i, machine in enumerate(machines):
        print(f"machine {i}")
        sub_answer = min_button_presses(machine)
        print(f"{sub_answer=}")
        answer += sub_answer
    return answer


if __name__ == "__main__":
    print(main(read_input()))

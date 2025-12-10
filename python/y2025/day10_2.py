import itertools

from coding_puzzle_tools import read_input
from y2025.day10_1 import JoltageError, Machine


def min_button_presses(machine: Machine):
    i = max(machine.required_joltages)
    while True:
        print(f"sub i: {i}")
        for combo in itertools.combinations_with_replacement(
            range(len(machine.buttons)), i
        ):
            for button in combo:
                machine.push_joltage_button(button)
                try:
                    machine.joltage_check()
                except JoltageError:
                    break
            else:
                if machine.joltage_check():
                    return i
            machine.joltage_reset()
        i += 1


def main(lines: list[str]) -> int:
    machines = [Machine(line) for line in lines]
    answer = 0
    for i, machine in enumerate(machines):
        print(f"{i=}")
        sub_answer = min_button_presses(machine)
        print(f"{sub_answer=}")
        answer += sub_answer
    return answer


if __name__ == "__main__":
    print(main(read_input()))

import math

from y2023.day08_1 import process_input


def main(lines):
    instructions, map = process_input(lines)
    start_states = [key for key in map if key[-1] == "A"]
    moves_by_state = []

    for start_state in start_states:
        current_state = start_state
        num_moves = 0
        instruction_index = 0

        while current_state[-1] != "Z":
            instruction = instructions[instruction_index]
            current_state = map[current_state][0] if instruction == "L" else map[current_state][1]
            num_moves += 1
            instruction_index = (instruction_index + 1) % len(instructions)

        moves_by_state.append(num_moves)

    return math.lcm(*moves_by_state)


if __name__ == "__main__":
    with open("../../data/2023/input08.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

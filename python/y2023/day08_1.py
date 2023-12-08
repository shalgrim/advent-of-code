def process_input(lines):
    instructions = lines[0]

    map = {}
    for line in lines[2:]:
        key = line.split()[0]
        elements = line.split("=")[1].strip()[1:-1]
        map[key] = tuple([e.strip() for e in elements.split(",")])

    return instructions, map


def main(lines):
    instructions, map = process_input(lines)
    current_state = "AAA"
    num_moves = 0
    instruction_index = 0
    num_loops = -1
    seen_states = set()

    while current_state != "ZZZ":
        if instruction_index == 0:
            num_loops += 1
        print(f"{num_loops=}, {instruction_index=}, {num_moves=}")
        instruction = instructions[instruction_index]
        state = (current_state, instruction_index)
        if state in seen_states:
            print("YOU'VE SEEN ME!!!")
        seen_states.add(state)

        if instruction == "L":
            current_state = map[current_state][0]
        elif instruction == "R":
            current_state = map[current_state][1]
        num_moves += 1
        instruction_index = (instruction_index + 1) % len(instructions)

    return num_moves


if __name__ == "__main__":
    with open("../../data/2023/input08.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

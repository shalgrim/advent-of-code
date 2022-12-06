from y2022.day05_1 import build_stacks


def process_instructions(stacks, lines):
    for i, line in enumerate(lines):
        if not line:
            break

    for line in lines[i + 1 :]:
        words = line.split()
        num_to_move = int(words[1])
        from_stack = int(words[3]) - 1
        to_stack = int(words[5]) - 1

        elements = stacks[from_stack][-num_to_move:]
        stacks[from_stack] = stacks[from_stack][:-num_to_move]
        stacks[to_stack].extend(elements)


def main(lines):
    stacks = build_stacks(lines)
    process_instructions(stacks, lines)
    answer = ''.join(stack[-1] for stack in stacks)
    return answer


if __name__ == '__main__':
    with open('../../data/2022/input05.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))

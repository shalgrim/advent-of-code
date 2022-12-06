def process_instructions(stacks, lines):
    for i, line in enumerate(lines):
        if not line:
            break

    for line in lines[i + 1 :]:
        words = line.split()
        num_to_move = int(words[1])
        from_stack = int(words[3]) - 1
        to_stack = int(words[5]) - 1

        for _ in range(num_to_move):
            element = stacks[from_stack].pop()
            stacks[to_stack].append(element)


def build_stacks(lines):
    for i, line in enumerate(lines):
        if not line:
            break
    number_line = lines[i - 1]
    num_stacks = int(number_line.split()[-1])
    stacks = [list() for _ in range(num_stacks)]
    for line_index in range(i - 2, -1, -1):
        for i, c in enumerate(lines[line_index]):
            if ord('A') <= ord(c) <= ord('Z'):
                # figure out what stack it goes in
                stack_index = i // 4
                stacks[stack_index].append(c)

    return stacks


def main(lines):
    stacks = build_stacks(lines)
    process_instructions(stacks, lines)
    answer = ''.join(stack[-1] for stack in stacks)
    return answer


if __name__ == '__main__':
    with open('../../data/2022/input05.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))

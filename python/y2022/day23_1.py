def propose_move(elf, elves):
    pass


def elves_from_lines(lines):
    answer = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                answer.append((x, y))
    return answer


def lines_to_elves(elves):
    left = min(elf[0] for elf in elves)
    right = max(elf[0] for elf in elves)
    top = min(elf[1] for elf in elves)
    bottom = max(elf[1] for elf in elves)
    lines = []
    for y in range(top, bottom + 1):
        line = []
        for x in range(left, right + 1):
            c = "#" if (x, y) in elves else "."
            line.append(c)
        lines.append("".join(line))
    return lines


def main(lines):
    pass


if __name__ == "__main__":
    with open("../../data/2022/input22.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

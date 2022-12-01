def get_elves(lines):
    elves = []
    elf_carrying = []
    for line in lines:
        if line:
            elf_carrying.append(int(line))
        else:
            elves.append(elf_carrying)
            elf_carrying = []
    return elves


def main(lines):
    elves = get_elves(lines)
    elf_sums = [sum(elf) for elf in elves]
    sorted_sums = sorted(elf_sums, reverse=True)
    return sum(sorted_sums[:3])


if __name__ == '__main__':
    with open('../data/input01.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    answer = main(lines)
    print(answer)

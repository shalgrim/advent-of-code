def main(lines):
    l1 = [int(line.split()[0]) for line in lines]
    l2 = [int(line.split()[1]) for line in lines]
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    return sum([abs(foo[0] - foo[1]) for foo in zip(sorted_l1, sorted_l2)])


if __name__ == "__main__":
    with open("../../data/2024/input01.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

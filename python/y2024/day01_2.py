from collections import Counter


def similarity_score(num, counter):
    return counter.get(num, 0)


def main(lines):
    l1 = [int(line.split()[0]) for line in lines]
    l2 = [int(line.split()[1]) for line in lines]
    counter = Counter(l2)
    return sum(num * counter.get(num, 0) for num in l1)


if __name__ == "__main__":
    with open("../../data/2024/input01.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

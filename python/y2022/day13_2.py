from functools import cmp_to_key
from itertools import zip_longest


def packet_sorter(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
        else:
            return 0
    elif isinstance(p1, list) and isinstance(p2, list):
        for e1, e2 in zip_longest(p1, p2):
            if e1 is None:
                return -1
            if e2 is None:
                return 1
            element_answer = packet_sorter(e1, e2)
            if element_answer == 0:
                continue
            return element_answer
        return 0
    elif isinstance(p1, list):
        for e1, e2 in zip_longest(p1, [p2]):
            if e1 is None:
                return -1
            if e2 is None:
                return 1
            element_answer = packet_sorter(e1, e2)
            if element_answer == 0:
                continue
            return element_answer
        return 0
    else:  # p1 is int, p2 is list
        for e1, e2 in zip_longest([p1], p2):
            if e1 is None:
                return -1
            if e2 is None:
                return 1
            element_answer = packet_sorter(e1, e2)
            if element_answer == 0:
                continue
            return element_answer
        return 0


def main(lines):
    packets = [eval(line) for line in lines if line]
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=cmp_to_key(packet_sorter))
    index1 = sorted_packets.index([[2]]) + 1
    index2 = sorted_packets.index([[6]]) + 1
    return index1 * index2


if __name__ == '__main__':
    with open('../../data/2022/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

from itertools import zip_longest


def build_packets(lines):
    packets = []
    for i in range(0, len(lines), 3):
        first_line = lines[i]
        second_line = lines[i + 1]
        packets.append((eval(first_line), eval(second_line)))

    return packets


def in_correct_order(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return True
        elif p1 > p2:
            return False
        else:
            return -1
    elif isinstance(p1, list) and isinstance(p2, list):
        for e1, e2 in zip_longest(p1, p2):
            if e1 is None:
                return True
            if e2 is None:
                return False
            element_answer = in_correct_order(e1, e2)
            if element_answer == -1:
                continue
            return element_answer
        return -1
    elif isinstance(p1, list):
        for e1, e2 in zip_longest(p1, [p2]):
            if e1 is None:
                return True
            if e2 is None:
                return False
            element_answer = in_correct_order(e1, e2)
            if element_answer == -1:
                continue
            return element_answer
        return -1
    else:  # p1 is int, p2 is list
        for e1, e2 in zip_longest([p1], p2):
            if e1 is None:
                return True
            if e2 is None:
                return False
            element_answer = in_correct_order(e1, e2)
            if element_answer == -1:
                continue
            return element_answer
        return -1


def main(lines):
    packets = build_packets(lines)
    packet_indexes_in_correct_order = set()
    for (
        i,
        (p1, p2),
    ) in enumerate(packets):
        if in_correct_order(p1, p2) == True:
            packet_indexes_in_correct_order.add(i + 1)

    print(sorted(list(packet_indexes_in_correct_order)))
    return sum(packet_indexes_in_correct_order)


if __name__ == '__main__':
    with open('../../data/2022/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

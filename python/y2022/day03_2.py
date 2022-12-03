from y2022.day03_1 import priority


def main(lines):
    answer = 0
    for i in range(0, len(lines), 3):
        first = set(lines[i])
        second = set(lines[i+1])
        third = lines[i+2]
        shared_item = first.intersection(second).intersection(third).pop()
        answer += priority(shared_item)

    return answer


if __name__ == '__main__':
    with open('../../data/2022/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

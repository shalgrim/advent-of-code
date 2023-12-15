from collections import defaultdict
from y2023.day15_1 import hash


def calc_focusing_power(boxes):
    answer = 0
    for i in range(1, 256):
        box_contents = boxes[i - 1]
        for j, val in enumerate(box_contents.values(), start=1):
            answer += i * j * val

    return answer


def main(text):
    steps = text.split(",")
    boxes = defaultdict(dict)
    for step in steps:
        if step[-1] == "-":
            label = step[:-1]
            box = hash(label)
            boxes[box].pop(label, None)
        else:
            label, focal_length = step.split("=")
            box = hash(label)
            boxes[box][label] = int(focal_length)

    answer = calc_focusing_power(boxes)
    return answer


if __name__ == "__main__":  # 226357 is wrong
    with open("../../data/2023/input15.txt") as f:
        txt = f.read().strip()
    print(main(txt))

from collections import defaultdict

from y2023.day15_1 import hash


def calc_focusing_power(boxes):
    answer = 0
    for i in range(1, 257):
        box_contents = boxes[i - 1]
        for j, val in enumerate(box_contents.values(), start=1):
            answer += i * j * val

    return answer


def format_box(k, v):
    return f"[{k} {v}]"


def print_boxes(boxes):
    for i in range(256):
        if i not in boxes:
            continue
        box_contents = boxes[i]
        if box_contents:
            outline = f"Box {i}: "
            outline += " ".join([f"[{k} {v}]" for k, v in box_contents.items()])
            print(outline)


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
        # input("Go to next step")
        # print(f'After "{step}":')
        # print_boxes(boxes)
        # print()

    print_boxes(boxes)
    answer = calc_focusing_power(boxes)
    return answer


if __name__ == "__main__":  # 226357 is wrong
    # main("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
    with open("../../data/2023/input15.txt") as f:
        txt = f.read().strip()
    print(main(txt))

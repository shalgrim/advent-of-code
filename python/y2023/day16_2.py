from y2023.day16_1 import Direction, Beam
from y2023.day16_1 import main as main1


def main(lines):
    best_answer = 0

    print("DOWN")
    for x in range(len(lines[0])):
        print(f"{x=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, x, 0, Direction.DOWN))

    print("UP")
    for x in range(len(lines[0])):
        print(f"{x=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, x, len(lines) - 1, Direction.UP))

    print("RIGHT")
    for y in range(len(lines)):
        print(f"{y=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, 0, y, Direction.RIGHT))

    print("LEFT")
    for y in range(len(lines)):
        print(f"{y=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, len(lines) - 1, y, Direction.LEFT))

    return best_answer


if __name__ == "__main__":
    with open("../../data/2023/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

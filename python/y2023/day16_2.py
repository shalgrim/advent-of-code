# from y2023.day16_1 import Direction, Beam
# from y2023.day16_1 import main as main1
from day16_1 import Direction, Beam
from day16_1 import main as main1


def main(lines):
    """
    TODO: Refactor for speed:
    1. Instead of breadth-processing of beams, do depth-processing.
       I.e., run each beam until it can't move or hits a point that another beam has already hit
    2. Track from each state what cells it will energize
    3. So when a beam reaches a previously-seen state, we can immediately energize those cells
    """
    best_answer = 0

    # STATUS (grid is 110x110, 12,110 cells)
    #  Through: LEFT 75
    #  Best: 7987
    print("DOWN")
    for x in range(len(lines[0])):
        print(f"{x=}, {best_answer=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, x, 0, Direction.DOWN))

    print("UP")
    for x in range(len(lines[0])):
        print(f"{x=}, {best_answer=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, x, len(lines) - 1, Direction.UP))

    print("RIGHT")
    for y in range(len(lines)):
        print(f"{y=}, {best_answer=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, 0, y, Direction.RIGHT))

    print("LEFT")
    for y in range(len(lines)):
        print(f"{y=}, {best_answer=}")
        Beam.processed_states.clear()
        best_answer = max(best_answer, main1(lines, len(lines) - 1, y, Direction.LEFT))

    return best_answer


if __name__ == "__main__":
    with open("../../data/2023/input16.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

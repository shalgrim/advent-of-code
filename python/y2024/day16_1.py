import math
import sys
from dataclasses import dataclass
from enum import IntEnum
from typing import List


class Direction(IntEnum):
    E = 0
    S = 1
    W = 2
    N = 3


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


@dataclass
class State:
    x: int
    y: int
    dir: Direction
    has_turned: bool


def score_states(states: List[State]) -> int:
    answer = 0
    for state in states[1:]:
        if state.has_turned:
            answer += 1000
        else:
            answer += 1
    return answer


class Map:
    def __init__(self, lines):
        self.walls = set()
        self.best_score = math.inf
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                match char:
                    case "#":
                        self.walls.add((x, y))
                    case "S":
                        start_x, start_y = x, y
                    case "E":
                        self.end = x, y

        self.states = [State(start_x, start_y, Direction.E, False)]
        self.rightest = start_x
        self.highest = start_y
        self.closest = manhattan_distance((start_x, start_y), self.end)
        self.rightest_1 = -1
        self.highest_139 = math.inf

    def get_possible_moves(self):
        moves = []
        current_state = self.states[-1]
        me = current_state.x, current_state.y
        match current_state.dir:
            case Direction.E:
                facing_block = me[0] + 1, me[1]
                ccw_block = me[0], me[1] - 1
                cw_block = me[0], me[1] + 1
            case Direction.S:
                facing_block = me[0], me[1] + 1
                ccw_block = me[0] + 1, me[1]
                cw_block = me[0] - 1, me[1]
            case Direction.W:
                facing_block = me[0] - 1, me[1]
                cw_block = me[0], me[1] - 1
                ccw_block = me[0], me[1] + 1
            case Direction.N:
                facing_block = me[0], me[1] - 1
                ccw_block = me[0] - 1, me[1]
                cw_block = me[0] + 1, me[1]
            case _:
                raise ValueError(f"Unexpected Direction {current_state.dir}")
        if facing_block not in self.walls and all(
            facing_block != (state.x, state.y) for state in self.states
        ):
            moves.append(
                State(facing_block[0], facing_block[1], current_state.dir, False)
            )
        if not current_state.has_turned and cw_block not in self.walls:
            new_direction = Direction((current_state.dir + 1) % 4)
            moves.append(State(current_state.x, current_state.y, new_direction, True))
        if not current_state.has_turned and ccw_block not in self.walls:
            new_direction = Direction((current_state.dir - 1) % 4)
            moves.append(State(current_state.x, current_state.y, new_direction, True))

        return moves

    def find_best_route(self, move=None):
        if move is not None:
            self.states.append(move)
        current_state = self.states[-1]
        me = current_state.x, current_state.y
        if current_state.x > self.rightest:
            print(f"new rightest: {me=}")
            self.rightest = current_state.x
        if current_state.y < self.highest:
            print(f"new highest: {me=}")
            self.highest = current_state.y
        if current_state.y == 1 and current_state.x > self.rightest_1:
            print(f"new rightest_1: {me=}")
            self.rightest_1 = current_state.x
        if current_state.x == 139 and current_state.y < self.highest_139:
            print(f"new highest_139: {me=}")
            self.highest_139 = current_state.y

        distance = manhattan_distance(me, self.end)
        if distance < self.closest:
            print(f"new closest: {distance=} {me=}")
            self.closest = distance

        current_score = score_states(self.states)

        # base case
        if me == self.end:
            self.states.pop()
            print(f"Found path of {current_score=}")
            # sys.exit()
            return current_score

        # abort case
        if current_score > self.best_score:
            self.states.pop()
            return current_score

        possible_moves = self.get_possible_moves()

        # another abort case
        if not possible_moves:
            self.states.pop()
            return math.inf

        for move in possible_moves:
            score = self.find_best_route(move)
            self.best_score = min(score, self.best_score)

        self.states.pop()
        return self.best_score


def main(lines):
    map = Map(lines)
    return map.find_best_route()


if __name__ == "__main__":
    # TODO: Do Djikstra's (alternately add more logging around highest_n and rightest_n)
    with open(f"../../data/2024/test16_1.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    with open(f"../../data/2024/test16_2.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

    # sys.setrecursionlimit(10000)
    # with open(f"../../data/2024/input16.txt") as f:
    #     lines = [line.strip() for line in f.readlines()]
    # print(main(lines))
    # year, day = this_year_day(pad_day=True)
    # # testing = False
    # testing = True
    # filetype = "test" if testing else "input"
    # with open(f"../../data/{year}/{filetype}{day}.txt") as f:
    #     lines = [line.strip() for line in f.readlines()]
    # print(main(lines))

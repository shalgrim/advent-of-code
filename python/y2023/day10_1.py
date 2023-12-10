import sys
from copy import copy
from typing import List, Optional


def get_sloc(lines):
    for y, line in enumerate(lines):
        sindex = line.find("S")
        if sindex == -1:
            continue
        sloc = (sindex, y)
    return sloc


def get_possible_s_shapes(lines, sloc=None):
    x, y = sloc if sloc else get_sloc(lines)

    west = x > 0 and lines[y][x - 1] in "-LF"
    east = x < len(lines[0]) - 1 and lines[y][x + 1] in "-J7"
    north = y > 0 and lines[y - 1][x] in "|7F"
    south = y < len(lines) - 1 and lines[y + 1][x] in "|LJ"

    possibles = []
    if north and south:
        possibles.append("|")
    if east and west:
        possibles.append("-")
    if north and east:
        possibles.append("L")
    if north and west:
        possibles.append("J")
    if south and west:
        possibles.append("7")
    if south and east:
        possibles.append("F")

    return "".join(possibles)


def _generate_loop(lines: List[str], current_loop, s_shape) -> Optional[List[str]]:
    x, y = current_loop[-1]
    if len(current_loop) == 1:
        shape = str(s_shape)
    else:
        shape = lines[y][x]
    next_moves = []

    # north
    if y > 0:
        if ((x, y - 1) not in current_loop) or (
            len(current_loop) > 3 and (x, y - 1) not in current_loop[1:]
        ):
            if shape in "|LJ":
                next_moves.append((x, y - 1))

    # east
    if x < len(lines[0]) - 1:
        if ((x + 1, y) not in current_loop) or (
            len(current_loop) > 3 and (x + 1, y) not in current_loop[1:]
        ):
            if shape in "-LF":
                next_moves.append((x + 1, y))

    # south
    if y < len(lines) - 1:
        if ((x, y + 1) not in current_loop) or (
            len(current_loop) > 3 and (x, y + 1) not in current_loop[1:]
        ):
            if shape in "|7F":
                next_moves.append((x, y + 1))

    # west
    if x > 0:
        if ((x - 1, y) not in current_loop) or (
            len(current_loop) > 3 and (x - 1, y) not in current_loop[1:]
        ):
            if shape in "-J7":
                next_moves.append((x - 1, y))

    if current_loop[0] in next_moves:
        return current_loop

    for next_move in next_moves:
        next_loop = copy(current_loop)
        next_loop.append(next_move)
        if answer := _generate_loop(lines, next_loop, s_shape):
            return answer
    raise ValueError("No loop found")


def generate_loop(lines):
    sloc = get_sloc(lines)
    s_shapes = get_possible_s_shapes(lines, sloc)
    for s_shape in s_shapes:
        if loop := _generate_loop(lines, [sloc], s_shape):
            return s_shape, loop
    raise ValueError("No loop found")


def steps(loop):
    return int(len(loop) / 2)


def main(lines, distance_algorithm=steps):
    start_shape, loop = generate_loop(lines)
    return distance_algorithm(loop)


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    with open("../../data/2023/input10.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

from dataclasses import dataclass
from itertools import combinations

from sympy import symbols, Eq, solve


@dataclass
class Hailstone:
    x: int
    y: int
    z: int
    run: int
    rise: int
    zvel: int

    def slope(self):
        return float(self.rise) / self.run


def build_hailstone(line):
    pos, vel = line.split("@")
    pos_list = [int(foo.strip()) for foo in pos.split(",")]
    vel_list = [int(foo.strip()) for foo in vel.split(",")]
    return Hailstone(*pos_list, *vel_list)


def get_line_equation(stone):
    x, y = symbols("x y")
    eq = Eq(y - stone.y, stone.slope() * (x - stone.x))
    return eq
    # eq = eq.simplify()
    # b = solve(eq.subs(x, stone.x), y)[0]
    # line_eq = Eq(y, stone.slope() * x + b)
    # return line_eq


def intersect(stone1, stone2, lo, hi):
    x, y = symbols("x y")
    eq1 = get_line_equation(stone1)
    eq2 = get_line_equation(stone2)
    intersection = solve((eq1, eq2), (x, y))

    # is within bounds
    if intersection and all(lo <= p <= hi for p in intersection.values()):
        # will reach that in future
        if intersection[x] == 0 or stone1.run == 0:
            raise NotImplementedError

        # if they have the same sign it will happen in future
        if (
            stone1.run / (intersection[x] - stone1.x) > 0
            and stone2.run / (intersection[x] - stone2.x) > 0
        ):
            return intersection

    return None


def main(lines, lo, hi):
    hailstones = [build_hailstone(line) for line in lines]
    intersections = 0
    for i, combo in enumerate(combinations(hailstones, 2)):
        if i % 100 == 0:
            print(f"{i=}")
        intersection = intersect(combo[0], combo[1], lo, hi)
        if intersection is not None:
            intersections += 1
    return intersections


if __name__ == "__main__":
    with open("../../data/2023/input24.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    lo = 200000000000000
    hi = 400000000000000
    print(main(lines, lo, hi))

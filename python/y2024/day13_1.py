import math

from aoc.io import this_year_day


class Machine:
    def __init__(self, button_a, button_b, prize):
        self.a = button_a
        self.b = button_b
        self.prize = prize

    def calc_cheapest(self):
        possibilities = []

        for a in range(1, 101):
            for b in range(1, 101):
                if (
                    self.a[0] * a + self.b[0] * b == self.prize[0]
                    and self.a[1] * a + self.b[1] * b == self.prize[1]
                ):
                    possibilities.append((a, b))

        if not possibilities:
            return 0
        return min(p[0] * 3 + p[1] for p in possibilities)

    def calc_cheapest_alternate(self):
        # system of equations with two unkowns
        # self.a[0]a + self.b[0]b = self.prize[0]
        # self.a[1]a + self.b[1]b = self.prize[1]
        # where a and b are number of presses of each, respectively
        alcm = math.lcm(self.a[0], self.a[1])
        eq1_multiplier = alcm // self.a[0]
        eq2_multiplier = alcm // self.a[1]

        eq1a = self.a[0] * eq1_multiplier
        eq1b = self.b[0] * eq1_multiplier
        eq1prize = self.prize[0] * eq1_multiplier

        eq2a = self.a[1] * eq2_multiplier
        eq2b = self.b[1] * eq2_multiplier
        eq2prize = self.prize[1] * eq2_multiplier

        # now subtract the two equations
        assert eq1a == eq2a
        b_sub = eq1b - eq2b
        prize_sub = eq1prize - eq2prize
        if prize_sub % b_sub == 0 and (num_b_presses := prize_sub // b_sub) > 0:
            num_a_presses = (self.prize[0] - self.b[0] * num_b_presses) // self.a[0]
            return num_a_presses * 3 + num_b_presses
        return 0


def build_button(line, sep="+"):
    coordinates = line.split(":")[1].strip()
    raw_x, raw_y = [c.strip() for c in coordinates.split(",")]
    x = int(raw_x.split(sep)[1])
    y = int(raw_y.split(sep)[1])
    return x, y


def build_prize(line):
    return build_button(line, "=")


def build_machine(three_lines):
    button_a = build_button(three_lines[0])
    button_b = build_button(three_lines[1])
    prize = build_prize(three_lines[2])
    return Machine(button_a, button_b, prize)


def build_machines(lines):
    machines = []
    storage = []
    for line in lines:
        if not line:
            machines.append(build_machine(storage))
            storage = []
        else:
            storage.append(line)
    machines.append(build_machine(storage))

    return machines


def main(lines):
    machines = build_machines(lines)
    cheapest = [machine.calc_cheapest() for machine in machines]
    return sum(cheapest)


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

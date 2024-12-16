import math

from aoc.io import this_year_day

weird_count = 0


class Machine:
    def __init__(self, button_a, button_b, prize):
        self.a = button_a
        self.b = button_b
        self.prize = prize[0] + 10000000000000, prize[1] + 10000000000000

    def calc_cheapest_alternate(self):
        # system of equations with two unkowns
        # self.a[0]a + self.b[0]b = self.prize[0]
        # self.a[1]a + self.b[1]b = self.prize[1]
        # where a and b are number of presses of each, respectively
        alcm = math.lcm(
            self.a[0], self.a[1]
        )  # maybe want to go with lesser of two lcms here due to size of numbers
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
        if prize_sub % b_sub == 0:
            num_b_presses = prize_sub // b_sub
            num_a_presses = (self.prize[0] - self.b[0] * num_b_presses) // self.a[0]
            assert num_a_presses > 0 and num_b_presses > 0
            try:
                assert (
                    num_a_presses * self.a[0] + num_b_presses * self.b[0]
                    == self.prize[0]
                    and num_a_presses * self.a[1] + num_b_presses * self.b[1]
                    == self.prize[1]
                )
            except AssertionError:
                global weird_count
                weird_count += 1
                return 0  # for debugging
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
    cheapest = [machine.calc_cheapest_alternate() for machine in machines]
    return sum(cheapest)


# 81905908280345 is too high
# 875318608908 is too low but it's the correct number for the test
if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
    print(weird_count)

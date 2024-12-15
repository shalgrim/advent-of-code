from aoc.io import this_year_day


class Machine:
    def __init__(self, button_a, button_b, prize):
        self.a = button_a
        self.b = button_b
        self.prize = prize

    def calc_cheapest(self):
        # max_a_presses = min(self.prize[0] // self.a[0], self.prize[1] // self.a[1])
        # max_b_presses = min(self.prize[0] // self.b[0], self.prize[1] // self.b[1])
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
        # print(len(possibilities))
        return min(p[0] * 3 + p[1] for p in possibilities)


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
    # testing = False
    testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

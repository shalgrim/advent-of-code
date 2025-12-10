import itertools

from coding_puzzle_tools import read_input


class Machine:
    def __init__(self, line):
        self._extract_lights(line.split()[0])
        self._extract_buttons(line.split()[1:-1])
        # ignore joltages for now
        self._reset()

    def _extract_lights(self, brackets: str):
        self.total_lights = len(brackets) - 2
        self.required_lights = [
            i for i, light in enumerate(brackets[1:-1]) if light == "#"
        ]
        self.answer = [
            True if i in self.required_lights else False
            for i in range(self.total_lights)
        ]

    def _extract_buttons(self, raw_button_data: str):
        self.buttons = []
        for raw_button in raw_button_data:
            numbers = raw_button[1:-1].split(",")
            self.buttons.append([int(n) for n in numbers])

    def push_button(self, index: int) -> None:
        for light_to_switch in self.buttons[index]:
            self.lights[light_to_switch] = not self.lights[light_to_switch]

    def check(self) -> bool:
        return self.lights == self.answer

    def _reset(self):
        self.lights = [False for _ in range(self.total_lights)]

    def reset(self):
        self._reset()


def min_button_presses(machine: Machine) -> int:
    i = 1
    while True:
        for combo in itertools.combinations(range(len(machine.buttons)), i):
            for button in combo:
                machine.push_button(button)
            if machine.check():
                return i
            machine.reset()
        i += 1


def main(lines: list[str]):
    machines = [Machine(line) for line in lines]
    return sum(min_button_presses(machine) for machine in machines)


if __name__ == "__main__":
    print(main(read_input()))

from y2023.day20_1 import Machine


def main(lines):
    machine = Machine(lines)
    pushes = 0

    while not machine.on:
        if pushes % 100_000 == 0:
            print(f"{pushes=}")
        pushes += 1
        machine.push_button()
    return pushes


if __name__ == "__main__":
    with open("../../data/2023/input20.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

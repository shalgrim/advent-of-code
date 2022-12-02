# from day11_1 import PUZZLE_INPUT
from day11_1 import make_octopus_grid, process_flashes


def all_flashed(grid):
    for line in grid:
        if any([o.energy for o in line]):
            return False
    return True


def main(lines):
    grid = make_octopus_grid(lines)
    steps = 0
    while not all_flashed(grid):
        for y, line in enumerate(grid):
            for x, octopus in enumerate(line):
                octopus.increase_energy()

        process_flashes(grid)

        for line in grid:
            for octopus in line:
                octopus.unflash()
        steps += 1

    return steps


if __name__ == '__main__':
    with open('../data/input11.txt') as f:
        PUZZLE_INPUT = [line.strip() for line in f.readlines()]

    print(main(PUZZLE_INPUT))

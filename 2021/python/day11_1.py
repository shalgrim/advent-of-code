class Octopus():
    def __init__(self, energy):
        self.energy = energy
        self.total_flashes = 0
        self.flashed = False

    def increase_energy(self):
        if self.energy == 9:
            self.total_flashes += 1
        self.energy += 1

    def __str__(self):
        return str(self.energy)

    def unflash(self):
        if self.energy > 9:
            self.energy = 0
        self.flashed = False

    @property
    def unprocessed_flash(self):
        return self.energy > 9 and not self.flashed


def make_octopus_grid(lines):
    grid = []
    for line in lines:
        grid.append([Octopus(int(c)) for c in line])

    return grid


def contains_unprocessed_flashes(grid):
    for line in grid:
        if any([o.unprocessed_flash for o in line]):
            return True
    return False


def increase_neighbors(grid, x, y):
    if x == 0:
        if y == 0:
            neighbors = [(x+1, y), (x, y+1), (x+1, y+1)]
        elif y == len(grid) - 1:
            neighbors = [(x+1, y-1), (x, y-1), (x+1, y)]
        else:
            neighbors = [(x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    elif x == len(grid[0]) - 1:
        if y == 0:
            neighbors = [(x-1, y), (x, y+1), (x-1, y+1)]
        elif y == len(grid) - 1:
            neighbors = [(x-1, y-1), (x, y-1), (x-1, y)]
        else:
            neighbors = [(x, y-1), (x, y+1), (x-1, y-1), (x-1, y), (x-1, y+1)]
    elif y == 0:
        neighbors = [(x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    elif y == len(grid) - 1:
        neighbors = [(x-1, y), (x+1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
    else:
        neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

    for nx, ny in neighbors:
        octopus = grid[ny][nx]
        octopus.increase_energy()


def process_flashes(grid):
    while contains_unprocessed_flashes(grid):
        for y, line in enumerate(grid):
            for x, octopus in enumerate(line):
                if octopus.unprocessed_flash:
                    increase_neighbors(grid, x, y)
                    octopus.flashed = True


def print_grid(grid):
    for line in grid:
        print(''.join([str(o.energy) for o in line]))


def main(lines):
    grid = make_octopus_grid(lines)

    for i in range(100):
        print(f'After step {i}')
        print_grid(grid)
        print()

        for y, line in enumerate(grid):
            for x, octopus in enumerate(line):
                octopus.increase_energy()

        process_flashes(grid)

        for line in grid:
            for octopus in line:
                octopus.unflash()

    total_flashes = 0
    for line in grid:
        total_flashes += sum([octopus.total_flashes for octopus in line])

    return total_flashes


if __name__ == '__main__':
    with open('../data/input11.txt') as f:
        PUZZLE_INPUT = [line.strip() for line in f.readlines()]

    print(main(PUZZLE_INPUT))

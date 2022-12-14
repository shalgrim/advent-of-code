class Map:
    def __init__(self, lines):
        self.lines = lines
        self.rocks = set()
        self.sand = set()

        for line in lines:
            coordinate_pairs = line.split(' -> ')
            for i, cp in enumerate(coordinate_pairs[:-1]):
                x = int(cp.split(',')[0])
                y = int(cp.split(',')[1])
                next_pair = coordinate_pairs[i + 1]
                next_x = int(next_pair.split(',')[0])
                next_y = int(next_pair.split(',')[1])

                if x == next_x:  # vertical
                    lower = y if y < next_y else next_y
                    higher = y if y >= next_y else next_y
                    for j in range(lower, higher + 1):
                        self.rocks.add((x, j))
                    pass
                else:  # horizontal
                    lower = x if x < next_x else next_x
                    higher = x if x >= next_x else next_x
                    for j in range(lower, higher + 1):
                        self.rocks.add((j, y))

        self.max_depth = max(rock[1] for rock in self.rocks)

    def get_next_loc(self, sand_loc):
        sand_x, sand_y = sand_loc
        potential = sand_x, sand_y + 1
        if potential not in self.rocks.union(self.sand):
            return potential
        potential = sand_x - 1, sand_y + 1
        if potential not in self.rocks.union(self.sand):
            return potential
        potential = sand_x + 1, sand_y + 1
        if potential not in self.rocks.union(self.sand):
            return potential
        return sand_loc

    def add_sand(self):
        sand = (500, 0)
        while (new_sand := self.get_next_loc(sand)) != sand:
            sand = new_sand
            if sand[1] > self.max_depth:
                return -1
        self.sand.add(sand)

    @property
    def can_add_more(self):
        return (500, 0) not in self.sand


def main(lines):
    map = Map(lines)
    while map.can_add_more:
        sentinel = map.add_sand()
        if sentinel == -1:
            break
    return len(map.sand)


if __name__ == '__main__':
    with open('../../data/2022/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

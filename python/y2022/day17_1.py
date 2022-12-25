from time import sleep


class Rock:
    def __init__(self, chamber):
        self.coordinates = None
        self.chamber = chamber
        self.falling = True

    @property
    def can_fall(self):
        return all(
            self.chamber.is_free(x, y - 1)
            for x, y in self.coordinates
            if (x, y - 1) not in self.coordinates
        )

    def blow(self, direction):
        if direction == '<' and self.can_move(-1):
            self.move(-1)
        elif direction == '>' and self.can_move(1):
            self.move(1)

    def can_move(self, direction):
        return all(
            self.chamber.is_free(x + direction, y)
            for x, y in self.coordinates
            if (x + direction, y) not in self.coordinates
        )

    def move(self, direction):
        self.coordinates = [(x + direction, y) for x, y in self.coordinates]

    def drop(self):
        self.coordinates = [(x, y - 1) for x, y in self.coordinates]


class RockMinus(Rock):
    def __init__(self, chamber):
        super().__init__(chamber)
        y = chamber.height + 4
        self.coordinates = [(x, y) for x in range(2, 6)]


class RockPlus(Rock):
    def __init__(self, chamber):
        super().__init__(chamber)
        lowest_y = chamber.height + 4
        leftmost_x = 2
        self.coordinates = [(leftmost_x + offset, lowest_y + 1) for offset in range(3)]
        self.coordinates.append((leftmost_x + 1, lowest_y))
        self.coordinates.append((leftmost_x + 1, lowest_y + 2))


class RockL(Rock):
    def __init__(self, chamber):
        super().__init__(chamber)
        lowest_y = chamber.height + 4
        leftmost_x = 2
        self.coordinates = [(leftmost_x + offset, lowest_y) for offset in range(3)]
        self.coordinates += [
            (leftmost_x + 2, lowest_y + offset) for offset in range(1, 3)
        ]


class RockPipe(Rock):
    def __init__(self, chamber):
        super().__init__(chamber)
        lowest_y = chamber.height + 4
        self.coordinates = [(2, y) for y in range(lowest_y, lowest_y + 4)]


class RockSquare(Rock):
    def __init__(self, chamber):
        super().__init__(chamber)
        lowest_y = chamber.height + 4
        leftmost_x = 2
        self.coordinates = [
            (leftmost_x, lowest_y),
            (leftmost_x + 1, lowest_y),
            (leftmost_x, lowest_y + 1),
            (leftmost_x + 1, lowest_y + 1),
        ]


ROCK_TYPES = [RockMinus, RockPlus, RockL, RockPipe, RockSquare]


class RockFactory:
    rock_types = [RockMinus, RockPlus, RockL, RockPipe, RockSquare]

    def __init__(self):
        self.next_rock_type = 0

    def make_rock(self, chamber):
        new_rock = ROCK_TYPES[self.next_rock_type](chamber)
        self.next_rock_type = (self.next_rock_type + 1) % 5
        return new_rock


class Chamber:
    def __init__(self, air_pattern):
        self.air_pattern = air_pattern
        self.factory = RockFactory()
        self.air_index = 0
        self.rocks = []

    @property
    def height(self):
        if not self.rocks:
            return 0
        all_ys = set()
        for rock in self.rocks:
            all_ys.update({coordinate[1] for coordinate in rock.coordinates})
        return max(all_ys)

    @property
    def falling_rock(self):
        if not self.rocks:
            return set()

        most_recent_rock = self.rocks[-1]
        if not most_recent_rock.falling:
            return set()

        return set(most_recent_rock.coordinates)

    @property
    def stopped_rocks(self):
        answer = set()
        for rock in self.rocks:
            if not rock.falling:
                answer.update(set(rock.coordinates))
        return answer

    def drop_new_rock(self):
        rock = self.factory.make_rock(self)
        self.rocks.append(rock)
        # print(self)
        self.blow_rock(rock)
        # print(self)
        while rock.can_fall:
            rock.drop()
            # print(self)
            self.blow_rock(rock)
            # print(self)
        rock.falling = False
        # print(self)

    def blow_rock(self, rock):
        direction = self.air_pattern[self.air_index]
        rock.blow(direction)
        self.air_index = (self.air_index + 1) % len(self.air_pattern)

    def is_free(self, x, y):
        return (
            0 <= x <= 6
            and y >= 1
            and (x, y) not in self.falling_rock
            and (x, y) not in self.stopped_rocks
        )

    def __str__(self):
        lines = ['', '+-------+']
        for y in range(1, self.height + 1):
            line = ['|']
            for x in range(7):
                if (x, y) in self.stopped_rocks:
                    next_char = '#'
                elif (x, y) in self.falling_rock:
                    next_char = '@'
                else:
                    next_char = '.'
                line.append(next_char)
            line.append('|')
            lines.append(''.join(line))
        lines.append('')
        return '\n'.join(lines[::-1])


def main(air_pattern):
    chamber = Chamber(air_pattern)
    for rock_num in range(2022):
        chamber.drop_new_rock()
        print(rock_num, chamber.height)
        # if rock_num % 100 == 0:
        #     sleep(2)
    return chamber.height


if __name__ == '__main__':
    with open('../../data/2022/input17.txt') as f:
        txt = f.read().strip()
    print(main(txt))

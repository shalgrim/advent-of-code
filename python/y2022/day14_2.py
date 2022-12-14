from y2022.day14_1 import Map


class Map2(Map):
    def __init__(self, lines):
        super().__init__(lines)
        self.max_depth = self.max_depth + 2

    def get_next_loc(self, sand_loc):
        sand_x, sand_y = sand_loc
        next_y = sand_y + 1
        if next_y == self.max_depth:
            return sand_loc
        no_go = self.rocks.union(self.sand)
        for next_x in (sand_x, sand_x - 1, sand_x + 1):
            potential = next_x, next_y
            if potential not in no_go:
                return potential
        return sand_loc

    def __str__(self):
        leftmost = min(item[0] for item in self.rocks.union(self.sand))
        rightmost = max(item[0] for item in self.rocks.union(self.sand))
        lines = []
        for y in range(self.max_depth):
            line = []
            for x in range(leftmost, rightmost+1):
                if (x, y) in self.rocks:
                    line.append('#')
                elif (x, y) in self.sand:
                    line.append('o')
                else:
                    line.append('.')
            lines.append(''.join(line))
        last_line = '#' * (rightmost - leftmost + 1)
        lines.append(last_line)
        return '\n'.join(lines)


def main(lines):
    map = Map2(lines)
    while map.can_add_more:
        # if map.sand and len(map.sand) % 1000 == 0:
        if map.sand and len(map.sand) % 1000 == 0:
            leftmost = min(sand[0] for sand in map.sand)
            rightmost = max(sand[0] for sand in map.sand)
            print(map)
            print (f'========ENDMAP======={len(map.sand)=}========{leftmost=}========={rightmost=}')
            # print(f'current sand: {len(map.sand)}')
            # # print(f'lowest sand: {max(sand[1] for sand in map.sand)}')
            # highest_sand = min(sand[1] for sand in map.sand)
            # print(f'  {highest_sand=}')
            # print(f'    num at highest: {len([sand for sand in map.sand if sand[1] == highest_sand])}')
            # print(f'    leftmost at highest: {min(sand[0] for sand in map.sand if sand[1] == highest_sand)}')
            # print(f'    rightmost at highest: {max(sand[0] for sand in map.sand if sand[1] == highest_sand)}')
            # print(f'  leftmost sand: {min(sand[0] for sand in map.sand)}')
            # print(f'  rightmost sand: {max(sand[0] for sand in map.sand)}')
        map.add_sand()
    return len(map.sand)


if __name__ == '__main__':
    with open('../../data/2022/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

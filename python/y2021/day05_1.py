from collections import defaultdict, Counter


class Line():
    def __init__(self, inline):
        origin, destination = inline.split(' -> ')
        x1, y1 = origin.split(',')
        x2, y2 = destination.split(',')
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)

    @property
    def horizontal(self):
        return self.y1 == self.y2

    @property
    def vertical(self):
        return self.x1 == self.x2


def main(inlines):
    lines = [Line(inline) for inline in inlines]
    lines_of_concern = [line for line in lines if line.horizontal or line.vertical]

    points_covered = []

    for line in lines_of_concern:
        if line.x1 == line.x2:
            lower = min(line.y1, line.y2)
            upper = max(line.y1, line.y2)
            points_covered += [(line.x1, y) for y in range(lower, upper+1)]
        elif line.y1 == line.y2:
            lower = min(line.x1, line.x2)
            upper = max(line.x1, line.x2)
            points_covered += [(x, line.y1) for x in range(lower, upper+1)]

    counter = Counter(points_covered)
    num_crosses = len([1 for v in counter.values() if v > 1])
    return num_crosses


if __name__ == '__main__':
    with open('../data/input05.txt') as f:
        inlines = [line.strip() for line in f.readlines()]

    print(main(inlines))

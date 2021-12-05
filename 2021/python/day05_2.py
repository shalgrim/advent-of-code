from collections import Counter

from day05_1 import Line


def main(inlines):
    lines = [Line(inline) for inline in inlines]

    points_covered = []

    for line in lines:
        if line.x1 == line.x2:
            lower = min(line.y1, line.y2)
            upper = max(line.y1, line.y2)
            points_covered += [(line.x1, y) for y in range(lower, upper + 1)]
        elif line.y1 == line.y2:
            lower = min(line.x1, line.x2)
            upper = max(line.x1, line.x2)
            points_covered += [(x, line.y1) for x in range(lower, upper + 1)]
        else:  # it's diagonal
            lower_x = min(line.x1, line.x2)
            upper_x = max(line.x1, line.x2)
            lower_y = min(line.y1, line.y2)
            upper_y = max(line.y1, line.y2)

            if lower_x == line.x1 and lower_y == line.y1 or lower_x == line.x2 and lower_y == line.y2:
                ## it's a backslash \ line
                y = lower_y - 1
                for x in range(lower_x, upper_x + 1):
                    y += 1
                    points_covered.append((x, y))
            else:
                ## it's a forward slash / line
                y = upper_y + 1
                for x in range(lower_x, upper_x + 1):
                    y -= 1
                    points_covered.append((x, y))

    counter = Counter(points_covered)
    num_crosses = len([1 for v in counter.values() if v > 1])
    return num_crosses


if __name__ == '__main__':
    with open('../data/input05.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

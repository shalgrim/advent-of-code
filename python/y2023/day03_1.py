import re


def is_adjacent(location, value, symbol_locations):
    my_locations = [location]
    my_val = value // 10

    while my_val:
        my_locations.append((my_locations[-1][0] + 1, my_locations[-1][1]))
        my_val = my_val // 10

    leftest = max(0, my_locations[0][0] - 1)
    rightest = my_locations[-1][0] + 1
    uppest = max(0, location[1] - 1)
    downest = location[1] + 1

    for y in range(uppest, downest + 1):
        for x in range(leftest, rightest + 1):
            if (x, y) in symbol_locations:
                return True
    return False


def main(lines):
    number_locations = {}
    symbol_locations = set()
    for y, line in enumerate(lines):
        matches = list(re.finditer(r"\d+", line))
        for match in matches:
            number_locations[(match.start(), y)] = int(match.group())
        for x, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_locations.add((x, y))
    sum = 0
    for location, value in number_locations.items():
        if is_adjacent(location, value, symbol_locations):
            sum += value
    return sum


if __name__ == "__main__":
    with open("../../data/2023/input03.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

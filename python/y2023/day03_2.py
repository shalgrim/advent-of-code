import re


def get_adjacent_numbers(location, number_locations):
    answer = []
    for number_loc, value in number_locations.items():
        found = False
        my_locs = [number_loc]
        my_val = value // 10

        while my_val:
            my_locs.append((my_locs[-1][0] + 1, my_locs[-1][1]))
            my_val = my_val // 10
        leftest = max(0, my_locs[0][0] - 1)
        rightest = my_locs[-1][0] + 1
        uppest = max(0, number_loc[1] - 1)
        downest = number_loc[1] + 1
        for y in range(uppest, downest + 1):
            if found:
                break
            for x in range(leftest, rightest + 1):
                if found:
                    break
                if (x, y) == location:
                    answer.append(value)
                    found = True
    return answer


def get_gear_value(location, number_locations):
    adjacent_numbers = get_adjacent_numbers(location, number_locations)
    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    return 0


def main(lines):
    number_locations = {}
    potential_gear_locations = set()
    for y, line in enumerate(lines):
        matches = list(re.finditer(r"\d+", line))
        for match in matches:
            number_locations[(match.start(), y)] = int(match.group())
        for x, char in enumerate(line):
            if char == "*":
                potential_gear_locations.add((x, y))

    sum = 0
    for location in potential_gear_locations:
        sum += get_gear_value(location, number_locations)
    return sum


if __name__ == "__main__":
    with open("../../data/2023/input03.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

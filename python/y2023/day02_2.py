from y2023.day02_1 import process_input


def get_min_possible(draws):
    blueval = max(draw.get("blue", 0) for draw in draws)
    greenval = max(draw.get("green", 0) for draw in draws)
    redval = max(draw.get("red", 0) for draw in draws)
    return blueval, greenval, redval


def get_power_of_set(blueval, greenval, redval):
    return blueval * greenval * redval


def get_power_of_minset(draws):
    return get_power_of_set(*get_min_possible(draws))


def main(lines):
    games = process_input(lines)
    return sum(get_power_of_minset(draws) for draws in games.values())


if __name__ == "__main__":
    with open("../../data/2023/input02.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

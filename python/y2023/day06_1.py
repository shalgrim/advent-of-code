import math


def build_races(lines):
    times = [int(num) for num in lines[0].split()[1:]]
    distances = [int(num) for num in lines[1].split()[1:]]
    return [(t, d) for t, d in zip(times, distances)]


def calc_distance(charging_time, race_time):
    speed = charging_time
    run_time = race_time - charging_time
    return speed * run_time


def get_ways_to_beat(time, distance):
    answer = 0
    for t in range(1, time):
        if calc_distance(t, time) > distance:
            answer += 1
    return answer


def main(lines):
    races = build_races(lines)
    ways_to_beat = [get_ways_to_beat(*race) for race in races]
    return math.prod(ways_to_beat)


if __name__ == "__main__":
    with open("../../data/2023/input06.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

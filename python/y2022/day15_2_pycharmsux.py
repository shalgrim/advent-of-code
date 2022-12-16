from y2022.day15_1 import build_sensors, get_impossibles


def main(lines, max_val):
    sensors = build_sensors(lines)
    all_known_beacons = [(s.beacon_x, s.beacon_y) for s in sensors]
    all_impossibles = set()
    for y in range(max_val+1):
        # current issue is that for y == 0 the logic says any x is possible, no impossibles for any sensor, which what?
        # easiest counterexample there is that there's a sensor at 2, 0 that detects a beacon at 2, 10
        # that's a distance of 8. So there should be no possible beacons at anything on row 0 where x >= 10
        impossibles = get_impossibles(sensors, all_known_beacons, y)
        all_impossibles = all_impossibles.union({(x, y) for x in impossibles})
    for x in range(max_val):
        for y in range(max_val):
            if (x, y) not in all_impossibles:
                return x, y


if __name__ == '__main__':
    with open('../../data/2022/test15.txt') as f:
    # with open('../../data/2022/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, 20))
    # print(main(lines, 2_000_000))

from y2022.day15_1 import build_sensors, get_impossibles


def main(lines, max_val):
    sensors = build_sensors(lines)
    all_known_beacons = [(s.beacon_x, s.beacon_y) for s in sensors]
    all_impossibles = set()
    for y in range(max_val+1):
        print(f'{y=}')
        impossibles = get_impossibles(sensors, all_known_beacons, y)
        all_impossibles = all_impossibles.union({(x, y) for x in impossibles})
    for x in range(max_val):
        print(f'{x=}')
        for y in range(max_val):
            if (x, y) not in all_impossibles and (x, y) not in all_known_beacons:
                return x, y


if __name__ == '__main__':
    # Status: There are certainly performance gains to be made by just being more efficient down these calls; I suspect it requires a different algorithm altogether tho
    # with open('../../data/2022/test15.txt') as f:
    with open('../../data/2022/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    # print(main(lines, 20))
    print(main(lines, 2_000_000))

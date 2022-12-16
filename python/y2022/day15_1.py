def manhattan_distance(p1, p2):
    return sum([abs(p2[i] - p1[i]) for i in range(2)])


class Sensor:
    def __init__(self, sensor_coordinates, beacon_coordinates):
        self.x, self.y = sensor_coordinates
        self.beacon_x, self.beacon_y = beacon_coordinates
        self.distance_to_closest_beacon = manhattan_distance(
            sensor_coordinates, beacon_coordinates
        )

    def impossibles(self, y, all_known_beacons):
        distance_to_row = abs(self.y - y)
        if self.distance_to_closest_beacon < distance_to_row:
            return set()
        if self.distance_to_closest_beacon == distance_to_row:
            if self.beacon_y == y:
                return set()
            return set([self.x])

        known_beacons_on_row = {
            beacon for beacon in all_known_beacons if beacon[1] == y
        }
        if not known_beacons_on_row:
            leftover_distance = self.distance_to_closest_beacon - distance_to_row
            return set(
                range(self.x - leftover_distance, self.x + leftover_distance + 1)
            )
        known_beacons_to_left_on_row = [
            beacon for beacon in known_beacons_on_row if beacon[0] <= self.x
        ]
        easy_minimum_x = self.x - (self.distance_to_closest_beacon - distance_to_row)
        if known_beacons_to_left_on_row:
            nearest_beacon_x_to_left_on_row = max(
                beacon[0] for beacon in known_beacons_to_left_on_row
            )
            minimum_x = max(easy_minimum_x, nearest_beacon_x_to_left_on_row)
        else:
            minimum_x = easy_minimum_x

        known_beacons_to_right_on_row = [
            beacon for beacon in known_beacons_on_row if beacon[0] >= self.x
        ]
        easy_maximum_x = self.x + (self.distance_to_closest_beacon - distance_to_row)
        if known_beacons_to_right_on_row:
            nearest_beacon_x_to_right_on_row = min(
                beacon[0] for beacon in known_beacons_to_right_on_row
            )
            maximum_x = min(easy_maximum_x, nearest_beacon_x_to_right_on_row)
        else:
            maximum_x = easy_maximum_x

        impossible_xs = set(range(minimum_x, maximum_x + 1)).difference(
            beacon[0] for beacon in known_beacons_on_row
        )
        return impossible_xs


def coordinates_from_line(line_info):
    initial_stuff, y_info = line_info.split(',')
    x_info = initial_stuff.split()[-1]
    x = int(x_info.split('=')[1])
    y = int(y_info.split('=')[1])
    return x, y


def build_sensors(lines):
    sensors = []
    for line in lines:
        sensor_info, beacon_info = line.split(': ')
        beacon_coordinates = coordinates_from_line(beacon_info)
        sensor_coordinates = coordinates_from_line(sensor_info)
        sensors.append(Sensor(sensor_coordinates, beacon_coordinates))

    return sensors


def main(lines, y):
    sensors = build_sensors(lines)
    all_known_beacons = [(s.beacon_x, s.beacon_y) for s in sensors]
    answer = get_impossibles(sensors, all_known_beacons, y)

    return len(answer)


def get_impossibles(sensors, all_known_beacons, y):
    the_impossibles = [sensor.impossibles(y, all_known_beacons) for sensor in sensors]
    answer = set()
    for impossible in the_impossibles:
        answer = answer.union(impossible)
    return answer


if __name__ == '__main__':
    # with open('../../data/2022/test15.txt') as f:
    with open('../../data/2022/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    # print(main(lines, 10))
    print(main(lines, 2_000_000))

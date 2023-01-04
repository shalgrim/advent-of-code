from enum import Enum


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


def parse_input(lines):
    map = {}
    for y, line in enumerate(lines):
        if not line:
            break
        for x, c in enumerate(line):
            if c in ['.', '#']:
                map[(x, y)] = c

    raw_instructions = lines[-1].strip()
    stored_value = 0
    path = []
    for c in raw_instructions:
        try:
            stored_value = stored_value * 10 + int(c)
        except ValueError:
            path.append((stored_value, c))
            stored_value = 0

    return map, path


def get_start_location(map):
    leftmost_open_x = min(x for (x, y), tile in map.items() if y == 0 and tile == '.')
    return leftmost_open_x, 0


def get_next_tile(map, location, direction):
    if direction == Direction.RIGHT:
        if (location[0] + 1, location[1]) in map:
            return location[0] + 1, location[1]
        else:
            leftmost_x = min(k[0] for k in map.keys() if k[1] == location[1])
            return leftmost_x, location[1]
    elif direction == Direction.LEFT:
        if (location[0] - 1, location[1]) in map:
            return location[0] - 1, location[1]
        else:
            rightmost_x = max(k[0] for k in map.keys() if k[1] == location[1])
            return rightmost_x, location[1]
    elif direction == Direction.UP:
        if (location[0], location[1] - 1) in map:
            return location[0], location[1] - 1
        else:
            lowermost_y = max(k[1] for k in map.keys() if k[0] == location[0])
            return location[0], lowermost_y
    elif direction == Direction.DOWN:
        if (location[0], location[1] + 1) in map:
            return location[0], location[1] + 1
        else:
            uppermost_y = min(k[1] for k in map.keys() if k[0] == location[0])
            return location[0], uppermost_y
    else:
        raise ValueError(f'Unknown Direction {direction}')


def move(map, location, direction, magnitude):
    current_loc = location
    for _ in range(magnitude):
        next_tile_location = get_next_tile(map, current_loc, direction)
        if map[next_tile_location] == '#':
            break
        current_loc = next_tile_location

    return current_loc


def get_new_direction(direction, turn):
    if turn == 'R':
        inc_or_dec = 1
    elif turn == 'L':
        inc_or_dec = -1
    else:
        raise ValueError(f"Invalid turn {turn}")
    new_value = direction.value + inc_or_dec
    return Direction(new_value % 4)


def get_last_magnitude(line):
    value = 0
    for c in line[::-1]:
        try:
            value = value * 10 + int(c)
        except ValueError:
            return value


def main(lines):
    map, path = parse_input(lines)
    location = get_start_location(map)
    direction = Direction.RIGHT

    for magnitude, turn in path:
        location = move(map, location, direction, magnitude)
        direction = get_new_direction(direction, turn)

    last_magnitude = get_last_magnitude(lines[-1].strip())
    location = move(map, location, direction, last_magnitude)

    final_row = location[1] + 1
    final_column = location[0] + 1
    final_facing = direction.value
    return 1000 * final_row + 4 * final_column + final_facing


if __name__ == '__main__':
    with open('../../data/2022/input22.txt') as f:
        lines = f.readlines()
    print(main(lines))

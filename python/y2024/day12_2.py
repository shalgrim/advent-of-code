from collections import defaultdict

from aoc.io import this_year_day
from y2024.day12_1 import is_adjacent, combine_regions


def get_num_straight_sides(region, crop_of_interest):
    vertical_segments = set()
    horizontal_segments = set()

    for x, y in region:
        west = x - 1, y
        east = x + 1, y
        north = x, y - 1
        south = x, y + 1

        if west not in region:
            vertical_segments.add((x, y))
        if east not in region:
            vertical_segments.add((x + 1, y))
        if north not in region:
            horizontal_segments.add((x, y))
        if south not in region:
            horizontal_segments.add((x, y + 1))

    # all segments are created, now put them together
    # vertical walls first
    num_vertical_walls = 0
    westest_vertical_wall = min(p[0] for p in vertical_segments)
    eastest_vertical_wall = max(p[0] for p in vertical_segments)

    for x in range(westest_vertical_wall, eastest_vertical_wall + 1):
        candidate_segments = sorted(
            [segment for segment in vertical_segments if segment[0] == x]
        )
        previous_y = -2
        previous_crop_side = "X"
        for segment in candidate_segments:
            y = segment[1]
            crop_side = "W" if (x - 1, y) in region else "E"
            if previous_y == -2:
                num_vertical_walls += 1
            elif y != previous_y + 1:
                num_vertical_walls += 1
            elif crop_side != previous_crop_side:
                num_vertical_walls += 1
            previous_crop_side = crop_side
            previous_y = y

    # then horizontal walls
    num_horizontal_walls = 0
    northest_horizontal_wall = min(p[1] for p in horizontal_segments)
    southest_horizontal_wall = max(p[1] for p in horizontal_segments)

    for y in range(northest_horizontal_wall, southest_horizontal_wall + 1):
        candidate_segments = sorted(
            [segment for segment in horizontal_segments if segment[1] == y]
        )
        previous_x = -2
        previous_crop_side = "X"
        for segment in candidate_segments:
            x = segment[0]
            crop_side = "N" if (x, y - 1) in region else "S"
            if previous_x == -2:
                num_horizontal_walls += 1
            elif x != previous_x + 1:
                num_horizontal_walls += 1
            elif crop_side != previous_crop_side:
                num_horizontal_walls += 1
            previous_x = x
            previous_crop_side = crop_side

    return num_vertical_walls + num_horizontal_walls


def main(lines):
    all_locations = defaultdict(set)
    regions = defaultdict(list)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coords = x, y
            all_locations[char].add(coords)
            for region in regions[char]:
                if is_adjacent(coords, region):
                    region.add(coords)
                    break
            else:
                regions[char].append({coords})

    regions = combine_regions(regions)

    answer = 0
    for crop, crop_regions in regions.items():
        for region in crop_regions:
            num_straight_sides = get_num_straight_sides(region, crop)
            area = len(region)
            price = num_straight_sides * area
            print(f"{crop=}, {price=}")
            answer += price

    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    # with open(f"../../data/{year}/{filetype}{day}_1.txt") as f:  # 80
    # with open(f"../../data/{year}/{filetype}{day}_2.txt") as f:  # 436
    # with open(f"../../data/{year}/{filetype}{day}_3.txt") as f:  # 1206
    # with open(f"../../data/{year}/{filetype}{day}_4.txt") as f:  # 236
    # with open(f"../../data/{year}/{filetype}{day}_5.txt") as f:  # 368
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:  # 830198 is wrong
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

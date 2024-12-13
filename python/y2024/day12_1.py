from collections import defaultdict
from copy import copy
from itertools import combinations

from aoc.io import this_year_day


def calc_perim(region):
    answer = 0
    for x, y in region:
        adjacent = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
        answer += 4 - len(region.intersection(adjacent))

    return answer


def is_adjacent(coords, region):
    x, y = coords
    adjacent = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
    return len(adjacent.intersection(region)) > 0


def combine_regions(regions):
    combined_regions = {}

    for crop, crop_regions in regions.items():
        if len(crop_regions) == 1:
            combined_regions[crop] = copy(crop_regions)
        else:
            in_any_combination = set()
            combined_regions[crop] = []
            can_be_combined = defaultdict(list)
            for combo in combinations(range(len(crop_regions)), 2):
                region1 = crop_regions[combo[0]]
                region2 = crop_regions[combo[1]]
                if len(region1) < len(region2):
                    smaller_region = region1
                    larger_region = region2
                else:
                    smaller_region = region2
                    larger_region = region1

                adjacent_to_smaller = set()
                for x, y in smaller_region:
                    adjacent_to_smaller.update(
                        {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
                    )
                if adjacent_to_smaller.intersection(larger_region):
                    can_be_combined[combo[0]].append(combo[1])
                    can_be_combined[combo[1]].append(combo[0])
                    in_any_combination.add(combo[0])
                    in_any_combination.add(combo[1])

            transitive_sets = defaultdict(set)
            for key_index, list_of_other_indexes in can_be_combined.items():
                transitive_sets[key_index].update(set(list_of_other_indexes))
                for other_index in list_of_other_indexes:
                    transitive_sets[other_index] = transitive_sets[key_index]

            has_been_combined = set()
            for region_index, region in enumerate(crop_regions):
                if region_index not in transitive_sets:
                    combined_regions[crop].append(copy(region))
                elif region_index not in has_been_combined:
                    new_region = copy(region)
                    has_been_combined.add(region_index)
                    for other_region_index in transitive_sets[region_index]:
                        new_region.update(copy(crop_regions[other_region_index]))
                        has_been_combined.add(other_region_index)
                    combined_regions[crop].append(new_region)

    return combined_regions


def main(lines, perim_calculator=None):
    if perim_calculator is None:
        perim_calculator = calc_perim
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
            perimeter = perim_calculator(region)
            area = len(region)
            price = perimeter * area
            print(f"{crop=}, {price=}")
            answer += price

    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    # with open(f"../../data/{year}/{filetype}{day}_1.txt") as f:
    # with open(f"../../data/{year}/{filetype}{day}_2.txt") as f:
    # with open(f"../../data/{year}/{filetype}{day}_3.txt") as f:
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

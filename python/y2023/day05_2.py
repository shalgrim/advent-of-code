from tqdm import tqdm
from y2023.day05_1 import build_maps, mega_convert


def get_seeds2(line):
    seeds = set()
    nums = [int(num) for num in line.split()[1:]]
    print(f"{len(nums)=}")
    for i in range(0, len(nums), 2):
        start = nums[i]
        length = nums[i + 1]
        seeds.update(set(range(start, start + length)))
        print(f"{len(seeds)=}")
    return seeds


def get_seed_ranges(line):
    nums = [int(num) for num in line.split()[1:]]
    ranges = []
    for i in range(0, len(nums), 2):
        start = nums[i]
        length = nums[i + 1]
        ranges.append((start, start + length))
    return ranges


def get_lowest_possible_location(maps):
    to_location_map = maps[-1]
    return min(drs for drs in to_location_map.destination_range_starts)


def get_highest_possible_location(maps):
    to_location_map = maps[-1]
    answer = 0
    for drs, rl in zip(
        to_location_map.destination_range_starts, to_location_map.range_lengths
    ):
        answer = max(answer, drs + rl)
    return answer


def main(lines):
    seed_ranges = get_seed_ranges(lines[0])
    maps = build_maps(lines[2:])
    print(f"lowest possible location: {get_lowest_possible_location(maps)}")
    print(f"highest possible location: {get_highest_possible_location(maps)}")
    lowest = get_highest_possible_location(maps)
    for isr, seed_range in enumerate(seed_ranges):
        print(f"{isr=}")
        for seed in tqdm(range(*seed_range)):
            if mega_convert(seed, maps) < lowest:
                lowest = mega_convert(seed, maps)
                print(f"{lowest=}")
    return lowest


# TODO: the key is probably to work backwards here
# I.e., work from the lowest possible backwards to see if you can get there
if __name__ == "__main__":
    with open("../../data/2023/input05.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

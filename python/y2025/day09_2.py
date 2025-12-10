import itertools

from coding_puzzle_tools import read_input
from y2025.day09_1 import get_red_tiles, rect_size


def has_only_red_or_green(
    combo: tuple[tuple[int, int], tuple[int, int]], red_tiles: list[tuple[int, int]]
) -> bool:
    # there has to be a better way than just calculating every green tile?
    raise NotImplementedError


def main(lines: list[str]):
    red_tiles = get_red_tiles(lines)
    sizes = {}
    for combo in itertools.combinations(red_tiles, 2):
        if has_only_red_or_green(combo, red_tiles):
            sizes[combo] = rect_size(*combo)
    return max(sizes.values())


if __name__ == "__main__":
    print(main(read_input()))

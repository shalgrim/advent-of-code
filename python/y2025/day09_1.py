import itertools

from coding_puzzle_tools import read_input


def rect_size(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    return (abs(tile2[0] - tile1[0]) + 1) * (abs(tile2[1] - tile1[1]) + 1)


def main(lines: list[str]):
    split_lines = [line.split(",") for line in lines]
    red_tiles: list[tuple[int, int]] = [(int(sl[0]), int(sl[1])) for sl in split_lines]
    # return max(rect_size(*combo) for combo in itertools.combinations(red_tiles, 2))
    sizes = {}
    for combo in itertools.combinations(red_tiles, 2):
        sizes[combo] = rect_size(*combo)
    return max(sizes.values())


if __name__ == "__main__":
    print(main(read_input()))

import time

from y2024.day11_1 import process_stones

# @lru_cache
# seems to go much faster (but still too slow) if this is inlined in process_stone
#   oh no i may have run this with testing=True so the number will be wrong...
# maybe next steps are something like...run 125 until you find another 125 within it
# and then you can at least short-circuit that one?
# same for 17
# def process_stone(stone):
#     if stone == "0":
#         return "1"
#     elif len(stone) % 2 == 0:
#         midpoint = len(stone) // 2
#         left = stone[:midpoint]
#         right = str(
#             int(stone[midpoint:])
#         )  # would be faster to lstrip 0s probably but watch out for number that is all 0s - nope, it's faster as is
#         return [left, right]
#     else:
#         # maybe just add a cache to this one since i bet we're losing a lot of time here
#         return str(int(stone) * 2024)

KNOWN_LENGTHS = {}
ALL_STONES = {}


class StoneTree:
    def __init__(self, stone_number):
        self.number = stone_number
        self.raw_children = process_stones([stone_number])
        self.expansion_lengths = {0: 1, 1: len(self.raw_children)}
        ALL_STONES[stone_number] = self
        self.children = []

    def get_length(self, num_expansions):
        if answer := self.expansion_lengths.get(num_expansions):
            return answer

        # figure it out...
        if not self.children:
            # create children
            self.children = [
                ALL_STONES.get(raw_child) or StoneTree(raw_child)
                for raw_child in self.raw_children
            ]

        # and ask them for answers
        self.expansion_lengths[num_expansions] = sum(
            child.get_length(num_expansions - 1) for child in self.children
        )
        return self.expansion_lengths[num_expansions]


def main(text, total_iterations):
    stone_trees = [StoneTree(stone_number) for stone_number in text.split()]
    return sum(st.get_length(total_iterations) for st in stone_trees)


if __name__ == "__main__":
    with open("../../data//2024/input11.txt") as f:
        # with open(f"../../data/2024/{filetype}11.txt") as f:
        text = f.read().strip()

    start_time = time.time()
    print(main(text, 75))
    print("--- %s seconds ---" % (time.time() - start_time))

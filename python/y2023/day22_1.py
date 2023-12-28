from collections import defaultdict


def do_ranges_overlap(tup1, tup2):
    min1, max1 = sorted([tup1[0], tup1[1]])
    min2, max2 = sorted([tup2[0], tup2[1]])

    return min1 <= max2 and min2 <= max2


class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.overlapping_bricks = []
        self.supporting_bricks = []

    def key(self):
        return self.x1, self.y1, self.z1

    def __str__(self):
        return str(max(self.z1, self.z2))

    def set_supporting_bricks(self, bricks_by_highest_z):
        # NEXT: Once everything has dropped can't I just find supporting bricks
        # by looking one level lower? And I should assert that everything with z > 1
        # has at least one blocking brick
        supporting_bricks = []

        for z in range(min(self.z1, self.z2) - 1, 0, -1):
            candidates = bricks_by_highest_z[z]
            supporting_bricks = [
                brick for brick in candidates if self.has_overlap(brick)
            ]
            if supporting_bricks:
                break
        self.supporting_bricks = supporting_bricks

    def has_overlap(self, other):
        return do_ranges_overlap(
            (self.x1, self.x2), (other.x1, other.x2)
        ) and do_ranges_overlap((self.y1, self.y2), (other.y1, other.y2))

    def set_overlapping_bricks(self, all_bricks):
        self.overlapping_bricks = [
            brick
            for brick in all_bricks
            if self.has_overlap(brick) and self.key() != brick.key()
        ]


def build_brick(line):
    points = line.split("~")
    p1 = tuple(int(d) for d in points[0].split(","))
    p2 = tuple(int(d) for d in points[1].split(","))
    return Brick(*p1, *p2)


def is_supported_by(
    potential_other_supporting_brick_index, index_of_og_brick, supports, supported_by
):
    """
    Returns true if the brick at potential_other_supporting_brick_index is supported by
    the brick at index_of_og_brick or by any brick transitively supported by index_of_og_brick
    """
    new_indexes_to_search = supports[index_of_og_brick]
    really_new_indexes = set()

    while not new_indexes_to_search:
        if potential_other_supporting_brick_index in new_indexes_to_search:
            return False
        really_new_indexes.clear()
        for index in new_indexes_to_search:
            really_new_indexes.update(supports[index])
        new_indexes_to_search = really_new_indexes

    return True


def can_disintegrate_brick(i, directly_supports, directly_supported_by):
    indexes_of_bricks_supported_by_brick = directly_supports.get(i)

    # if the brick supports nothing, easy call
    if not indexes_of_bricks_supported_by_brick:
        return True

    # if it does support something, find out what is directly supported by it
    # then check to see if anything else is directly supported by that thing
    # Now I need all of those bricks to be directly supported by something else
    for (
        brick_we_need_to_find_another_support_for
    ) in indexes_of_bricks_supported_by_brick:
        if len(directly_supported_by[brick_we_need_to_find_another_support_for]) == 1:
            return False
    return True


def get_transitive_supported_by(brick, supported_by):
    answer = supported_by.get(brick, set())
    old_len = 0
    new_len = len(answer)

    while new_len != old_len:
        new_answer = set()
        for b in answer:
            new_answer.update(supported_by.get(b, set()))
        answer.update(new_answer)
        old_len = new_len
        new_len = len(answer)

    return answer


def build_directly_supported_by(supported_by):
    answer = {}

    for key, value in sorted(supported_by.items(), key=lambda x: x[0]):
        # TODO: Starts to really slow down in here
        print(f"{key=}")
        potentially_directly_supporting_bricks = value
        reachable_secondarily = set()
        for brick in potentially_directly_supporting_bricks:
            foo = get_transitive_supported_by(brick, supported_by)
            reachable_secondarily.update(foo)
        bar = potentially_directly_supporting_bricks.difference(reachable_secondarily)
        answer[key] = bar

    return answer


def build_directly_supports(directly_supported_by):
    answer = defaultdict(set)
    for k, v in directly_supported_by.items():
        print(f"{k=}")
        for v2 in v:
            answer[v2].add(k)
    return answer


def drop_bricks(bricks_by_lowest_z):
    did_drop = False
    for z, bricks in sorted(bricks_by_lowest_z.items()):
        for brick in bricks:
            lo_z, hi_z = sorted([brick.z1, brick.z2])
            would_block = [
                b for b in brick.overlapping_bricks if max(b.z1, b.z2) < lo_z
            ]
            if would_block:
                blocking_z = max([max(b.z1, b.z2) for b in would_block])
                levels_to_drop = lo_z - blocking_z - 1
            else:
                levels_to_drop = lo_z - 1

            brick.z1 -= levels_to_drop
            brick.z2 -= levels_to_drop
            if not did_drop and levels_to_drop > 0:
                did_drop = True

    return did_drop


def get_bricks_by_z(bricks):
    bricks_by_highest_z = defaultdict(list)
    bricks_by_lowest_z = defaultdict(list)
    for brick in bricks:
        ordered_zs = sorted([brick.z1, brick.z2])
        bricks_by_lowest_z[ordered_zs[0]].append(brick)
        bricks_by_highest_z[ordered_zs[1]].append((brick))
    return bricks_by_lowest_z, bricks_by_highest_z


def main(lines):
    bricks = [build_brick(line) for line in lines]
    for brick in bricks:
        brick.set_overlapping_bricks(bricks)

    bricks_by_lowest_z, bricks_by_highest_z = get_bricks_by_z(bricks)

    while drop_bricks(bricks_by_lowest_z):
        bricks_by_lowest_z, bricks_by_highest_z = get_bricks_by_z(bricks)

    for brick in bricks:
        brick.set_supporting_bricks(bricks_by_highest_z)

    undisintegratable_bricks = set()
    for brick in bricks:
        if len(brick.supporting_bricks) == 1:
            undisintegratable_bricks.add(brick.supporting_bricks[0].key())

    return len(bricks) - len(undisintegratable_bricks)


if __name__ == "__main__":  # 749 is too high...and now I'm getting 909 sigh
    with open("../../data/2023/input22.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

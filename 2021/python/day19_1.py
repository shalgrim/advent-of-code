from collections import defaultdict
from copy import copy
from enum import IntEnum
from itertools import combinations


class Rotation(IntEnum):
    """
    each scanner could be in any of 24 different orientations:
    facing positive or negative x, y, or z, and considering any of four directions "up" from that facing
    """

    XYZ = 0
    XY_Z = 1
    X_YZ = 2
    X_Y_Z = 3
    XZY = 4
    XZ_Y = 5
    X_ZY = 6
    X_Z_Y = 7
    YXZ = 8
    YX_Z = 9
    Y_XZ = 10
    Y_X_Z = 11
    YZX = 12
    YZ_X = 13
    Y_ZX = 14
    Y_Z_X = 15
    ZXY = 16
    ZX_Y = 17
    Z_XY = 18
    Z_X_Y = 19
    ZYX = 20
    ZY_X = 21
    Z_YX = 22
    Z_Y_X = 23


def rotate(beacon, target_rotation):
    """a specific helper for get_rotation function"""
    if target_rotation == 0:
        return copy(beacon)
    elif target_rotation == 1:
        return [beacon[0], beacon[2], beacon[1]]
    elif target_rotation == 2:
        return [beacon[1], beacon[0], beacon[2]]
    elif target_rotation == 3:
        return [beacon[1], beacon[2], beacon[0]]
    elif target_rotation == 4:
        return [beacon[2], beacon[0], beacon[1]]
    elif target_rotation == 5:
        return [beacon[2], beacon[1], beacon[0]]
    else:
        raise Exception(f"Did not expect to see {target_rotation=}")


def polarity_rotate(beacon, target_rotation):
    """a specific helper for get_rotation function"""
    if target_rotation == 1:
        return [beacon[0], beacon[1], -beacon[2]]
    elif target_rotation == 2:
        return [beacon[0], -beacon[1], beacon[2]]
    elif target_rotation == 3:
        return [beacon[0], -beacon[1], -beacon[2]]
    else:
        raise Exception(f"Did not expect to see polarity {target_rotation=}")


def get_rotation(diffs1, diffs2, scanner1_rotation=None):
    """given the same beacon same two scanners, gives the second scanner's rotation"""
    diff1_magnitudes = [abs(v) for v in diffs1]
    diff2_magnitudes = [abs(v) for v in diffs2]

    if len(set(diff1_magnitudes)) < 3:
        return None  # only works if all three magnitudes are different

    # first find the xyz ordering
    rotation = 0
    copied_diff2_mags = copy(diff2_magnitudes)
    while copied_diff2_mags != diff1_magnitudes:
        rotation += 1
        copied_diff2_mags = rotate(diff2_magnitudes, rotation)

    # then put original in that order
    rotated_diffs2 = rotate(diffs2, rotation)

    # then figure out which of the possible four negativenesses it is
    polarity_rotation = 0
    copied_rotated_diffs2 = copy(rotated_diffs2)
    while copied_rotated_diffs2 != diffs1:
        if all([-d1 == d2 for d1, d2 in zip(diffs1, copied_rotated_diffs2)]):
            # if this is the case then I just subtracted different beacons from each other in s1 and s2
            copied_rotated_diffs2 = [-crd for crd in copied_rotated_diffs2]
            break

        polarity_rotation += 1
        copied_rotated_diffs2 = polarity_rotate(rotated_diffs2, polarity_rotation)

    # TODO: if scanner1_rotation is not None give absolute Rotation...I think the best way to do it is to unrotate diffs1 at start
    # Or could I make sense of it from squinting at Rotation?...that would be so much nicer
    return Rotation(4 * rotation + polarity_rotation)


def get_position(beacon1, beacon2, known_position):
    """
    :param beacon1: beacon from Scanner with no position, rotated to be as if in XYZ
    :param beacon2: same beacon from Scanner with known position, rotated to be as if in XYZ
    :param known_position: position of Scanner containing beacon2
    :return: the position of Scanner containing beacon1 in absolute coordinates
    """
    foo = tuple(
        beacon1[i] + beacon2[i] for i in range(3)
    )  # without respect to known position
    return tuple(known_position[i] + foo[i] for i in range(3))


def coords_from_lines(lines):
    coords = []
    for line in lines.split():
        coords.append([int(c) for c in line.split(',')])
    return coords


def manhattan_distance(p1, p2):
    return sum([abs(p2[i] - p1[i]) for i in range(3)])


def distances_from_coords(coords):
    source_to_dest_distances = defaultdict(dict)
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dist = manhattan_distance(coords[i], coords[j])
            source_to_dest_distances[i][j] = dist

    distance_dict = defaultdict(list)
    for source, subd in source_to_dest_distances.items():
        for dest, dist in subd.items():
            distance_dict[dist].append((source, dest))

    return distance_dict


def magnitude_diffs_from_coords(coords):
    answer = []
    combos = combinations(coords, 2)
    for c1, c2 in combos:
        answer.append({abs(c1[i] - c2[i]) for i in range(3)})

    return answer


def distance_signatures_from_coords(coords):
    distance_signatures = {}
    for i, source in enumerate(coords):
        distance_signature = []
        for j, dest in enumerate(coords):
            if i == j:
                continue
            distance_signature.append(
                frozenset({abs(source[k] - dest[k]) for k in range(3)})
            )
        distance_signatures[i] = distance_signature

    return distance_signatures


def find_shared_nodes(ds0, ds1):
    for node_id, distance_signature in ds0.items():
        for other_node_id, other_distance_signature in ds1.items():
            if (
                len(set(distance_signature).intersection(set(other_distance_signature)))
                >= 11
            ):
                print(node_id, other_node_id)


def process_input(lines):
    scanners = {}
    scanner_id = -1
    for line in lines:
        if not line:
            continue
        if line.startswith('---'):
            scanner_id = int(line.split()[2])
            scanners[scanner_id] = Scanner(scanner_id)
        else:
            coords = line.split(',')
            coords = [int(c) for c in coords]
            scanners[scanner_id].add_beacon(coords)

    return scanners


class Scanner:
    def __init__(self, scanner_id):
        self.sid = scanner_id
        self.beacons = {}
        self.position = None
        self.rotation = None

    def add_beacon(self, coords):
        beacon_id = 0 if not self.beacons else max(self.beacons.keys()) + 1
        self.beacons[beacon_id] = coords

    @property
    def distance_signatures(self):
        answer = {}
        for source_beacon_id, source in self.beacons.items():
            ds = []
            for destination_beacon_id, destination in self.beacons.items():
                if source_beacon_id == destination_beacon_id:
                    continue
                ds.append(
                    frozenset({abs(source[i] - destination[i]) for i in range(3)})
                )
            answer[source_beacon_id] = ds
        return answer

    def overlap_set(self, other):
        overlap_ids = set()
        for self_beacon_id, self_ds in self.distance_signatures.items():
            for other_beacon_id, other_ds in other.distance_signatures.items():
                if len(set(self_ds).intersection(set(other_ds))) >= 11:
                    overlap_ids.add(self_beacon_id)

        return {tuple(self.beacons[beacon_id]) for beacon_id in overlap_ids}

    def overlaps(self, other):
        for self_beacon_id, self_ds in self.distance_signatures.items():
            for other_beacon_id, other_ds in other.distance_signatures.items():
                if len(set(self_ds).intersection(set(other_ds))) >= 11:
                    return self_beacon_id, other_beacon_id
        return False

    def rotate_beacon_by_id(self, beacon_id):
        beacon = self.beacons[beacon_id]
        return self.rotate_beacon(beacon)

    def rotate_beacon(self, beacon):
        dividend = self.rotation // 6
        if dividend == 0:
            rotated = copy(beacon)
        elif dividend == 1:
            rotated = [beacon[0], beacon[2], beacon[1]]
        elif dividend == 2:
            rotated = [beacon[1], beacon[0], beacon[2]]
        elif dividend == 3:
            rotated = [beacon[1], beacon[2], beacon[0]]
        elif dividend == 4:
            rotated = [beacon[2], beacon[0], beacon[1]]
        elif dividend == 5:
            rotated = [beacon[2], beacon[1], beacon[0]]
        else:
            raise Exception(f'Unexpected {dividend=}')

        mod = self.rotation % 4
        if mod == 0:
            final = copy(rotated)
        elif mod == 1:
            final = [rotated[0], rotated[1], -rotated[2]]
        elif mod == 2:
            final = [rotated[0], -rotated[1], rotated[2]]
        elif mod == 3:
            final = [rotated[0], -rotated[1], -rotated[2]]
        else:
            raise Exception(f'Unexpected {mod=}')

        return final

    def absolutify_beacon(self, beacon_id):
        rotated = self.rotate_beacon_by_id(beacon_id)
        absolute = [self.position[i] - rotated[i] for i in range(3)]
        return absolute

    def orient(self, other):
        """orients self using already oriented other"""
        mapping = {}
        for source_beacon_id, source_ds in self.distance_signatures.items():
            for dest_beacon_id, dest_ds in other.distance_signatures.items():
                if len(set(source_ds).intersection(set(dest_ds))) >= 11:
                    mapping[source_beacon_id] = dest_beacon_id
        assert len(mapping) >= 12
        beacon_pairs = list(mapping.items())
        first_pair, second_pair = beacon_pairs[:2]
        source_b1 = self.beacons[first_pair[0]]
        source_b2 = self.beacons[second_pair[0]]
        dest_b1 = other.beacons[first_pair[1]]
        dest_b2 = other.beacons[second_pair[1]]
        diffs_1 = [source_b2[i] - source_b1[i] for i in range(3)]
        diffs_2 = [dest_b2[i] - dest_b1[i] for i in range(3)]
        self.rotation = get_rotation(diffs_1, diffs_2, other.rotation)
        self.position = get_position(
            self.rotate_beacon_by_id(first_pair[0]),
            other.rotate_beacon_by_id(first_pair[1]),
            other.position,
        )


def orient(scanner1, scanner2):
    mapping = {}
    for source_beacon_id, source_ds in scanner1.distance_signatures.items():
        for dest_beacon_id, dest_ds in scanner2.distance_signatures.items():
            if len(set(source_ds).intersection(set(dest_ds))) >= 11:
                mapping[source_beacon_id] = dest_beacon_id

    assert len(mapping) >= 12
    beacon_pairs = list(mapping.items())
    first_pair, second_pair = beacon_pairs[:2]

    # now rotate
    source_b1 = scanner1.beacons[first_pair[0]]
    source_b2 = scanner1.beacons[second_pair[0]]
    dest_b1 = scanner2.beacons[first_pair[1]]
    dest_b2 = scanner2.beacons[second_pair[1]]

    diffs_1 = [source_b2[i] - source_b1[i] for i in range(3)]
    if len(set(diffs_1)) < 3:
        print("WARNING you didn't code for this")
    diffs_2 = [dest_b2[i] - dest_b1[i] for i in range(3)]

    rotation = []
    polarity = []
    for self_index, self_val in enumerate(diffs_1):
        if self_val in diffs_2:
            other_index = diffs_2.index(self_val)
            polarity.append(1)
        else:
            other_index = diffs_2.index(-self_val)
            polarity.append(-1)
        rotation.append(other_index)

    position = []

    for i, source_val in enumerate(source_b1):
        dest_val = dest_b1[rotation[i]]
        pol = polarity[i]
        if pol < 0:
            position.append(source_val - -dest_val)
        else:
            position.append(source_val - dest_val)

    return position, rotation, polarity


def absolutify(
    relative_position,
    relative_rotation,
    relative_polarity,
    reference_position,
    reference_rotation,
    reference_polarity,
):

    # this loop got me four out of five in the test
    # out_position = []
    # for rel_pos, ref_pos, ref_pol in zip(relative_position, reference_position, reference_polarity):
    #     out_position.append(ref_pol * rel_pos + ref_pos)

    out_position = []
    for i in range(3):
        rel_pos = relative_position[reference_rotation[i]] * reference_polarity[i]
        ref_pos = reference_position[i]
        out_position.append(rel_pos + ref_pos)

    out_rotation = []
    for rel_rot in relative_rotation:
        out_rotation.append(reference_rotation[rel_rot])

    out_polarity = []
    for rel_pol, ref_pol in zip(relative_polarity, reference_polarity):
        out_polarity.append(rel_pol * ref_pol)

    return out_position, out_rotation, out_polarity


def absolutify_beacon(beacon, scanner_position, scanner_rotation, scanner_polarity):
    absolute_position = []
    for i in range(3):
        absolute_position.append(
            beacon[scanner_rotation[i]] * scanner_polarity[i] + scanner_position[i]
        )
    return tuple(absolute_position)


def generate_all_beacons_with_absolute_coordinates(
    scanners, positions, rotations, polarities
):
    all_beacons = []
    for scanner_id, scanner in scanners.items():
        scanner_position = positions[scanner_id]
        scanner_rotation = rotations[scanner_id]
        scanner_polarity = polarities[scanner_id]

        for beacon in scanner.beacons.values():
            all_beacons.append(
                absolutify_beacon(
                    beacon, scanner_position, scanner_rotation, scanner_polarity
                )
            )

    return all_beacons


def main(lines):
    scanners = process_input(lines)
    overlaps = get_overlaps(scanners)
    print(f'{overlaps=}')

    # now try orienting all of them so I can uniquify all
    # positions = {0: [0, 0, 0]}
    # rotations = {0: [0, 1, 2]}
    # polarities = {0: [1, 1, 1]}
    scanners[0].position = (0, 0, 0)
    scanners[0].rotation = Rotation.XYZ

    while not all(s.position for s in scanners):
        for overlap in overlaps:
            s1 = scanners[overlap[0]]
            s2 = scanners[overlap[1]]

            if s1.sid.position and not s2.sid.position:
                s2.orient(s1)
                continue  # just here for the breakpoint
            elif s2.position and not s1.position:
                s1.orient(s2)
                continue  # just here for the breakpoint

    all_beacons = generate_all_beacons_with_absolute_coordinates(scanners)
    return len(set(all_beacons))


def get_overlaps(scanners):
    overlaps = []
    for scanner_id, scanner in scanners.items():
        for other_scanner_id, other_scanner in scanners.items():
            if other_scanner_id <= scanner_id:
                continue
            if scanner.overlaps(other_scanner):
                overlaps.append((scanner_id, other_scanner_id))
    return overlaps


if __name__ == '__main__':
    with open('../data/input19.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

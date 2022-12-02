from collections import defaultdict
from copy import copy
from enum import IntEnum
from itertools import combinations


class Rotation(IntEnum):
    """
    A Rotation stores the order in which it stores the "absolute" axes (absolute is arbirtary but always defined)
    So, if a scanner sees a beacon as (1, 3, 2), but its rotation is XZY, that means that in absolute terms the beacon
    is actually at (1, 2, 3)
    So to unrotate is to absolutify, which is to "undo" the rotation stored
    """

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5

    @staticmethod
    def unrotate(beacon, beacon_rotation):
        if beacon_rotation == Rotation.XYZ:
            return beacon
        elif beacon_rotation == Rotation.XZY:
            return [beacon[0], beacon[2], beacon[1]]
        elif beacon_rotation == Rotation.YXZ:
            return [beacon[1], beacon[0], beacon[2]]
        elif beacon_rotation == Rotation.YZX:
            return [beacon[2], beacon[0], beacon[1]]
        elif beacon_rotation == Rotation.ZXY:
            return [beacon[1], beacon[2], beacon[0]]
        elif beacon_rotation == Rotation.ZYX:
            return [beacon[2], beacon[1], beacon[0]]
        else:
            raise Exception(f'Invalid Rotation={beacon_rotation}')


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


def determine_rotation(
    diffs_from_beacon_with_known_rotation,
    diffs_from_beacon_with_unknown_rotation,
    known_rotation=None,
):
    """given the same beacon same two scanners, gives the second scanner's rotation"""
    known_diff_magnitdues = [abs(v) for v in diffs_from_beacon_with_known_rotation]
    rotated_known_diff_magnitudes = unrotate_and_polarize_beacon(
        known_diff_magnitdues, known_rotation, (1, 1, 1)
    )
    unknown_diff_magnitudes = [abs(v) for v in diffs_from_beacon_with_unknown_rotation]

    for rotation in Rotation:
        if (
            unrotate_and_polarize_beacon(unknown_diff_magnitudes, rotation, (1, 1, 1))
            == rotated_known_diff_magnitudes
        ):
            return rotation
    else:
        raise Exception(
            f"Couldn't find rotation to match {diffs_from_beacon_with_known_rotation=} and {diffs_from_beacon_with_unknown_rotation=}"
        )


def determine_position(
    beacon_from_scanner_with_unknown_position,
    beacon_from_scanner_with_known_position,
    known_position,
):
    """
    :param beacon_from_scanner_with_known_position: beacon from Scanner with no position, rotated to be as if in XYZ
    :param beacon_from_scanner_with_known_position: same beacon from Scanner with known position, rotated to be as if in XYZ
    :param known_position: position of Scanner containing beacon2
    :return: the position of Scanner containing beacon1 in absolute coordinates
    """
    return tuple(
        [
            beacon_from_scanner_with_known_position[i]
            - beacon_from_scanner_with_unknown_position[i]
            + known_position[i]
            for i in range(3)
        ]
    )


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


def unrotate_and_polarize_beacon(beacon, rotation, polarity):
    rotated = Rotation.unrotate(beacon, rotation)
    final = [r * p for r, p in zip(rotated, polarity)]
    return final


class Scanner:
    def __init__(self, scanner_id):
        self.sid = scanner_id
        self.beacons = {}
        self.position = None
        self.rotation = None
        self.polarity = None  # always store in absolute (unrotated) order

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

    def unrotate_and_polarize_beacon_by_id(self, beacon_id):
        beacon = self.beacons[beacon_id]
        return unrotate_and_polarize_beacon(beacon, self.rotation, self.polarity)

    def absolutify_beacon_by_id(self, beacon_id):
        rotated = self.unrotate_and_polarize_beacon_by_id(beacon_id)
        absolute = [self.position[i] + rotated[i] for i in range(3)]
        return absolute

    def determine_polarity_of_axis(
        self, axis, unrotated_other_beacons, unrotated_source_beacons
    ):
        summed_axis = [
            source[axis] + dest[axis]
            for source, dest in zip(unrotated_source_beacons, unrotated_other_beacons)
        ]
        if len(set(summed_axis)) == 1:
            answer = -1
        else:
            diffed_axis = [
                source[axis] - dest[axis]
                for source, dest in zip(
                    unrotated_source_beacons, unrotated_other_beacons
                )
            ]
            assert len(set(diffed_axis)) == 1
            answer = 1
        return answer

    def determine_polarity(self, other, beacon_to_beacon_mapping):
        """
        Determine the absolute polarity of this
        :param other: A scanner with a known polarity
        :param beacon_to_beacon_mapping: dict mapping overlapping beacon IDs from self to other
        :return: an absolute polarity for self
        """
        source_beacons = []
        other_beacons = []

        for source_beacon_id, other_beacon_id in beacon_to_beacon_mapping.items():
            source_beacons.append(self.beacons[source_beacon_id])
            other_beacons.append(other.beacons[other_beacon_id])

        assert (
            self.rotation is not None
        ), "How did I get here with rotation not being assigned"

        unrotated_source_beacons = [
            unrotate_and_polarize_beacon(beacon, self.rotation, (1, 1, 1))
            for beacon in source_beacons
        ]
        unrotated_other_beacons = [
            unrotate_and_polarize_beacon(beacon, other.rotation, other.polarity)
            for beacon in other_beacons
        ]

        polarity = [
            self.determine_polarity_of_axis(
                i, unrotated_other_beacons, unrotated_source_beacons
            )
            for i in range(3)
        ]
        return tuple(polarity)

    def orient(self, other):
        """orients self using already oriented other"""
        beacon_to_beacon_mapping = {}
        for source_beacon_id, source_ds in self.distance_signatures.items():
            for dest_beacon_id, dest_ds in other.distance_signatures.items():
                if len(set(source_ds).intersection(set(dest_ds))) >= 11:
                    beacon_to_beacon_mapping[source_beacon_id] = dest_beacon_id
        assert len(beacon_to_beacon_mapping) >= 12
        beacon_pairs = list(beacon_to_beacon_mapping.items())
        first_pair, second_pair = beacon_pairs[:2]

        beacon1_from_self = self.beacons[first_pair[0]]
        beacon1_from_other = other.beacons[first_pair[1]]
        beacon2_from_self = self.beacons[second_pair[0]]
        beacon2_from_other = other.beacons[second_pair[1]]
        diffs_from_beacon2_to_beacon1_from_self = [
            beacon2_from_self[i] - beacon1_from_self[i] for i in range(3)
        ]
        diffs_from_beacon2_to_beacon1_from_other = [
            beacon2_from_other[i] - beacon1_from_other[i] for i in range(3)
        ]
        self.rotation = determine_rotation(
            diffs_from_beacon2_to_beacon1_from_other,
            diffs_from_beacon2_to_beacon1_from_self,
            other.rotation,
        )

        self.polarity = self.determine_polarity(other, beacon_to_beacon_mapping)
        self.position = determine_position(
            self.unrotate_and_polarize_beacon_by_id(first_pair[0]),
            other.unrotate_and_polarize_beacon_by_id(first_pair[1]),
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


def generate_all_beacons_with_absolute_coordinates(scanners):
    all_beacons = []
    for scanner_id, scanner in scanners.items():
        all_beacons.extend(
            [
                tuple(scanner.absolutify_beacon_by_id(beacon_id))
                for beacon_id in scanner.beacons
            ]
        )

    return all_beacons


def get_overlaps(scanners):
    overlaps = []
    for scanner_id, scanner in scanners.items():
        for other_scanner_id, other_scanner in scanners.items():
            if other_scanner_id <= scanner_id:
                continue
            if scanner.overlaps(other_scanner):
                overlaps.append((scanner_id, other_scanner_id))
    return overlaps


def main(lines):
    scanners = create_and_position_all_scanners(lines)
    all_beacons = generate_all_beacons_with_absolute_coordinates(scanners)
    return len(set(all_beacons))


def create_and_position_all_scanners(lines):
    scanners = process_input(lines)
    overlaps = get_overlaps(scanners)
    print(f'{overlaps=}')
    scanners[0].position = (0, 0, 0)
    scanners[0].rotation = Rotation.XYZ
    scanners[0].polarity = (1, 1, 1)
    while not all(s.position for s in scanners.values()):
        for overlap in overlaps:
            s1 = scanners[overlap[0]]
            s2 = scanners[overlap[1]]

            if s1.position and not s2.position:
                print(f'orienting {s2.sid} based on {s1.sid}')
                s2.orient(s1)
                print(f'{s2.position} {s2.rotation} {s2.polarity}')
            elif s2.position and not s1.position:
                print(f'orienting {s1.sid} based on {s2.sid}')
                s1.orient(s2)
                print(f'{s1.position} {s1.rotation} {s1.polarity}')
    return scanners


if __name__ == '__main__':
    with open('../data/input19.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

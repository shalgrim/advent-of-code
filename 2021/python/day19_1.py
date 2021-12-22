from collections import defaultdict
from itertools import combinations


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

    def overlaps(self, other):
        for self_beacon_id, self_ds in self.distance_signatures.items():
            for other_beacon_id, other_ds in other.distance_signatures.items():
                if len(set(self_ds).intersection(set(other_ds))) >= 11:
                    return self_beacon_id, other_beacon_id
        return False


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


def main(lines):
    scanners = process_input(lines)
    overlaps = []
    shared_beacons = []
    for scanner_id, scanner in scanners.items():
        for other_scanner_id, other_scanner in scanners.items():
            if other_scanner_id <= scanner_id:
                continue
            if scanner.overlaps(other_scanner):
                overlaps.append((scanner_id, other_scanner_id))

    print(f'{overlaps=}')

    # now try orienting all of them so I can uniquify all
    positions = {0: [0, 0, 0]}
    rotations = {0: [0, 1, 2]}
    polarities = {0: [1, 1, 1]}

    while len(positions) < len(scanners):
        for overlap in overlaps:
            # TODO: for every shared beacon add in the form:
            # (source_scanner_id, destination_scanner_id, source_beacon_id, destination_beacon_id)
            # and then what...?
            # it may make more sense to absolutely identify positions and orientations because
            # then i can uniquify all beacons
            # let's try the second thing first and if that doesn't work i've got the first idea

            s1 = scanners[overlap[0]]
            s2 = scanners[overlap[1]]

            if s1.sid in positions and s2.sid not in positions:
                relative_position, relative_rotation, relative_polarity = orient(s1, s2)
                absolute_position, absolute_rotation, absolute_polarity = absolutify(
                    relative_position,
                    relative_rotation,
                    relative_polarity,
                    positions[s1.sid],
                    rotations[s1.sid],
                    polarities[s1.sid],
                )
                positions[s2.sid] = absolute_position
                rotations[s2.sid] = absolute_rotation
                polarities[s2.sid] = absolute_polarity
                continue  # just here for the breakpoint
            elif s2.sid in positions and s1.sid not in positions:
                relative_position, relative_rotation, relative_polarity = orient(s2, s1)
                absolute_position, absolute_rotation, absolute_polarity = absolutify(
                    relative_position,
                    relative_rotation,
                    relative_polarity,
                    positions[s2.sid],
                    rotations[s2.sid],
                    polarities[s2.sid],
                )
                positions[s1.sid] = absolute_position
                rotations[s1.sid] = absolute_rotation
                polarities[s1.sid] = absolute_polarity
                continue  # just here for the breakpoint

    raise NotImplementedError


if __name__ == '__main__':
    with open('../data/test19.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

from collections import defaultdict
from itertools import combinations


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
                    return True
        return False

    # def overlap_sets(self, other):
    #     answer = []
    #     for self_beacon_id, self_ds in self.distance_signatures.items():
    #         for other_beacon_id, other_ds in other.distance_signatures.items():



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
                # TODO: for every shared beacon add in the form:
                # (source_scanner_id, destination_scanner_id, source_beacon_id, destination_beacon_id)
                # and then what...?
                # it may make more sense to absolutely identify positions and orientations because
                # then i can uniquify all beacons

    raise NotImplementedError


if __name__ == '__main__':
    with open('../data/test19.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

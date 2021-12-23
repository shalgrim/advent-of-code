from collections import defaultdict

import pytest
from day19_1 import get_overlaps, Rotation
from day19_1 import main as main1
from day19_1 import process_input

OVERLAPS = defaultdict(dict)
OVERLAPS[0][1] = {
    (-618, -824, -621),
    (-537, -823, -458),
    (-447, -329, 318),
    (404, -588, -901),
    (544, -627, -890),
    (528, -643, 409),
    (-661, -816, -575),
    (390, -675, -793),
    (423, -701, 434),
    (-345, -311, 381),
    (459, -707, 401),
    (-485, -357, 347),
}
OVERLAPS[1][0] = {
    (686, 422, 578),
    (605, 423, 415),
    (515, 917, -361),
    (-336, 658, 858),
    (-476, 619, 847),
    (-460, 603, -452),
    (729, 430, 532),
    (-322, 571, 750),
    (-355, 545, -477),
    (413, 935, -424),
    (-391, 539, -444),
    (553, 889, -390),
}

# the 12 beacons recognized by 1 and 4 but from perspective of 0
ABSOLUTE_OVERLAPS_14 = {
    (459, -707, 401),
    (-739, -1745, 668),
    (-485, -357, 347),
    (432, -2009, 850),
    (528, -643, 409),
    (423, -701, 434),
    (-345, -311, 381),
    (408, -1815, 803),
    (534, -1912, 768),
    (-687, -1600, 576),
    (-447, -329, 318),
    (-635, -1737, 486),
}


@pytest.fixture
def test_input():
    with open('../../data/test19.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_main1(test_input):
    assert main1(test_input) == 78


def test_main1_in_pieces(test_input):
    scanners = process_input(test_input)
    overlaps = get_overlaps(scanners)
    assert set(overlaps) == {(0, 1), (1, 3), (1, 4), (2, 4)}
    s0 = scanners[0]
    s1 = scanners[1]
    s0.position = (0, 0, 0)
    s0.rotation = Rotation.XYZ
    assert s0.overlap_set(s1) == OVERLAPS[0][1]
    assert s1.overlap_set(s0) == OVERLAPS[1][0]
    s1.orient(s0)
    assert s1.position == (68, -1246, -43)
    assert s1.rotation == Rotation.X_YZ
    # s0.beacons[9] is the same beacon as s1.beacons[0]
    assert s0.beacons[9] == s1.absolutify_beacon(0)
    s1_absolute_beacons = {tuple(s1.absolutify_beacon(sid)) for sid in s1.beacons}
    assert len(s1_absolute_beacons.intersection(OVERLAPS[0][1])) == 12
    assert s1_absolute_beacons.issuperset(OVERLAPS[0][1])

    # confirm ABSOLUTE_OVERLAPS_14 are all in s1.beacons when absolutified
    for beacon in ABSOLUTE_OVERLAPS_14:
        assert beacon in s1_absolute_beacons

    # works up to here

    # orient s4 and confirm its position
    s4 = scanners[4]
    s4.orient(s1)
    assert s4.position == (-20, -1133, 1061)

    # get overlap between s1 and s4 and assert that when absolutified they are ABSOLUTE_OVERLAPS_14

    s2 = scanners[2]
    s2.orient(s4)
    assert s2.position == (1105, -1205, 1229)

    s3 = scanners[3]
    s3.orient(s1)
    assert s3.position == (-92, -2380, -20)

from day18_1 import SnailfishNumber, explode, needs_to_explode, split


def test_needs_to_explode():
    assert needs_to_explode([[[[[9, 8], 1], 2], 3], 4])
    assert needs_to_explode([7, [6, [5, [4, [3, 2]]]]])
    assert needs_to_explode([[6, [5, [4, [3, 2]]]], 1])
    assert needs_to_explode([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
    assert needs_to_explode([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])


def test_can_explode():
    assert SnailfishNumber([[[[[9, 8], 1], 2], 3], 4]).can_explode()
    assert SnailfishNumber([7, [6, [5, [4, [3, 2]]]]]).can_explode()
    assert SnailfishNumber([[6, [5, [4, [3, 2]]]], 1]).can_explode()
    assert SnailfishNumber([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]).can_explode()
    assert SnailfishNumber([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]).can_explode()


def test_explode():
    assert explode([[[[[9, 8], 1], 2], 3], 4]) == [[[[0, 9], 2], 3], 4]
    assert explode([7, [6, [5, [4, [3, 2]]]]]) == [7, [6, [5, [7, 0]]]]
    assert explode([[6, [5, [4, [3, 2]]]], 1]) == [[6, [5, [7, 0]]], 3]
    assert explode([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]) == [
        [3, [2, [8, 0]]],
        [9, [5, [4, [3, 2]]]],
    ]
    assert explode([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]) == [
        [3, [2, [8, 0]]],
        [9, [5, [7, 0]]],
    ]


def test_split():
    assert split([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]) == [
        [[[0, 7], 4], [[7, 8], [0, 13]]],
        [1, 1],
    ]
    assert split([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]) == [
        [[[0, 7], 4], [[7, 8], [0, [6, 7]]]],
        [1, 1],
    ]


def test_addition():
    added = SnailfishNumber([1, 2]) + SnailfishNumber([[3, 4], 5])
    assert added.raw_form() == [[1, 2], [[3, 4], 5]]

from day18_1 import (
    SnailfishNumber,
    explode,
    needs_to_explode,
    reduce,
    reduce_from_file,
    split,
)


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


def test_can_split():
    assert SnailfishNumber([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]).can_split()
    assert SnailfishNumber([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]).can_split()


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


def test_reduce():
    assert reduce([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]) == [
        [[[0, 7], 4], [[7, 8], [6, 0]]],
        [8, 1],
    ]


def test_reduce_from_file():
    assert reduce_from_file('../../data/test18_1.txt') == [
        [[[1, 1], [2, 2]], [3, 3]],
        [4, 4],
    ]
    assert reduce_from_file('../../data/test18_2.txt') == [
        [[[3, 0], [5, 3]], [4, 4]],
        [5, 5],
    ]
    assert reduce_from_file('../../data/test18_3.txt') == [
        [[[5, 0], [7, 4]], [5, 5]],
        [6, 6],
    ]
    assert reduce_from_file('../../data/test18_4.txt') == [
        [[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
        [[[0, 7], [6, 6]], [8, 7]],
    ]


def test_magnitude():
    assert SnailfishNumber([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]).magnitude() == 4140

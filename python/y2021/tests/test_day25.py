import pytest

from day25_1 import map_step, map_step_n
from day25_1 import main as main1


@pytest.fixture
def test_input():
    with open('../../data/test25.txt') as f:
        return [line.strip() for line in f.readlines()]


example_1_0 = [
    list('...>...'),
    list('.......'),
    list('......>'),
    list('v.....>'),
    list('......>'),
    list('.......'),
    list('..vvv..'),
]
example_1_1 = [
    list('..vv>..'),
    list('.......'),
    list('>......'),
    list('v.....>'),
    list('>......'),
    list('.......'),
    list('....v..'),
]

example_1_2 = [
    list('....v>.'),
    list('..vv...'),
    list('.>.....'),
    list('......>'),
    list('v>.....'),
    list('.......'),
    list('.......'),
]
example_1_3 = [
    list('......>'),
    list('..v.v..'),
    list('..>v...'),
    list('>......'),
    list('..>....'),
    list('v......'),
    list('.......'),
]

example_1_4 = [
    list('>......'),
    list('..v....'),
    list('..>.v..'),
    list('.>.v...'),
    list('...>...'),
    list('.......'),
    list('v......'),
]


def map_from_text(raw_text):
    lines = raw_text.split()
    return [list(line.strip()) for line in lines]


example_2_0 = map_from_text(
    """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
)

example_2_1 = map_from_text(
    """....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v"""
)

example_2_2 = map_from_text(
    """>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv."""
)

example_2_3 = map_from_text(
    """v>v.v>.>v.
v...>>.v.v
>vv>.>v>..
>>v>v.>.v>
..>....v..
.>.>v>v..v
..v..v>vv>
v.v..>>v..
.v>....v.."""
)

example_2_4 = map_from_text(
    """v>..v.>>..
v.v.>.>.v.
>vv.>>.v>v
>>.>..v>.>
..v>v...v.
..>>.>vv..
>.v.vv>v.v
.....>>vv.
vvv>...v.."""
)

example_2_5 = map_from_text(
    """vv>...>v>.
v.v.v>.>v.
>.v.>.>.>v
>v>.>..v>>
..v>v.v...
..>.>>vvv.
.>...v>v..
..v.v>>v.v
v.v.>...v."""
)

example_2_10 = map_from_text(
    """..>..>>vv.
v.....>>.v
..v.v>>>v>
v>.>v.>>>.
..v>v.vv.v
.v.>>>.v..
v.v..>v>..
..v...>v.>
.vv..v>vv."""
)

example_2_20 = map_from_text(
    """v>.....>>.
>vv>.....v
.>v>v.vv>>
v>>>v.>v.>
....vv>v..
.v.>>>vvv.
..v..>>vv.
v.v...>>.v
..v.....v>"""
)

example_2_30 = map_from_text(
    """.vv.v..>>>
v>...v...>
>.v>.>vv.>
>v>.>.>v.>
.>..v.vv..
..v>..>>v.
....v>..>v
v.v...>vv>
v.v...>vvv"""
)

example_2_40 = map_from_text(
    """>>v>v..v..
..>>v..vv.
..>>>v.>.v
..>>>>vvv>
v.....>...
v.v...>v>>
>vv.....v>
.>v...v.>v
vvv.v..v.>"""
)

example_2_50 = map_from_text(
    """..>>v>vv.v
..v.>>vv..
v.>>v>>v..
..>>>>>vv.
vvv....>vv
..v....>>>
v>.......>
.vv>....v>
.>v.vv.v.."""
)

example_2_55 = map_from_text(
    """..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv...>..>
>vv.....>.
.>v.vv.v.."""
)

example_2_56 = map_from_text(
    """..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv....>.>
>vv......>
.>v.vv.v.."""
)

example_2_57 = map_from_text(
    """..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v.."""
)

example_2_58 = map_from_text(
    """..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v..
"""
)


def test_map_step():
    assert map_step([list('...>>>>>...')]) == [list('...>>>>.>..')]
    assert map_step([list('...>>>>.>..')]) == [list('...>>>.>.>.')]
    assert map_step(
        [list('..........'), list('.>v....v..'), list('.......>..'), list('..........')]
    ) == [
        list('..........'),
        list('.>........'),
        list('..v....v>.'),
        list('..........'),
    ]
    assert map_step(example_1_0) == example_1_1
    assert map_step(example_1_1) == example_1_2
    assert map_step(example_1_2) == example_1_3
    assert map_step(example_1_3) == example_1_4
    assert map_step(example_2_0) == example_2_1
    assert map_step(example_2_1) == example_2_2
    assert map_step(example_2_2) == example_2_3
    assert map_step(example_2_3) == example_2_4
    assert map_step(example_2_4) == example_2_5
    assert map_step(map_step(map_step(map_step(map_step(example_2_5))))) == example_2_10
    assert map_step(example_2_55) == example_2_56
    assert map_step(example_2_56) == example_2_57
    assert map_step(example_2_57) == example_2_58


def test_map_step_n():
    assert map_step_n(example_2_10, 10) == example_2_20
    assert map_step_n(example_2_20, 10) == example_2_30
    assert map_step_n(example_2_30, 10) == example_2_40
    assert map_step_n(example_2_40, 10) == example_2_50
    assert map_step_n(example_2_50, 5) == example_2_55


def test_main1(test_input):
    assert main1(test_input) == 58

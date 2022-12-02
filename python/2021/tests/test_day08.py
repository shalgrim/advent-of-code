import pytest
from day08_2 import get_configuration, get_output_display, main

FIRST_EXAMPLE_LINE = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'


@pytest.fixture
def test_lines():
    with open('../../data/test08.txt') as f:
        return [line.strip() for line in f.readlines()]


def test_get_output_display():
    assert (
        get_output_display(
            'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
        )
        == 5353
    )


def test_get_configuration():
    assert get_configuration(FIRST_EXAMPLE_LINE) == {
        0: 'd',
        1: 'e',
        2: 'a',
        3: 'f',
        4: 'g',
        5: 'b',
        6: 'c',
    }


def test_part_2(test_lines):
    assert main(test_lines) == 61229

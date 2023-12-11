import pytest
from y2023.day10_1 import generate_loop, get_possible_s_shapes, main
from y2023.day10_2 import main as main2


@pytest.fixture
def test_input1():
    with open("../../../data/2023/test10_1.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input2():
    with open("../../../data/2023/test10_2.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input3():
    with open("../../../data/2023/test10_3.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input4():
    with open("../../../data/2023/test10_4.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input5():
    with open("../../../data/2023/test10_5.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input6():
    with open("../../../data/2023/test10_6.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_get_possible_s_shapes(test_input1, test_input2):
    assert get_possible_s_shapes(test_input1) == "F"
    assert get_possible_s_shapes(test_input2) == "F"


def test_generate_loop(test_input1, test_input2):
    assert generate_loop(test_input1) == (
        "F",
        [
            (1, 1),
            (2, 1),
            (3, 1),
            (3, 2),
            (3, 3),
            (2, 3),
            (1, 3),
            (1, 2),
        ],
    )
    assert generate_loop(test_input2) == (
        "F",
        [
            (0, 2),
            (1, 2),
            (1, 1),
            (2, 1),
            (2, 0),
            (3, 0),
            (3, 1),
            (3, 2),
            (4, 2),
            (4, 3),
            (3, 3),
            (2, 3),
            (1, 3),
            (1, 4),
            (0, 4),
            (0, 3),
        ],
    )


def test_part_1(test_input1, test_input2):
    assert main(test_input1) == 4
    assert main(test_input2) == 8


def test_part_2(test_input3, test_input4, test_input5, test_input6):
    assert main2(test_input3) == 4
    assert main2(test_input4) == 4
    assert main2(test_input5) == 8
    assert (
        main2(
            test_input6,
            "../../../data/2023/test10_clean_map6.txt",
            "../../../data/2023/test10_clean_map6_enclose.txt",
        )
        == 10
    )

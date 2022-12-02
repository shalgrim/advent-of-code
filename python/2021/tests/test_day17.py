import pytest
from day17_1 import REAL_INPUT, TEST_INPUT, input_parser
from day17_1 import main as main1
from day17_1 import main2 as main1_1
from day17_2 import find_pairs_that_work, find_pairs_that_work_for_initial_yvel
from day17_2 import main as main2
from day17_2 import submain


TEST_ANSWER_TEXT = """23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
    25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
    8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
    26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
    20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
    25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
    25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
    8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
    24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
    7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
    23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
    27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
    8,-2    27,-8   30,-5   24,-7"""


def get_part_two_test_answer(answer_txt):
    parsed = answer_txt.split()
    given_answer = []
    for p in parsed:
        x, y = p.split(',')
        x = int(x)
        y = int(y)
        given_answer.append((x, y))
    return given_answer


PART_TWO_TEST_ANSWER = get_part_two_test_answer(TEST_ANSWER_TEXT)


def test_input_parser():
    assert input_parser(TEST_INPUT) == (20, 30, -5, -10)
    assert input_parser(REAL_INPUT) == (117, 164, -89, -140)


def test_main1():
    txt = 'target area: x=20..30, y=-10..-5'
    assert main1(txt) == 45
    assert main1_1(-89, -140) == 9730


def test_find_pairs_that_work_for_initial_yvel():
    for init_yvel in range(-10, 9+1):
        given_answer = [
            loc for loc in PART_TWO_TEST_ANSWER if loc[1] == init_yvel
        ]
        my_answer = find_pairs_that_work_for_initial_yvel(20, 30, -5, -10, 6, 30, init_yvel)
        assert len(given_answer) == len(my_answer)
        assert sorted(given_answer) == sorted(my_answer)


def test_find_pairs_that_work():
    my_answer = find_pairs_that_work(*input_parser(TEST_INPUT))
    assert sorted(my_answer) == sorted(PART_TWO_TEST_ANSWER)


# @pytest.mark.skip('not working yet')
def test_main2():
    assert main2(TEST_INPUT) == 112

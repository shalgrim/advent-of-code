import pytest
from y2022.day25_1 import backconvert, convert, fuelsum, main


@pytest.fixture
def tst_input():
    with open("../../../data/2022/test25.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_convert():
    assert convert("1=-0-2") == 1747
    assert convert("10=100") == 2900


def test_fuelsum(tst_input):
    assert fuelsum(tst_input) == 4890


def test_backconvert():
    assert backconvert(0) == "0"
    assert backconvert(1) == "1"
    assert backconvert(2) == "2"
    assert backconvert(3) == "1="
    assert backconvert(4) == "1-"
    assert backconvert(5) == "10"
    assert backconvert(6) == "11"
    assert backconvert(7) == "12"
    assert backconvert(8) == "2="
    assert backconvert(9) == "2-"
    assert backconvert(10) == "20"
    assert backconvert(11) == "21"
    assert backconvert(12) == "22"
    assert backconvert(13) == "1=="
    assert backconvert(14) == "1=-"
    assert backconvert(15) == "1=0"
    # NEXT: breaks here, gives me "0=" instead
    assert backconvert(23) == "10="
    assert backconvert(2900) == "10=100"
    assert backconvert(4890) == "2=-1=0"


def test_main(tst_input):
    assert main(tst_input) == "2=-1=0"

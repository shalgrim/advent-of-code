from day17_1 import main as main1


def test_main1():
    txt = 'target area: x=20..30, y=-10..-5'
    assert main1(txt) == 45

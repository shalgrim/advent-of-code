from y2023.day15_1 import hash, main
from y2023.day15_2 import main as main2


def test_hash():
    assert hash("HASH") == 52


def test_part_1():
    assert main("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7") == 1320


def test_part_2():
    assert main2("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7") == 145

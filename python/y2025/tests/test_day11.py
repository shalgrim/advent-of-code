import pytest
from y2025.day11_1 import get_devices, main
from y2025.day11_2 import get_all_paths
from y2025.day11_2 import main as main2


@pytest.fixture
def test_file_11():
    with open("data/2025/test11.txt") as f:
        return [line.rstrip() for line in f.readlines()]


@pytest.fixture
def test_file_11_2():
    with open("data/2025/test11_2.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def test_part1(test_file_11):
    assert main(test_file_11) == 5


def test_get_all_paths(test_file_11_2):
    devices = get_devices(test_file_11_2)

    all_paths = get_all_paths(devices, "ggg")
    set_all_path_strings = {",".join(ap) for ap in all_paths}
    assert set_all_path_strings == {"ggg,out"}


#     all_paths = get_all_paths(devices, "hhh")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {"hhh,out"}
#
#     all_paths = get_all_paths(devices, "fff")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {"fff,ggg,out", "fff,hhh,out"}
#
#     all_paths = get_all_paths(devices, "hub")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {"hub,fff,ggg,out", "hub,fff,hhh,out"}
#
#     all_paths = get_all_paths(devices, "dac")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {"dac,fff,ggg,out", "dac,fff,hhh,out"}
#
#     all_paths = get_all_paths(devices, "ddd")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {"ddd,hub,fff,ggg,out", "ddd,hub,fff,hhh,out"}
#
#     all_paths = get_all_paths(devices, "eee")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {"eee,dac,fff,ggg,out", "eee,dac,fff,hhh,out"}
#
#     all_paths = get_all_paths(devices, "ccc")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {
#         "ccc,ddd,hub,fff,ggg,out",
#         "ccc,ddd,hub,fff,hhh,out",
#         "ccc,eee,dac,fff,ggg,out",
#         "ccc,eee,dac,fff,hhh,out",
#     }
#
#     all_paths = get_all_paths(devices, "svr")
#     set_all_path_strings = {",".join(ap) for ap in all_paths}
#     assert set_all_path_strings == {
#         "svr,aaa,fft,ccc,ddd,hub,fff,ggg,out",
#         "svr,aaa,fft,ccc,ddd,hub,fff,hhh,out",
#         "svr,aaa,fft,ccc,eee,dac,fff,ggg,out",
#         "svr,aaa,fft,ccc,eee,dac,fff,hhh,out",
#         "svr,bbb,tty,ccc,ddd,hub,fff,ggg,out",
#         "svr,bbb,tty,ccc,ddd,hub,fff,hhh,out",
#         "svr,bbb,tty,ccc,eee,dac,fff,ggg,out",
#         "svr,bbb,tty,ccc,eee,dac,fff,hhh,out",
#     }
#
#
def test_part2(test_file_11_2):
    assert main2(test_file_11_2) == 2

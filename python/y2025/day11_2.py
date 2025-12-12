from coding_puzzle_tools import read_input
from y2025.day11_1 import get_devices

# There's gotta be a way to build this up
# Like start with all the foo: out devices
# Then we know there is 1 route from foo to out
# So then find all the devices that go to foo
# Figure out how many routes from each of their other outputs go to out
# then we'll know how many from that device total go to out
# and you can keep building it up that way


def main(lines: list[str]) -> int:
    devices = get_devices(lines)
    paths = [[output] for output in devices["svr"]]
    while not all(path[-1] == "out" for path in paths):
        new_paths = []
        for path in paths:
            device = path[-1]
            if device != "out":
                for output in devices[device]:
                    if output in path:  # loop
                        continue
                    new_paths.append(path + [output])
        paths = new_paths
    valid_paths = [path for path in paths if "fft" in path and "dac" in path]
    return len(valid_paths)


if __name__ == "__main__":
    print(main(read_input()))

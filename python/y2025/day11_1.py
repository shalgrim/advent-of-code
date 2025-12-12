from coding_puzzle_tools import read_input


def get_devices(lines):
    answer = {}
    for line in lines:
        key = line.split(":")[0]
        outputs = line.split()[1:]
        answer[key] = outputs
    return answer


def main(lines: list[str]) -> int:
    """does not recognize loops"""
    devices = get_devices(lines)
    paths = devices["you"]
    while not all(path[-3:] == "out" for path in paths):
        new_paths = []
        for path in paths:
            device = path[-3:]
            if device == "out":
                new_paths.append(path)
            else:
                for output in devices[device]:
                    new_paths.append(path + output)
        paths = new_paths
    return len(paths)


if __name__ == "__main__":
    print(main(read_input()))

class Map:
    def __init__(self, lines):
        self.name = lines[0].split()[0]
        self.destination_range_starts = [int(line.split()[0]) for line in lines[1:]]
        self.source_range_starts = [int(line.split()[1]) for line in lines[1:]]
        self.range_lengths = [int(line.split()[2]) for line in lines[1:]]

    def convert(self, num):
        for srs, drs, rl in zip(
            self.source_range_starts, self.destination_range_starts, self.range_lengths
        ):
            if srs <= num < srs + rl:
                return drs + num - srs
        return num


def get_seeds(line):
    return [int(num) for num in line.split()[1:]]


def build_maps(lines):
    mapping_groups = []
    current_group = []
    for line in lines:
        if not line.strip():
            mapping_groups.append(current_group)
            current_group = []
        else:
            current_group.append(line)
    mapping_groups.append(current_group)

    return [Map(group) for group in mapping_groups]


def mega_convert(num, maps):
    for m in maps:
        num = m.convert(num)
    return num


def main(lines):
    seeds = get_seeds(lines[0])
    maps = build_maps(lines[2:])
    return min(mega_convert(seed, maps) for seed in seeds)


if __name__ == "__main__":
    with open("../../data/2023/input05.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

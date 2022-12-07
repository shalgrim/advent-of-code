from day07_1 import build_dirs

TOTAL_DISK_SPACE_AVAILABLE = 70_000_000
NEEDED_UNUSED_SPACE = 30_000_000


def main(lines):
    all_dirs = build_dirs(lines)
    used_space = all_dirs[0].size
    current_free_space = TOTAL_DISK_SPACE_AVAILABLE - used_space
    space_to_delete = NEEDED_UNUSED_SPACE - current_free_space
    dirs_i_could_delete = [d for d in all_dirs if d.size >= space_to_delete]
    return min(d.size for d in dirs_i_could_delete)


if __name__ == '__main__':
    with open('../../data/2022/input07.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))

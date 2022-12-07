from enum import Enum


class State(Enum):
    LISTING = 1
    AWAITING = 2


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.directories = {}

    @property
    def size(self):
        total_size = sum(self.files.values())
        for sub_dir in self.directories.values():
            total_size += sub_dir.size
        return total_size


def main(lines):
    all_dirs = build_dirs(lines)
    big_dirs = [d for d in all_dirs if d.size <= 100000]
    answer = sum(bd.size for bd in big_dirs)
    return answer


def build_dirs(lines):
    # assume line 0 is `cd /`
    root = Directory('root', None)
    all_dirs = [root]
    current_dir = root
    for i, line in enumerate(lines[1:]):
        print(i)
        if line == '$ ls':
            continue
        elif line.startswith('$ cd'):
            next_dir = line.split()[2]
            if next_dir == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.directories[next_dir]
        elif line.startswith('dir'):
            dir_name = line.split()[1]
            new_dir = Directory(dir_name, current_dir)
            all_dirs.append(new_dir)
            current_dir.directories[dir_name] = new_dir
        else:
            size, filename = line.split()
            current_dir.files[filename] = int(size)
    return all_dirs


if __name__ == '__main__':  # 1315285 is correct
    with open('../../data/2022/input07.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    print(main(lines))

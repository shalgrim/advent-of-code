def main(depths):
    old_depth = depths[0]
    increases = 0

    for depth in depths[1:]:
        if depth > old_depth:
            increases += 1
        old_depth = depth

    return increases


if __name__ == '__main__':
    with open('../data/input01.txt') as f:
        depths = [int(line) for line in f.readlines()]

    print(main(depths))

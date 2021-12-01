def main(depths):
    # this is dumb, should have just compared element 4 to 1, element 5 to 2, etc
    old_total = sum(depths[:3])
    increases = 0
    for i in range(1, len(depths)-2):
        total = sum(depths[i:i+3])
        if total > old_total:
            increases += 1
        old_total = total
    return increases


if __name__ == '__main__':
    with open('../data/input01.txt') as f:
        depths = [int(line) for line in f.readlines()]

    print(main(depths))

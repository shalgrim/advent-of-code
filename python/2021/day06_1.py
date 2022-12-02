def main(data):
    fish = [int(fish) for fish in data.split(',')]

    for _ in range(80):
        new_fish = []
        new_new_fish = []
        for f in fish:
            if f > 0:
                new_fish.append(f-1)
            else:
                new_fish.append(6)
                new_new_fish.append(8)

        new_fish += new_new_fish
        fish = new_fish

    return len(fish)


if __name__ == '__main__':
    # for some stupid pycharm reason this has a different working dir
    with open('./data/input06.txt') as f:
        data = f.read().strip()

    print(main(data))

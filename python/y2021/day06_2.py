from collections import Counter, defaultdict


def main(data):
    fish = Counter([int(fish) for fish in data.split(",")])

    days_left = 256

    while days_left > 0:
        days_left -= 1
        new_fish = defaultdict(lambda: 0)
        for k, v in fish.items():
            if k == 0:
                new_fish[6] += v
                new_fish[8] += v
            else:
                new_fish[k - 1] += v
        fish = new_fish

    return sum(fish.values())


if __name__ == "__main__":
    with open("../data/input06.txt") as f:
        data = f.read().strip()

    print(main(data))

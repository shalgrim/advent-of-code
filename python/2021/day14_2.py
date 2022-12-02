from collections import Counter, defaultdict
from copy import copy
from datetime import datetime


def process_input(lines):
    template = lines[0]
    rules = {
        line.split('->')[0].strip(): line.split('->')[1].strip() for line in lines[2:]
    }
    return template, rules


def apply_insertion(template, rules, num):
    pairs = Counter([template[i : i + 2] for i in range(len(template) - 1)])
    for j in range(num):
        print(f'{datetime.now()} {j=}')
        new_pairs = defaultdict(int)

        for pair, middle in rules.items():
            char1, char2 = pair
            new_pairs[f'{char1}{middle}'] += pairs[pair]
            new_pairs[f'{middle}{char2}'] += pairs[pair]

        pairs = new_pairs

    return pairs


def main(lines, num=40):
    template, rules = process_input(lines)
    pair_counts = apply_insertion(template, rules, num)
    character_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        for c in pair:
            character_counts[c] += count
    actual_character_counts = {k: v//2 for k, v in character_counts.items()}
    actual_character_counts[template[0]] += 1
    actual_character_counts[template[-1]] += 1
    counts = Counter(actual_character_counts)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


if __name__ == '__main__':
    with open('../data/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

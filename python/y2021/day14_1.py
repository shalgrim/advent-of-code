from collections import Counter
from copy import copy


def process_input(lines):
    template = lines[0]
    rules = {
        line.split('->')[0].strip(): line.split('->')[1].strip() for line in lines[2:]
    }
    return template, rules


def apply_insertion(template, rules, num):
    output = copy(template)
    for j in range(num):
        print(f'{j=}')
        new_output = output[0]

        for i in range(len(output)-1):
            pair = output[i:i+2]
            new_output += f'{rules[pair]}{pair[1]}'

        output = new_output
    return output


def main(lines):
    template, rules = process_input(lines)
    polymer = apply_insertion(template, rules, 10)
    counts = Counter(polymer)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


if __name__ == '__main__':
    with open('../data/input14.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

"""
 0000
1    2
1    2
 3333
4    5
4    5
 6666
"""


def get_configuration(line):
    configuration = {}
    input = line.split('|')[0].strip().split()
    output = line.split('|')[1].strip().split()

    # get some known digits
    for digit in input:
        if len(digit) == 2:
            digit_1 = digit
        elif len(digit) == 3:
            digit_7 = digit
        elif len(digit) == 4:
            digit_4 = digit
        elif len(digit) == 7:
            digit_8 = digit

    # determine position 0 by diffing digits 7 and 1
    configuration[0] = set(digit_7).difference(set(digit_1)).pop()

    # figure out 2 and 5 by figuring which is not in all of 0, 6, 9
    digits_069 = [digit for digit in input if len(digit) == 6]

    for c in set(digit_1):
        if all([c in digit for digit in digits_069]):
            configuration[5] = c

    for c in set(digit_1):
        if c != configuration[5]:
            configuration[2] = c

    # narrow down 3 and 6 by finding the size 5 char that has both (digit 3)
    for digit in input:
        if len(digit) != 5:
            continue
        if len(set(digit).intersection(digit_7)) == 3:
            digit_3 = digit
            positions_36 = set(digit_3).difference(digit_7)

    # determine 3 and 6 by figuring out which is in digit 4
    for p in positions_36:
        if p in digit_4:
            configuration[3] = p
        else:
            configuration[6] = p

    # determine 1 and 4 (only remaining ones) by seeing which is in digit 4
    positions_14 = set('abcdefg').difference(set(configuration.values()))
    for p in positions_14:
        if p in digit_4:
            configuration[1] = p
        else:
            configuration[4] = p

    return configuration


def get_output_digit(output, configuration):
    positions_to_light_up = [configuration[d] for d in output]
    position_set = set(positions_to_light_up)
    if position_set == {0, 1, 2, 4, 5, 6}:
        return 0
    elif position_set == {2, 5}:
        return 1
    elif position_set == {0, 2, 3, 4, 6}:
        return 2
    elif position_set == {0, 2, 3, 5, 6}:
        return 3
    elif position_set == {1, 2, 3, 5}:
        return 4
    elif position_set == {0, 1, 3, 5, 6}:
        return 5
    elif position_set == {0, 1, 3, 4, 5, 6}:
        return 6
    elif position_set == {0, 2, 5}:
        return 7
    elif position_set == {0, 1, 2, 3, 4, 5, 6}:
        return 8
    elif position_set == {0, 1, 2, 3, 5, 6}:
        return 9
    else:
        raise Exception('unknown {position_set=}')


def get_output_display(line):
    configuration = get_configuration(line)
    reversed_configuration = {v: k for k, v in configuration.items()}
    output = line.split('|')[1].strip().split()
    output_digits = [get_output_digit(o, reversed_configuration) for o in output]
    return int(''.join([str(od) for od in output_digits]))


def main(lines):
    return sum([get_output_display(line) for line in lines])


if __name__ == '__main__':
    with open('../data/input08.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

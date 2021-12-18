import math

from day16_1 import convert_literal, create_bin_string, get_version_and_type


def collect_subpackets(bin_string, cursor, num_subpackets):
    values = []
    for i in range(num_subpackets):
        packet_version, packet_type = get_version_and_type(bin_string, cursor)
        if packet_type == 4:
            cursor += 6
            subpacket_value, cursor = convert_literal(bin_string, cursor)
        else:
            subpacket_value, cursor = calculate(bin_string, cursor)
        values.append(subpacket_value)
    return cursor, values


def add_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = sum(values)
    return answer, cursor


def prod_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = math.prod(values)
    return answer, cursor


def minimum_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = min(values)
    return answer, cursor


def maximum_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = max(values)
    return answer, cursor


def gt_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = 1 if values[0] > values[1] else 0
    return answer, cursor


def lt_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = 1 if values[0] < values[1] else 0
    return answer, cursor


def eq_num_subpackets(bin_string, num_subpackets, cursor):
    cursor, values = collect_subpackets(bin_string, cursor, num_subpackets)
    answer = 1 if values[0] == values[1] else 0
    return answer, cursor


def collect_subpackets_by_bits(bin_string, cursor, num_bits):
    values = []
    last_bit = cursor + num_bits
    while cursor < last_bit:
        packet_version, packet_type = get_version_and_type(bin_string, cursor)
        if packet_type == 4:
            cursor += 6
            subpacket_value, cursor = convert_literal(bin_string, cursor)
        else:
            subpacket_value, cursor = calculate(bin_string, cursor)
        values.append(subpacket_value)
    return cursor, values


def add_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = sum(values)
    return answer, cursor


def prod_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = math.prod(values)
    return answer, cursor


def minimum_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = min(values)
    return answer, cursor


def maximum_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = max(values)
    return answer, cursor


def gt_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = 1 if values[0] > values[1] else 0
    return answer, cursor


def lt_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = 1 if values[0] < values[1] else 0
    return answer, cursor


def eq_num_bits(bin_string, num_bits, cursor):
    cursor, values = collect_subpackets_by_bits(bin_string, cursor, num_bits)
    answer = 1 if values[0] == values[1] else 0
    return answer, cursor


def calculate(bin_string, cursor=0):
    # while cursor < len(bin_string) and int(bin_string[cursor:], 2):
    packet_version, packet_type = get_version_and_type(bin_string, cursor)
    cursor += 6

    if packet_type == 0:  # sum
        length_type_id = bin_string[cursor]
        cursor += 1

        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = add_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = add_num_subpackets(bin_string, num_subpackets, cursor)
    elif packet_type == 1:  # product
        length_type_id = bin_string[cursor]
        cursor += 1

        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = prod_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = prod_num_subpackets(bin_string, num_subpackets, cursor)
    elif packet_type == 2:  # minimum
        length_type_id = bin_string[cursor]
        cursor += 1
        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = minimum_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = minimum_num_subpackets(bin_string, num_subpackets, cursor)
    elif packet_type == 3:  # maximum
        length_type_id = bin_string[cursor]
        cursor += 1
        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = maximum_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = maximum_num_subpackets(bin_string, num_subpackets, cursor)
    elif packet_type == 5:  # greater_than
        length_type_id = bin_string[cursor]
        cursor += 1
        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = gt_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = gt_num_subpackets(bin_string, num_subpackets, cursor)
    elif packet_type == 6:  # less_than
        length_type_id = bin_string[cursor]
        cursor += 1
        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = lt_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = lt_num_subpackets(bin_string, num_subpackets, cursor)
    elif packet_type == 7:  # equal
        length_type_id = bin_string[cursor]
        cursor += 1
        if length_type_id == '0':
            num_bits = int(bin_string[cursor : cursor + 15], 2)
            cursor += 15
            value, cursor = eq_num_bits(bin_string, num_bits, cursor)
        else:
            num_subpackets = int(bin_string[cursor : cursor + 11], 2)
            cursor += 11
            value, cursor = eq_num_subpackets(bin_string, num_subpackets, cursor)
    else:
        raise NotImplementedError(f'{packet_type=}')

    return value, cursor


def main(hex_string):
    bin_string = create_bin_string(hex_string)
    return calculate(bin_string)[0]


if __name__ == '__main__':  # 180890865630 is too low
    with open('../data/input16.txt') as f:
        number = f.read().strip()

    print(main(number))

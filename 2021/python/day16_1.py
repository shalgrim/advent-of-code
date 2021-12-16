def convert_literal(bin_string, cursor):
    new_bin_string = ''
    while bin_string[cursor] != '0':  # am I missing some weird advancement tho?
        new_bin_string += bin_string[cursor + 1 : cursor + 5]
        cursor += 5
    new_bin_string += bin_string[cursor + 1 : cursor + 5]
    cursor += 5
    return int(new_bin_string, 2), cursor


def get_version_and_type(bin_string, cursor):
    version = int(bin_string[cursor : cursor + 3], 2)
    packet_type = int(bin_string[cursor + 3 : cursor + 6], 2)
    return version, packet_type


def convert(hex_string):
    value = int(hex_string, 16)
    bin_string = bin(value)[2:]
    version = int(bin_string[:3], 2)
    packet_type = int(bin_string[3:6], 2)

    if packet_type == 4:
        return version, convert_literal(bin_string)

    # operator packet
    length_type_id = bin_string[6]
    if length_type_id == '0':
        length_length = 15
        num_bits = int(bin_string[7 : 7 + length_length], 2)
        smashed_subpackets = bin_string[7 + length_length : num_bits]
        i = 7 + length_length + num_bits
    else:  # length_type_id == '1':
        length_length = 11
        num_subpackets = int(bin_string[7 : 7 + length_length], 2)
        i = 7 + length_length
        for _ in range(num_subpackets):
            subpacket = bin_string[i : i + length_length]
            i += length_length

    return version, i


def calc_version_sum(hex_string):
    bin_string = create_bin_string(hex_string)
    cursor = 0
    version_sum = 0

    while cursor < len(bin_string) and int(bin_string[cursor:], 2):
        packet_version, packet_type = get_version_and_type(bin_string, cursor)
        cursor += 6
        version_sum += packet_version

        if packet_type == 4:
            literal_value, cursor = convert_literal(bin_string, cursor)
        else:
            length_type_id = bin_string[cursor]
            cursor += 1

            if length_type_id == '0':
                num_bits_of_contained_subpackets = int(
                    bin_string[cursor : cursor + 15], 2
                )
                cursor += 15
            else:
                num_subpackets = int(bin_string[cursor : cursor + 11], 2)
                cursor += 11

    return version_sum


def create_bin_string(hex_string):
    bin_string = bin(int(hex_string, 16))[2:]
    mod = len(bin_string) % 4

    if mod:
        bin_string = '0' * (4 - mod) + bin_string

    for c in hex_string:  # mod solution doesn't account for leading zeroes
        if c != '0':
            break
        bin_string = '0000' + bin_string

    return bin_string


if __name__ == '__main__':
    with open('../data/input16.txt') as f:
        number = f.read().strip()

    print(calc_version_sum(number))

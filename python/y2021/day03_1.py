def sort_bits_by_commonness(lines, index):
    bitlist = [line[index] for line in lines]
    num_0 = bitlist.count('0')
    num_1 = len(bitlist) - num_0
    return ('0', '1') if num_0 > num_1 else ('1', '0')


def get_rate(lines, rate_type):
    rate = ''
    for i in range(len(lines[0])):
        mcb, lcb = sort_bits_by_commonness(lines, i)
        if rate_type == 'gamma':
            rate += mcb
        else:
            rate += lcb

    return rate


def main(lines):
    gamma = get_rate(lines, 'gamma')
    epsilon = get_rate(lines, 'epsilon')
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    with open('../data/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

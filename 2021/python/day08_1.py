UNIQUE_DIGIT_LENGTHS = {1: 2, 7: 3, 4: 4, 8: 7}


def output_contains_how_many(line, num):
    output = line.split('|')[1].strip().split()
    answer = len([o for o in output if len(o) == UNIQUE_DIGIT_LENGTHS[num]])
    if num == 7:
        print(f'{answer=}')
    return answer


def main(lines):
    num_1s = sum([output_contains_how_many(line, 1) for line in lines])
    num_4s = sum([output_contains_how_many(line, 4) for line in lines])
    num_7s = sum([output_contains_how_many(line, 7) for line in lines])
    num_8s = sum([output_contains_how_many(line, 8) for line in lines])
    print(f'{num_1s=}')
    print(f'{num_4s=}')
    print(f'{num_7s=}')
    print(f'{num_8s=}')
    return num_1s + num_4s + num_7s + num_8s


if __name__ == '__main__':
    with open('../data/input08.txt') as f:
            lines = [line.strip() for line in f.readlines()]
    print(main(lines))

def main(pair_section_assignments):
    answer = 0
    for ass1, ass2 in [psa.split(',') for psa in pair_section_assignments]:
        lo1, hi1 = [int(x) for x in ass1.split('-')]
        lo2, hi2 = [int(x) for x in ass2.split('-')]

        if (
            lo2 <= lo1 <= hi2
            or lo2 <= hi1 <= hi2
            or lo1 <= lo2 <= hi1
            or lo1 <= hi2 <= hi1
        ):
            answer += 1

    return answer


if __name__ == '__main__':
    with open('../../data/2022/input04.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

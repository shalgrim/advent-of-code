from functools import cache

from aoc.io import this_year_day


@cache
def secret_number(number, times=1):
    answer = number
    for _ in range(times):
        modulo = 16777216
        # m64 = number * 64
        # answer = number ^ m64
        # answer %= modulo
        answer = ((answer * 64) ^ answer) % modulo

        # d32 = answer // 32
        # answer = answer ^ d32
        # answer %= modulo
        answer = ((answer // 32) ^ answer) % modulo

        # m2048 = answer * 2048
        # answer = answer ^ m2048
        # answer %= modulo
        answer = ((answer * 2048) ^ answer) % modulo
    return answer


def main(lines):
    answers = [secret_number(int(line), 2000) for line in lines]
    return sum(answers)


if __name__ == "__main__":
    # testing = True
    testing = False
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
    # print(secret_number(123))
    # print(secret_number(1, 2000))

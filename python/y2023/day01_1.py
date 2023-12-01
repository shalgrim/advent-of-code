def get_first_digit(line):
    for c in line:
        if c.isdigit():
            return int(c)


def get_last_digit(line):
    for c in line[::-1]:
        if c.isdigit():
            return int(c)


def calibration_value(line):
    return 10 * get_first_digit(line) + get_last_digit(line)


def main(lines):
    return sum(calibration_value(line) for line in lines)


if __name__ == "__main__":
    with open("../../data/2023/input01.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

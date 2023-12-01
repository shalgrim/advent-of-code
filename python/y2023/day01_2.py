import re

pattern = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")
converter = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def really_find_all(line):
    answer = []
    match = pattern.search(line, 0)
    while match:
        answer.append(match.group())
        match = pattern.search(line, match.start()+1)
    return answer


def get_last_number(line):
    # raw = pattern.findall(line)[-1]
    raw = really_find_all(line)[-1]
    print(raw)
    try:
        return int(raw)
    except ValueError:
        return converter[raw]


def get_first_number(line):
    raw = pattern.findall(line)[0]
    print(raw)
    try:
        return int(raw)
    except ValueError:
        return converter[raw]


def calibration_value(line):
    print(line)
    first_num = get_first_number(line)
    last_num = get_last_number(line)
    answer = 10 * first_num + last_num
    print(f"10 * {first_num} + {last_num} = {answer}")
    return answer


def main(lines):
    return sum(calibration_value(line) for line in lines)


if __name__ == "__main__":
    # 57325 is wrong?!?
    with open("../../data/2023/input01.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

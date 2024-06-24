import math

converter = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


def convert(s: str) -> int:
    answer = 0
    for power, c in enumerate(s[::-1]):
        answer += converter[c] * 5**power

    return answer


def backconvert(n: int) -> str:
    if n in [0, 1, 5]:
        num_places = 1
    else:
        num_places = math.ceil(math.log(n, 5))

    string_assembly = ""
    sub_n = n
    carryover = 0
    for _ in range(num_places):
        mod = (sub_n + carryover) % 5
        if mod == 0:
            carryover = carryover
            string_assembly += str(mod)
        elif mod < 3:
            carryover = 0
            string_assembly += str(mod)
        elif mod == 3:
            carryover = 1
            string_assembly += "="
        elif mod == 4:
            carryover = 1
            string_assembly += "-"
        else:
            raise ValueError(f"Unexpected {mod=}")
        if sub_n == 5:
            carryover = 1
            break
        sub_n = sub_n // 5
    if carryover:
        string_assembly += "1"
    answer = string_assembly[::-1]
    return answer


def fuelsum(requirements: list[str]) -> int:
    return sum(convert(r) for r in requirements)


def main(lines: list[str]) -> str:
    decimal = fuelsum(lines)
    print(decimal)
    return backconvert(decimal)


if __name__ == "__main__":
    # 2=20-=-2=111=210=100 is incorrect
    with open("../../data/2022/input25.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

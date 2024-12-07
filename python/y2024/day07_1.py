import itertools

from aoc.io import this_year_day


def create_equation(line):
    answer = int(line.split(":")[0])
    operands = [int(n) for n in line.split(":")[1].split()]
    return answer, operands


def calculate(operands, operators):
    first_operator = operators[0]
    if first_operator == "+":
        answer = operands[0] + operands[1]
    else:
        answer = operands[0] * operands[1]

    for operator, operand in zip(operators[1:], operands[2:]):
        if operator == "+":
            answer += operand
        else:
            answer *= operand

    return answer


def could_be_true(equation):
    answer, operands = equation
    num_operators = len(operands) - 1
    for combo in itertools.product(("+", "*"), repeat=num_operators):
        if answer == calculate(operands, combo):
            return True
    return False


def main(lines):
    equations = [create_equation(line) for line in lines]
    correct_answers = [equation[0] for equation in equations if could_be_true(equation)]
    return sum(correct_answers)


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

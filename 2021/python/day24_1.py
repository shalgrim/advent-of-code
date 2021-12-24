from itertools import product


def number_generator():
    digits = '987654321'
    sub_generator = product(digits, repeat=14)

    for subg in sub_generator:
        yield int(''.join(list(subg)))


def run_program(lines, number):
    input_index = 0
    registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for line in lines:
        command = line.split()[0]
        if command == 'inp':
            variable = line.split()[1]
            registers[variable] = int(str(number)[input_index])
            input_index += 1
        elif command in ['add', 'mul', 'div', 'mod']:
            var1, var2 = line.split()[1:]
            val1 = registers[var1]
            val2 = registers[var2] if var2 in registers else int(var2)

            if command == 'add':
                output = val1 + val2
            elif command == 'mul':
                output = val1 * val2
            elif command == 'div':
                if val2 == 0:
                    raise ZeroDivisionError
                output = val1 // val2
            elif command == 'mod':
                if val1 < 0 or val2 <= 0:
                    raise ZeroDivisionError('Invalid mod operation')
                output = val1 % val2
            else:
                raise Exception(f'Unexpected {command=}')

            registers[var1] = output

    return registers['z']


def main(lines):
    for number in number_generator():
        try:
            program_output = run_program(lines, number)
        except ZeroDivisionError:
            continue
        else:
            if number % 9999 == 0:
                print(f'{number=}: {program_output=}')
            if run_program(lines, number) == 0:
                return number
    return -1


if __name__ == '__main__':
    with open('../data/input24.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

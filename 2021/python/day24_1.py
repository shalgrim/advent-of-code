from itertools import product


def number_generator(start_from=0):
    starting_number = start_from if start_from else 99_999_999_999_999
    for num in range(starting_number, 0, -1):
        yield num


def run_program(lines, number, bad_starts):
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
                    bad_starts.add(str(number)[:input_index])
                    raise ZeroDivisionError
                output = val1 // val2
            elif command == 'mod':
                if val1 < 0 or val2 <= 0:
                    bad_starts.add(str(number)[:input_index])
                    raise ZeroDivisionError('Invalid mod operation')
                output = val1 % val2
            else:
                raise Exception(f'Unexpected {command=}')

            registers[var1] = output

    return registers['z']


def has_bad_start(number, bad_starts):
    string_number = str(number)
    return any(string_number.startswith(start) for start in bad_starts)


def main(lines, start_from=0):
    bad_starts = set()
    for number in number_generator(start_from=start_from):
        if has_bad_start(number, bad_starts):
            continue
        try:
            program_output = run_program(lines, number, bad_starts)
        except ZeroDivisionError:
            continue
        else:
            if number % 9999 == 0:
                print(f'{number=}: {program_output=}')
            if program_output == 0:
                return number
    return -1


if __name__ == '__main__':
    with open('../data/input24.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines, start_from=99999837226179))

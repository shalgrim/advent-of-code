from aoc.io import this_year_day
from y2024.day17_1 import run_program


def helper(program, currently_working_with, successfully_found):
    for number_to_try in range(currently_working_with, currently_working_with + 8):
        program_output = [
            int(v) for v in run_program(program, number_to_try, 0, 0).split(",")
        ]
        if program_output == program[-(successfully_found + 1) :]:
            if program_output == program:
                return number_to_try
            elif answer := helper(program, number_to_try * 8, successfully_found + 1):
                return answer
            continue  # try the next one
    # If I went through those 8 and didn't find an answer need to go back and ask for the next one in my caller's list
    return None


def find_smallest_a_that_self_replicates_program(program):
    return helper(program, 0, 0)


def main(lines):
    program = [int(code) for code in lines[4].split()[-1].split(",")]
    answer = find_smallest_a_that_self_replicates_program(program)
    return answer


if __name__ == "__main__":
    testing = False
    # testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    filename = "test17_2.txt" if testing else "input17.txt"
    with open(f"../../data/{year}/{filename}") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

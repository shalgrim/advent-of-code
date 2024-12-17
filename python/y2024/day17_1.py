from typing import List

from aoc.io import this_year_day


def combo_translator(operand, registers):
    if operand < 4:
        return operand
    if operand == 4:
        return registers["a"]
    if operand == 5:
        return registers["b"]
    if operand == 6:
        return registers["c"]


# So what does my input program do
# Program: 2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0
# Loops until register A = 0
# 2, 4 - RegB <- RegA % 8
# 1, 1 - RegB <- RegB ^ 1  # flips least significant bit; 0 becomes 1 and vice-versa; 2 becomes 3 and vice-versa; ...
# 7, 5 - RegC <- RegA // 2^RegB  # ...?... this one is weird because C could be quite large and then it gets bitwise xor'd and then B gets quite large...
# 1, 5 - RegB <- RegB ^ 5  # flips most significant bit; basically adds four then takes modulo 8 (but what if B is already bigger than 8 then it gets weird, either adding or subtracting four...)
# 4, 3 - RegB <- RegB ^ RegC # ...?...
# 5, 5 - Output RegB % 8
# 0, 3 - RegA <- RegA // 8
# 3, 0 - (the loop part)

# Note that everything in a loop depends on what A is set to at the start
# And clearly Reg A is getting divided by 8 after each round
# So figure out what is the smallest number less than 8 that produces 0 as the final digit
# and then go backwards from there ... can I just keep multiplying by 8 or does it get more complicated?

# Ah, I see how to do this...
# I try setting register A to 0 and running the program...do that until I get 0 (it's 4)
# Then I multiply that by 8 (I get 32) and try the program on 32-39 until I get 3, 0 (it's 37)
# Then I multiply that by 8 ...


def run_program(program: List[int], a: int, b: int, c: int) -> str:
    registers = {"a": a, "b": b, "c": c}
    ip = 0
    output = []
    while ip < len(program) - 1:
        opcode, operand = program[ip : ip + 2]
        match opcode:
            case 0:  # adv, division
                registers["a"] //= 2 ** combo_translator(operand, registers)
            case 1:  # bxl, bitwise xor
                registers["b"] ^= operand
            case 2:  # bst, modulo 8
                registers["b"] = combo_translator(operand, registers) % 8
            case 3:  # jnz, jump if a != 0
                ip = ip + 2 if registers["a"] == 0 else operand
            case 4:  # bxc bitwise xor
                registers["b"] ^= registers["c"]
            case 5:  # out
                output.append(combo_translator(operand, registers) % 8)
            case 6:  # bdv, division
                registers["b"] = registers["a"] // 2 ** combo_translator(
                    operand, registers
                )
            case 7:  # cdv, division
                registers["c"] = registers["a"] // 2 ** combo_translator(
                    operand, registers
                )
        ip = ip + 2 if opcode != 3 else ip
    return ",".join([str(o) for o in output])


def main(lines):
    a = int(lines[0].split()[-1])
    b = int(lines[1].split()[-1])
    c = int(lines[2].split()[-1])
    program = [int(code) for code in lines[4].split()[-1].split(",")]
    answer = run_program(program, a, b, c)
    return answer


if __name__ == "__main__":
    # testing = False
    testing = True
    filetype = "test" if testing else "input"
    year, day = this_year_day(pad_day=True)
    with open(f"../../data/{year}/{filetype}{day}.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

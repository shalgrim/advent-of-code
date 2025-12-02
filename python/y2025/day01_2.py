from coding_puzzle_tools import read_input

def main(lines):
    pointer = 50
    answer = 0
    for line in lines:
        direction = line[0]
        amount_to_move = int(line[1:][-2:])
        number_of_full_cycle_str = line[1:][:-2] or "0"
        number_of_full_cycles = int(number_of_full_cycle_str)
        if direction == "R":
            if pointer + amount_to_move >= 100:
                answer += 1
            pointer = (pointer + amount_to_move) % 100
        else:
            if pointer > 0 and pointer - amount_to_move <= 0:
                answer += 1

            pointer -= amount_to_move
            if pointer < 0:
                pointer += 100

        answer += number_of_full_cycles

    return answer

if __name__ == '__main__':
    print(main(read_input()))

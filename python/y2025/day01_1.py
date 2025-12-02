from coding_puzzle_tools import read_input

def main(lines):
    pointer = 50
    answer = 0
    for line in lines:
        direction = line[0]
        amount_to_move = int(line[1:][-2:])
        if direction == "R":
            pointer = (pointer + amount_to_move) % 100
        else:
            pointer -= amount_to_move
            if pointer < 0:
                pointer += 100

        if pointer == 0:
            answer += 1
    return answer

if __name__ == '__main__':
    print(main(read_input()))

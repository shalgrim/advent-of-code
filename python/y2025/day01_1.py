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
    # TODO: Fix so it works with files that start with "day" as well as just "d"
    # print(main(read_input()))
    with open("../../data/2025/input01.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

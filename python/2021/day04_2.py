from day04_1 import build_boards


def main(lines):
    numbers_to_draw = [int(number) for number in lines[0].split(',')]
    boards = build_boards(lines[2:])

    for number in numbers_to_draw:
        for board in boards:
            board.mark_number(number)

        if len(boards) == 1 and boards[0].winner:
            return board.score(number)

        boards = [board for board in boards if not board.winner]


if __name__ == '__main__':
    with open('../data/input04.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

class Board():
    WINNERS = [
        set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
        set([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]),
        set([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]),
        set([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]),
        set([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]),
        set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
        set([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]),
        set([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]),
        set([(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)]),
        set([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]),
        set([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]),
        set([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]),
    ]

    def __init__(self, lines):
        self.numbers = {}
        self.marked = set()
        for y, line in enumerate(lines):
            for x, number in enumerate([int(number) for number in line.split()]):
                self.numbers[number] = (x, y)

    def mark_number(self, number):
        if number in self.numbers:
            self.marked.add(self.numbers[number])
            return True
        return False

    @property
    def winner(self):
        return any([len(winner.intersection(self.marked)) >= 5 for winner in Board.WINNERS])

    def score(self, last_number_called):
        uncalled_numbers = []
        for number, location in self.numbers.items():
            if location not in self.marked:
                uncalled_numbers.append(number)

        return sum(uncalled_numbers) * last_number_called


def build_boards(lines):
    boards = []
    i = 0
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue
        boards.append(Board(lines[i:i+5]))
        i += 5
    return boards


def main(lines):
    numbers_to_draw = [int(number) for number in lines[0].split(',')]
    boards = build_boards(lines[2:])

    for number in numbers_to_draw:
        for board in boards:
            board.mark_number(number)
            if board.winner:
                return board.score(number)


if __name__ == '__main__':
    with open('../data/input04.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

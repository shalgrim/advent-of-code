OPENERS = '([{<'
CLOSERS = ')]}>'
RELATED = {')': '(', ']': '[', '}': '{', '>': '<'}
VALUES = {')': 3, ']': 57, '}': 1197, '>': 25137}


def score_of_first_syntax_error_in_line_if_corrupted(line):
    stack = []
    for c in line:
        if c in OPENERS:
            stack.append(c)
        elif stack.pop() != RELATED[c]:
            return VALUES[c]

    return 0


def main(lines):
    return sum(
        [score_of_first_syntax_error_in_line_if_corrupted(line) for line in lines]
    )


if __name__ == '__main__':
    with open('../data/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

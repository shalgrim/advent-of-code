from day10_1 import OPENERS, score_of_first_syntax_error_in_line_if_corrupted

RELATED = {'(': ')', '[': ']', '{': '}', '<': '>'}
VALUES = {')': 1, ']': 2, '}': 3, '>': 4}


def complete_line(line):
    stack = []
    for c in line:
        if c in OPENERS:
            stack.append(c)
        else:
            stack.pop()

    completion = ''
    for c in stack[::-1]:
        completion += RELATED[c]

    return completion


def score_completion(completion):
    score = 0
    for c in completion:
        score *= 5
        score += VALUES[c]

    return score


def main(lines):
    incomplete_lines = [
        line
        for line in lines
        if not score_of_first_syntax_error_in_line_if_corrupted(line)
    ]
    completions = [complete_line(line) for line in incomplete_lines]
    scores = [score_completion(completion) for completion in completions]
    sorted_scores = sorted(scores)
    return sorted_scores[len(sorted_scores) // 2]


if __name__ == '__main__':
    with open('../data/input10.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

import sys

SHAPE_SCORES = {'X': 1, 'Y': 2, 'Z': 3}


def score_round(opponent, me):
    outcome = None
    if opponent == 'A':  # rock
        if me == 'X':  # rock
            outcome = 3
        elif me == 'Y':  # paper
            outcome = 6
        else:  # Z == scissors
            outcome = 0
    elif opponent == 'B':  # paper
        if me == 'X':  # rock
            outcome = 0
        elif me == 'Y':  # paper
            outcome = 3
        else:  # Z == scissors
            outcome = 6
    else:  # C == scissors
        if me == 'X':  # rock
            outcome = 6
        elif me == 'Y':  # paper
            outcome = 0
        else:  # Z == scissors
            outcome = 3

    return outcome + SHAPE_SCORES[me]


def main(strategy_guide):
    round_scores = [score_round(*round) for round in strategy_guide]
    return sum(round_scores)


if __name__ == '__main__':
    infn = '../data/input02.txt'
    with open(infn) as f:
        strategy_guide = [line.split() for line in f.readlines()]
    print(main(strategy_guide))

SHAPE_SCORES = {'rock': 1, 'paper': 2, 'scissors': 3}
OUTCOME_SCORES = {'X': 0, 'Y': 3, 'Z': 6}


def score_round(opponent, outcome):
    shape = ''
    if opponent == 'A':  # rock
        if outcome == 'X':  # lose
            shape = 'scissors'
        elif outcome == 'Y':  # draw
            shape = 'rock'
        else:  # Z == win
            shape = 'paper'
    elif opponent == 'B':  # paper
        if outcome == 'X':  # lose
            shape = 'rock'
        elif outcome == 'Y':  # draw
            shape = 'paper'
        else:  # Z == win
            shape = 'scissors'
    else:  # C == scissors
        if outcome == 'X':  # lose
            shape = 'paper'
        elif outcome == 'Y':  # draw
            shape = 'scissors'
        else:  # Z == win
            shape = 'rock'

    return OUTCOME_SCORES[outcome] + SHAPE_SCORES[shape]


def main(strategy_guide):
    round_scores = [score_round(*round) for round in strategy_guide]
    return sum(round_scores)


if __name__ == '__main__':
    infn = '../data/input02.txt'
    with open(infn) as f:
        strategy_guide = [line.split() for line in f.readlines()]
    print(main(strategy_guide))

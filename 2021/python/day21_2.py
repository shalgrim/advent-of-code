"""
The counting might be reasonable if you consider that on each player's turn they'll roll a total of:
3 - once
4 - thrice
5 - six times
6 - seven times
7 - six times
8 - thrice
9 - once

So you can make copies of universes with counts and go from there

You will probably also need to consolidate based on scores and positions after each player's turn or after each round
However, since we're only going to a total of 21, just managing the above might be enough
"""

from collections import Counter
from collections import defaultdict


def get_new_position(current_position, roll):
    new_position = (current_position + roll) % 10
    return new_position


def generate_game_key(game_key, roll):
    p1_score, p2_score, p1_position, p2_position, next_player = game_key
    if next_player == 0:
        p1_position = get_new_position(p1_position, roll)
        p1_score += p1_position + 1
    else:
        p2_position = get_new_position(p2_position, roll)
        p2_score += p2_position + 1

    next_player = (next_player + 1) % 2

    return p1_score, p2_score, p1_position, p2_position, next_player


def generate_roll(game_key):
    game_key_3 = generate_game_key(game_key, 3)
    game_key_4 = generate_game_key(game_key, 4)
    game_key_5 = generate_game_key(game_key, 5)
    game_key_6 = generate_game_key(game_key, 6)
    game_key_7 = generate_game_key(game_key, 7)
    game_key_8 = generate_game_key(game_key, 8)
    game_key_9 = generate_game_key(game_key, 9)

    # Counter would be perfect here if I had the docs
    # upon further reflection it's probably unnecessary since incoming game key is always the same
    answer = defaultdict(int)
    answer[game_key_3] += 1
    answer[game_key_4] += 3
    answer[game_key_5] += 6
    answer[game_key_6] += 7
    answer[game_key_7] += 6
    answer[game_key_8] += 3
    answer[game_key_9] += 1

    return answer


def main(p1_start, p2_start):
    # represent a game as (p1_score, p2_score, p1_position, p2_position, next_player)
    games = defaultdict(int)
    games[(0, 0, p1_start-1, p2_start-1, 0)] = 1

    while any([key[0] < 21 and key[1] < 21 for key in games.keys()]):
        print(f'{len(games)=}')
        new_games = defaultdict(int)
        for game_key, game_count in games.items():
            if game_key[0] >= 21 or game_key[1] >= 21:
                # this game is over, somebody has won
                new_games[game_key] += game_count
            for new_game_key, new_game_count in generate_roll(game_key).items():
                new_games[new_game_key] += game_count * new_game_count

        games = new_games

    p1_wins = sum([v for k, v in games.items() if k[0] > k[1]])
    p2_wins = sum([v for k, v in games.items() if k[0] < k[1]])

    return p1_wins, p2_wins


if __name__ == '__main__':
    # 4, 8 is test input:
    #   p1 wins 444_356_092_776_315 times
    #   p2 wins 341_960_390_180_808 times
    # but I got much higher numbers:
    # (1737835340729268534253101094, 617915082342836639405918710)
    # 10, 8 is my actual input
    print(main(4, 8))

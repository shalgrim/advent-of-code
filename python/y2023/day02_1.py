def process_input(lines):
    answer = {}
    for line in lines:
        game_part, rest = line.split(":")
        game_num = int(game_part.split()[1].strip())
        answer[game_num] = []
        for round in rest.split(";"):
            colors = round.split(",")
            this_round = {}
            for color in colors:
                num, this_color = color.split()
                this_round[this_color.strip()] = int(num.strip())
            answer[game_num].append(this_round)

    return answer


def get_nums_possible_with(games, given):
    answer = []
    for game_num, draws in games.items():
        game_possible = True
        for draw in draws:
            if not game_possible:
                break
            for color in ["red", "green", "blue"]:
                if draw.get(color, 0) > given[color]:
                    game_possible = False
                    break
        if game_possible:
            answer.append(game_num)
    return answer


def main(lines):
    games = process_input(lines)
    nums = get_nums_possible_with(games, {"red": 12, "green": 13, "blue": 14})
    return sum(nums)


if __name__ == "__main__":
    with open("../../data/2023/input02.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))

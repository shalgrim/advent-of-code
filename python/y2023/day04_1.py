def create_cards(lines):
    answer = {}
    for line in lines:
        card_num, data = line.split(":")
        card_num = int(card_num.split()[1])
        winning_numbers, my_numbers = data.split("|")
        winning_numbers = {int(num) for num in winning_numbers.split()}
        my_numbers = {int(num) for num in my_numbers.split()}
        answer[card_num] = (winning_numbers, my_numbers)
    return answer


def get_card_value(winning_numbers, my_numbers):
    num_matches = len(winning_numbers.intersection(my_numbers))
    if not num_matches:
        return 0
    return 2 ** (num_matches - 1)


def main(lines):
    cards = create_cards(lines)
    return sum(get_card_value(*card) for card in cards.values())


if __name__ == "__main__":
    with open("../../data/2023/input04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

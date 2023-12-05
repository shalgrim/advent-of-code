from collections import Counter

from y2023.day04_1 import create_cards


def main(lines):
    original_cards = create_cards(lines)
    counts_of_cards = Counter()

    for card_num, card in original_cards.items():
        counts_of_cards[card_num] += 1
        amount_of_this_card = counts_of_cards[card_num]
        num_matches = len(card[0].intersection(card[1]))
        for won_card_num in range(card_num + 1, card_num + 1 + num_matches):
            counts_of_cards[won_card_num] += amount_of_this_card

    return counts_of_cards.total()


if __name__ == "__main__":
    with open("../../data/2023/input04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

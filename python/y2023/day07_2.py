from collections import Counter

from y2023.day07_1 import Hand


def card_less_than_joker(card1: str, card2: str):
    if card1 == "J" and card2 == "J":
        return False
    if card1 == "J":
        return True
    if card2 == "J":
        return False
    if card1.isdigit() and card2.isdigit():
        return int(card1) < int(card2)
    if card1.isdigit():
        return True
    if card2.isdigit():
        return False
    if card1 == "A":
        return False
    if card1 == "K":
        return card2 == "A"
    if card1 == "Q":
        return card2 in ("A", "K")
    if card1 == "T":
        return card2 in ("A", "K", "Q")
    raise ValueError(f"Invalid cards: {card1=} {card2=}")


class JokerHand(Hand):
    STRENGTH = {
        "high_card": 0,
        "pair": 1,
        "two_pair": 2,
        "three_of_a_kind": 3,
        # "straight": 4,
        # "flush": 5,
        "full_house": 6,
        "four_of_a_kind": 7,
        "five_of_a_kind": 8,
    }

    def calc_strength(self):
        counter = Counter(self.cards)
        if len(counter) == 1:
            return self.STRENGTH["five_of_a_kind"]
        elif len(counter) == 2:
            if "J" in counter:
                return self.STRENGTH["five_of_a_kind"]
            if 4 in counter.values():
                return self.STRENGTH["four_of_a_kind"]
            return self.STRENGTH["full_house"]
        elif len(counter) == 3:
            if "J" in counter:
                if counter["J"] in (3, 2):
                    return self.STRENGTH["four_of_a_kind"]
                if 3 in counter.values():
                    return self.STRENGTH["four_of_a_kind"]
                return self.STRENGTH["full_house"]
            if 3 in counter.values():
                return self.STRENGTH["three_of_a_kind"]
            return self.STRENGTH["two_pair"]
        elif len(counter) == 4:
            if "J" in counter:
                if counter["J"] == 2:
                    return self.STRENGTH["three_of_a_kind"]
                if 2 in counter.values():
                    return self.STRENGTH["three_of_a_kind"]
                return self.STRENGTH["two_pair"]
            return self.STRENGTH["pair"]
        elif "J" in counter:
            return self.STRENGTH["pair"]
        return self.STRENGTH["high_card"]

    def __lt__(self, other):
        if self.strength == other.strength:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card == other_card:
                    continue
                return card_less_than_joker(self_card, other_card)
            raise ValueError(f"Invalid cards: {self.cards=} {other.cards=}")
        return self.strength < other.strength


def main(lines):
    hands = [JokerHand(line.split()[0], int(line.split()[1])) for line in lines]
    sorted_hands = sorted(hands)
    return sum(i * hand.bid for i, hand in enumerate(sorted_hands, start=1))


if __name__ == "__main__":
    with open("../../data/2023/input07.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))

import typing
from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from functools import reduce

from utils import print_and_time_result, get_input


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    @classmethod
    def map_to_type(cls, cards: str, with_joker: bool = False):
        card_count_map = {
            1: HandType.HIGH_CARD,
            2: HandType.ONE_PAIR,
            3: HandType.THREE_OF_A_KIND,
            4: HandType.FOUR_OF_A_KIND,
            5: HandType.FIVE_OF_A_KIND,
        }
        c = Counter(cards) if not with_joker else cls.count_cards_with_joker(cards)
        if not c:
            return HandType.FIVE_OF_A_KIND
        _, highest_amount = c.most_common(1).pop()
        card_amounts = sorted(c.values())
        if highest_amount == 3 and card_amounts == [2, 3]:
            return HandType.FULL_HOUSE
        elif highest_amount == 2 and card_amounts == [1, 2, 2]:
            return HandType.TWO_PAIR
        else:
            return card_count_map[highest_amount]

    @classmethod
    def count_cards_with_joker(cls, cards) -> Counter or None:
        cards_without_joker = cards.replace("J", "")
        joker_count = cards.count("J")
        if not cards_without_joker:
            return
        c = Counter(cards_without_joker)
        card_symbol, _ = c.most_common(1).pop()
        c[card_symbol] += joker_count
        return c


@dataclass(init=False)
class Hand:
    cards: str
    bid: int
    hand_type: HandType
    card_value_map: typing.ClassVar[dict[str, int]] = None

    def __init__(self, cards: str, bid: str, with_joker: bool = False):
        self.cards = cards
        self.bid = int(bid)
        self.hand_type = HandType.map_to_type(self.cards, with_joker)

    @classmethod
    def set_card_value_map(cls, card_value_map: dict[str, int]):
        cls.card_value_map = card_value_map

    def __lt__(self, other):
        if self.hand_type is not other.hand_type:
            return self.hand_type < other.hand_type
        else:
            for i in range(len(self.cards)):
                if (
                    Hand.card_value_map[self.cards[i]]
                    == Hand.card_value_map[other.cards[i]]
                ):
                    continue
                return (
                    Hand.card_value_map[self.cards[i]]
                    < Hand.card_value_map[other.cards[i]]
                )


def parse_input1(raw_input: str):
    return [Hand(*line.strip().split()) for line in raw_input]


def parse_input2(raw_input: str):
    return [Hand(*line.strip().split(), with_joker=True) for line in raw_input]


@print_and_time_result(part_num=1, day_num=7)
def part1():
    Hand.set_card_value_map({symbol: num for num, symbol in enumerate("23456789TJQKA")})
    hands = get_input(7, parse_input1, test=False)
    return reduce(
        lambda acc, tup: acc + (tup[1].bid * tup[0]),
        enumerate(sorted(hands), 1),
        0,
    )


@print_and_time_result(part_num=2, day_num=7)
def part2():
    Hand.set_card_value_map({symbol: num for num, symbol in enumerate("J23456789TQKA")})
    hands = get_input(7, parse_input2, test=False)
    return reduce(
        lambda acc, tup: acc + (tup[1].bid * tup[0]),
        enumerate(sorted(hands), 1),
        0,
    )


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

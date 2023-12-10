import dataclasses
import re
from dataclasses import dataclass
from pprint import pprint

from utils import print_result, get_input


@dataclass
class Card:
    index_number: int
    winning_set: set
    numbers_set: set
    amount: int

    @property
    def get_won_amount(self):
        return len(self.winning_set & self.numbers_set)


def parse_input(raw_input: list[str]):
    re_pattern = re.compile(r"\s(\d+): ([\d\s]+) \| ([\d ]+)")
    card_lines = [
        re_pattern.findall(line).pop()
        for line in raw_input
    ]
    cards = {
        int(card_num): Card(
            index_number=int(card_num),
            winning_set=set(winning.split()),
            numbers_set=set(numbers_got.split()),
            amount=1
        )
        for card_num, winning, numbers_got in card_lines
    }
    return cards


@print_result(part_num=1, day_num=4)
def part1():
    cards: dict[int, Card] = get_input(4, parse_input, test=False, part_num=1)
    sum_points = 0
    for card in cards.values():
        exponent = card.get_won_amount
        points = 2 ** (exponent - 1) if exponent > 0 else 0
        sum_points += points

    return sum_points


@print_result(part_num=2, day_num=4)
def part2():
    cards: dict[int, Card] = get_input(4, parse_input, test=False, part_num=1)
    sum_cards_won = 0
    for num, card in cards.items():
        cards_won = card.get_won_amount
        for i in range(num + 1, num + cards_won + 1):
            cards[i].amount += card.amount
        sum_cards_won += card.amount

    return sum_cards_won


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

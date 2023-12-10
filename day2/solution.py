import re
from functools import reduce
from operator import mul

from utils import get_input, print_result
from collections import defaultdict

CUBES_LIMIT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

RED = 'red'
BLUE = 'blue'
GREEN = 'green'
COLORS = [RED, BLUE, GREEN]


def parse_games_part1(raw_inpt: str):
    """
    {
        1: [ {red: 2, blue: 2}, {red: 1, green: 1} ],
        2: [ {red: 2, blue: 2}, {red: 1, green: 1} ],
        3: [ {red: 2, blue: 2} ],
    }

    :param raw_inpt:
    :return:
    """
    games = dict()
    c = re.compile(r"\s(\d+):\s(.*)")
    for line in raw_inpt:
        game_num, cube_sets = c.search(line).groups()
        game_num = int(game_num)
        games[game_num] = []
        cube_sets = cube_sets.split("; ")
        for _set in cube_sets:
            throws = defaultdict(int)
            _throws = _set.split(", ")
            for throw in _throws:
                cube_num, cube_color = throw.split(" ")
                throws[cube_color] += int(cube_num)
            games[game_num].append(throws)

    return games


def parse_games_part2(raw_inpt: str):
    """
    [
        {red: 2, blue: 7, green: 8},
        {red: 23, blue: 52, green: 12},
        {red: 12, blue: 21, green: 28},
    ]
    """

    def get_cube_num_and_color(cube_string: str):
        cube = cube_string.split(" ")
        return int(cube[0]), cube[1]

    games = []
    for line in raw_inpt:
        game_throws: dict = defaultdict(int)
        _, cube_sets = line.strip().split(": ")
        for _set in cube_sets.split("; "):
            for throw in _set.split(", "):
                cube_num, cube_color = get_cube_num_and_color(throw)
                if game_throws[cube_color] < cube_num:
                    game_throws[cube_color] = cube_num
        games.append(game_throws)
    return games


@print_result(part_num=1, day_num=2)
def part1():
    games: dict = get_input(input_parser=parse_games_part1, day_num=2, part_num=1)
    games_possible = []
    for game_num, sets in games.items():
        game_possible = True
        for cube_set in sets:
            for color, cube_num in cube_set.items():
                if cube_num > CUBES_LIMIT[color]:
                    game_possible = False
                    break
            if not game_possible:
                break
        if game_possible:
            games_possible.append(game_num)

    return sum(games_possible)


@print_result(part_num=2, day_num=2)
def part2():
    games: dict = get_input(input_parser=parse_games_part2, day_num=2, part_num=1)
    return sum([reduce(mul, min_cubes.values()) for min_cubes in games])


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

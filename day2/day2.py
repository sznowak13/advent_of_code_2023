import re

from utils import get_input, print_result
from collections import defaultdict

CUBES_LIMIT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_games(line: str):
    """
    {
        1: [ {red: 2, blue: 2}, {red: 1, green: 1} ],
        2: [ {red: 2, blue: 2}, {red: 1, green: 1} ],
        3: [ {red: 2, blue: 2} ],
    }

    :param line:
    :return:
    """
    games = []
    c = re.compile(r".*(\d): (.*)")
    game_num, cube_sets = c.search(line).groups()
    cube_sets = cube_sets.split("; ")
    for _set in cube_sets:
        throws = defaultdict(int)
        _throws = _set.split(", ")
        for throw in _throws:
            cube_num, cube_color = throw.split(" ")
            throws[cube_color] += int(cube_num)
        games[game_num].append(throws)

    return games


@print_result(part_num=1)
def part1():
    games = get_input(parse_games, day_num=2, test=True, part_num=1)
    for game in games.items():
        pass


@print_result(part_num=2)
def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

import re
from operator import mul

from utils import get_input, print_and_time_result


def parse_input(raw_inpt: str):
    return [line.strip() for line in raw_inpt]


NON_SPECIAL_SYMBOLS = [*list(map(str, range(10))), "."]


class GridMember:
    def __init__(self, x: int, y: int, repr_str: str):
        self.x = x
        self.y = y
        self.repr_str = repr_str
        self.neighbours: list[GridMember] = []

    def __repr__(self):
        return f"Member: {self.repr_str} at [{self.x}, {self.y}]"

    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)


class GridNumber(GridMember):
    def __init__(self, x: int, y: int, repr_str: str):
        super().__init__(x, y, repr_str)
        self.value = int(repr_str)
        self.neighbours = []

    @property
    def char_len(self) -> int:
        return len(self.repr_str)

    def is_part_number(self):
        return bool(
            [
                neighbour
                for neighbour in self.neighbours
                if isinstance(neighbour, GridSymbol)
            ]
        )


class GridSymbol(GridMember):
    def __init__(self, x: int, y: int, repr_str: str):
        super().__init__(x, y, repr_str)

    def is_gear(self):
        return (
            len(
                [
                    neighbour
                    for neighbour in self.neighbours
                    if isinstance(neighbour, GridNumber)
                ]
            )
            == 2
        )

    def get_gear_ratio(self):
        return mul(
            *[
                neighbour.value
                for neighbour in self.neighbours
                if isinstance(neighbour, GridNumber)
            ]
        )


class Grid(list):
    def __init__(self, grid_list: list[str]):
        super().__init__(grid_list)
        self.members = []
        self.grid_model = None

    @property
    def width(self):
        return len(self[0])

    @property
    def numbers(self):
        return [member for member in self.members if isinstance(member, GridNumber)]

    @property
    def symbols(self):
        return [member for member in self.members if isinstance(member, GridSymbol)]

    @property
    def height(self):
        return len(self)

    def model_grid(self):
        self.grid_model = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]
        number_regex = re.compile(r"(\d+)")
        symbol_regex = re.compile(r"([^0-9.])")

        for y, row in enumerate(self):
            for digit_match in number_regex.finditer(row):
                number = GridNumber(x=digit_match.start(), y=y, repr_str=digit_match[0])
                self.members.append(number)
                for x in range(digit_match.start(), digit_match.end()):
                    self.grid_model[y][x] = number
            for symbol_match in symbol_regex.finditer(row):
                symbol = GridSymbol(
                    x=symbol_match.start(), y=y, repr_str=symbol_match[0]
                )
                self.members.append(symbol)
                self.grid_model[y][symbol_match.start()] = symbol

        for member in self.members:
            self.identify_neighbours(member)
            # print(member, member.neighbours)
        # pprint(self.grid_model)

    def get_part_numbers(self):
        return [number for number in self.numbers if number.is_part_number()]

    def get_gears(self):
        return [symbol for symbol in self.symbols if symbol.is_gear()]

    def identify_neighbours(self, member: GridMember):
        for y_offset in range(-1, 2):
            neighbour_y = member.y + y_offset
            if not 0 <= neighbour_y < self.height:
                continue
            for x_offset in range(-1, 2):
                neighbour_x = member.x + x_offset
                if not 0 <= neighbour_x < self.width:
                    continue
                neighbour = self.grid_model[neighbour_y][neighbour_x]
                if neighbour and neighbour != member:
                    member.add_neighbour(neighbour)
                    neighbour.add_neighbour(member)


@print_and_time_result(part_num=1, day_num=3)
def part1():
    grid: Grid = Grid(
        get_input(input_parser=parse_input, day_num=3, test=False, part_num=1)
    )
    grid.model_grid()

    part_numbers = grid.get_part_numbers()
    return sum([part_num.value for part_num in part_numbers])


@print_and_time_result(part_num=2, day_num=3)
def part2():
    grid: Grid = Grid(
        get_input(input_parser=parse_input, day_num=3, test=False, part_num=1)
    )
    grid.model_grid()
    gears = grid.get_gears()
    return sum([gear.get_gear_ratio() for gear in gears])


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

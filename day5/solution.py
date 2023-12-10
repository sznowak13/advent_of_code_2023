import re
from dataclasses import dataclass

from utils import print_result, get_input

MAP_NAMES = (
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
)


@dataclass
class Range:
    destination_start: int
    source_start: int
    range_length: int

    @property
    def source_end(self):
        return self.source_start + self.range_length

    def __contains__(self, item: int):
        return self.source_start <= item <= self.source_end


@dataclass
class RangeMap:
    name: str
    ranges: list[Range]

    def map_to_destination_number(self, source_number: int):
        try:
            _range: Range = self._get_range_for(source_number)
            destination_number = (source_number - _range.source_start) + _range.destination_start
            return destination_number
        except ValueError:
            return source_number

    def _get_range_for(self, number: int):
        for _range in self.ranges:
            if number in _range:
                return _range

        raise ValueError("No corresponding range found")


def parse_input(raw_input: str) -> tuple[list[int], dict[str, RangeMap]]:
    seed_pattern = re.compile(r"seeds: ([\d ]+)")
    map_patterns: dict[str, re.Pattern] = {name: re.compile(fr"{name} map:(\n[\d\s]+)+") for name in MAP_NAMES}
    maps = {}
    seed_numbers = list(map(int, seed_pattern.findall(raw_input).pop().split(' ')))
    for name, pattern in map_patterns.items():
        ranges = [list(map(int, range_str.split(' '))) for range_str in
                  # f*u if you think its ugly i dun care
                  pattern.findall(raw_input).pop().strip().split('\n')]
        ranges = [Range(*rng) for rng in ranges]
        maps[name] = RangeMap(name, ranges)

    return seed_numbers, maps


@print_result(part_num=1, day_num=5)
def part1():
    seed_numbers: list[int]
    maps: dict[str, RangeMap]
    seed_numbers, maps = get_input(5, parse_input, test=False, to_list=False)
    mapped_numbers = []
    for seed_number in seed_numbers:
        source_number = seed_number
        for name in MAP_NAMES:
            destination_number = maps[name].map_to_destination_number(source_number)
            source_number = destination_number
        mapped_numbers.append(source_number)

    return min(mapped_numbers)


@print_result(part_num=2, day_num=5)
def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

import math
import re
from dataclasses import dataclass
from functools import reduce
from operator import mul, sub

from utils import print_and_time_result, get_input


def parse_input1(raw_input: list):
    num_pattern = re.compile(r"\d+")
    raw_times, raw_records = raw_input
    times = list(map(int, num_pattern.findall(raw_times)))
    records = list(map(int, num_pattern.findall(raw_records)))
    return times, records


def parse_input2(raw_input: list):
    raw_time, raw_record = raw_input
    time = int(raw_time.split(":")[1].replace(" ", ""))
    record = int(raw_record.split(":")[1].replace(" ", ""))
    return time, record


def solve_quad(a: int, b: int, c: int):
    sol1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    sol2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return abs(math.ceil(sol2)), abs(math.floor(sol1))


def debug_races(time):
    speed, hold = 0, 0
    for sec in range(time):
        distance = speed * (time - hold)
        print(f"{distance=}, {speed=}, {hold=}")
        hold += 1
        speed += 1


@print_and_time_result(part_num=1, day_num=6)
def part1():
    return reduce(
        mul,
        [
            sub(*solve_quad(1, time, record + 1)) + 1
            for time, record in zip(*get_input(6, parse_input1, test=False))
        ],
    )


@print_and_time_result(part_num=2, day_num=6)
def part2():
    time, record = get_input(6, parse_input2, test=False)
    return sub(*solve_quad(1, time, record + 1)) + 1


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

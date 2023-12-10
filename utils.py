from functools import wraps
from pathlib import Path
from typing import Callable

import sys
import os


def get_input(day_num: int, input_parser: Callable = None, test: bool = False, part_num: int = 1, to_list: bool = True):
    input_name = "input" if not test else f"part{part_num}test"
    _path = Path(f"day{day_num}/{input_name}.txt")

    with open(_path) as f:
        read_func = f.readlines if to_list else f.read
        inpt = input_parser(read_func()) if input_parser else read_func()

    return inpt


def print_result(part_num: int, day_num: int):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"Result calculated for part {part_num} of day {day_num}: {result}")

        return wrapper

    return deco

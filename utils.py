from functools import wraps
from pathlib import Path
from typing import Callable

import sys
import os


def get_input(line_func: Callable, day_num: int, test: bool = False, part_num: int = 1):
    input_name = "input" if not test else f"part{part_num}test"
    _path = Path(f"day{day_num}/{input_name}.txt")
    with open(_path) as f:
        inpt = [line_func(line) for line in f.readlines()]

    return inpt


def print_result(part_num: int):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"Result calculated for part {part_num}: {result}")

        return wrapper

    return deco

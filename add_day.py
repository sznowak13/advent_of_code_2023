import os
from pathlib import Path

import typer

solution_file_template = """import re
from dataclasses import dataclass
from utils import print_and_time_result, get_input


def parse_input(raw_input: str):
    pass


@print_and_time_result(part_num=1, day_num={day_num})
def part1():
    pass


@print_and_time_result(part_num=2, day_num={day_num})
def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
"""


def main(day_num: int):
    day_dir_root = Path(f"day{day_num}")
    if os.path.isdir(day_dir_root):
        raise FileExistsError(f"Day {day_num} already exists")
    os.makedirs(day_dir_root)
    with open(day_dir_root.joinpath("__init__.py"), "w") as f:
        f.write(f"from day{day_num}.solution import main as day{day_num}_solution")
    open(day_dir_root.joinpath("input.txt"), "w").close()
    open(day_dir_root.joinpath("part1test.txt"), "w").close()
    with open(day_dir_root.joinpath("solution.py"), "w") as f:
        f.write(solution_file_template.format(day_num=day_num))


if __name__ == "__main__":
    typer.run(main)

from pathlib import Path

INPUT_DIR_PATH = Path('inputs')


def get_input(input_name: str):
    _path = INPUT_DIR_PATH.joinpath(f"{input_name}.txt")
    with open(_path) as f:
        inpt = [line.strip() for line in f.readlines()]

    return inpt

import importlib
import os
import re

days_modules = []

day_pattern = re.compile(r"day\d")
for _dir in os.listdir("."):
    if os.path.isdir(_dir) and day_pattern.match(_dir):
        days_modules.append(importlib.import_module(_dir))


def main():
    for day_module in days_modules:
        day_module.solution.main()


if __name__ == "__main__":
    main()

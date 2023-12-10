from functools import reduce

from utils import get_input, print_result

NUM_WORDS_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_input(raw_input):
    return [line.strip() for line in raw_input]


def calc_digit_calibration_value_from_line(line: str) -> int:
    first, last = "", ""
    i = 0
    while not first or not last:
        if not first and line[i].isdigit():
            first = line[i]
        if not last and line[-i - 1].isdigit():
            last = line[-i - 1]
        i += 1
    return int(first + last)


def calc_word_calibration_value_from_line(line: str) -> int:
    first_digit, last_digit, front_scan, back_scan = "", "", "", ""

    def try_for_digit_in_scan(scan: str):
        digit = ""
        for num_word, num in NUM_WORDS_DICT.items():
            if num_word in scan:
                digit = num
        return digit

    i = 0
    while not first_digit or not last_digit:
        curr_back = line[-i - 1]
        curr_front = line[i]
        if not first_digit:
            if curr_front.isdigit():
                first_digit = curr_front
            else:
                front_scan += curr_front
                first_digit = try_for_digit_in_scan(front_scan)

        if not last_digit:
            if curr_back.isdigit():
                last_digit = curr_back
            else:
                back_scan += curr_back
                last_digit = try_for_digit_in_scan("".join(reversed(back_scan)))

        i += 1
    return int(first_digit + last_digit)


@print_result(part_num=1, day_num=1)
def part1():
    return reduce(
        lambda acc, line: acc + calc_digit_calibration_value_from_line(line),
        get_input(input_parser=parse_input, day_num=1),
        0,
    )


@print_result(part_num=2, day_num=1)
def part2():
    return reduce(
        lambda acc, line: acc + calc_word_calibration_value_from_line(line),
        get_input(input_parser=parse_input, day_num=1),
        0,
    )


def main():
    part1()
    part2()

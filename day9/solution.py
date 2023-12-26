from utils import print_and_time_result, get_input


def parse_input(raw_input: str):
    return [list(map(int, line.strip().split(" "))) for line in raw_input]


def predict_next_value(history: list):
    if not any(history):
        return 0
    return history[-1] + predict_next_value(
        [next_val - curr_val for curr_val, next_val in zip(history, history[1:])]
    )


@print_and_time_result(part_num=1, day_num=9)
def part1():
    histories = get_input(9, parse_input, test=False)
    next_values = [predict_next_value(history) for history in histories]
    return sum(next_values)


@print_and_time_result(part_num=2, day_num=9)
def part2():
    histories = get_input(9, parse_input, test=False)
    next_values = [predict_next_value(list(reversed(history))) for history in histories]
    return sum(next_values)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

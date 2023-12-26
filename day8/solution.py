import math
from itertools import cycle
from typing import Callable

from utils import print_and_time_result, get_input


def parse_input(raw_input: str) -> tuple[str, dict]:
    dirs, *nodes_str = [line.strip() for line in raw_input if line.strip()]
    node_definitions = {}
    for node_str in nodes_str:
        node_name, subs = node_str.split(" = ")
        node_definitions[node_name] = subs.strip("()").split(", ")
    return dirs, node_definitions


def break_condition_part1(node: tuple[str, list]):
    return node[0] == "ZZZ"


def break_condition_part2(node: tuple[str, list]):
    return node[0].endswith("Z")


def count_steps(
    start_node: tuple[str, list[str]],
    nodes: dict[str, tuple[str, list[str]]],
    break_condition: Callable,
    directions: str,
):
    curr_node = start_node
    steps = 0
    for direction in cycle(directions):
        if break_condition(curr_node):
            return steps

        if direction == "R":
            next_node = curr_node[1][1]
            curr_node = (next_node, nodes[next_node])
        elif direction == "L":
            next_node = curr_node[1][0]
            curr_node = (next_node, nodes[next_node])
        steps += 1


@print_and_time_result(part_num=1, day_num=8)
def part1():
    dirs: str
    nodes: dict
    dirs, nodes = get_input(8, parse_input, test=False)
    curr_node = ("AAA", nodes["AAA"])
    return count_steps(curr_node, nodes, break_condition_part1, dirs)


@print_and_time_result(part_num=2, day_num=8)
def part2():
    dirs: str
    nodes: dict
    dirs, nodes = get_input(8, parse_input, test=False)
    start_nodes = {
        name: sub_nodes for name, sub_nodes in nodes.items() if name.endswith("A")
    }
    return math.lcm(
        *[
            count_steps(start_node, nodes, break_condition_part2, dirs)
            for start_node in start_nodes.items()
        ]
    )


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()

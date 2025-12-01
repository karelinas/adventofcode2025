from sys import stdin
from typing import Callable

INITIAL_DIAL: int = 50


def main():
    instructions = parse_instruction(stdin.read())
    print("Part 1", count_zeros(instructions, count_if_stops_on_zero))
    print("Part 2", count_zeros(instructions, count_all_zero_clicks))


def parse_instruction(s: str) -> list[int]:
    get_sign: Callable[[str], int] = lambda x: -1 if x[0] == "L" else 1
    get_int: Callable[[str], int] = lambda x: int(x[1:])
    return [get_sign(line) * get_int(line) for line in s.split("\n") if line]


def count_zeros(instructions: list[int], count_fn: Callable[[int, int], int]) -> int:
    dial: int = INITIAL_DIAL
    zeros: int = 0
    for inst in instructions:
        zeros += count_fn(dial, dial + inst)
        dial = (dial + inst) % 100
    return zeros


def count_if_stops_on_zero(_: int, end: int) -> int:
    return 1 if (end % 100) == 0 else 0


def count_all_zero_clicks(start: int, end: int) -> int:
    zeros: int = abs(end) // 100
    if end == 0 or (end < 0 and start != 0):
        zeros += 1
    return zeros


if __name__ == "__main__":
    main()

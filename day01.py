from sys import stdin
from typing import Callable


def main():
    dial: int = 50
    instructions = parse_instruction(stdin.read())
    zeros: int = 0
    for inst in instructions:
        zeros += count_zeros(dial, dial + inst)
        dial = (dial + inst) % 100

    print(zeros)


def parse_instruction(s: str) -> list[int]:
    get_sign: Callable[[str], int] = lambda x: -1 if x[0] == "L" else 1
    get_int: Callable[[str], int] = lambda x: int(x[1:])
    return [get_sign(line) * get_int(line) for line in s.split("\n") if line]


def count_zeros(start: int, end: int) -> int:
    zeros = abs(end) // 100
    if end < 0 and start != 0:
        zeros += 1
    if end == 0:
        zeros += 1
    return zeros


if __name__ == "__main__":
    main()

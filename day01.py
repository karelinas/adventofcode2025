from sys import stdin
from typing import Callable


def main():
    dial: int = 50
    instructions = parse_instruction(stdin.read())
    zeros: int = 0
    for inst in instructions:
        dial += inst
        dial %= 100
        if dial == 0:
            zeros += 1

    print(zeros)


def parse_instruction(s: str) -> list[int]:
    get_sign: Callable[[str], int] = lambda x: -1 if x[0] == "L" else 1
    get_int: Callable[[str], int] = lambda x: int(x[1:])
    return [get_sign(line) * get_int(line) for line in s.split("\n") if line]


if __name__ == "__main__":
    main()

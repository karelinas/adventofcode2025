import re
from dataclasses import dataclass
from functools import reduce
from operator import add, mul
from sys import stdin
from typing import Any, Callable

from lib import transpose

Operator = Callable[[Any, Any], Any]

OPERATORS: dict[str, Operator] = {"*": mul, "+": add}


@dataclass(frozen=True)
class Problem:
    numbers: list[int]
    op: Operator

    def solve(self) -> int:
        return reduce(self.op, self.numbers)


def main():
    problems: list[Problem] = parse_problems(stdin.read())
    print("Part 1:", sum_solutions(problems))


def parse_problems(s: str) -> list[Problem]:
    return [
        Problem(numbers=[int(val) for val in col[:-1]], op=OPERATORS[col[-1]])
        for col in transpose(
            [cell for cell in re.split(r"\s+", line) if cell]
            for line in s.strip().split("\n")
            if line
        )
    ]


def sum_solutions(problems: list[Problem]) -> int:
    return sum(p.solve() for p in problems)


if __name__ == "__main__":
    main()

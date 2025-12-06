import re
from dataclasses import dataclass
from functools import reduce
from operator import add, mul
from sys import stdin
from typing import Any, Callable, Optional

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
    problem_str = stdin.read()

    problems: list[Problem] = parse_problems(problem_str)
    print("Part 1:", sum_solutions(problems))

    problems = parse_problems_in_columns(problem_str)
    print("Part 2:", sum_solutions(problems))


def parse_problems(s: str) -> list[Problem]:
    return [
        Problem(numbers=[int(val) for val in col[:-1]], op=OPERATORS[col[-1]])
        for col in transpose(
            [cell for cell in re.split(r"\s+", line) if cell]
            for line in s.strip().split("\n")
            if line
        )
    ]


def parse_problems_in_columns(s: str) -> list[Problem]:
    problems: list[Problem] = []

    lines = [line for line in s.split("\n") if line]
    max_length: int = max(len(line) for line in lines)
    lines = [line.ljust(max_length) for line in lines]
    columns = list("".join(col) for col in transpose(lines))

    numbers: list[int] = []
    op: Optional[Operator] = None
    for col in columns:
        if not col.strip():
            assert op
            problems.append(Problem(numbers, op))
            numbers = []
            op = None

        cells = re.split(r"\s+", col)
        for cell in cells:
            cell = cell.strip()
            if not cell:
                continue
            if cell in OPERATORS or cell[-1] in OPERATORS:
                op = OPERATORS[cell[-1]]
                cell = cell[:-1]
            if cell.strip():
                numbers.append(int(cell))

    if numbers and op:
        problems.append(Problem(numbers, op))

    return problems


def sum_solutions(problems: list[Problem]) -> int:
    return sum(p.solve() for p in problems)


if __name__ == "__main__":
    main()

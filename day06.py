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

    # Read in lines of input normally
    lines = [line for line in s.split("\n") if line]

    # Pad line lengths to a normalized length for easier transposition
    max_length: int = max(len(line) for line in lines)
    lines = [line.ljust(max_length) for line in lines]

    # Transpose columns into lines
    columns = "\n".join("".join(col).strip() for col in transpose(lines))

    for problem_str in columns.split("\n\n"):
        new_numbers: list[int] = []
        new_op: Optional[Operator] = None

        for line in problem_str.split("\n"):
            # Check if operator is at the end and remove, so that we can read
            # in the integer that it might be attached to
            if line[-1] in OPERATORS.keys():
                new_op = OPERATORS[line[-1]]
                line = line[:-1]

            # Add the number to this problem's number list
            new_numbers.append(int(line))

        # Input format promises operator is in every problem set...
        assert new_op

        # Finally add the new Problem to the list
        problems.append(Problem(new_numbers, new_op))

    return problems


def sum_solutions(problems: list[Problem]) -> int:
    return sum(p.solve() for p in problems)


if __name__ == "__main__":
    main()

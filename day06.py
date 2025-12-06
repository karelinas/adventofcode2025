import re
from dataclasses import dataclass
from functools import reduce
from operator import add, mul
from sys import stdin
from typing import Any, Callable, Optional

from lib import normalize_line_lengths, rstrip_lines, transpose, transpose_str

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
    # Transposition turns this:
    #    123 328
    #     45 64
    #      6 98
    #    *   +
    #
    # Into this:
    #    1  *
    #    24
    #    356
    #
    #    369+
    #    248
    #    8
    transposed_s = rstrip_lines(transpose_str(normalize_line_lengths(s)))

    problems: list[Problem] = []
    # After transposition, problems are separated by an empty line between
    # them, so we can parse them one by one
    for problem_str in transposed_s.split("\n\n"):
        new_numbers: list[int] = []
        new_op: Optional[Operator] = None

        for line in problem_str.split("\n"):
            # If the operator is at the end, read it in and remove it so that
            # we can parse the integer that comes before it
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

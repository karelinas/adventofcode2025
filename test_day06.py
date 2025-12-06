import unittest

from day06 import parse_problems, parse_problems_in_columns, sum_solutions

EXAMPLE_INPUT: str = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""


class Day06TestCase(unittest.TestCase):
    def test_example_data(self):
        with self.subTest("Part 1"):
            problems = parse_problems(EXAMPLE_INPUT)
            self.assertEqual(sum_solutions(problems), 4277556)
        with self.subTest("Part 2"):
            problems = parse_problems_in_columns(EXAMPLE_INPUT)
            self.assertEqual(sum_solutions(problems), 3263827)

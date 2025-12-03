import unittest

from day03 import parse_banks, sum_of_jolts, sum_of_super_jolts

EXAMPLE_INPUT: str = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


class Day03TestCase(unittest.TestCase):
    def test_example_data(self):
        banks = parse_banks(EXAMPLE_INPUT)

        with self.subTest("Part 1"):
            self.assertEqual(sum_of_jolts(banks), 357)
        with self.subTest("Part 2"):
            self.assertEqual(sum_of_super_jolts(banks), 3121910778619)

import unittest

from day01 import (
    count_all_zero_clicks,
    count_if_stops_on_zero,
    count_zeros,
    parse_instruction,
)

EXAMPLE_INPUT: str = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


class Day01TestCase(unittest.TestCase):
    def test_example_data(self):
        instructions = parse_instruction(EXAMPLE_INPUT)

        with self.subTest("Part 1"):
            self.assertEqual(count_zeros(instructions, count_if_stops_on_zero), 3)
        with self.subTest("Part 2"):
            self.assertEqual(count_zeros(instructions, count_all_zero_clicks), 6)

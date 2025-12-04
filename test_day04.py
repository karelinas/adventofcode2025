import unittest

from day04 import Grid

EXAMPLE_INPUT: str = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


class Day04TestCase(unittest.TestCase):
    def test_example_data(self):
        grid = Grid.from_string(EXAMPLE_INPUT)

        with self.subTest("Part 1"):
            self.assertEqual(Grid.count_accessible_rolls(grid), 13)

import unittest

from day05 import Database

EXAMPLE_INPUT: str = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


class Day05TestCase(unittest.TestCase):
    def test_example_data(self):
        db = Database.from_string(EXAMPLE_INPUT)

        with self.subTest("Part 1"):
            self.assertEqual(db.count_fresh_ingredients(), 3)
        with self.subTest("Part 2"):
            self.assertEqual(db.count_all_possible_fresh_ids(), 14)

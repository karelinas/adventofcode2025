import unittest

from day02 import parse_ranges, sum_invalid_ids

EXAMPLE_INPUT: str = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
    "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
    "824824821-824824827,2121212118-2121212124"
)


class Day02TestCase(unittest.TestCase):
    def test_example_data(self):
        ranges = parse_ranges(EXAMPLE_INPUT)

        with self.subTest("Part 1"):
            self.assertEqual(sum_invalid_ids(ranges), 1227775554)

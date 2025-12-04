from sys import stdin
from typing import Iterable

from lib import Point, neighborhood


def main():
    grid = Grid.from_string(stdin.read())
    print("Part 1:", grid.count_accessible_rolls())
    print("Part 2:", grid.remove_all_rolls())


class Grid:
    def __init__(self, rolls: set[Point]) -> None:
        self.rolls: set[Point] = rolls

    @staticmethod
    def from_string(s: str) -> "Grid":
        lines: list[str] = [line.strip() for line in s.split("\n") if line]
        return Grid(
            {
                Point(x, y)
                for y, line in enumerate(lines)
                for x, ch in enumerate(line)
                if ch == "@"
            }
        )

    def count_accessible_rolls(self) -> int:
        return len(self.accessible_rolls())

    def remove_all_rolls(self) -> int:
        def all_removals() -> Iterable[int]:
            while (removed := self.remove_rolls()) > 0:
                yield removed

        return sum(all_removals())

    def remove_rolls(self) -> int:
        """
        Does one pass of removing rolls from the grid and returns the number
        of rolls that was removed.
        """
        to_remove = self.accessible_rolls()
        self.rolls -= to_remove
        return len(to_remove)

    def accessible_rolls(self) -> set[Point]:
        return {
            coord
            for coord in self.rolls
            if sum(1 for neighbor in neighborhood(coord) if neighbor in self.rolls) < 4
        }


if __name__ == "__main__":
    main()

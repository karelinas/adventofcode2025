from sys import stdin

from lib import Point, neighborhood


def main():
    grid = Grid.from_string(stdin.read())
    print("Part 1:", grid.count_accessible_rolls())
    print("Part 2:", grid.remove_all_rolls())


class Grid:
    def __init__(self, grid: dict[Point, str]) -> None:
        self.grid: dict[Point, str] = grid

    @staticmethod
    def from_string(s: str) -> "Grid":
        lines: list[str] = [line.strip() for line in s.split("\n") if line]
        return Grid(
            {
                Point(x, y): ch
                for y, line in enumerate(lines)
                for x, ch in enumerate(line)
                if ch == "@"
            }
        )

    def count_accessible_rolls(self) -> int:
        return len(self.accessible_rolls())

    def remove_all_rolls(self) -> int:
        total_removed: int = 0
        while (removed := self.remove_rolls()) > 0:
            total_removed += removed
        return total_removed

    def remove_rolls(self) -> int:
        """
        Does one pass of removing rolls from the grid and returns the number
        of rolls that was removed.
        """
        to_remove = self.accessible_rolls()
        self.grid = {key: val for key, val in self.grid.items() if key not in to_remove}

        return len(to_remove)

    def accessible_rolls(self) -> set[Point]:
        return {
            coord
            for coord in self.grid.keys()
            if sum(1 for neighbor in neighborhood(coord) if neighbor in self.grid) < 4
        }


if __name__ == "__main__":
    main()

from sys import stdin

from lib import Point, neighborhood


def main():
    grid = Grid.from_string(stdin.read())
    print("Part 1:", grid.count_accessible_rolls())


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
        return sum(
            (
                1
                if sum(1 for neighbor in neighborhood(coord) if neighbor in self.grid)
                < 4
                else 0
            )
            for coord in self.grid.keys()
        )


if __name__ == "__main__":
    main()

from dataclasses import dataclass
from sys import stdin


@dataclass(frozen=True, eq=True, order=True)
class Range:
    start: int
    end: int

    def __contains__(self, item: int) -> bool:
        return item >= self.start and item <= self.end

    def overlaps(self, other: "Range") -> bool:
        return self.start in other or self.end in other

    def length(self) -> int:
        return self.end - self.start + 1

    def merge(self, other: "Range") -> "Range":
        return Range(start=min(self.start, other.start), end=max(self.end, other.end))

    @staticmethod
    def from_string(s: str) -> "Range":
        start_str, end_str, *_ = s.strip().split("-")
        return Range(start=int(start_str), end=int(end_str))


@dataclass(frozen=True)
class Database:
    ranges: list[Range]
    items: list[int]

    def count_fresh_ingredients(self) -> int:
        return sum(
            1 if any(item in range for range in self.ranges) else 0
            for item in self.items
        )

    def count_all_possible_fresh_ids(self) -> int:
        return sum(range.length() for range in self.merged_ranges())

    def merged_ranges(self) -> list[Range]:
        new_ranges: list[Range] = []
        remainder: list[Range] = list(sorted(self.ranges))
        while len(remainder) > 0:
            collapsed_range: Range = remainder.pop(0)
            while len(remainder) > 0 and remainder[0].overlaps(collapsed_range):
                collapsed_range = collapsed_range.merge(remainder.pop(0))
            new_ranges.append(collapsed_range)

        return new_ranges

    @staticmethod
    def from_string(s: str) -> "Database":
        ranges_str, items_str, *_ = s.strip().split("\n\n")
        return Database(
            ranges=[Range.from_string(line) for line in ranges_str.strip().split("\n")],
            items=[int(line) for line in items_str.strip().split("\n") if line],
        )


def main():
    db = Database.from_string(stdin.read())
    print("Part 1:", db.count_fresh_ingredients())
    print("Part 2:", db.count_all_possible_fresh_ids())


if __name__ == "__main__":
    main()

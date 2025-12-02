from re import Pattern, compile
from sys import stdin
from typing import Callable

REPEAT_REGEX: Pattern = compile(r"^(\d+)\1+$")


def main():
    ranges = parse_ranges(stdin.read())
    print("Part 1", sum_invalid_ids(ranges, repeats_twice))
    print("Part 2", sum_invalid_ids(ranges, repeats))


def parse_ranges(data: str) -> list[tuple[int, int]]:
    def make_pair(s: str):
        l, r, *_ = s.split("-", maxsplit=1)
        return (int(l), int(r))

    return [make_pair(item) for item in data.strip().split(",") if item.strip()]


def sum_invalid_ids(
    ranges: list[tuple[int, int]], is_invalid_fn: Callable[[str], bool]
) -> int:
    return sum(
        item if is_invalid_fn(str(item)) else 0
        for start, end in ranges
        for item in range(start, end + 1)
    )


def repeats_twice(s: str) -> bool:
    return (len(s) % 2) == 0 and s[: len(s) // 2] == s[len(s) // 2 :]


def repeats(s: str) -> bool:
    return REPEAT_REGEX.match(s) is not None


if __name__ == "__main__":
    main()

from sys import stdin
from typing import Callable, Iterable


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
    def pieces(length: int) -> Iterable[str]:
        return (s[n : n + length] for n in range(0, len(s), length))

    def all_equal(items: Iterable[str]) -> bool:
        it = iter(items)
        first = next(it)
        return all(n == first for n in it)

    return any(all_equal(pieces(length)) for length in range(1, (len(s) // 2) + 1))


if __name__ == "__main__":
    main()

from sys import stdin

INITIAL_DIAL: int = 50


def main():
    ranges = parse_ranges(stdin.read())
    print("Part 1", sum_invalid_ids(ranges))


def parse_ranges(data: str) -> list[tuple[int, int]]:
    def make_pair(s: str):
        l, r, *_ = s.split("-", maxsplit=1)
        return (int(l), int(r))

    return [make_pair(item) for item in data.strip().split(",") if item.strip()]


def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    def len_even(s: str) -> bool:
        return (len(s) % 2) == 0

    def left(s: str) -> str:
        return s[: len(s) // 2]

    def right(s: str) -> str:
        return s[len(s) // 2 :]

    def item_sum(s: str) -> int:
        return int(s) if len_even(s) and left(s) == right(s) else 0

    return sum(
        item_sum(str(item)) for start, end in ranges for item in range(start, end + 1)
    )


if __name__ == "__main__":
    main()

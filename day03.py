from operator import itemgetter
from sys import stdin

Bank = list[int]


def main():
    banks = parse_banks(stdin.read())
    print("Part 1:", sum_of_jolts(banks))
    print("Part 2:", sum_of_super_jolts(banks))


def parse_banks(s: str) -> list[Bank]:
    return [bank_from_str(line.strip()) for line in s.split("\n") if line]


def bank_from_str(s: str) -> Bank:
    return [int(ch) for ch in s.strip()]


def sum_of_jolts(banks: list[Bank]) -> int:
    return sum(max_jolt(bank, digits=2) for bank in banks)


def sum_of_super_jolts(banks: list[Bank]) -> int:
    return sum(max_jolt(bank, digits=12) for bank in banks)


def max_jolt(bank: Bank, digits: int = 2) -> int:
    jolt_value: int = 0
    current_index: int = 0

    places: list[tuple[int, int]] = list(enumerate(10**n for n in range(digits)))
    for place, place_factor in reversed(places):
        index, place_value = max(
            enumerate(bank[current_index : len(bank) - place]), key=itemgetter(1)
        )
        jolt_value += place_value * place_factor
        current_index = current_index + index + 1

    return jolt_value


if __name__ == "__main__":
    main()

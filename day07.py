from dataclasses import dataclass
from functools import cache, cached_property
from sys import stdin
from typing import Optional

from lib import Point


@dataclass(frozen=True)
class TachyonManifold:
    splitters: frozenset[Point]

    @cached_property
    def height(self) -> int:
        return max(s.y for s in self.splitters)


def main():
    beam: Point
    manifold: TachyonManifold
    beam, manifold = parse_manifold(stdin.read())
    print("Part 1:", count_splits(beam, manifold))
    print("Part 2:", quantum_splits(beam, manifold))


def parse_manifold(s: str) -> tuple[Point, TachyonManifold]:
    beam_start: Optional[Point] = None
    splitters: set[Point] = set()

    for y, line in enumerate(s.split("\n")):
        for x, ch in enumerate(line.strip()):
            if ch == "S":
                beam_start = Point(x, y)
            elif ch == "^":
                splitters.add(Point(x, y))

    # Spec promises that input always contains beam start
    assert beam_start

    return beam_start, TachyonManifold(frozenset(splitters))


def count_splits(start_beam: Point, manifold: TachyonManifold) -> int:
    seen: set[Point] = set()
    beams: list[Point] = [start_beam]
    split_count: int = 0

    while beams:
        beam = beams.pop()

        # Has beam gone out of bounds?
        if beam.y > manifold.height:
            continue

        # Have we already counted a beam at this location?
        if beam in seen:
            continue

        seen.add(beam)

        # Has beam hit a splitter?
        if beam in manifold.splitters:
            split_count += 1
            beams.append(beam + Point.west())
            beams.append(beam + Point.east())
        # Otherwise beam just continues south
        else:
            beams.append(beam + Point.south())

    return split_count


@cache
def quantum_splits(beam: Point, manifold: TachyonManifold) -> int:
    # Has beam gone out of bounds?
    if beam.y > manifold.height:
        return 1

    # Has beam hit a splitter?
    if beam in manifold.splitters:
        west: Point = beam + Point.west()
        east: Point = beam + Point.east()
        return quantum_splits(west, manifold) + quantum_splits(east, manifold)

    # Otherwise beam just continues south
    return quantum_splits(beam + Point.south(), manifold)


if __name__ == "__main__":
    main()

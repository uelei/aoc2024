from __future__ import annotations

import argparse
import os.path
from typing import List

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input")


matrix = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (1, -1), (2, -2), (3, -3)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
]


def extract_xmas_from_lines(lines, cords, x, y) -> str:
    xmas = ""
    for cord in cords:
        x_cord = x + cord[0]
        y_cord = y + cord[1]
        if x_cord < 0 or y_cord < 0:
            return ""
        try:
            car = lines[x_cord][y_cord]
        except IndexError:
            return ""
        xmas += car
    return xmas


def find_xmas(lines: List[List[str]], x: int, y: int) -> dict[List[tuple[int, int]] : str]:
    found = {}
    for coords in matrix:
        word = extract_xmas_from_lines(lines, coords, x, y)
        if word == "XMAS" or word == "SAMX":
            n_coords = [(x + c[0], y + c[1]) for c in coords]
            found[tuple(sorted(n_coords))] = word
    return found


def compute(s: str) -> int:
    lines = []
    for line in s.splitlines():
        lines.append(list(line))
    found_xmas = {}
    for l, line in enumerate(lines):
        for c, car in enumerate(line):
            if car == "X" or car == "S":
                found = find_xmas(lines, l, c)
                if found:
                    for k, v in found.items():
                        if k not in found_xmas:
                            found_xmas[k] = v
    return len(found_xmas)


INPUT_S = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
EXPECTED = 18


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

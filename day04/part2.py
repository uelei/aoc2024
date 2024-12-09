from __future__ import annotations

import argparse
import os.path
from typing import List

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input")


matrix = [(-1, 1), (1, 1), (-1, -1), (1, -1)]


def extract_xmas_from_lines(lines, cords, x, y) -> str:
    found = []
    for cord in cords:
        x_cord = x + cord[0]
        y_cord = y + cord[1]
        if x_cord < 0 or y_cord < 0:
            return ""
        try:
            car = lines[x_cord][y_cord]
        except IndexError:
            return ""
        found.append(car)

    return found


def find_xmas(lines: List[List[str]], x: int, y: int) -> bool:
    word = extract_xmas_from_lines(lines, matrix, x, y)
    if not word:
        return False
    if (word[0], word[3]) in [("M", "S"), ("S", "M")] and (word[1], word[2]) in [("M", "S"), ("S", "M")]:
        return True

    return False


def compute(s: str) -> int:
    lines = []
    for line in s.splitlines():
        lines.append(list(line))
    total = 0
    for l, line in enumerate(lines):
        for c, car in enumerate(line):
            if car == "A":
                found = find_xmas(lines, l, c)
                total += 1 if found else 0
    return total


INPUT_S = """\
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
EXPECTED = 9


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

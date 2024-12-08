from __future__ import annotations

import argparse
import os.path
import re
from typing import List

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input")


LIN_REG = re.compile(r"(\d+)   (\d+)")


class SolutionDay01:
    l1: List[int] = []
    l2: List[int] = []

    def __init__(self, data):
        self.data = data

    def parse_line(self):
        for line in self.data:
            match = re.match(LIN_REG, line)

            if match:
                x, y = map(int, match.groups())

                self.l1.append(x)
                self.l2.append(y)

            if not match:
                print("no match for line ", line)

    def part1(self):
        self.parse_line()
        total_distance = 0
        ll1 = sorted(self.l1)
        ll2 = sorted(self.l2)

        for l1, l2 in zip(ll1, ll2):
            total_distance += abs(l1 - l2)
        return total_distance


def compute(s: str) -> int:
    solution = SolutionDay01(s.splitlines())

    return solution.part1()


INPUT_S = """\

"""
EXPECTED = 1


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

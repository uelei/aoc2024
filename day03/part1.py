from __future__ import annotations

import argparse
import os.path
import re

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input")


MULTIPLY = re.compile(r"mul\((\d+),(\d+)\)")


def compute(s: str) -> int:
    lines = s.splitlines()
    total = 0
    for line in lines:
        for match in MULTIPLY.findall(line):
            t = int(match[0]) * int(match[1])
            total += t
    return total


INPUT_S = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
EXPECTED = 161


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

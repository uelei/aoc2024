from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input")


def check_diff_numbers(a, b):
    return abs(a - b) in [1, 2, 3]


def check_reports_with_dump(my_list):
    result = [my_list[:i] + my_list[i + 1 :] for i in range(len(my_list))]

    for report in result:
        if check_reports(report):
            return True
    return False


def check_reports(reports):
    if reports != sorted(reports) and sorted(reports, reverse=True) != reports:
        return False

    lline = 0
    while lline < len(reports) - 1:
        if not check_diff_numbers(reports[lline], reports[lline + 1]):
            return False

        lline += 1

    return True


class SolutionDay02:
    lines = []

    def __init__(self, data):
        self.data = data
        self.parse_line()

    def parse_line(self):
        for line in self.data:
            if not line:
                continue
            reports = list(map(int, line.split(" ")))

            if not reports:
                print("no match for line ", line)
            self.lines.append(reports)

    def part1(self):
        safes = 0
        for line in self.lines:
            if line and check_reports(line):
                safes += 1
        return safes

    def part2(self):
        safes = 0
        for line in self.lines:
            if line and check_reports_with_dump(line):
                safes += 1
        return safes


def compute(s: str) -> int:
    solution = SolutionDay02(s.splitlines())

    return solution.part2()


@pytest.mark.parametrize(
    "reports,expected",
    [
        (
            [7, 6, 4, 2, 1],
            True,
        ),  # : Safe because the levels are all decreasing by 1 or 2.
        ([1, 2, 7, 8, 9], False),  # : Unsafe because 2 7 is an increase of 5.
        ([9, 7, 6, 2, 1], False),  # : Unsafe because 6 2 is a decrease of 4.
        (
            [1, 3, 2, 4, 5],
            False,
        ),  # : Unsafe because 1 3 is increasing but 3 2 is decreasing.
        (
            [8, 6, 4, 4, 1],
            False,
        ),  # : Unsafe because 4 4 is neither an increase or a decrease.
        (
            [1, 3, 6, 7, 9],
            True,
        ),  # : Safe because the levels are all increasing by 1, 2, or 3.
    ],
)
def test_solution_check_valid(reports, expected):
    r = check_reports(reports)

    assert r == expected


@pytest.mark.parametrize(
    "reports,expected",
    [
        (
            [7, 6, 4, 2, 1],
            True,
        ),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        (
            [1, 3, 2, 4, 5],
            True,
        ),
        (
            [8, 6, 4, 4, 1],
            True,
        ),
        (
            [1, 3, 6, 7, 9],
            True,
        ),
    ],
)
def test_solution_check_valid_with_dump(reports, expected):
    r = check_reports_with_dump(reports)

    assert r == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

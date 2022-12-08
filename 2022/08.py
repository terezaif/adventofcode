from aocd import get_data
import math


def part1(data):
    input = [list(s) for s in data.split("\n")]
    w, h = len(input[0]), len(input)
    # if any line or column has all trees smaller
    visible = [
        any(
            [
                all(input[j][i - r] < input[j][i] for r in range(1, i + 2)),
                all(input[j][i + r] < input[j][i] for r in range(1, w - i)),
                all(input[j - r][i] < input[j][i] for r in range(1, j + 2)),
                all(input[j + r][i] < input[j][i] for r in range(1, h - j)),
            ]
        )
        for j in range(1, h - 1)
        for i in range(1, w - 1)
    ]

    return 2 * (w + h - 2) + sum(visible)


def part2(data):
    input = [list(s) for s in data.split("\n")]
    w, h = len(input[0]), len(input)
    # get distance of larger tree on line/col (either direction in order of furthest from tree)
    forest_l = [
        math.prod(
            [
                next(
                    r
                    for r in range(1, i + 2)
                    if input[j][i - r] >= input[j][i] or i - r == 0
                ),
                next(
                    r
                    for r in range(1, w - i)
                    if input[j][i + r] >= input[j][i] or i + r == w - 1
                ),
                next(
                    r
                    for r in range(1, j + 2)
                    if input[j - r][i] >= input[j][i] or j - r == 0
                ),
                next(
                    r
                    for r in range(1, h - j)
                    if input[j + r][i] >= input[j][i] or j + r == h - 1
                ),
            ]
        )
        for j in range(1, h - 1)
        for i in range(1, w - 1)
    ]

    return max(forest_l)


def test_part1():
    assert part1(test_data) == 21


def test_part2():
    assert part2(test_data) == 8


data = get_data(day=8, year=2022)

print(part1(data))
print(part2(data))

test_data = """30373
25512
65332
33549
35390"""

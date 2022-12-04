from aocd import get_data
import re


def part1(data):
    lists = [[int(n) for n in re.split(",|-", s)] for s in data.split("\n")]
    diffs = [(li[0] - li[2]) * (li[1] - li[3]) <= 0 for li in lists]
    return sum(diffs)


def part2(data):
    lists = [[int(n) for n in re.split(",|-", s)] for s in data.split("\n")]
    ds = [
        any(
            [
                li[0] <= li[2] <= li[1],
                li[0] <= li[3] <= li[1],
                li[2] <= li[0] <= li[3],
                li[2] <= li[1] <= li[3],
            ]
        )
        for li in lists
    ]
    return sum(ds)


def test_part1():
    assert part1(test_data) == 2


def test_part2():
    assert part2(test_data) == 4


data = get_data(day=4, year=2022)

print(part1(data))
print(part2(data))

test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
4-4,5-5"""

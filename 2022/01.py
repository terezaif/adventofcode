from aocd import get_data
import re


def part1(data):
    calories = [sum([int(c) for c in s.split("\n")]) for s in data.split("\n\n")]
    m = max(calories)
    return m



def part2(data):
    calories = [sum([int(c) for c in s.split("\n")]) for s in data.split("\n\n")]
    calories.sort(reverse = True)
    top = sum(calories[0:3])
    return top


def test_part1():
    assert part1(test_data) == 24000


def test_part2():
    assert part2(test_data) == 45000


data = get_data(day=1, year=2022)

print(part1(data))
print(part2(data))

test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

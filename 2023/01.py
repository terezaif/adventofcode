from aocd import get_data


def part1(data):
    input = [s for s in data.split("\n")]
    out = sum(
        int(next(j for j in i if j.isdigit()) + next(j for j in i[::-1] if j.isdigit()))
        for i in input
    )

    return out


def replacenumbers(str):
    numbers = [
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine"),
    ]
    for r in numbers:
        str = str.replace(*r)

    return str


def part2(data):
    input = [replacenumbers(s) for s in data.split("\n")]
    input = [list(filter(str.isdigit, i)) for i in input]
    out = sum(int(i[0] + i[-1]) for i in input)

    return out


def test_part1():
    assert part1(test_data) == 142


def test_part2():
    assert part2(test_data2) == 281


data = get_data(day=1, year=2023)

print(part1(data))
print(part2(data))

test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_data2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

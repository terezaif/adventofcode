from aocd import get_data


def getOrdinal(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 64 + 26


def part1(data):
    rs = [[char for char in s] for s in data.split("\n")]
    common = [
        list(set(r[0 : len(r) // 2]).intersection(set(r[len(r) // 2 :]))) for r in rs
    ]
    return sum([getOrdinal(j) for i in common for j in i])


def part2(data):
    rs = [[char for char in s] for s in data.split("\n")]
    common = [
        list(set(rs[i]).intersection(set(rs[i + 1])).intersection(set(rs[i + 2])))
        for i in range(0, len(rs), 3)
    ]
    return sum([getOrdinal(j) for i in common for j in i])


def test_part1():
    assert part1(test_data) == 157


def test_part2():
    assert part2(test_data) == 70


data = get_data(day=3, year=2022)

print(part1(data))
print(part2(data))

test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

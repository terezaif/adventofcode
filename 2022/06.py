from aocd import get_data


def part1(data, le):
    return next(
        i + le for i in range(len(data) - le) if len(set(list(data)[i : i + le])) == le
    )


def test_part1():
    assert part1(test_data, 4) == 5


def test_part2():
    assert part1(test_data, 14) == 23


data = get_data(day=6, year=2022)

print(part1(data, 4))
print(part1(data, 14))

test_data = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

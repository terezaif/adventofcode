from aocd import get_data


def part1(data):

    return 1


def part2(data):

    return 2


def test_floors():
    d = "(())"
    assert part1(d) == 1


def test_basement():
    d = ")"
    assert part2(d) == 2


# data = get_data(day=2, year=2015)
# floors(data)

from aocd import get_data


def depth(data):
    depths = [int(s) for s in data.split("\n")]
    diffs = [a - b for (a, b) in zip(depths[:-1], depths[1:])]
    increases = [x < 0 for x in diffs]
    return sum(increases)


def depthby3(data):
    depths = [int(s) for s in data.split("\n")]
    threes = [sum(items) for items in zip(depths[:-2], depths[1:-1], depths[2:])]
    # depth part
    return sum([a - b < 0 for (a, b) in zip(threes[:-1], threes[1:])])


def test_depth():
    assert depth(test_data) == 7


def test_depthby3():
    assert depthby3(test_data) == 5


data = get_data(day=1, year=2021)

print(depth(data))
print(depthby3(data))

test_data = """199
200
208
210
200
207
240
269
260
263"""

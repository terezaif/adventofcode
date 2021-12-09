from aocd import get_data

DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def part1(data):
    lava = [list(s) for s in data.split("\n")]
    points = {}
    for i in range(len(lava)):
        for j in range(len(lava[0])):
            points[i, j] = int(lava[i][j])

    lows = 0
    for point in points:
        neighbors = [
            (point[0] + i, point[1] + j)
            for (i, j) in DIRS
            if (point[0] + i, point[1] + j) in points
        ]
        if all([points[point] < points[adj] for adj in neighbors]):
            lows += 1 + points[point]

    return lows


def part2(data):
    lava = [list(s) for s in data.split("\n")]
    points = {}
    for i in range(len(lava)):
        for j in range(len(lava[0])):
            points[i, j] = int(lava[i][j])

    sizes = []
    for point in points:
        neighbors = [
            (point[0] + i, point[1] + j)
            for (i, j) in DIRS
            if (point[0] + i, point[1] + j) in points
        ]
        if any([points[point] >= points[adj] for adj in neighbors]):
            continue

        unchecked = set([point])
        basin = set([point])
        while len(unchecked) > 0:
            newpoints = set()
            for un in unchecked:
                neighborsloop = [
                    (un[0] + i, un[1] + j)
                    for (i, j) in DIRS
                    if (un[0] + i, un[1] + j) in points
                    and (un[0] + i, un[1] + j) not in basin
                    and points[un[0] + i, un[1] + j] != 9
                ]
                newpoints = newpoints | set(neighborsloop)
                basin = basin | set(neighborsloop)
            unchecked = newpoints
        sizes.append(len(basin))

    sorts = sorted(sizes, reverse=True)[:3]
    return sorts[0] * sorts[1] * sorts[2]


def test_part1():
    assert part1(test_data) == 15


def test_part2():
    assert part2(test_data) == 1134


data = get_data(day=9, year=2021)

print(part1(data))
print(part2(data))

test_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

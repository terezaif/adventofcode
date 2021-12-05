from aocd import get_data
from parse import parse


def get_horizontal_line_points(hv):
    points = dict()
    dups = dict()
    for line in hv:
        for x in range(line[0], line[2] + 1):
            for y in range(line[1], line[3] + 1):
                if points.get((x, y)):
                    dups[(x, y)] = 1
                points[(x, y)] = points.setdefault((x, y), 0) + 1

    return points, dups


def part1(data):
    input = [parse("{:d},{:d} -> {:d},{:d}", s) for s in data.split("\n")]
    hv = [
        [min(p[0], p[2]), min(p[1], p[3]), max(p[0], p[2]), max(p[1], p[3])]
        for p in input
        if p[0] == p[2] or p[1] == p[3]
    ]
    points, dups = get_horizontal_line_points(hv)
    len(dups)

    return len(dups)


def part2(data):
    input = [parse("{:d},{:d} -> {:d},{:d}", s) for s in data.split("\n")]
    hv = [
        [min(p[0], p[2]), min(p[1], p[3]), max(p[0], p[2]), max(p[1], p[3])]
        for p in input
        if p[0] == p[2] or p[1] == p[3]
    ]
    dia = [[p[0], p[1], p[2], p[3]] for p in input if p[0] != p[2] and p[1] != p[3]]

    points, dups = get_horizontal_line_points(hv)

    for line in dia:
        for (x, y) in zip(
            list(range(line[0], line[2], 1 if line[0] < line[2] else -1)),
            list(range(line[1], line[3], 1 if line[1] < line[3] else -1)),
        ):
            if points.get((x, y)):
                dups[(x, y)] = 1
            points[(x, y)] = points.setdefault((x, y), 0) + 1
        if points.get((line[2], line[3])):
            dups[(line[2], line[3])] = 1
        points[(line[2], line[3])] = points.setdefault((line[2], line[3]), 0) + 1
    points
    len(dups)

    return len(dups)


def test_part1():
    assert part1(test_data) == 5


def test_part2():
    assert part2(test_data) == 12


data = get_data(day=5, year=2021)

print(part1(data))
print(part2(data))

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

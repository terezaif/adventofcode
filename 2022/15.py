from aocd import get_data
from parse import parse
from tqdm import tqdm


def md(p):  # x, y , sx, sy
    return abs(p[0] - p[2]) + abs(p[1] - p[3])


def part1(data, r):
    input = [
        parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", s)
        for s in data.split("\n")
    ]
    input = [
        [
            int(i[0]),
            int(i[1]),
            int(i[2]),
            int(i[3]),
            abs(int(i[0]) - int(i[2])) + abs(int(i[1]) - int(i[3])),
        ]
        for i in input
    ]
    # no ties.. so all points closer than the sensor cannot be.. in diamond shape
    cb = set()
    bs = set()
    for sp in input:
        d = sp[4]
        bs.add((sp[2], sp[3]))  # adding the beacon to bs
        if -d < sp[1] - r < d + 1:
            cb |= set(
                [
                    (sp[0] + offx, r)
                    for offx in range(-(d - abs(r - sp[1])), d - abs(r - sp[1]) + 1)
                ]
            )
    cb = cb - bs

    return len([i for i in cb if i[1] == r])


def part2(data, max):
    input = [
        parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}", s)
        for s in data.split("\n")
    ]
    input = [
        [
            int(i[0]),
            int(i[1]),
            int(i[2]),
            int(i[3]),
            abs(int(i[0]) - int(i[2])) + abs(int(i[1]) - int(i[3])),
        ]
        for i in input
    ]
    # points further than the diamond
    rx = []
    couldbe = set()
    incr = 1
    while len(rx) == 0:
        print(incr)
        for sp in tqdm(input):
            d = sp[4] + incr
            scan = [
                (sp[0] + offx, sp[1] + offy)
                for offx in range(-d, d + 1)
                for offy in set([-d + abs(offx), d - abs(offx)])
                if 0 < sp[0] + offx < max and 0 < sp[1] + offy < max
            ]
            couldbe |= set(scan)
            rx = [
                c
                for c in couldbe
                if all([abs(c[0] - s[0]) + abs(c[1] - s[1]) > s[4] for s in input])
            ]
            if len(rx) > 0:
                print(rx)
                break
        incr += 1

    return rx[0][0] * 4000000 + rx[0][1]


def test_part1():
    assert part1(test_data, 10) == 26


def test_part2():
    assert part2(test_data, 20) == 56000011


data = get_data(day=15, year=2022)

print(part1(data, 2000000))
print(part2(data, 4000000))

test_data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

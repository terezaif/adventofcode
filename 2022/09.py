from aocd import get_data

xinc = {"R": 1, "L": -1, "U": 0, "D": 0}
yinc = {"R": 0, "L": 0, "U": -1, "D": 1}


def part1(data):
    input = [s.split(" ") for s in data.split("\n")]
    h = [5, 0]
    t = [5, 0]
    pos = set()
    pos.add(tuple(t))
    for [d, n] in input:
        print(d, n)
        n = int(n)
        while n > 0:
            prevh = h.copy()
            h[0] += yinc[d]
            h[1] += xinc[d]
            if abs(h[1] - t[1]) > 1 or abs(h[0] - t[0]) > 1:
                t = prevh
                pos.add(tuple(t))
            n -= 1
    print(pos)
    return len(pos)


def part2(data, n):
    input = [s.split(" ") for s in data.split("\n")]
    rx = [0] * n
    ry = [5] * n
    pos = set()
    pos.add((ry[-1], rx[-1]))
    for [d, n] in input:
        n = int(n)
        while n > 0:
            rx[0] += xinc[d]
            ry[0] += yinc[d]
            for i in range(1, len(rx)):
                if abs(rx[i] - rx[i - 1]) + abs(ry[i] - ry[i - 1]) >= 3:
                    rx[i] = rx[i] + int((rx[i - 1] - rx[i]) / abs(rx[i] - rx[i - 1]))
                    ry[i] = ry[i] + int((ry[i - 1] - ry[i]) / abs(ry[i] - ry[i - 1]))
                    pos.add((ry[-1], rx[-1]))
                if abs(rx[i] - rx[i - 1]) == 2:
                    rx[i] = rx[i] + int((rx[i - 1] - rx[i]) / 2)
                    pos.add((ry[-1], rx[-1]))
                elif abs(ry[i] - ry[i - 1]) == 2:
                    ry[i] = ry[i] + int((ry[i - 1] - ry[i]) / 2)
                    pos.add((ry[-1], rx[-1]))
            n -= 1
    return len(pos)


def test_part1():
    assert part2(test_data, 2) == 88


def test_part2():
    assert part2(test_data, 10) == 36


data = get_data(day=9, year=2022)

print(part2(data, 2))
print(part2(data, 10))

test_data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

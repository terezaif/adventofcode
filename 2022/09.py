from aocd import get_data

xinc = {"R": 1, "L": -1, "U": 0, "D": 0}
yinc = {"R": 0, "L": 0, "U": -1, "D": 1}


def part2(data, r):
    input = [s.split(" ") for s in data.split("\n")]
    rx = [0] * r
    ry = [5] * r
    pos = set()
    pos.add((ry[-1], rx[-1]))
    for [d, n] in input:
        for _ in range(int(n)):
            rx[0] += xinc[d]
            ry[0] += yinc[d]
            for i in range(1, len(rx)):
                _x = rx[i - 1] - rx[i]
                _y = ry[i - 1] - ry[i]
                if abs(_x) + abs(_y) >= 3:
                    rx[i] += _x / abs(_x)
                    ry[i] += _y / abs(_y)
                    pos.add((ry[-1], rx[-1]))
                elif abs(_x) == 2:
                    rx[i] += (_x) // 2
                    pos.add((ry[-1], rx[-1]))
                elif abs(_y) == 2:
                    ry[i] += (_y) // 2
                    pos.add((ry[-1], rx[-1]))

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

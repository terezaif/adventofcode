from aocd import get_data

dirs = [[0, 1], [-1, 1], [1, 1]]


def place_sand(cave, bottom, start):
    while start[1] < bottom:
        moves = [
            (start[0] + d[0], start[1] + d[1])
            for d in dirs
            if (start[0] + d[0], start[1] + d[1]) not in cave
        ]
        if len(moves) == 0:  # all blocked rest
            return start, True
        else:
            start = moves[0]
    return start, False


def place_sand_bott(cave, bottom, start):
    while True:
        moves = [
            (start[0] + d[0], start[1] + d[1])
            for d in dirs
            if (start[0] + d[0], start[1] + d[1]) not in cave
            and start[1] + d[1] != bottom
        ]
        if len(moves) == 0:  # all blocked rest
            if start[1] == 0:
                return start, False  # blocked top
            return start, True
        else:
            start = moves[0]


def part1(data):
    input = [[p.split(",") for p in s.split(" -> ")] for s in data.split("\n")]
    cave = set()
    for path in input:
        for i in range(len(path) - 1):
            s, e = path[i], path[i + 1]
            x0, x1 = min(int(s[0]), int(e[0])), min(int(s[1]), int(e[1]))
            y0, y1 = max(int(s[0]), int(e[0])), max(int(s[1]), int(e[1]))
            wall = set([(a, b) for a in range(x0, y0 + 1) for b in range(x1, y1 + 1)])
            cave |= wall
    bottom = max([p[1] for p in list(cave)])
    start = [500, 0]
    i = 0
    ok = True
    while ok:
        news, ok = place_sand(cave, bottom, start)
        cave.add(news)
        i += 1

    return i - 1


def part2(data):
    input = [[p.split(",") for p in s.split(" -> ")] for s in data.split("\n")]
    cave = set()
    for path in input:
        for i in range(len(path) - 1):
            s, e = path[i], path[i + 1]
            x0, x1 = min(int(s[0]), int(e[0])), min(int(s[1]), int(e[1]))
            y0, y1 = max(int(s[0]), int(e[0])), max(int(s[1]), int(e[1]))
            wall = set([(a, b) for a in range(x0, y0 + 1) for b in range(x1, y1 + 1)])
            cave |= wall
    bottom = max([p[1] for p in list(cave)]) + 2
    start = (500, 0)
    i = 0
    ok = True
    while ok:
        news, ok = place_sand_bott(cave, bottom, start)
        cave.add(news)
        i += 1

    return i


def test_part1():
    assert part1(test_data) == 24


def test_part2():
    assert part2(test_data) == 93


data = get_data(day=14, year=2022)

print(part1(data))
print(part2(data))

test_data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

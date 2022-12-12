from aocd import get_data
import copy

# BFS

# n - p <=1

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def part1(data):
    input = [[ord(s) - 96 for s in list(s)] for s in data.split("\n")]
    w, h = len(input[0]), len(input)
    start = [(j, i) for j in range(h) for i in range(w) if input[j][i] == -13][0]
    end = [(j, i) for j in range(h) for i in range(w) if input[j][i] == -27][0]
    input = [
        [
            input[j][i] if input[j][i] > 0 else 1 if input[j][i] == -13 else 26
            for i in range(w)
        ]
        for j in range(h)
    ]
    paths = set([start])
    visited = set()
    newpaths = set()
    iter = 0
    shortest = None
    while len(paths) > 0 and shortest is None:
        iter += 1
        visited = visited | paths
        for path in paths:
            j, i = path[0], path[1]
            nnext = set(
                [
                    (j + d[0], i + d[1])
                    for d in DIRS
                    if 0 <= j + d[0] < h
                    and 0 <= i + d[1] < w
                    and input[j + d[0]][i + d[1]] - input[j][i] <= 1
                    and (j + d[0], i + d[1]) not in visited
                ]
            )
            if end in nnext:
                shortest = iter
            newpaths |= nnext

        paths = newpaths
        newpaths = set()

    return shortest


def part2(data):
    input = [[ord(s) - 96 for s in list(s)] for s in data.split("\n")]
    w, h = len(input[0]), len(input)
    end = [(j, i) for j in range(h) for i in range(w) if input[j][i] == -27][0]
    input = [
        [
            input[j][i] if input[j][i] > 0 else 1 if input[j][i] == -13 else 26
            for i in range(w)
        ]
        for j in range(h)
    ]
    paths = set([end])
    visited = set()
    newpaths = set()
    iter = 0
    shortest = None
    while len(paths) > 0 and shortest is None:
        iter += 1
        visited = visited | paths
        for path in paths:
            j, i = path[0], path[1]
            nnext = set(
                [
                    (j + d[0], i + d[1])
                    for d in DIRS
                    if 0 <= j + d[0] < h
                    and 0 <= i + d[1] < w
                    and input[j][i] - input[j + d[0]][i + d[1]] <= 1
                    and (j + d[0], i + d[1]) not in visited
                ]
            )
            if 1 in [input[n[0]][n[1]] for n in list(nnext)]:
                shortest = iter
                print(nnext)
            newpaths |= nnext

        paths = newpaths
        newpaths = set()

    return shortest


def test_part1():
    assert part1(test_data) == 31


def test_part2():
    assert part2(test_data) == 29


data = get_data(day=12, year=2022)

print(part1(data))
print(part2(data))

test_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

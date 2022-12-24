from aocd import get_data

moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
SD = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}


def part1(data):
    input = [list(s) for s in data.split("\n")]
    w, h = len(input[0]), len(input)
    storms = [
        (i - 1, j - 1, input[i][j])
        for i in range(h)
        for j in range(w)
        if input[i][j] in SD.keys()
    ]

    stormsInT = {}

    def stormint(T):
        if T in stormsInT:
            return stormsInT[T]
        newst = [
            ((x + T * SD[s][0]) % (h - 2), (y + T * SD[s][1]) % (w - 2), s)
            for x, y, s in storms
        ]
        stormsmap = set([(x + 1, y + 1) for x, y, s in newst])
        stormsInT[T] = stormsmap
        return stormsmap

    st = (0, 1)
    end = (h - 1, w - 2)

    def walk(src, dest, t):
        q = [(src[0], src[1], t)]
        visited = set(q)
        while q:
            q2 = []
            for x, y, t in q:
                if x == dest[0]:
                    return t
                stormnow = stormint(t + 1)
                nextmoves = [
                    (mx + x, my + y)
                    for mx, my in moves
                    if (mx + x, my + y)
                    if 0 <= mx + x < h and 0 <= my + y <= w
                ]
                for xx, yy in nextmoves:
                    if input[xx][yy] == "#":
                        continue
                    if (xx, yy) in stormnow:
                        continue
                    N = (xx, yy, t + 1)
                    if N in visited:
                        continue
                    q2.append(N)
                    visited.add(N)
            q = q2

    mins = walk(st, end, 0)
    back = walk(end, st, mins)
    backback = walk(st, end, back)
    return mins, backback


def test_part1():
    assert part1(test_data)[0] == 18


def test_part2():
    assert part1(test_data)[1] == 54


data = get_data(day=24, year=2022)

print(part1(data))


test_data = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

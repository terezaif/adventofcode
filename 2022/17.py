from aocd import get_data
from tqdm import tqdm
import functools

JET = {">": [1, 0], "<": [-1, 0]}

rocks = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split(
    "\n\n"
)
rocks = [r.split("\n") for r in rocks]
rocks = [
    [
        (i, len(r) - 1 - j)
        for j, rr in enumerate(r)
        for i, n in enumerate(list(rr))
        if n == "#"
    ]
    for r in rocks
]


def show(R):
    maxY = max([y for (x, y) in R])
    for y in range(maxY, 0, -1):
        row = ""
        for x in range(7):
            if (x, y) in R:
                row += "#"
            else:
                row += " "
        print(row)


@functools.cache
def part1(data, blc):
    jts = [s for s in list(data)]
    block = []
    ji = 0
    turns = 0
    TOP = frozenset([(i, 0) for i in range(7)])
    top = 0
    c = 0
    added = 0
    STATES = {}

    def isvalidmove(bl):
        # shouldnt hit walls, shouldnt cross horizon
        w = all(0 <= b[0] < 7 for b in bl)
        h = all(b not in TOP for b in bl)
        return w and h

    def updatehorizon(block, top):
        # keep only top  30 .. easier than calculating the outline
        maxy = max(y for x, y in TOP)
        top = [(x, y) for x, y in top.union(set(block)) if maxy - y <= 30]
        return frozenset(top)

    def sig(top):
        # keep only top  30 .. easier than calculating the outline
        maxy = max(y for x, y in TOP)
        top = [(x, maxy - y) for x, y in top if maxy - y <= 30]
        return frozenset(top)

    while c < blc:
        # for c in tqdm(range(blc)):
        sy = max(y for x, y in TOP) + 3 + 1
        block = [(x + 2, y + sy) for x, y in rocks[c % len(rocks)]]
        turns = 1
        while True:
            if turns % 2:
                jt = jts[ji]
                mvbl = [(x + JET[jt][0], y + JET[jt][1]) for x, y in block]
                if isvalidmove(mvbl):
                    block = mvbl.copy()
                ji = (ji + 1) % len(jts)
            else:
                # print("falls")
                mvbl = [(x, y - 1) for x, y in block]
                if isvalidmove(mvbl):
                    block = mvbl.copy()
                else:  # it settles
                    # print(c, " settled")
                    TOP = updatehorizon(block, TOP)
                    top = max([y for (x, y) in TOP])
                    ST = (ji, c % 5, sig(TOP))
                    if ST in STATES and c > 2022:
                        # print("history repeating")
                        oldc, oldy = STATES[ST]
                        dc = c - oldc
                        dy = top - oldy
                        amt = (blc - c) // dc
                        added += amt * dy
                        c += amt * dc
                        assert c <= blc
                    STATES[ST] = (c, top)
                    break

            turns += 1
        c += 1

    return top + added


def part2(data):
    input = [s for s in data.split("\n")]
    print(len(input))

    return 900


def test_part1():
    assert part1(test_data, 2022) == 3068


def test_part18():
    assert part1(test_data, 12) == 21


def test_part2():
    assert part1(test_data, 1000000000000) == 1514285714288


data = get_data(day=17, year=2022)

print(part1(data, 2022))
print(part1(data, 1000000000000))

test_data = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

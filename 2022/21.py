from aocd import get_data


op = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
}


def part1(data):
    input = [s for s in data.split("\n")]
    mk = {}
    root = "root"
    mk[root] = 0
    while mk[root] == 0:
        for line in input:
            match line.split(" "):
                case [m, b]:
                    mk[m[:-1]] = int(b)
                case [m, a, o, b]:
                    if a in mk and b in mk:
                        mk[m[:-1]] = op[o](mk[a], mk[b])

    return mk["root"]


def getdiff(input, youn):
    root = "root:"
    you = "humn:"
    mk = {}
    while root[:-1] not in mk:
        for line in input:
            match line.split(" "):
                case [m, b]:
                    mk[m[:-1]] = youn if m == you else int(b)
                case [m, a, o, b]:
                    if a in mk and b in mk:
                        mk[m[:-1]] = (
                            op["-"](mk[a], mk[b]) if m == root else op[o](mk[a], mk[b])
                        )
    # print(mk)
    return mk["root"]


def part2(data):
    input = [s for s in data.split("\n")]
    x = [1000, 5000]
    y1 = getdiff(input, x[0])
    y2 = getdiff(input, x[1])
    m = (y2 - y1) / (x[1] - x[0])
    b = y1 - m * x[0]

    youn = int(-b // m)

    print(youn)
    print(3678125408016, getdiff(input, 3678125408016))
    print(3678125408017, getdiff(input, 3678125408017))
    # still needed to converge..
    return youn


def test_part1():
    assert part1(test_data) == 152


def test_part2():
    assert part2(test_data) == 301


data = get_data(day=21, year=2022)

# print(part1(data))
print(part2(data))

test_data = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

# print(part2(test_data))

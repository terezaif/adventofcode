from aocd import get_data


def part1(data):
    x, c = 1, 1
    xs = [[c, x]]
    cs = [20, 60, 100, 140, 180, 220]
    for line in data.split("\n"):
        match line.split(" "):
            case ["noop"]:
                xs.append([c, x])
                c += 1
            case ["addx", d]:
                xs.append([c, x])
                xs.append([c + 1, x])
                n = int(d)
                c += 2
                x += n

    return sum([i[0] * i[1] for i in xs if i[0] in cs])


def part2(data):
    w = 40
    x, c = 1, 0
    str = [[]]
    for line in data.split("\n"):
        match line.split(" "):
            case ["noop"]:
                p = "#" if c % w in [x - 1, x, x + 1] else "."
                str.append([p]) if len(str) <= c // w else str[c // w].append(p)
                c += 1
            case ["addx", d]:
                p = "#" if c % w in [x - 1, x, x + 1] else "."
                str.append([p]) if len(str) <= c // w else str[c // w].append(p)
                c += 1
                p = "#" if c % w in [x - 1, x, x + 1] else "."
                str.append([p]) if len(str) <= c // w else str[c // w].append(p)
                c += 1
                n = int(d)
                x += n

    [print("".join(s)) for s in str]

    return "".join(str[1])


def test_part1():
    assert part1(test_data) == 13140


def test_part2():
    assert part2(test_data) == "###...###...###...###...###...###...###."


data = get_data(day=10, year=2022)

print(part1(data))
print(part2(data))

test_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

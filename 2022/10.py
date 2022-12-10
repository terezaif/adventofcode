from aocd import get_data


def part1(data):
    x = 1
    xs = [x]
    for line in data.split("\n"):
        xs.append(x)
        match line.split(" "):
            case ["addx", d]:
                xs.append(x)
                x += int(d)

    return sum([i * xs[i] for i in range(20, 260, 40)])


def part2(data):
    w = 40
    x, c = 1, 0
    str = [[]]
    for line in data.split("\n"):
        p = "#" if abs(c % w - x) <= 1 else "."
        str.append([p]) if len(str) <= c // w else str[c // w].append(p)
        c += 1
        match line.split(" "):
            case ["addx", d]:
                p = "#" if abs(c % w - x) <= 1 else "."
                str.append([p]) if len(str) <= c // w else str[c // w].append(p)
                c += 1
                x += int(d)

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

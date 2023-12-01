from aocd import get_data

# the gold star is in 23


# 4,3,2,1,0 <- 2,1,0, -1, -2
D = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def desnuf(x):
    return sum([D[c] * 5 ** (len(x) - i - 1) for i, c in enumerate(x)])


def tosnafu(n):
    R = {v: k for k, v in D.items()}
    s = []
    while n > 0:
        r = n % 5
        if r >= 3:
            r -= 5
            n += 5
        n //= 5
        s.append(R[r])
    return "".join(s[::-1])


def part1(data):
    input = [s for s in data.split("\n")]
    input = [desnuf(s) for s in input]
    si = sum(input)
    o = tosnafu(si)
    return o


def part2(data):
    input = [s for s in data.split("\n")]

    return len(input)


def test_part1():
    assert part1(test_data) == "2=-1=0"


def test_part2():
    assert part2(test_data) == 900


data = get_data(day=25, year=2022)

print(part1(data))
# print(part2(data))

test_data = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

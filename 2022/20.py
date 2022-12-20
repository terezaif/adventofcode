from aocd import get_data


def mixing(input, mix, MUL):
    L = len(input)
    i = 0
    while i < L:
        d = input[i]
        if d != 0:
            ci = next(e for e in range(L) if mix[e] == i)
            ni = (ci + d * MUL) % (L - 1)
            mix.insert(ni, mix.pop(ci))
        i += 1
    return mix


def part2(data, N, key):
    n = [1000, 2000, 3000]
    input = [int(s) for s in data.split("\n")]
    L = len(input)
    mix = [i for i in range(L)]
    for i in range(N):
        mix = mixing(input, mix, key)
    output = [input[i] * key for i in mix]
    zero = next(e for e in range(L) if output[e] == 0)
    return sum([output[(i + zero) % L] for i in n])


def test_part1():
    assert part2(test_data, 1, 1) == 3


def test_part2():
    assert part2(test_data, 10, 811589153) == 1623178306


data = get_data(day=20, year=2022)

print(part2(data, 1, 1))  # part 1
print(part2(data, 10, 811589153))

test_data = """1
2
-3
3
-2
0
4"""

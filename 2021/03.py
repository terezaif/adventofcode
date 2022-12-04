from aocd import get_data


def part1(data):
    splits = [list(s) for s in data.split("\n")]
    li = len(splits[0])
    mask = "".join(["1" for i in range(li)])
    g = [
        str(int(sum([int(codes[i]) for codes in splits]) >= len(splits) / 2))
        for i in range(0, li)
    ]
    gamma = int("".join(g), 2)
    return gamma * (gamma ^ int(mask, 2))


def part2(data):
    splits = [list(s) for s in data.split("\n")]
    oxygen = splits.copy()
    co2 = splits.copy()
    i = 0
    while len(oxygen) > 1:
        bit = int(sum([int(codes[i]) for codes in oxygen]) >= len(oxygen) / 2)
        oxygen = [codes for codes in oxygen if int(codes[i]) == bit]
        i += 1
    i = 0
    while len(co2) > 1:
        cbit = int(sum([int(codes[i]) for codes in co2]) < len(co2) / 2)
        co2 = [codes for codes in co2 if int(codes[i]) == cbit]
        i += 1
    return int("".join(oxygen[0]), 2) * int("".join(co2[0]), 2)


def test_part1():
    assert part1(test_data) == 198


def test_part2():
    assert part2(test_data) == 230


data = get_data(day=3, year=2021)

print(part1(data))
print(part2(data))

test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

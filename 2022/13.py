from aocd import get_data
from functools import cmp_to_key


# this was r evil
def check(ll, lr) -> int:
    if isinstance(ll, int) and isinstance(lr, int):
        if ll < lr:
            return 1
        if ll > lr:
            return -1
        return 0
    elif isinstance(ll, list) and isinstance(lr, list):
        i = 0
        while i < len(ll) and i < len(lr):
            c = check(ll[i], lr[i])
            if c == 1:
                return 1
            if c == -1:
                return -1
            i += 1
        if i < len(lr):
            return 1
        elif i < len(ll):
            return -1
        else:
            return 0
    elif isinstance(ll, list) and isinstance(lr, int):
        return check(ll, [lr])
    elif isinstance(ll, int) and isinstance(lr, list):
        return check([ll], lr)
    return 0


def part1(data):
    input = [s for s in data.split("\n")]
    res = [
        i // 3 + 1 if check(eval(input[i]), eval(input[i + 1])) == 1 else 0
        for i in range(0, len(input), 3)
    ]
    return sum(res)


def part2(data):
    input = [s for s in data.split("\n")]
    divs = [[[2]], [[6]]]
    input = [
        eval(input[i])
        for i in range(len(input))
        if i not in [ex for ex in range(2, len(input), 3)]
    ] + divs
    # reverse cause -1 and 1 are opposite for part 1
    input = sorted(input, key=cmp_to_key(lambda a, b: check(a, b)), reverse=True)
    res = [i + 1 for i in range(len(input)) if input[i] in divs]

    return res[0] * res[1]


def test_part1():
    assert part1(test_data) == 13


def test_part2():
    assert part2(test_data) == 140


data = get_data(day=13, year=2022)

print(part1(data))
print(part2(data))

test_data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

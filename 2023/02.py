from aocd import get_data


def part1(data):
    max = {"red": 12, "green": 13, "blue": 14}
    input = [(s + ",").split() for s in data.split("\n")]
    out = [
        int(g[1][:-1])
        for g in input
        if (
            all(
                int(g[i * 2 + 2]) <= max[g[i * 2 + 3][:-1]]
                for i in range(len(g) // 2 - 1)
            )
        )
    ]

    return sum(out)


def part2(data):
    input = [(s + ",").split() for s in data.split("\n")]
    power = []
    for g in input:
        needed = {"red": 0, "green": 0, "blue": 0}
        for i in range(len(g) // 2 - 1):
            needed[g[i * 2 + 3][:-1]] = max(
                needed[g[i * 2 + 3][:-1]], int(g[i * 2 + 2])
            )
        li = list(needed.values())
        power.append(li[0] * li[1] * li[2])
    return sum(power)


def test_part1():
    assert part1(test_data) == 8


def test_part2():
    assert part2(test_data) == 2286


data = get_data(day=2, year=2023)

print(part1(data))
print(part2(data))

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# print(part2(test_data))

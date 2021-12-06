from aocd import get_data


def part1(data, days):
    input = [s.split(",") for s in data.split("\n")][0]
    jellyfish = [0] * 9  # need 9.. last 2 are for jellyfish babies and children

    for jf in input:
        jellyfish[int(jf)] += 1

    for d in range(days):
        reproduce = d % 7
        grownups = jellyfish[7]
        jellyfish[7] = jellyfish[8]
        jellyfish[8] = jellyfish[reproduce]
        jellyfish[reproduce] = jellyfish[reproduce] + grownups
        fish = sum(jellyfish)

    return sum(jellyfish)


def test_part1():
    assert part1(test_data, 80) == 5934


def test_part2():
    assert part1(test_data, 256) == 26984457539


data = get_data(day=6, year=2021)

print(part1(data, 80))
print(part1(data, 256))

test_data = """3,4,3,1,2"""

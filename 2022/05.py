from aocd import get_data
import re

"move 1 from 2 to 1"


def part1(data):
    input = [[c for c in s.split("\n")] for s in data.split("\n\n")]
    crates = [[list(i)[j] for j in range(1, len(input[0][0]), 4)] for i in input[0]]
    moves = [[int(n) for n in re.findall(r"\d+", i)] for i in input[1]]
    stacks = [
        [
            crates[len(crates) - 2 - j][i]
            for j in range(len(crates) - 1)
            if crates[len(crates) - 2 - j][i] != " "
        ]
        for i in range(len(crates[0]))
    ]

    for move in moves:
        source = move[1]
        dest = move[2]
        for i in range(move[0]):
            m = stacks[source - 1].pop()
            stacks[dest - 1].append(m)

    return "".join([s[-1] for s in stacks])


def part2(data):
    input = [[c for c in s.split("\n")] for s in data.split("\n\n")]
    crates = [[list(i)[j] for j in range(1, len(input[0][0]), 4)] for i in input[0]]
    moves = [[int(n) for n in re.findall(r"\d+", i)] for i in input[1]]
    stacks = [
        [
            crates[len(crates) - 2 - j][i]
            for j in range(len(crates) - 1)
            if crates[len(crates) - 2 - j][i] != " "
        ]
        for i in range(len(crates[0]))
    ]

    for move in moves:
        source = move[1]
        dest = move[2]
        stacks[dest - 1].extend(stacks[source - 1][move[0] * -1 :])
        del stacks[source - 1][len(stacks[source - 1]) - move[0] :]

    return "".join([s[-1] for s in stacks])


def test_part1():
    assert part1(test_data) == "CMZ"


def test_part2():
    assert part2(test_data) == "MCD"


data = get_data(day=5, year=2022)

print(part1(data))
print(part2(data))

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

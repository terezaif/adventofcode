from aocd import get_data


pair = {"(": ")", "[": "]", "<": ">", "{": "}"}
illegal = {")": 3, "]": 57, "}": 1197, ">": 25137}
compl = {"(": 1, "[": 2, "{": 3, "<": 4}


def part1(data):
    chunks = [s for s in data.split("\n")]
    score = 0
    for chunk in chunks:
        forward = []
        for c in chunk:
            if c in pair:
                forward.append(c)
            else:
                if c == pair[forward[-1]]:
                    forward.pop()
                else:
                    score += illegal[c]
                    break

    return score


def part2(data):
    chunks = [s for s in data.split("\n")]
    score = []
    for chunk in chunks:
        incorrect = False
        forward = []
        for c in chunk:
            if c in pair:
                forward.append(c)
            else:
                if c == pair[forward[-1]]:
                    forward.pop()
                else:
                    incorrect = True
                    break
        if not incorrect:
            sc = 0
            for i in reversed(forward):
                sc = 5 * sc + compl[i]
            score.append(sc)

    return sorted(score)[int(len(score) / 2)]


def test_part1():
    assert part1(test_data) == 26397


def test_part2():
    assert part2(test_data) == 288957


data = get_data(day=10, year=2021)

print(part1(data))
print(part2(data))

test_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

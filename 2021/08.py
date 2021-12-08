from posixpath import splitext
from aocd import get_data
from parse import parse

# digits
# 0: abcefg = [a + 1  + eg] + b
# 1: cf
# 2: acdeg = [a +  eg] + cd
# 3: acdfg = [a + 1] + dg
# 4: bcdf = bd + 1
# 5 abdfg = [a + bd] + fg
# 6 abdefg = [a + bd + eg] +    f
# 7: acf = a + 1
# 8: abcdefg = eg + [a + bd +cf]
# 9:  abcdfg = [a + bd + 1] + g

simple = {2: "1", 4: "4", 3: "7", 7: "8"}


def part1(data):
    # data = test_data
    signals = [parse("{} | {}", s) for s in data.split("\n")]
    signals = [[p[0].split(" "), p[1].split(" ")] for p in signals]

    return sum([len(o) < 5 or len(o) == 7 for s in signals for o in s[1]])


def get_code(signal):

    cf = set([o for s in signal[0] + signal[1] for o in s if len(s) == 2])  # 1
    acf = set([o for s in signal[0] + signal[1] for o in s if len(s) == 3])  # 7
    bcdf = set([o for s in signal[0] + signal[1] for o in s if len(s) == 4])  # 4
    abcdefg = set([o for s in signal[0] + signal[1] for o in s if len(s) == 7])  # 7
    a = acf - cf
    bd = bcdf - cf
    eg = abcdefg - a - bd - cf
    abcdf = a | bd | cf
    acfeg = a | cf | eg
    abdeg = a | bd | eg
    abd = a | bd
    aeg = a | eg
    acf = a | cf

    outputs = [set(list(s)) for s in signal[1]]
    pr = ""
    for o in outputs:
        if len(o) < 5 or len(o) == 7:
            pr += simple[len(o)]
        elif len(o.intersection(abcdf)) == 5:
            pr += "9"
        elif len(o.intersection(acfeg)) == 5:
            pr += "0"
        elif len(o.intersection(abdeg)) == 5:
            pr += "6"
        elif len(o.intersection(abd)) == 3:
            pr += "5"
        elif len(o.intersection(aeg)) == 3:
            pr += "2"

        elif len(o.intersection(acf)) == 3:
            pr += "3"

    return int(pr)


def part2(data):
    signals = [parse("{} | {}", s) for s in data.split("\n")]
    signals = [[p[0].split(" "), p[1].split(" ")] for p in signals]
    codes = [get_code(s) for s in signals]

    return sum(codes)


def test_code():
    input = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""
    signals = [parse("{} | {}", s) for s in input.split("\n")]
    signals = [[p[0].split(" "), p[1].split(" ")] for p in signals]

    assert get_code(signals[0]) == 5353


def test_part1():
    assert part1(test_data) == 26


def test_part2():
    assert part2(test_data) == 61229


data = get_data(day=8, year=2021)

print(part1(data))
print(part2(data))

test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

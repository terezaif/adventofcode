from aocd import get_data

rps = {'A':0,'B':1,'C':2,'X':0,'Y':1,'Z':2}

#[4, 1, 7, 9]
def game2(input)->int:
    f = rps.get(input[0])
    s = rps.get(input[-1])
    print(input, f, s)
    return (s==0)*((f+2)%3 +1) +  (s==1)*(f+1 + 3) + (s==2)*((f+1)%3 +1 + 6)


def game1(input)->int:
    f = rps.get(input[0])
    s = rps.get(input[-1])
    return ((f+2)%3 == s)*(s+1) + (s==f)*(s+1 + 3) + ((f+1)%3 == s)*(s+1 + 6)

def part1(data):
    guide = [game1(s.split(" ")) for s in data.split("\n")]
    return sum(guide)


def part2(data):
    guide = [game2(s.split(" ")) for s in data.split("\n")]
    return sum(guide)


def test_part1():
    assert part1(test_data) == 15


def test_part2():
    assert part2(test_data) == 12


data = get_data(day=2, year=2022)

print(part1(data))
print(part2(data))

test_data = """A Y
B X
C Z"""

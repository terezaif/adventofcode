from aocd import get_data
from parse import compile
import math

p = compile(
    """Monkey {m}:
  Starting items: {items}
  Operation: new = old {op} {second}
  Test: divisible by {div}
    If true: throw to monkey {mt}
    If false: throw to monkey {mf}"""
)

op = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


# monkey day
def part1(data):
    input = [p.parse(s) for s in data.split("\n\n")]
    input = [
        {
            "items": [int(i) for i in r["items"].split(", ")],
            "op": r["op"],
            "second": r["second"],
            "div": int(r["div"]),
            "mt": int(r["mt"]),
            "mf": int(r["mf"]),
            "active": 0,
        }
        for r in input
    ]
    rounds = 20
    for r in range(rounds):
        for i in range(len(input)):
            m = input[i]
            for item in m["items"]:
                item = op[m["op"]](
                    item, item if m["second"] == "old" else int(m["second"])
                )
                item = item // 3  # bored
                target = m["mt"] if item % m["div"] == 0 else m["mf"]
                input[target]["items"].append(item)

            input[i]["active"] += len(m["items"])
            input[i]["items"] = []

    active = sorted([i["active"] for i in input], reverse=True)[:2]
    return active[0] * active[1]


def part2(data):
    input = [p.parse(s) for s in data.split("\n\n")]
    input = [
        {
            "items": [int(i) for i in r["items"].split(", ")],
            "op": r["op"],
            "second": r["second"],
            "div": int(r["div"]),
            "mt": int(r["mt"]),
            "mf": int(r["mf"]),
            "active": 0,
        }
        for r in input
    ]
    div = math.prod([i["div"] for i in input])
    rounds = 10000
    for r in range(rounds):
        for i in range(len(input)):
            m = input[i]
            for item in m["items"]:
                item = op[m["op"]](
                    item, item if m["second"] == "old" else int(m["second"])
                )
                # item = item//3 # bored
                target = m["mt"] if item % m["div"] == 0 else m["mf"]
                input[target]["items"].append(item % div)

            input[i]["active"] += len(m["items"])
            input[i]["items"] = []

    active = sorted([i["active"] for i in input], reverse=True)[:2]
    return active[0] * active[1]


def test_part1():
    assert part1(test_data) == 10605


def test_part2():
    assert part2(test_data) == 2713310158


data = get_data(day=11, year=2022)

print(part1(data))
print(part2(data))

test_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

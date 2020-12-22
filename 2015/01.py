from aocd import get_data


def floors(data):
    floors = [1 if c == "(" else -1 for c in data]
    o = sum(floors)
    print(o)
    return o


def basement(data):
    floors = [1 if c == "(" else -1 for c in data]
    cf = 0
    for i, f in enumerate(floors):
        cf += f
        if cf == -1:
            break
    print(i + 1)
    return i + 1


def test_floors():
    d = "(())"
    assert floors(d) == 0


def test_basement():
    d = ")"
    assert basement(d) == 1


def test_basement_1():
    d = "()())"
    assert basement(d) == 5


data = get_data(day=1, year=2015)
floors(data)
basement(data)

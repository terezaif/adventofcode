from aocd import get_data


def depth(data):
    depths = [s.split(" ") for s in data.split("\n")]
    x, y = 0, 0
    for dir, value in depths:
        match dir:
            case "forward":
                x += int(value)
            case "down":
                y += int(value)
            case "up":
                y -= int(value)

    return x * y


def aim(data):
    depths = [s.split(" ") for s in data.split("\n")]

    x, y, a = 0, 0, 0
    for dir, value in depths:
        match dir:
            case "forward":
                x += int(value)
                y += int(value) * a
            case "down":
                a += int(value)
            case "up":
                a -= int(value)

    return x * y


def test_depth():
    assert depth(test_data) == 150


def test_aim():
    assert aim(test_data) == 900


data = get_data(day=2, year=2021)

print(depth(data))
print(aim(data))

test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

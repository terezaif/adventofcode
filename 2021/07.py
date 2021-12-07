from aocd import get_data
import statistics


def part1(data):
    hor = [int(s) for s in data.split(",")]
    median = int(statistics.median(hor))

    cost = [abs(h - median) for h in hor]

    return sum(cost)


# 356992
def part2(data):
    hor = [int(s) for s in data.split(",")]
    # the upper avg works on test but not on input data
    avg = statistics.mean(hor)  # or sum/len
    avg_l = int(avg)
    avg_h = round(avg)

    cost_l = [dd for d in hor for dd in range(1, abs(d - avg_l) + 1)]
    cost_h = [dd for d in hor for dd in range(1, abs(d - avg_h) + 1)]

    return min(sum(cost_l), sum(cost_h))


def test_part1():
    assert part1(test_data) == 37


def test_part2():
    assert part2(test_data) == 168


data = get_data(day=7, year=2021)

print(part1(data))
print(part2(data))

test_data = """16,1,2,0,4,2,7,1,2,14"""
